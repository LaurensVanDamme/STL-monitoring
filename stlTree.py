import pandas as pd
from numbers import Number
import numpy
import matplotlib.pyplot as plt
from stlUtils import *

OPERATORS = {'=': lambda x, y: x == y,
      '!=': lambda x, y: x != y,
      '>=': lambda x, y: x >= y,
      '<=': lambda x, y: x <= y,
      '>': lambda x, y: x > y,
      '<': lambda x, y: x < y}

currentPlot = 0


class Node:  # Abstract class
    count = 0

    def __init__(self):
        self.children = []
        self.parent = None
        self.id = type(self).count  # Causes every node to be unique (handy for dot)
        type(self).count += 1  # Raise the counter every time

        # Location of the node in the formula for debugging purposes
        self.line = 0
        self.column = 0

        # For the creation of the tree
        self.doublePop = False
        self.negateNext = False

    # Add a childnode
    def add(self, node):
        self.children.append(node)
        self.children[-1].parent = self

    def name(self):
        return self.__class__.__name__.split('Node')[0]

    # Merge a node with this node
    def merge(self, node):
        node.parent.children.remove(node)
        self.children = node.children + self.children
        for child in node.children:
            child.parent = self

    # Execute the (stl) node
    # Expects a pandas dataframe with the signals
    # Expects a string with the type of semantic that will be used, default = boolean
    # returns a single signal or number
    def validate(self, signals, semantic='quantitative', plot=False):
        # Empty function to be overridden in derived classes
        pass

    # To know how many plots will be made
    def calculatePlotAmount(self):
        return sum([x.calculatePlotAmount() for x in self.children]) + 0

    # Processes the token (terminal node in ANTLR AST)
    def processToken(self, token):
        # Empty function to be overridden in derived classes which handle tokens
        pass

    def text(self):
        return self.name()

    def dotRepresentation(self):
        return '\t"' + self.name() + '_' + str(self.id) + '"[label="' + self.text() + '"];\n'

    def toDot(self, file):
        if self.parent is None:
            file.write("digraph stlTree {\n")
            file.write(self.dotRepresentation())
        else:
            file.write(self.dotRepresentation())
            file.write('\t"' + self.parent.name() + '_' + str(self.parent.id) + '" -> "' + self.name() + '_' + str(
                self.id) + '";\n')

        for child in self.children:
            child.toDot(file)
        if self.parent is None:
            file.write("}")

    # # Check if two nodes in the AST can merge
    # def canMerge(self, node):
    #     return node.__class__ == self.__class__

    def throwError(self, text):
        raise Exception("({}:{}) : ".format(self.line, self.column) + text)

    def printWarning(self, text):
        print("Warning ({}:{}) : ".format(self.line, self.column) + text)


class ContentNode(Node):
    def __init__(self):
        Node.__init__(self)

    def validate(self, signals, semantic='quantitative', plot=False):
        if semantic != 'boolean' and semantic != 'quantitative':
            raise Exception('No valid semantic given!')
        else:
            if plot is not False:
                global currentPlot
                currentPlot = 0
                plotAmount = self.calculatePlotAmount()
                fig, axs = plt.subplots(plotAmount, sharex=True, sharey=True)
                fig.set_size_inches(cm2inch(15), cm2inch(plotAmount * 3))
                result = self.children[0].validate(signals, semantic, axs)
                plt.show()
                return result
            else:
                return self.children[0].validate(signals, semantic, plot)[1][0]

        # if semantic == 'boolean':
        #     return self.children[0].validate(signals, semantic, plot)[0]
        # elif semantic == 'semantic':
        #     return self.children[0].validate(signals, semantic, plot)[0] > 0
        # else:
        #     raise Exception('No valid semantic given!')


class FormulaNode(Node):  # Abstract class
    def __init__(self):
        Node.__init__(self)

    def text(self):
        return self.name() + ' [' + str(self.id) + ']'

    def calculatePlotAmount(self):
        return sum([x.calculatePlotAmount() for x in self.children]) + 1

    def plot(self, signal, axs, semantic='quantitative'):
        global currentPlot
        if not isinstance(axs, numpy.ndarray):
            axs = [axs]
        if semantic == 'boolean':
            axs[currentPlot].step(signal[0], signal[1], 'r-', where='post')
        else:
            axs[currentPlot].plot(signal[0], signal[1], 'r-')
        # axs[currentPlot].set_ylabel(self.text(), rotation='horizontal', va="center")
        axs[currentPlot].set_title(self.text())
        currentPlot += 1


