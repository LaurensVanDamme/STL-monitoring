// Generated from C:/Users/laure/OneDrive/UAntwerpen/Master 2/Research project 2/STL\stl.g4 by ANTLR 4.8
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link stlParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface stlVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link stlParser#content}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitContent(stlParser.ContentContext ctx);
	/**
	 * Visit a parse tree produced by the {@code always}
	 * labeled alternative in {@link stlParser#formula}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlways(stlParser.AlwaysContext ctx);
	/**
	 * Visit a parse tree produced by the {@code booleanFilter}
	 * labeled alternative in {@link stlParser#formula}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBooleanFilter(stlParser.BooleanFilterContext ctx);
	/**
	 * Visit a parse tree produced by the {@code negation}
	 * labeled alternative in {@link stlParser#formula}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNegation(stlParser.NegationContext ctx);
	/**
	 * Visit a parse tree produced by the {@code or}
	 * labeled alternative in {@link stlParser#formula}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitOr(stlParser.OrContext ctx);
	/**
	 * Visit a parse tree produced by the {@code and}
	 * labeled alternative in {@link stlParser#formula}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAnd(stlParser.AndContext ctx);
	/**
	 * Visit a parse tree produced by the {@code implication}
	 * labeled alternative in {@link stlParser#formula}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitImplication(stlParser.ImplicationContext ctx);
	/**
	 * Visit a parse tree produced by the {@code scope}
	 * labeled alternative in {@link stlParser#formula}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitScope(stlParser.ScopeContext ctx);
	/**
	 * Visit a parse tree produced by the {@code eventually}
	 * labeled alternative in {@link stlParser#formula}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitEventually(stlParser.EventuallyContext ctx);
	/**
	 * Visit a parse tree produced by the {@code until}
	 * labeled alternative in {@link stlParser#formula}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUntil(stlParser.UntilContext ctx);
	/**
	 * Visit a parse tree produced by {@link stlParser#diamond}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDiamond(stlParser.DiamondContext ctx);
	/**
	 * Visit a parse tree produced by {@link stlParser#square}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSquare(stlParser.SquareContext ctx);
	/**
	 * Visit a parse tree produced by the {@code product}
	 * labeled alternative in {@link stlParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitProduct(stlParser.ProductContext ctx);
	/**
	 * Visit a parse tree produced by the {@code absolute}
	 * labeled alternative in {@link stlParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAbsolute(stlParser.AbsoluteContext ctx);
	/**
	 * Visit a parse tree produced by the {@code sum}
	 * labeled alternative in {@link stlParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSum(stlParser.SumContext ctx);
	/**
	 * Visit a parse tree produced by the {@code value}
	 * labeled alternative in {@link stlParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitValue(stlParser.ValueContext ctx);
	/**
	 * Visit a parse tree produced by the {@code signal}
	 * labeled alternative in {@link stlParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSignal(stlParser.SignalContext ctx);
	/**
	 * Visit a parse tree produced by {@link stlParser#constant}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitConstant(stlParser.ConstantContext ctx);
	/**
	 * Visit a parse tree produced by {@link stlParser#intValue}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIntValue(stlParser.IntValueContext ctx);
	/**
	 * Visit a parse tree produced by {@link stlParser#floatValue}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFloatValue(stlParser.FloatValueContext ctx);
}