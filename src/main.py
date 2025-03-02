import argparse
from .Parser.Parser import Parser
from .Parser.CommandType import CommandType
from .Code.Code import Code
import logging

logging.basicConfig(filename='main.log',
                    filemode='w',
                    level=logging.DEBUG)

logger = logging.getLogger(__name__)

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=str, default = None, help='directory of asm file to be translated')

    return parser.parse_args()

def main(args: argparse.Namespace):

    logger.info("Starting assembler program")

    parser = Parser(args.input)
    code = Code()
    while parser.hasMoreCommands():
        parser.advance()
        retCode = 0b0000000000000000
        if parser.currentCommandType == CommandType.C_COMMAND:
            retCode |= 0b111<<13
            retCode |= code.jump(parser.jump())<<0
            retCode |= code.dest(parser.dest())<<4
            retCode |= code.comp(parser.comp())<<7
            logger.info("{}: {:016b}".format(parser.currentCommandType, retCode))
        
        else:
            retCode |= int(parser.symbol())
            logger.info("{}: {:016b}".format(parser.currentCommandType, retCode))
        
if __name__ == "__main__":
    args = parse_args()
    main(args)