class NegationNode(FormulaNode):
    def __init__(self):
        FormulaNode.__init__(self)

    def validate(self, signals, semantic='quantitative', plot=False):
        result = self.children[0].validate(signals, semantic, plot)
        temp = []
        if semantic == 'boolean':
            temp += [result[0], [-x+1 for x in result[1]]]
        elif semantic == 'quantitative':
            temp.append(result[0])
            temp.append([-x for x in result[1]])
            temp.append([-x for x in result[2]])
        if plot is not False:
            self.plot(temp, plot, semantic)
        return temp


class AndNode(FormulaNode):
    def __init__(self):
        FormulaNode.__init__(self)

    def validate(self, signals, semantic='quantitative', plot=False):
        result = [self.children[0].validate(signals, semantic, plot), self.children[1].validate(signals, semantic, plot)]
        temp = [[], []]
        if semantic == 'boolean':
            result = list(getPunctualIntersection(result[0], result[1], semantic='boolean'))
            for i in range(len(result[0][0])):
                temp[0].append(result[0][0][i])
                temp[1].append(result[0][1][i] and result[1][1][i])
        elif semantic == 'quantitative':
            # calculate_and_or already performs a getPunctualIntersection
            temp = calculate_and_or(result[0], result[1])
        if plot is not False:
            self.plot(temp, plot, semantic)
        return temp


