import argparse
from .Parser.Parser import Parser

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=str, default = None, help='directory of asm file to be translated')

    return parser.parse_args()

def main(args: argparse.Namespace):

    parser = Parser(args.input)
    while parser.hasMoreCommands():
        parser.advance()
        print(parser.currentCommand)
        
if __name__ == "__main__":
    args = parse_args()
    main(args)