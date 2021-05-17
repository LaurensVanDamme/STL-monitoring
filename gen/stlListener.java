// Generated from C:/Users/laure/OneDrive/UAntwerpen/Master 2/Research project 2/STL\stl.g4 by ANTLR 4.8
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link stlParser}.
 */
public interface stlListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link stlParser#content}.
	 * @param ctx the parse tree
	 */
	void enterContent(stlParser.ContentContext ctx);
	/**
	 * Exit a parse tree produced by {@link stlParser#content}.
	 * @param ctx the parse tree
	 */
	void exitContent(stlParser.ContentContext ctx);
	/**
	 * Enter a parse tree produced by the {@code always}
	 * labeled alternative in {@link stlParser#formula}.
	 * @param ctx the parse tree
	 */
	void enterAlways(stlParser.AlwaysContext ctx);
	/**
	 * Exit a parse tree produced by the {@code always}
	 * labeled alternative in {@link stlParser#formula}.
	 * @param ctx the parse tree
	 */
	void exitAlways(stlParser.AlwaysContext ctx);
	/**
	 * Enter a parse tree produced by the {@code booleanFilter}
	 * labeled alternative in {@link stlParser#formula}.
	 * @param ctx the parse tree
	 */
	void enterBooleanFilter(stlParser.BooleanFilterContext ctx);
	/**
	 * Exit a parse tree produced by the {@code booleanFilter}
	 * labeled alternative in {@link stlParser#formula}.
	 * @param ctx the parse tree
	 */
	void exitBooleanFilter(stlParser.BooleanFilterContext ctx);
	/**
	 * Enter a parse tree produced by the {@code negation}
	 * labeled alternative in {@link stlParser#formula}.
	 * @param ctx the parse tree
	 */
	void enterNegation(stlParser.NegationContext ctx);
	/**
	 * Exit a parse tree produced by the {@code negation}
	 * labeled alternative in {@link stlParser#formula}.
	 * @param ctx the parse tree
	 */
	void exitNegation(stlParser.NegationContext ctx);
	/**
	 * Enter a parse tree produced by the {@code or}
	 * labeled alternative in {@link stlParser#formula}.
	 * @param ctx the parse tree
	 */
	void enterOr(stlParser.OrContext ctx);
	/**
	 * Exit a parse tree produced by the {@code or}
	 * labeled alternative in {@link stlParser#formula}.
	 * @param ctx the parse tree
	 */
	void exitOr(stlParser.OrContext ctx);
	/**
	 * Enter a parse tree produced by the {@code and}
	 * labeled alternative in {@link stlParser#formula}.
	 * @param ctx the parse tree
	 */
	void enterAnd(stlParser.AndContext ctx);
	/**
	 * Exit a parse tree produced by the {@code and}
	 * labeled alternative in {@link stlParser#formula}.
	 * @param ctx the parse tree
	 */
	void exitAnd(stlParser.AndContext ctx);
	/**
	 * Enter a parse tree produced by the {@code implication}
	 * labeled alternative in {@link stlParser#formula}.
	 * @param ctx the parse tree
	 */
	void enterImplication(stlParser.ImplicationContext ctx);
	/**
	 * Exit a parse tree produced by the {@code implication}
	 * labeled alternative in {@link stlParser#formula}.
	 * @param ctx the parse tree
	 */
	void exitImplication(stlParser.ImplicationContext ctx);
	/**
	 * Enter a parse tree produced by the {@code scope}
	 * labeled alternative in {@link stlParser#formula}.
	 * @param ctx the parse tree
	 */
	void enterScope(stlParser.ScopeContext ctx);
	/**
	 * Exit a parse tree produced by the {@code scope}
	 * labeled alternative in {@link stlParser#formula}.
	 * @param ctx the parse tree
	 */
	void exitScope(stlParser.ScopeContext ctx);
	/**
	 * Enter a parse tree produced by the {@code eventually}
	 * labeled alternative in {@link stlParser#formula}.
	 * @param ctx the parse tree
	 */
	void enterEventually(stlParser.EventuallyContext ctx);
	/**
	 * Exit a parse tree produced by the {@code eventually}
	 * labeled alternative in {@link stlParser#formula}.
	 * @param ctx the parse tree
	 */
	void exitEventually(stlParser.EventuallyContext ctx);
	/**
	 * Enter a parse tree produced by the {@code until}
	 * labeled alternative in {@link stlParser#formula}.
	 * @param ctx the parse tree
	 */
	void enterUntil(stlParser.UntilContext ctx);
	/**
	 * Exit a parse tree produced by the {@code until}
	 * labeled alternative in {@link stlParser#formula}.
	 * @param ctx the parse tree
	 */
	void exitUntil(stlParser.UntilContext ctx);
	/**
	 * Enter a parse tree produced by {@link stlParser#diamond}.
	 * @param ctx the parse tree
	 */
	void enterDiamond(stlParser.DiamondContext ctx);
	/**
	 * Exit a parse tree produced by {@link stlParser#diamond}.
	 * @param ctx the parse tree
	 */
	void exitDiamond(stlParser.DiamondContext ctx);
	/**
	 * Enter a parse tree produced by {@link stlParser#square}.
	 * @param ctx the parse tree
	 */
	void enterSquare(stlParser.SquareContext ctx);
	/**
	 * Exit a parse tree produced by {@link stlParser#square}.
	 * @param ctx the parse tree
	 */
	void exitSquare(stlParser.SquareContext ctx);
	/**
	 * Enter a parse tree produced by the {@code product}
	 * labeled alternative in {@link stlParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterProduct(stlParser.ProductContext ctx);
	/**
	 * Exit a parse tree produced by the {@code product}
	 * labeled alternative in {@link stlParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitProduct(stlParser.ProductContext ctx);
	/**
	 * Enter a parse tree produced by the {@code absolute}
	 * labeled alternative in {@link stlParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterAbsolute(stlParser.AbsoluteContext ctx);
	/**
	 * Exit a parse tree produced by the {@code absolute}
	 * labeled alternative in {@link stlParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitAbsolute(stlParser.AbsoluteContext ctx);
	/**
	 * Enter a parse tree produced by the {@code sum}
	 * labeled alternative in {@link stlParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterSum(stlParser.SumContext ctx);
	/**
	 * Exit a parse tree produced by the {@code sum}
	 * labeled alternative in {@link stlParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitSum(stlParser.SumContext ctx);
	/**
	 * Enter a parse tree produced by the {@code value}
	 * labeled alternative in {@link stlParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterValue(stlParser.ValueContext ctx);
	/**
	 * Exit a parse tree produced by the {@code value}
	 * labeled alternative in {@link stlParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitValue(stlParser.ValueContext ctx);
	/**
	 * Enter a parse tree produced by the {@code signal}
	 * labeled alternative in {@link stlParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterSignal(stlParser.SignalContext ctx);
	/**
	 * Exit a parse tree produced by the {@code signal}
	 * labeled alternative in {@link stlParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitSignal(stlParser.SignalContext ctx);
	/**
	 * Enter a parse tree produced by {@link stlParser#constant}.
	 * @param ctx the parse tree
	 */
	void enterConstant(stlParser.ConstantContext ctx);
	/**
	 * Exit a parse tree produced by {@link stlParser#constant}.
	 * @param ctx the parse tree
	 */
	void exitConstant(stlParser.ConstantContext ctx);
	/**
	 * Enter a parse tree produced by {@link stlParser#intValue}.
	 * @param ctx the parse tree
	 */
	void enterIntValue(stlParser.IntValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link stlParser#intValue}.
	 * @param ctx the parse tree
	 */
	void exitIntValue(stlParser.IntValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link stlParser#floatValue}.
	 * @param ctx the parse tree
	 */
	void enterFloatValue(stlParser.FloatValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link stlParser#floatValue}.
	 * @param ctx the parse tree
	 */
	void exitFloatValue(stlParser.FloatValueContext ctx);
}