class UntilNode(FormulaNode):
    def __init__(self):
        FormulaNode.__init__(self)

    def validate(self, signals, semantic='quantitative', plot=False):
        # Check if one or two formula nodes as children, if one -> add true signal
        result = [self.children[-1].validate(signals, semantic, plot)]
        if len(self.children) == 3:  # With two formulas it would be 4 (2 formula, 2 int for interval)
            result = [[result[0][0], ([1] * len(result[0][0])), ([0] * len(result[0][0]))]] + result
        else:
            result = [self.children[0].validate(signals, semantic, plot)] + result
            result = list(getPunctualIntersection(result[0], result[1], semantic))

        # Get the size for which all needed data is present
        size = len(result[0][0])

        # Get the values
        a = self.children[len(self.children) - 3].validate(signals, semantic, plot)
        b = self.children[len(self.children) - 2].validate(signals, semantic, plot)

        until = []

        if semantic == 'boolean':
            # Get the true intervals of the signals
            intervals_1 = []
            intervals_2 = []
            temp_1 = []
            temp_2 = []
            true_1 = False
            true_2 = False
            for i in range(size):
                if result[0][1][i] and not true_1:
                    true_1 = True
                    temp_1.append(result[0][0][i])
                elif not result[0][1][i] and true_1:
                    true_1 = False
                    # temp_1.append(result[0][0][i - 1])  # Closed interval (discrete time steps)
                    temp_1.append(result[0][0][i])  # Half open interval [a,b) (continuous time steps)
                    intervals_1.append(temp_1)
                    temp_1 = []

                if result[1][1][i] and not true_2:
                    true_2 = True
                    temp_2.append(result[1][0][i])
                elif not result[1][1][i] and true_2:
                    true_2 = False
                    # temp_2.append(result[1][0][i - 1])  # Closed interval (discrete time steps)
                    temp_2.append(result[1][0][i])  # Half open interval [a,b) (continuous time steps)
                    intervals_2.append(temp_2)
                    temp_2 = []
            if true_1:
                temp_1.append(result[0][0][size - 1])
                intervals_1.append(temp_1)
            if true_2:
                temp_2.append(result[1][0][size - 1])
                intervals_2.append(temp_2)

            # Decompose and calculate the Until for the decompositions
            intervals_until = []
            for inter_1 in intervals_1:
                for inter_2 in intervals_2:
                    intersection = getBooleanIntersection(inter_1, inter_2)
                    if intersection:
                        interval = [max(0, intersection[0] - b), min(size, intersection[1] - a)]
                        if interval[0] > interval[1]:  # Interval doesn't exist
                            continue
                        intersection = getBooleanIntersection(interval, inter_1)
                        if intersection:
                            intervals_until.append(intersection)

            # Calculate the entire until - make the intervals true in the until
            until += [result[1][0].copy()] + [[0] * size]
            for inter in intervals_until:
                for t in inter:
                    if t in until[0]:
                        until[1][until[0].index(t)] = 1
                    else:
                        for i in range(len(until[0])):
                            if until[0][i] > t:
                                until[0] = until[0][:i] + [t] + until[0][i:]
                                until[1] = until[1][:i] + [1] + until[1][i:]
                                break
                for i in range(until[0].index(inter[0]), until[0].index(inter[1]) + 1):
                    until[1][i] = 1
                # The interval is from until (half open), so from the second time step it's zero again
                until[1][until[0].index(inter[1])] = 0
            for i in reversed(range(len(until[0]))):
                if until[0][i] > result[0][0][-1] - b:
                    if until[0][i - 1] < result[0][0][-1] - b:
                        until[0][-1] = result[0][0][-1] - b
                        until[1][-1] = until[1][-2]
                        # until[0][i] = result[0][0][-1] - b
                        # until[1][i] = until[1][i - 1]
                    else:
                        until[0].pop(-1)
                        until[1].pop(-1)
                        # until[1][i] = 0

                # for i in range(inter[0], inter[1] + 1):
                #     if i < size - b:
                #         until[1][i] = 1
        elif semantic == 'quantitative':
            # import time
            # start_1 = time.time()

            short_algo = True
            # result = [result[1], result[0]]
            until += [[], [], []]
            if short_algo:
                for i in range(size):
                    t = result[1][0][i]
                    t_a = t + a
                    t_b = t + b
                    inter_2 = getSignalInterval(result[1], t_a, t_b)
                    values = []
                    derivatives = []
                    for j in range(len(inter_2[0])):
                        k = inter_2[0][j]
                        inter_1 = getSignalInterval(result[0], t, k)
                        values.append(min(inter_2[1][j], min(inter_1[1])))
                        derivatives.append(min(inter_2[2][j], min(inter_1[2])))
                    until[0].append(t)
                    until[1].append(max(values))
                    until[2].append(max(derivatives))
                for i in reversed(range(len(until[0]))):
                    if until[0][i] > result[0][0][-1] - b:
                        if until[0][i - 1] < result[0][0][-1] - b:
                            until[0][-1] = result[0][0][-1] - b
                            until[1][-1] = getAffinePoint(until, result[0][0][-1] - b)
                            until[2][-1] = until[2][-2]
                            # until[0][i] = result[0][0][-1] - b
                            # until[1][i] = getAffinePoint(until, result[0][0][-1] - b)
                            # until[2][i] = until[2][i - 1]
                        else:
                            until[0].pop(-1)
                            until[1].pop(-1)
                            until[2].pop(-1)
                            # until[1][i] = 0
                            # until[2][i] = 0
            else:
                def shift(y, v):
                    temp = [t - v for t in y[0]]  # Shift the signal
                    i = 0
                    while i < len(y[0]) and temp[i] < 0:  # Count how many values have a time step smaller than 0
                        i += 1

                    if len(y[0]) == i:
                        return [[], [], []]

                    result = [temp[i:], y[1][i:], y[2][i:]]

                    if i > 0 and result[0][0] != 0 and y[2][i] != 0:  # Add a point at time step 0 if the derivative of the last deleted point isn't 0
                        result[0] = [0] + result[0]
                        result[1] = [getAffinePoint(y, v)] + result[1]
                        result[2] = list(numpy.diff([result[1][0], result[1][1]]) / numpy.diff([result[0][0], result[0][1]])) + result[2]
                    return result

                def computeAnd(x, y):
                    x, y = getPunctualIntersection(x, y)
                    return calculate_and_or(x, y)

                def computeOr(x, y):
                    x, y = getPunctualIntersection(x, y)
                    return calculate_and_or(x, y, 'or')

                def computeEventually(x, t_0=float('inf')):
                    if t_0 == float('inf'):
                        t_0 = x[0][0]
                    y_a = shift(x, a)
                    y_b = shift(x, b)
                    y = computeOr(y_a, y_b)

                    s = x[0][0] - b
                    t = s
                    i = 0
                    M = {x[0][0]}

                    z = [[], [], []]

                    while t + a < x[0][-1]:
                        if i + 1 < len(x[0]) and len(M) > 0:
                            t = min(min(M) - a, x[0][i + 1] - b)
                        elif len(M) == 0:
                            t = x[0][i + 1] - b
                        else:
                            t = min(M) - a

                        if len(M) > 0 and t == min(M) - a:
                            M.remove(min(M))
                            # not sure if the z computation shouldn't be here... (gives the same result on the examples)
                            s = t

                        if s >= t_0:
                            if len(M) == 0:
                                computed_or = y
                            else:
                                yt_minM = getAffinePoint(x, min(M))

                                y_s_t = getSignalInterval(y, s, t)
                                y_constant = [y[0], [yt_minM] * len(y[0]), [0] * len(y[0])]
                                computed_or = computeOr(y_s_t, y_constant)

                            i_s = computed_or[0].index(s)
                            i_t = computed_or[0].index(t)

                            for index in range(i_s, i_t + 1):
                                if computed_or[0][index] not in z[0]:
                                    z[0].append(computed_or[0][index])
                                    z[1].append(computed_or[1][index])
                                    z[2].append(computed_or[2][index])
                                else:
                                    i_z = z[0].index(computed_or[0][index])
                                    z[1][i_z] = computed_or[1][index]
                                    z[2][i_z] = computed_or[2][index]

                        if i + 1 < len(x[0]) and t == x[0][i + 1] - b:
                            while len(M) != 0 and getAffinePoint(x, x[0][i + 1]) >= getAffinePoint(x, max(M)):
                                M.remove(max(M))
                            M.add(x[0][i + 1])
                            i += 1

                    return z

                # Begin algorithm for until
                until = [[], [], []]
                z_0 = [result[1][0], [0] * size, [0] * size]
                i = len(result[0][0]) - 2  # Has to be 2, not 1 because we use an extra +1 in the intervals
                # Because the algorithm doesn't include the last value, we act as if we don't have an half open interval in python
                while i >= 0:
                    if result[0][2][i] <= 0:
                        z_1 = computeAnd([x[i:(i+1)+1] for x in result[1]], [x[i:(i+1)+1] for x in result[0]])
                        z_2 = computeEventually(z_1, result[0][0][0])
                        z_3 = computeAnd([x[i:(i+1)+1] for x in result[0]], z_0)
                        temp = computeOr(z_2, z_3)
                    else:
                        z_1 = computeEventually([x[i:(i+1)+1] for x in result[1]], result[0][0][0])
                        z_2 = computeAnd(z_1, [x[i:(i+1)+1] for x in result[0]])
                        z_3 = computeAnd([result[0][0], [result[0][0][i+1]] * size, [0] * size], z_0)
                        temp = computeOr(z_2, z_3)

                    t_i = temp[0].index(result[1][0][i])
                    if result[1][0][i + 1] == result[1][0][-1]:  # The last (so first in algorithm) pair
                        t_i_1 = len(temp[0])
                    else:
                        t_i_1 = temp[0].index(result[1][0][i + 1])

                    until[0] = temp[0][t_i:t_i_1] + until[0]
                    until[1] = temp[1][t_i:t_i_1] + until[1]
                    until[2] = temp[2][t_i:t_i_1] + until[2]
                    i -= 1
                    # z_0 = [result[0][0], [until[1][until[0].index(result[0][0][i+1])]] * size, [0] * size]  # Should be the last added value?
                    z_0 = [result[0][0], [until[1][0]] * size, [0] * size]  # Should be the last added value?
        if plot is not False:
            self.plot(until, plot, semantic)

        # end_1 = time.time()
        # print(f'time for until operation: {end_1 - start_1}s')

        return until


