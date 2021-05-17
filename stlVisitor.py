# Generated from stl.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .stlParser import stlParser
else:
    from stlParser import stlParser

# This class defines a complete generic visitor for a parse tree produced by stlParser.

class stlVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by stlParser#content.
    def visitContent(self, ctx:stlParser.ContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#always.
    def visitAlways(self, ctx:stlParser.AlwaysContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#booleanFilter.
    def visitBooleanFilter(self, ctx:stlParser.BooleanFilterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#negation.
    def visitNegation(self, ctx:stlParser.NegationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#or.
    def visitOr(self, ctx:stlParser.OrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#quantitativeSignal.
    def visitQuantitativeSignal(self, ctx:stlParser.QuantitativeSignalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#and.
    def visitAnd(self, ctx:stlParser.AndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#implication.
    def visitImplication(self, ctx:stlParser.ImplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#scope.
    def visitScope(self, ctx:stlParser.ScopeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#eventually.
    def visitEventually(self, ctx:stlParser.EventuallyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#until.
    def visitUntil(self, ctx:stlParser.UntilContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#signalAbsolute.
    def visitSignalAbsolute(self, ctx:stlParser.SignalAbsoluteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#signalExpressionScope.
    def visitSignalExpressionScope(self, ctx:stlParser.SignalExpressionScopeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#signalProduct.
    def visitSignalProduct(self, ctx:stlParser.SignalProductContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#signalSum.
    def visitSignalSum(self, ctx:stlParser.SignalSumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#signalSignal.
    def visitSignalSignal(self, ctx:stlParser.SignalSignalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#product.
    def visitProduct(self, ctx:stlParser.ProductContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#absolute.
    def visitAbsolute(self, ctx:stlParser.AbsoluteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#sum.
    def visitSum(self, ctx:stlParser.SumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#expressionScope.
    def visitExpressionScope(self, ctx:stlParser.ExpressionScopeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#value.
    def visitValue(self, ctx:stlParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#signal.
    def visitSignal(self, ctx:stlParser.SignalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#constant.
    def visitConstant(self, ctx:stlParser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#intValue.
    def visitIntValue(self, ctx:stlParser.IntValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stlParser#floatValue.
    def visitFloatValue(self, ctx:stlParser.FloatValueContext):
        return self.visitChildren(ctx)



del stlParser