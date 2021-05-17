# Generated from stl.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .stlParser import stlParser
else:
    from stlParser import stlParser

# This class defines a complete listener for a parse tree produced by stlParser.
class stlListener(ParseTreeListener):

    # Enter a parse tree produced by stlParser#content.
    def enterContent(self, ctx:stlParser.ContentContext):
        pass

    # Exit a parse tree produced by stlParser#content.
    def exitContent(self, ctx:stlParser.ContentContext):
        pass


    # Enter a parse tree produced by stlParser#always.
    def enterAlways(self, ctx:stlParser.AlwaysContext):
        pass

    # Exit a parse tree produced by stlParser#always.
    def exitAlways(self, ctx:stlParser.AlwaysContext):
        pass


    # Enter a parse tree produced by stlParser#booleanFilter.
    def enterBooleanFilter(self, ctx:stlParser.BooleanFilterContext):
        pass

    # Exit a parse tree produced by stlParser#booleanFilter.
    def exitBooleanFilter(self, ctx:stlParser.BooleanFilterContext):
        pass


    # Enter a parse tree produced by stlParser#negation.
    def enterNegation(self, ctx:stlParser.NegationContext):
        pass

    # Exit a parse tree produced by stlParser#negation.
    def exitNegation(self, ctx:stlParser.NegationContext):
        pass


    # Enter a parse tree produced by stlParser#or.
    def enterOr(self, ctx:stlParser.OrContext):
        pass

    # Exit a parse tree produced by stlParser#or.
    def exitOr(self, ctx:stlParser.OrContext):
        pass


    # Enter a parse tree produced by stlParser#quantitativeSignal.
    def enterQuantitativeSignal(self, ctx:stlParser.QuantitativeSignalContext):
        pass

    # Exit a parse tree produced by stlParser#quantitativeSignal.
    def exitQuantitativeSignal(self, ctx:stlParser.QuantitativeSignalContext):
        pass


    # Enter a parse tree produced by stlParser#and.
    def enterAnd(self, ctx:stlParser.AndContext):
        pass

    # Exit a parse tree produced by stlParser#and.
    def exitAnd(self, ctx:stlParser.AndContext):
        pass


    # Enter a parse tree produced by stlParser#implication.
    def enterImplication(self, ctx:stlParser.ImplicationContext):
        pass

    # Exit a parse tree produced by stlParser#implication.
    def exitImplication(self, ctx:stlParser.ImplicationContext):
        pass


    # Enter a parse tree produced by stlParser#scope.
    def enterScope(self, ctx:stlParser.ScopeContext):
        pass

    # Exit a parse tree produced by stlParser#scope.
    def exitScope(self, ctx:stlParser.ScopeContext):
        pass


    # Enter a parse tree produced by stlParser#eventually.
    def enterEventually(self, ctx:stlParser.EventuallyContext):
        pass

    # Exit a parse tree produced by stlParser#eventually.
    def exitEventually(self, ctx:stlParser.EventuallyContext):
        pass


    # Enter a parse tree produced by stlParser#until.
    def enterUntil(self, ctx:stlParser.UntilContext):
        pass

    # Exit a parse tree produced by stlParser#until.
    def exitUntil(self, ctx:stlParser.UntilContext):
        pass


    # Enter a parse tree produced by stlParser#signalAbsolute.
    def enterSignalAbsolute(self, ctx:stlParser.SignalAbsoluteContext):
        pass

    # Exit a parse tree produced by stlParser#signalAbsolute.
    def exitSignalAbsolute(self, ctx:stlParser.SignalAbsoluteContext):
        pass


    # Enter a parse tree produced by stlParser#signalExpressionScope.
    def enterSignalExpressionScope(self, ctx:stlParser.SignalExpressionScopeContext):
        pass

    # Exit a parse tree produced by stlParser#signalExpressionScope.
    def exitSignalExpressionScope(self, ctx:stlParser.SignalExpressionScopeContext):
        pass


    # Enter a parse tree produced by stlParser#signalProduct.
    def enterSignalProduct(self, ctx:stlParser.SignalProductContext):
        pass

    # Exit a parse tree produced by stlParser#signalProduct.
    def exitSignalProduct(self, ctx:stlParser.SignalProductContext):
        pass


    # Enter a parse tree produced by stlParser#signalSum.
    def enterSignalSum(self, ctx:stlParser.SignalSumContext):
        pass

    # Exit a parse tree produced by stlParser#signalSum.
    def exitSignalSum(self, ctx:stlParser.SignalSumContext):
        pass


    # Enter a parse tree produced by stlParser#signalSignal.
    def enterSignalSignal(self, ctx:stlParser.SignalSignalContext):
        pass

    # Exit a parse tree produced by stlParser#signalSignal.
    def exitSignalSignal(self, ctx:stlParser.SignalSignalContext):
        pass


    # Enter a parse tree produced by stlParser#product.
    def enterProduct(self, ctx:stlParser.ProductContext):
        pass

    # Exit a parse tree produced by stlParser#product.
    def exitProduct(self, ctx:stlParser.ProductContext):
        pass


    # Enter a parse tree produced by stlParser#absolute.
    def enterAbsolute(self, ctx:stlParser.AbsoluteContext):
        pass

    # Exit a parse tree produced by stlParser#absolute.
    def exitAbsolute(self, ctx:stlParser.AbsoluteContext):
        pass


    # Enter a parse tree produced by stlParser#sum.
    def enterSum(self, ctx:stlParser.SumContext):
        pass

    # Exit a parse tree produced by stlParser#sum.
    def exitSum(self, ctx:stlParser.SumContext):
        pass


    # Enter a parse tree produced by stlParser#expressionScope.
    def enterExpressionScope(self, ctx:stlParser.ExpressionScopeContext):
        pass

    # Exit a parse tree produced by stlParser#expressionScope.
    def exitExpressionScope(self, ctx:stlParser.ExpressionScopeContext):
        pass


    # Enter a parse tree produced by stlParser#value.
    def enterValue(self, ctx:stlParser.ValueContext):
        pass

    # Exit a parse tree produced by stlParser#value.
    def exitValue(self, ctx:stlParser.ValueContext):
        pass


    # Enter a parse tree produced by stlParser#signal.
    def enterSignal(self, ctx:stlParser.SignalContext):
        pass

    # Exit a parse tree produced by stlParser#signal.
    def exitSignal(self, ctx:stlParser.SignalContext):
        pass


    # Enter a parse tree produced by stlParser#constant.
    def enterConstant(self, ctx:stlParser.ConstantContext):
        pass

    # Exit a parse tree produced by stlParser#constant.
    def exitConstant(self, ctx:stlParser.ConstantContext):
        pass


    # Enter a parse tree produced by stlParser#intValue.
    def enterIntValue(self, ctx:stlParser.IntValueContext):
        pass

    # Exit a parse tree produced by stlParser#intValue.
    def exitIntValue(self, ctx:stlParser.IntValueContext):
        pass


    # Enter a parse tree produced by stlParser#floatValue.
    def enterFloatValue(self, ctx:stlParser.FloatValueContext):
        pass

    # Exit a parse tree produced by stlParser#floatValue.
    def exitFloatValue(self, ctx:stlParser.FloatValueContext):
        pass



del stlParser