class BooleanFilterNode(FormulaNode):
    def __init__(self):
        FormulaNode.__init__(self)
        self.filter = None

    def processToken(self, token):
        self.filter = str(token)

    def validate(self, signals, semantic='quantitative', plot=False):
        result = [self.children[0].validate(signals, semantic, plot), self.children[1].validate(signals, semantic, plot)]
        temp = []
        if isinstance(result[0], list) and isinstance(result[1], list):
            result = list(getPunctualIntersection(result[0], result[1], semantic))
            temp += [[], []]
            for i in range(len(result[0][0])):
                temp[0].append(result[0][0][i])
                temp[1].append(int(OPERATORS[self.filter](result[0][1][i], result[1][1][i])))
        elif isinstance(result[0], list) and isinstance(result[1], Number):
            temp += [result[0][0], [int(OPERATORS[self.filter](x, result[1])) for x in result[0][1]]]
        else:
            self.throwError('Encountered a BooleanFilter of unknown types ' + str(type(result[0])) + ' and '
                            + str(type(result[1])))
        if semantic == 'quantitative':
            # Calculation of the derivative
            dydx = numpy.diff(temp[1]) / numpy.diff(temp[0])
            temp += [list(dydx) + [0]]
        if plot is not False:
            self.plot(temp, plot, semantic)
        return temp  # signal represented as (t, y <, dy>)

    def text(self):
        return 'BooleanFilter' + ' [' + str(self.id) + ']: ' + self.filter


