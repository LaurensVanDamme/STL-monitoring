// Generated from C:/Users/laure/OneDrive/UAntwerpen/Master 2/Research project 2/STL\stl.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class stlParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		OPEN_BRACKET=1, CLOSE_BRACKET=2, OPEN_CURLY=3, CLOSE_CURLY=4, OPEN_SQUARE=5, 
		CLOSE_SQUARE=6, PIPELINE=7, MINUS=8, PLUS=9, STAR=10, FORWARD_SLASH=11, 
		DOT=12, LARGER_THAN=13, LARGER_THAN_OR_EQUAL=14, SMALLER_THAN=15, SMALLER_THAN_OR_EQUAL=16, 
		EQUALS=17, UNEQUALS=18, DIAMOND=19, SQUARE=20, UNTIL=21, AND=22, OR=23, 
		NEGATE=24, ARROW=25, DIGIT=26, WHITE_SPACE=27, SIGNAL=28, COMMA=29;
	public static final int
		RULE_content = 0, RULE_formula = 1, RULE_diamond = 2, RULE_square = 3, 
		RULE_expression = 4, RULE_constant = 5, RULE_intValue = 6, RULE_floatValue = 7;
	private static String[] makeRuleNames() {
		return new String[] {
			"content", "formula", "diamond", "square", "expression", "constant", 
			"intValue", "floatValue"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'('", "')'", "'{'", "'}'", "'['", "']'", "'|'", "'-'", "'+'", 
			"'*'", "'/'", "'.'", "'>'", "'>='", "'<'", "'<='", "'='", "'!='", "'\u00E2\u2014\u0160'", 
			"'\u00E2\u2013\u00A1'", "'U'", "'\u00E2\u02C6\u00A7'", "'\u00E2\u02C6\u00A8'", 
			null, "'=>'", null, null, null, "','"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "OPEN_BRACKET", "CLOSE_BRACKET", "OPEN_CURLY", "CLOSE_CURLY", "OPEN_SQUARE", 
			"CLOSE_SQUARE", "PIPELINE", "MINUS", "PLUS", "STAR", "FORWARD_SLASH", 
			"DOT", "LARGER_THAN", "LARGER_THAN_OR_EQUAL", "SMALLER_THAN", "SMALLER_THAN_OR_EQUAL", 
			"EQUALS", "UNEQUALS", "DIAMOND", "SQUARE", "UNTIL", "AND", "OR", "NEGATE", 
			"ARROW", "DIGIT", "WHITE_SPACE", "SIGNAL", "COMMA"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "stl.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public stlParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ContentContext extends ParserRuleContext {
		public FormulaContext formula() {
			return getRuleContext(FormulaContext.class,0);
		}
		public TerminalNode EOF() { return getToken(stlParser.EOF, 0); }
		public ContentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_content; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof stlListener ) ((stlListener)listener).enterContent(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof stlListener ) ((stlListener)listener).exitContent(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof stlVisitor ) return ((stlVisitor<? extends T>)visitor).visitContent(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ContentContext content() throws RecognitionException {
		ContentContext _localctx = new ContentContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_content);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(16);
			formula(0);
			setState(17);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FormulaContext extends ParserRuleContext {
		public FormulaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_formula; }
	 
		public FormulaContext() { }
		public void copyFrom(FormulaContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class AlwaysContext extends FormulaContext {
		public SquareContext square() {
			return getRuleContext(SquareContext.class,0);
		}
		public TerminalNode OPEN_CURLY() { return getToken(stlParser.OPEN_CURLY, 0); }
		public List<IntValueContext> intValue() {
			return getRuleContexts(IntValueContext.class);
		}
		public IntValueContext intValue(int i) {
			return getRuleContext(IntValueContext.class,i);
		}
		public TerminalNode COMMA() { return getToken(stlParser.COMMA, 0); }
		public TerminalNode CLOSE_CURLY() { return getToken(stlParser.CLOSE_CURLY, 0); }
		public FormulaContext formula() {
			return getRuleContext(FormulaContext.class,0);
		}
		public AlwaysContext(FormulaContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof stlListener ) ((stlListener)listener).enterAlways(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof stlListener ) ((stlListener)listener).exitAlways(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof stlVisitor ) return ((stlVisitor<? extends T>)visitor).visitAlways(this);
			else return visitor.visitChildren(this);
		}
	}
	public static class BooleanFilterContext extends FormulaContext {
		public TerminalNode OPEN_BRACKET() { return getToken(stlParser.OPEN_BRACKET, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode CLOSE_BRACKET() { return getToken(stlParser.CLOSE_BRACKET, 0); }
		public TerminalNode LARGER_THAN() { return getToken(stlParser.LARGER_THAN, 0); }
		public TerminalNode SMALLER_THAN() { return getToken(stlParser.SMALLER_THAN, 0); }
		public TerminalNode EQUALS() { return getToken(stlParser.EQUALS, 0); }
		public TerminalNode UNEQUALS() { return getToken(stlParser.UNEQUALS, 0); }
		public TerminalNode LARGER_THAN_OR_EQUAL() { return getToken(stlParser.LARGER_THAN_OR_EQUAL, 0); }
		public TerminalNode SMALLER_THAN_OR_EQUAL() { return getToken(stlParser.SMALLER_THAN_OR_EQUAL, 0); }
		public BooleanFilterContext(FormulaContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof stlListener ) ((stlListener)listener).enterBooleanFilter(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof stlListener ) ((stlListener)listener).exitBooleanFilter(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof stlVisitor ) return ((stlVisitor<? extends T>)visitor).visitBooleanFilter(this);
			else return visitor.visitChildren(this);
		}
	}
	public static class NegationContext extends FormulaContext {
		public TerminalNode NEGATE() { return getToken(stlParser.NEGATE, 0); }
		public FormulaContext formula() {
			return getRuleContext(FormulaContext.class,0);
		}
		public NegationContext(FormulaContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof stlListener ) ((stlListener)listener).enterNegation(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof stlListener ) ((stlListener)listener).exitNegation(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof stlVisitor ) return ((stlVisitor<? extends T>)visitor).visitNegation(this);
			else return visitor.visitChildren(this);
		}
	}
	public static class OrContext extends FormulaContext {
		public List<FormulaContext> formula() {
			return getRuleContexts(FormulaContext.class);
		}
		public FormulaContext formula(int i) {
			return getRuleContext(FormulaContext.class,i);
		}
		public TerminalNode OR() { return getToken(stlParser.OR, 0); }
		public OrContext(FormulaContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof stlListener ) ((stlListener)listener).enterOr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof stlListener ) ((stlListener)listener).exitOr(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof stlVisitor ) return ((stlVisitor<? extends T>)visitor).visitOr(this);
			else return visitor.visitChildren(this);
		}
	}
	public static class AndContext extends FormulaContext {
		public List<FormulaContext> formula() {
			return getRuleContexts(FormulaContext.class);
		}
		public FormulaContext formula(int i) {
			return getRuleContext(FormulaContext.class,i);
		}
		public TerminalNode AND() { return getToken(stlParser.AND, 0); }
		public AndContext(FormulaContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof stlListener ) ((stlListener)listener).enterAnd(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof stlListener ) ((stlListener)listener).exitAnd(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof stlVisitor ) return ((stlVisitor<? extends T>)visitor).visitAnd(this);
			else return visitor.visitChildren(this);
		}
	}
	public static class ImplicationContext extends FormulaContext {
		public List<FormulaContext> formula() {
			return getRuleContexts(FormulaContext.class);
		}
		public FormulaContext formula(int i) {
			return getRuleContext(FormulaContext.class,i);
		}
		public TerminalNode ARROW() { return getToken(stlParser.ARROW, 0); }
		public ImplicationContext(FormulaContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof stlListener ) ((stlListener)listener).enterImplication(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof stlListener ) ((stlListener)listener).exitImplication(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof stlVisitor ) return ((stlVisitor<? extends T>)visitor).visitImplication(this);
			else return visitor.visitChildren(this);
		}
	}
	public static class ScopeContext extends FormulaContext {
		public TerminalNode OPEN_BRACKET() { return getToken(stlParser.OPEN_BRACKET, 0); }
		public FormulaContext formula() {
			return getRuleContext(FormulaContext.class,0);
		}
		public TerminalNode CLOSE_BRACKET() { return getToken(stlParser.CLOSE_BRACKET, 0); }
		public ScopeContext(FormulaContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof stlListener ) ((stlListener)listener).enterScope(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof stlListener ) ((stlListener)listener).exitScope(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof stlVisitor ) return ((stlVisitor<? extends T>)visitor).visitScope(this);
			else return visitor.visitChildren(this);
		}
	}
	public static class EventuallyContext extends FormulaContext {
		public DiamondContext diamond() {
			return getRuleContext(DiamondContext.class,0);
		}
		public TerminalNode OPEN_CURLY() { return getToken(stlParser.OPEN_CURLY, 0); }
		public List<IntValueContext> intValue() {
			return getRuleContexts(IntValueContext.class);
		}
		public IntValueContext intValue(int i) {
			return getRuleContext(IntValueContext.class,i);
		}
		public TerminalNode COMMA() { return getToken(stlParser.COMMA, 0); }
		public TerminalNode CLOSE_CURLY() { return getToken(stlParser.CLOSE_CURLY, 0); }
		public FormulaContext formula() {
			return getRuleContext(FormulaContext.class,0);
		}
		public EventuallyContext(FormulaContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof stlListener ) ((stlListener)listener).enterEventually(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof stlListener ) ((stlListener)listener).exitEventually(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof stlVisitor ) return ((stlVisitor<? extends T>)visitor).visitEventually(this);
			else return visitor.visitChildren(this);
		}
	}
	public static class UntilContext extends FormulaContext {
		public List<FormulaContext> formula() {
			return getRuleContexts(FormulaContext.class);
		}
		public FormulaContext formula(int i) {
			return getRuleContext(FormulaContext.class,i);
		}
		public TerminalNode UNTIL() { return getToken(stlParser.UNTIL, 0); }
		public TerminalNode OPEN_CURLY() { return getToken(stlParser.OPEN_CURLY, 0); }
		public List<IntValueContext> intValue() {
			return getRuleContexts(IntValueContext.class);
		}
		public IntValueContext intValue(int i) {
			return getRuleContext(IntValueContext.class,i);
		}
		public TerminalNode COMMA() { return getToken(stlParser.COMMA, 0); }
		public TerminalNode CLOSE_CURLY() { return getToken(stlParser.CLOSE_CURLY, 0); }
		public UntilContext(FormulaContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof stlListener ) ((stlListener)listener).enterUntil(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof stlListener ) ((stlListener)listener).exitUntil(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof stlVisitor ) return ((stlVisitor<? extends T>)visitor).visitUntil(this);
			else return visitor.visitChildren(this);
		}
	}

	public final FormulaContext formula() throws RecognitionException {
		return formula(0);
	}

	private FormulaContext formula(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		FormulaContext _localctx = new FormulaContext(_ctx, _parentState);
		FormulaContext _prevctx = _localctx;
		int _startState = 2;
		enterRecursionRule(_localctx, 2, RULE_formula, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(48);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				{
				_localctx = new BooleanFilterContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(20);
				match(OPEN_BRACKET);
				setState(21);
				expression(0);
				setState(22);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << LARGER_THAN) | (1L << LARGER_THAN_OR_EQUAL) | (1L << SMALLER_THAN) | (1L << SMALLER_THAN_OR_EQUAL) | (1L << EQUALS) | (1L << UNEQUALS))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(23);
				expression(0);
				setState(24);
				match(CLOSE_BRACKET);
				}
				break;
			case 2:
				{
				_localctx = new NegationContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(26);
				match(NEGATE);
				setState(27);
				formula(8);
				}
				break;
			case 3:
				{
				_localctx = new ScopeContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(28);
				match(OPEN_BRACKET);
				setState(29);
				formula(0);
				setState(30);
				match(CLOSE_BRACKET);
				}
				break;
			case 4:
				{
				_localctx = new EventuallyContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(32);
				diamond();
				setState(33);
				match(OPEN_CURLY);
				setState(34);
				intValue();
				setState(35);
				match(COMMA);
				setState(36);
				intValue();
				setState(37);
				match(CLOSE_CURLY);
				setState(38);
				formula(4);
				}
				break;
			case 5:
				{
				_localctx = new AlwaysContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(40);
				square();
				setState(41);
				match(OPEN_CURLY);
				setState(42);
				intValue();
				setState(43);
				match(COMMA);
				setState(44);
				intValue();
				setState(45);
				match(CLOSE_CURLY);
				setState(46);
				formula(3);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(70);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(68);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
					case 1:
						{
						_localctx = new OrContext(new FormulaContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_formula);
						setState(50);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(51);
						match(OR);
						setState(52);
						formula(8);
						}
						break;
					case 2:
						{
						_localctx = new UntilContext(new FormulaContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_formula);
						setState(53);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(54);
						match(UNTIL);
						setState(55);
						match(OPEN_CURLY);
						setState(56);
						intValue();
						setState(57);
						match(COMMA);
						setState(58);
						intValue();
						setState(59);
						match(CLOSE_CURLY);
						setState(60);
						formula(7);
						}
						break;
					case 3:
						{
						_localctx = new AndContext(new FormulaContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_formula);
						setState(62);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(63);
						match(AND);
						setState(64);
						formula(3);
						}
						break;
					case 4:
						{
						_localctx = new ImplicationContext(new FormulaContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_formula);
						setState(65);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(66);
						match(ARROW);
						setState(67);
						formula(2);
						}
						break;
					}
					} 
				}
				setState(72);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class DiamondContext extends ParserRuleContext {
		public TerminalNode SMALLER_THAN() { return getToken(stlParser.SMALLER_THAN, 0); }
		public TerminalNode LARGER_THAN() { return getToken(stlParser.LARGER_THAN, 0); }
		public TerminalNode DIAMOND() { return getToken(stlParser.DIAMOND, 0); }
		public DiamondContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_diamond; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof stlListener ) ((stlListener)listener).enterDiamond(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof stlListener ) ((stlListener)listener).exitDiamond(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof stlVisitor ) return ((stlVisitor<? extends T>)visitor).visitDiamond(this);
			else return visitor.visitChildren(this);
		}
	}

	public final DiamondContext diamond() throws RecognitionException {
		DiamondContext _localctx = new DiamondContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_diamond);
		try {
			setState(76);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case SMALLER_THAN:
				enterOuterAlt(_localctx, 1);
				{
				setState(73);
				match(SMALLER_THAN);
				setState(74);
				match(LARGER_THAN);
				}
				break;
			case DIAMOND:
				enterOuterAlt(_localctx, 2);
				{
				setState(75);
				match(DIAMOND);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SquareContext extends ParserRuleContext {
		public TerminalNode OPEN_SQUARE() { return getToken(stlParser.OPEN_SQUARE, 0); }
		public TerminalNode CLOSE_SQUARE() { return getToken(stlParser.CLOSE_SQUARE, 0); }
		public TerminalNode SQUARE() { return getToken(stlParser.SQUARE, 0); }
		public SquareContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_square; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof stlListener ) ((stlListener)listener).enterSquare(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof stlListener ) ((stlListener)listener).exitSquare(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof stlVisitor ) return ((stlVisitor<? extends T>)visitor).visitSquare(this);
			else return visitor.visitChildren(this);
		}
	}

	public final SquareContext square() throws RecognitionException {
		SquareContext _localctx = new SquareContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_square);
		try {
			setState(81);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case OPEN_SQUARE:
				enterOuterAlt(_localctx, 1);
				{
				setState(78);
				match(OPEN_SQUARE);
				setState(79);
				match(CLOSE_SQUARE);
				}
				break;
			case SQUARE:
				enterOuterAlt(_localctx, 2);
				{
				setState(80);
				match(SQUARE);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionContext extends ParserRuleContext {
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	 
		public ExpressionContext() { }
		public void copyFrom(ExpressionContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class ProductContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode STAR() { return getToken(stlParser.STAR, 0); }
		public TerminalNode FORWARD_SLASH() { return getToken(stlParser.FORWARD_SLASH, 0); }
		public ProductContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof stlListener ) ((stlListener)listener).enterProduct(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof stlListener ) ((stlListener)listener).exitProduct(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof stlVisitor ) return ((stlVisitor<? extends T>)visitor).visitProduct(this);
			else return visitor.visitChildren(this);
		}
	}
	public static class AbsoluteContext extends ExpressionContext {
		public List<TerminalNode> PIPELINE() { return getTokens(stlParser.PIPELINE); }
		public TerminalNode PIPELINE(int i) {
			return getToken(stlParser.PIPELINE, i);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public AbsoluteContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof stlListener ) ((stlListener)listener).enterAbsolute(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof stlListener ) ((stlListener)listener).exitAbsolute(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof stlVisitor ) return ((stlVisitor<? extends T>)visitor).visitAbsolute(this);
			else return visitor.visitChildren(this);
		}
	}
	public static class SumContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode PLUS() { return getToken(stlParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(stlParser.MINUS, 0); }
		public SumContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof stlListener ) ((stlListener)listener).enterSum(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof stlListener ) ((stlListener)listener).exitSum(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof stlVisitor ) return ((stlVisitor<? extends T>)visitor).visitSum(this);
			else return visitor.visitChildren(this);
		}
	}
	public static class ValueContext extends ExpressionContext {
		public ConstantContext constant() {
			return getRuleContext(ConstantContext.class,0);
		}
		public ValueContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof stlListener ) ((stlListener)listener).enterValue(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof stlListener ) ((stlListener)listener).exitValue(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof stlVisitor ) return ((stlVisitor<? extends T>)visitor).visitValue(this);
			else return visitor.visitChildren(this);
		}
	}
	public static class SignalContext extends ExpressionContext {
		public TerminalNode SIGNAL() { return getToken(stlParser.SIGNAL, 0); }
		public SignalContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof stlListener ) ((stlListener)listener).enterSignal(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof stlListener ) ((stlListener)listener).exitSignal(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof stlVisitor ) return ((stlVisitor<? extends T>)visitor).visitSignal(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ExpressionContext expression() throws RecognitionException {
		return expression(0);
	}

	private ExpressionContext expression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpressionContext _localctx = new ExpressionContext(_ctx, _parentState);
		ExpressionContext _prevctx = _localctx;
		int _startState = 8;
		enterRecursionRule(_localctx, 8, RULE_expression, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(90);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PIPELINE:
				{
				_localctx = new AbsoluteContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(84);
				match(PIPELINE);
				setState(85);
				expression(0);
				setState(86);
				match(PIPELINE);
				}
				break;
			case MINUS:
			case DIGIT:
				{
				_localctx = new ValueContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(88);
				constant();
				}
				break;
			case SIGNAL:
				{
				_localctx = new SignalContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(89);
				match(SIGNAL);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(100);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(98);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
					case 1:
						{
						_localctx = new ProductContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(92);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(93);
						_la = _input.LA(1);
						if ( !(_la==STAR || _la==FORWARD_SLASH) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(94);
						expression(6);
						}
						break;
					case 2:
						{
						_localctx = new SumContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(95);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(96);
						_la = _input.LA(1);
						if ( !(_la==MINUS || _la==PLUS) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(97);
						expression(5);
						}
						break;
					}
					} 
				}
				setState(102);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class ConstantContext extends ParserRuleContext {
		public IntValueContext intValue() {
			return getRuleContext(IntValueContext.class,0);
		}
		public FloatValueContext floatValue() {
			return getRuleContext(FloatValueContext.class,0);
		}
		public ConstantContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_constant; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof stlListener ) ((stlListener)listener).enterConstant(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof stlListener ) ((stlListener)listener).exitConstant(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof stlVisitor ) return ((stlVisitor<? extends T>)visitor).visitConstant(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ConstantContext constant() throws RecognitionException {
		ConstantContext _localctx = new ConstantContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_constant);
		try {
			setState(105);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(103);
				intValue();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(104);
				floatValue();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IntValueContext extends ParserRuleContext {
		public TerminalNode DIGIT() { return getToken(stlParser.DIGIT, 0); }
		public TerminalNode MINUS() { return getToken(stlParser.MINUS, 0); }
		public IntValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_intValue; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof stlListener ) ((stlListener)listener).enterIntValue(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof stlListener ) ((stlListener)listener).exitIntValue(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof stlVisitor ) return ((stlVisitor<? extends T>)visitor).visitIntValue(this);
			else return visitor.visitChildren(this);
		}
	}

	public final IntValueContext intValue() throws RecognitionException {
		IntValueContext _localctx = new IntValueContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_intValue);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(108);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==MINUS) {
				{
				setState(107);
				match(MINUS);
				}
			}

			setState(110);
			match(DIGIT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FloatValueContext extends ParserRuleContext {
		public List<TerminalNode> DIGIT() { return getTokens(stlParser.DIGIT); }
		public TerminalNode DIGIT(int i) {
			return getToken(stlParser.DIGIT, i);
		}
		public TerminalNode DOT() { return getToken(stlParser.DOT, 0); }
		public TerminalNode MINUS() { return getToken(stlParser.MINUS, 0); }
		public FloatValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_floatValue; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof stlListener ) ((stlListener)listener).enterFloatValue(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof stlListener ) ((stlListener)listener).exitFloatValue(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof stlVisitor ) return ((stlVisitor<? extends T>)visitor).visitFloatValue(this);
			else return visitor.visitChildren(this);
		}
	}

	public final FloatValueContext floatValue() throws RecognitionException {
		FloatValueContext _localctx = new FloatValueContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_floatValue);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(113);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==MINUS) {
				{
				setState(112);
				match(MINUS);
				}
			}

			setState(115);
			match(DIGIT);
			setState(116);
			match(DOT);
			setState(117);
			match(DIGIT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 1:
			return formula_sempred((FormulaContext)_localctx, predIndex);
		case 4:
			return expression_sempred((ExpressionContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean formula_sempred(FormulaContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 7);
		case 1:
			return precpred(_ctx, 6);
		case 2:
			return precpred(_ctx, 2);
		case 3:
			return precpred(_ctx, 1);
		}
		return true;
	}
	private boolean expression_sempred(ExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 4:
			return precpred(_ctx, 5);
		case 5:
			return precpred(_ctx, 4);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\37z\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\3\2\3\2\3\2\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\63\n\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3G\n\3\f\3\16\3"+
		"J\13\3\3\4\3\4\3\4\5\4O\n\4\3\5\3\5\3\5\5\5T\n\5\3\6\3\6\3\6\3\6\3\6\3"+
		"\6\3\6\5\6]\n\6\3\6\3\6\3\6\3\6\3\6\3\6\7\6e\n\6\f\6\16\6h\13\6\3\7\3"+
		"\7\5\7l\n\7\3\b\5\bo\n\b\3\b\3\b\3\t\5\tt\n\t\3\t\3\t\3\t\3\t\3\t\2\4"+
		"\4\n\n\2\4\6\b\n\f\16\20\2\5\3\2\17\24\3\2\f\r\3\2\n\13\2\u0082\2\22\3"+
		"\2\2\2\4\62\3\2\2\2\6N\3\2\2\2\bS\3\2\2\2\n\\\3\2\2\2\fk\3\2\2\2\16n\3"+
		"\2\2\2\20s\3\2\2\2\22\23\5\4\3\2\23\24\7\2\2\3\24\3\3\2\2\2\25\26\b\3"+
		"\1\2\26\27\7\3\2\2\27\30\5\n\6\2\30\31\t\2\2\2\31\32\5\n\6\2\32\33\7\4"+
		"\2\2\33\63\3\2\2\2\34\35\7\32\2\2\35\63\5\4\3\n\36\37\7\3\2\2\37 \5\4"+
		"\3\2 !\7\4\2\2!\63\3\2\2\2\"#\5\6\4\2#$\7\5\2\2$%\5\16\b\2%&\7\37\2\2"+
		"&\'\5\16\b\2\'(\7\6\2\2()\5\4\3\6)\63\3\2\2\2*+\5\b\5\2+,\7\5\2\2,-\5"+
		"\16\b\2-.\7\37\2\2./\5\16\b\2/\60\7\6\2\2\60\61\5\4\3\5\61\63\3\2\2\2"+
		"\62\25\3\2\2\2\62\34\3\2\2\2\62\36\3\2\2\2\62\"\3\2\2\2\62*\3\2\2\2\63"+
		"H\3\2\2\2\64\65\f\t\2\2\65\66\7\31\2\2\66G\5\4\3\n\678\f\b\2\289\7\27"+
		"\2\29:\7\5\2\2:;\5\16\b\2;<\7\37\2\2<=\5\16\b\2=>\7\6\2\2>?\5\4\3\t?G"+
		"\3\2\2\2@A\f\4\2\2AB\7\30\2\2BG\5\4\3\5CD\f\3\2\2DE\7\33\2\2EG\5\4\3\4"+
		"F\64\3\2\2\2F\67\3\2\2\2F@\3\2\2\2FC\3\2\2\2GJ\3\2\2\2HF\3\2\2\2HI\3\2"+
		"\2\2I\5\3\2\2\2JH\3\2\2\2KL\7\21\2\2LO\7\17\2\2MO\7\25\2\2NK\3\2\2\2N"+
		"M\3\2\2\2O\7\3\2\2\2PQ\7\7\2\2QT\7\b\2\2RT\7\26\2\2SP\3\2\2\2SR\3\2\2"+
		"\2T\t\3\2\2\2UV\b\6\1\2VW\7\t\2\2WX\5\n\6\2XY\7\t\2\2Y]\3\2\2\2Z]\5\f"+
		"\7\2[]\7\36\2\2\\U\3\2\2\2\\Z\3\2\2\2\\[\3\2\2\2]f\3\2\2\2^_\f\7\2\2_"+
		"`\t\3\2\2`e\5\n\6\bab\f\6\2\2bc\t\4\2\2ce\5\n\6\7d^\3\2\2\2da\3\2\2\2"+
		"eh\3\2\2\2fd\3\2\2\2fg\3\2\2\2g\13\3\2\2\2hf\3\2\2\2il\5\16\b\2jl\5\20"+
		"\t\2ki\3\2\2\2kj\3\2\2\2l\r\3\2\2\2mo\7\n\2\2nm\3\2\2\2no\3\2\2\2op\3"+
		"\2\2\2pq\7\34\2\2q\17\3\2\2\2rt\7\n\2\2sr\3\2\2\2st\3\2\2\2tu\3\2\2\2"+
		"uv\7\34\2\2vw\7\16\2\2wx\7\34\2\2x\21\3\2\2\2\r\62FHNS\\dfkns";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}