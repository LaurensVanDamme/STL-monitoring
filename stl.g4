grammar stl;

content
        : formula EOF
        ;

formula
        : OPEN_BRACKET signalExpression (LARGER_THAN|SMALLER_THAN|EQUALS|UNEQUALS|LARGER_THAN_OR_EQUAL|SMALLER_THAN_OR_EQUAL) (expression|signalExpression) CLOSE_BRACKET #booleanFilter
        | (NEGATE|MINUS) formula #negation
        | (SMALLER_THAN LARGER_THAN|DIAMOND) OPEN_CURLY constant COMMA constant CLOSE_CURLY formula #eventually
        | (OPEN_SQUARE CLOSE_SQUARE|SQUARE) OPEN_CURLY constant COMMA constant CLOSE_CURLY formula #always
        | formula AND formula #and
        | formula UNTIL OPEN_CURLY constant COMMA constant CLOSE_CURLY formula #until
        | OPEN_BRACKET formula CLOSE_BRACKET #scope
        | signalExpression #quantitativeSignal

        | formula (OR|PIPELINE) formula #or
        | formula (ARROW|SIGNLE_ARROW|DOUBLE_ARROW) formula #implication
        ;

// To make sure there is a signal on the left of the filter
signalExpression
        : OPEN_BRACKET signalExpression CLOSE_BRACKET #signalExpressionScope
        | expression (STAR|FORWARD_SLASH) signalExpression #signalProduct
        | signalExpression (STAR|FORWARD_SLASH) expression #signalProduct
        | expression (PLUS|MINUS) signalExpression #signalSum
        | signalExpression (PLUS|MINUS) expression #signalSum
        | PIPELINE signalExpression PIPELINE #signalAbsolute
        | SIGNAL #signalSignal
        ;

expression
        : OPEN_BRACKET expression CLOSE_BRACKET #expressionScope
        | expression (STAR|FORWARD_SLASH) expression #product
        | expression (PLUS|MINUS) expression #sum
        | PIPELINE expression PIPELINE #absolute
        | constant #value
        | SIGNAL #signal
        ;

constant
        : intValue
        | floatValue
        ;

intValue
        : MINUS? DIGIT
        ;

floatValue
        : MINUS? DIGIT DOT DIGIT
        ;


OPEN_BRACKET : '(';
CLOSE_BRACKET: ')';
OPEN_CURLY : '{';
CLOSE_CURLY: '}';
OPEN_SQUARE : '[';
CLOSE_SQUARE : ']';
PIPELINE : '|';

MINUS : '-';
PLUS : '+';
STAR : '*';
FORWARD_SLASH : '/';
DOT : '.';

LARGER_THAN : '>';
LARGER_THAN_OR_EQUAL : '>=';
SMALLER_THAN : '<';
SMALLER_THAN_OR_EQUAL : '<=';
EQUALS : '=';
UNEQUALS : '!=';

//INFINITE : 'infty';
DIAMOND : '◊';
SQUARE : '□';
UNTIL : 'U';
AND : [∧^&];
OR : [∨V]; // Or the pipeline
NEGATE : [¬-];
ARROW : '→';
SIGNLE_ARROW : '->';
DOUBLE_ARROW : '=>';

DIGIT : [0-9]+;
WHITE_SPACE : [ \n\r\t]+ -> skip;
SIGNAL : [a-zA-Z_][0-9a-zA-Z]*;
COMMA: ',';



//SEMICOLON: ';';
//AMPERSAND: '&';
//SINGLE_QUOTE : '\'';
//DOUBLE_QUOTE : '"';
//ASCII_CHARACTER : SINGLE_QUOTE [ -~] SINGLE_QUOTE;
//STRING : DOUBLE_QUOTE [ -~]* DOUBLE_QUOTE;
