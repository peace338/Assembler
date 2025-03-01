import argparse
from .Parser.Parser import Parser
from .Parser.CommandType import CommandType

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=str, default = None, help='directory of asm file to be translated')

    return parser.parse_args()

def main(args: argparse.Namespace):

    parser = Parser(args.input)
    while parser.hasMoreCommands():
        parser.advance()
        if parser.currentCommandType == CommandType.C_COMMAND:
            print("{}: {}, {}, {}".format(parser.currentCommandType, parser.dest(), parser.comp(), parser.jump()))
        else:
            print("{}: {}".format(parser.currentCommandType, parser.symbol()))
        
if __name__ == "__main__":
    args = parse_args()
    main(args)