class QuantitativeSignalNode(FormulaNode):
    def validate(self, signals, semantic='quantitative', plot=False):
        result = self.children[0].validate(signals, semantic, plot)
        temp = []
        if semantic == 'boolean':
            temp += [result[0], [1 if (x >= 0) else 0 for x in result[1]]]
        elif semantic == 'quantitative':
            temp = result
            # Calculation of the derivative
            dydx = numpy.diff(result[1]) / numpy.diff(result[0])
            temp = [result[0], result[1], list(dydx) + [0]]
        else:
            raise Exception('No valid semantic given!')
        if plot is not False:
            self.plot(temp, plot, semantic)
        return temp  # signal represented as (t, y <, dy>)

    def text(self):
        return self.name() + ' [' + str(self.id) + ']'


class OperationNode(Node):  # Abstract class
    def __init__(self):
        Node.__init__(self)
        self.operatorName = None
        self.operator = 1

    def processToken(self, token):
        self.operatorName = str(token)

    def text(self):
        return self.operatorName


class ProductNode(OperationNode):
    def __init__(self):
        OperationNode.__init__(self)

    def processToken(self, token):
        OperationNode.processToken(self, token)
        if self.operatorName == '/':
            self.operator = -1

    def validate(self, signals, semantic='quantitative', plot=False):  # TODO: test
        result = [self.children[0].validate(signals, semantic, plot), self.children[1].validate(signals, semantic, plot)]
        if isinstance(result[0], list) and isinstance(result[1], list):
            result = list(getPunctualIntersection(result[0], result[1], semantic))
            temp = [[], []]
            for i in range(len(result[0][0])):
                temp[0].append(result[0][0][i])
                temp[1].append(result[0][1][i] * pow(result[1][1][i], self.operator))
            return temp
        if isinstance(result[0], list) and isinstance(result[1], list):
            temp = []
            for i in range(min(len(result[0]), len(result[1]))):
                temp.append(result[0][i] * pow(result[1][i], self.operator))
            return temp
        elif isinstance(result[0], list) and isinstance(result[1], Number):
            return [x + (pow(result[1], self.operator)) for x in result[0]]
        elif isinstance(result[0], Number) and isinstance(result[1], list):
            return [result[0] + pow(x, self.operator) for x in result[1]]
        elif isinstance(result[0], Number) and isinstance(result[1], Number):
            return result[0] + pow(result[1], self.operator)
        else:
            self.throwError('Encountered a p[range(len(result[0][0]))], roduct/division of unknown types ' + str(type(result[0])) + ' and '
                            + str(type(result[1])))


