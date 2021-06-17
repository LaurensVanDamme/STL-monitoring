import sys
from stlTree import Node
import pandas as pd
from antlr4 import *
from STLLexer import stlLexer
from customStlListener import customStlListener
from stlParser import stlParser


def main(argv):
    # TODO: Add argument checker

    # Start a timer to time the whole process
    # import time
    # start = time.time()

    # Check the STL fomula
    text = FileStream(argv[1], encoding='utf-8')
    lexer = stlLexer(text)
    stream = CommonTokenStream(lexer)
    parser = stlParser(stream)
    tree = parser.content()

    # Make an STL tree
    listener = customStlListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    parser.addParseListener(listener)
    stlTree = listener.stlTree

    # TODO: make a min length algo that indicates how long signals should be to be validated
    #  + checks if the given is long enough

    # Print the STL tree
    with open('stlTree.dot', 'w') as file:
        stlTree.toDot(file)

    # Read the signals
    signals = pd.read_csv(argv[2])

    # Check if a semantic was given:
    if len(argv) < 4:
        argv.append('quantitative')

    # Validate the signals with the STL formula
    result = stlTree.validate(signals, semantic=argv[3].lower(), plot=True)
    print(result)

    import numpy as np
    numpy_array = np.array(result[:2])
    df = pd.DataFrame(numpy_array.T, columns=['s_t', 's'])
    df.to_csv('angles_ep5_bool.csv', index=False)

    # End the timer of the whole process
    # end = time.time()
    # print(f'time for the full operation: {end - start}s')


if __name__ == '__main__':
    main(sys.argv)
