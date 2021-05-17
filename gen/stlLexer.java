// Generated from C:/Users/laure/OneDrive/UAntwerpen/Master 2/Research project 2/STL\stl.g4 by ANTLR 4.8
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class stlLexer extends Lexer {
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
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"OPEN_BRACKET", "CLOSE_BRACKET", "OPEN_CURLY", "CLOSE_CURLY", "OPEN_SQUARE", 
			"CLOSE_SQUARE", "PIPELINE", "MINUS", "PLUS", "STAR", "FORWARD_SLASH", 
			"DOT", "LARGER_THAN", "LARGER_THAN_OR_EQUAL", "SMALLER_THAN", "SMALLER_THAN_OR_EQUAL", 
			"EQUALS", "UNEQUALS", "DIAMOND", "SQUARE", "UNTIL", "AND", "OR", "NEGATE", 
			"ARROW", "DIGIT", "WHITE_SPACE", "SIGNAL", "COMMA"
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


	public stlLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "stl.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\37\u0090\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31"+
		"\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\3\2\3\2\3\3\3"+
		"\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3"+
		"\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\21\3\21\3\21\3\22"+
		"\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26"+
		"\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\31\3\31\3\32\3\32\3\32\3\33"+
		"\6\33}\n\33\r\33\16\33~\3\34\6\34\u0082\n\34\r\34\16\34\u0083\3\34\3\34"+
		"\3\35\3\35\7\35\u008a\n\35\f\35\16\35\u008d\13\35\3\36\3\36\2\2\37\3\3"+
		"\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21"+
		"!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37\3\2"+
		"\7\5\2//\u00ae\u00ae\u00c4\u00c4\3\2\62;\5\2\13\f\17\17\"\"\5\2C\\aac"+
		"|\6\2\62;C\\aac|\2\u0092\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2"+
		"\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25"+
		"\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2"+
		"\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2"+
		"\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3"+
		"\2\2\2\29\3\2\2\2\2;\3\2\2\2\3=\3\2\2\2\5?\3\2\2\2\7A\3\2\2\2\tC\3\2\2"+
		"\2\13E\3\2\2\2\rG\3\2\2\2\17I\3\2\2\2\21K\3\2\2\2\23M\3\2\2\2\25O\3\2"+
		"\2\2\27Q\3\2\2\2\31S\3\2\2\2\33U\3\2\2\2\35W\3\2\2\2\37Z\3\2\2\2!\\\3"+
		"\2\2\2#_\3\2\2\2%a\3\2\2\2\'d\3\2\2\2)h\3\2\2\2+l\3\2\2\2-n\3\2\2\2/r"+
		"\3\2\2\2\61v\3\2\2\2\63x\3\2\2\2\65|\3\2\2\2\67\u0081\3\2\2\29\u0087\3"+
		"\2\2\2;\u008e\3\2\2\2=>\7*\2\2>\4\3\2\2\2?@\7+\2\2@\6\3\2\2\2AB\7}\2\2"+
		"B\b\3\2\2\2CD\7\177\2\2D\n\3\2\2\2EF\7]\2\2F\f\3\2\2\2GH\7_\2\2H\16\3"+
		"\2\2\2IJ\7~\2\2J\20\3\2\2\2KL\7/\2\2L\22\3\2\2\2MN\7-\2\2N\24\3\2\2\2"+
		"OP\7,\2\2P\26\3\2\2\2QR\7\61\2\2R\30\3\2\2\2ST\7\60\2\2T\32\3\2\2\2UV"+
		"\7@\2\2V\34\3\2\2\2WX\7@\2\2XY\7?\2\2Y\36\3\2\2\2Z[\7>\2\2[ \3\2\2\2\\"+
		"]\7>\2\2]^\7?\2\2^\"\3\2\2\2_`\7?\2\2`$\3\2\2\2ab\7#\2\2bc\7?\2\2c&\3"+
		"\2\2\2de\7\u00e4\2\2ef\7\u2016\2\2fg\7\u0162\2\2g(\3\2\2\2hi\7\u00e4\2"+
		"\2ij\7\u2015\2\2jk\7\u00a3\2\2k*\3\2\2\2lm\7W\2\2m,\3\2\2\2no\7\u00e4"+
		"\2\2op\7\u02c8\2\2pq\7\u00a9\2\2q.\3\2\2\2rs\7\u00e4\2\2st\7\u02c8\2\2"+
		"tu\7\u00aa\2\2u\60\3\2\2\2vw\t\2\2\2w\62\3\2\2\2xy\7?\2\2yz\7@\2\2z\64"+
		"\3\2\2\2{}\t\3\2\2|{\3\2\2\2}~\3\2\2\2~|\3\2\2\2~\177\3\2\2\2\177\66\3"+
		"\2\2\2\u0080\u0082\t\4\2\2\u0081\u0080\3\2\2\2\u0082\u0083\3\2\2\2\u0083"+
		"\u0081\3\2\2\2\u0083\u0084\3\2\2\2\u0084\u0085\3\2\2\2\u0085\u0086\b\34"+
		"\2\2\u00868\3\2\2\2\u0087\u008b\t\5\2\2\u0088\u008a\t\6\2\2\u0089\u0088"+
		"\3\2\2\2\u008a\u008d\3\2\2\2\u008b\u0089\3\2\2\2\u008b\u008c\3\2\2\2\u008c"+
		":\3\2\2\2\u008d\u008b\3\2\2\2\u008e\u008f\7.\2\2\u008f<\3\2\2\2\6\2~\u0083"+
		"\u008b\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}