class SumNode(OperationNode):
    def __init__(self):
        OperationNode.__init__(self)

    def processToken(self, token):
        OperationNode.processToken(self, token)
        if self.operatorName == '-':
            self.operator = -1

    def validate(self, signals, semantic='quantitative', plot=False):
        result = [self.children[0].validate(signals, semantic, plot), self.children[1].validate(signals, semantic, plot)]
        if isinstance(result[0], list) and isinstance(result[1], list):
            result = list(getPunctualIntersection(result[0], result[1], semantic))
            temp = [[], []]
            for i in range(len(result[0][0])):
                temp[0].append(result[0][0][i])
                temp[1].append(result[0][1][i] + (self.operator * result[1][1][i]))
            return temp
        elif isinstance(result[0], list) and isinstance(result[1], Number):
            return [result[0][0], [x + (self.operator * result[1]) for x in result[0][1]]]
        elif isinstance(result[0], Number) and isinstance(result[1], list):
            return [result[1][0], [result[0] + (self.operator * x) for x in result[1][1]]]
        elif isinstance(result[0], Number) and isinstance(result[1], Number):
            return result[0] + (self.operator * result[1])
        else:
            self.throwError('Encountered a sum/subtraction of unknown types ' + str(type(result[0])) + ' and '
                            + str(type(result[1])))


class AbsoluteNode(OperationNode):
    def __init__(self):
        OperationNode.__init__(self)

    def validate(self, signals, semantic='quantitative', plot=False):
        result = self.children[0].validate(signals, semantic, plot)
        if isinstance(result, list):
            return [result[0], list(map(abs, result[1]))]
        elif isinstance(result, Number):
            return abs(result)
        else:
            self.throwError('Encountered a value of unknown type ' + str(type(result)))

    def text(self):
        return self.name()


class ValueNode(Node):  # Abstract class
    def __init__(self):
        Node.__init__(self)
        self.sign = 1
        self.value = None

    def validate(self, signals, semantic='quantitative', plot=False):
        return self.value

    def text(self):
        return ('-' if self.sign < 0 else '') + str(self.value)


class IntValueNode(ValueNode):
    def __init__(self):
        ValueNode.__init__(self)

    def processToken(self, token):
        if token == '-':
            self.sign *= -1
            return
        self.value = self.sign * int(str(token))


class FloatValueNode(ValueNode):
    def __init__(self):
        ValueNode.__init__(self)
        self.integer = None
        self.fraction = None

    def processToken(self, token):
        if token == '-':
            self.sign *= -1
            return
        elif token == '.':
            return

        if self.integer is None:
            self.integer = int(str(token))
        else:
            self.fraction = token
            self.value = self.sign * float(str(self.integer) + '.' + str(self.fraction))


class SignalNode(Node):
    def __init__(self):
        Node.__init__(self)
        self.signalName = None

    def processToken(self, token):
        self.signalName = str(token)

    def validate(self, signals, semantic='quantitative', plot=False):
        signal = [[], [], []]  # [t, x, dx] = [time steps, values, derivatives]
        # Check if the signal exist before usage
        if self.signalName in signals.columns:
            signal[1] = [x for x in (list(signals[self.signalName])) if not pd.isnull(x)]
        else:
            self.throwError('The signal ' + self.signalName + ' doesn\'t exist!')

        if self.signalName + '_t' in signals.columns:
            signal[0] = [x for x in list(signals[self.signalName + '_t']) if not pd.isnull(x)]
        else:
            self.printWarning(
                'The signal ' + self.signalName + ' doesn\'t have timestamps (' + self.signalName + '_t) defined, they are generated automatically!')
            signal[0] = [x for x in range(len(signal[1]))]

        # if semantic == 'quantitative' and self.signalName + '_d' in signals.columns:
        #     signal[2] = [x for x in list(signals[self.signalName + '_d']) if not pd.isnull(x)]
        # else:
        #     self.printWarning(
        #         'The signal ' + self.signalName + ' doesn\'t have derivatives (' + self.signalName + '_d) defined, they are automatically calculated from the values!')
        #     # Calculation of the derivative
        #     dydx = numpy.diff(signal[1]) / numpy.diff(signal[0])
        #     signal[2] = list(dydx) + [0]

        return signal

    def text(self):
        return 'Signal: ' + self.signalName
