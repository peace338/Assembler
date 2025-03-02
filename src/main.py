import argparse
import logging
import os
import sys

from .Parser.Parser import Parser
from .Parser.CommandType import CommandType
from .Code.Code import Code
from .Export.Export import Export2Hack

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=str, default = None, help='path of asm file to be translated')
    parser.add_argument('-b', '--build', type=str, default = 'build', help='directory of artifacts')
    return parser.parse_args()

def main(args: argparse.Namespace):

    logger.debug("Starting assembler program")
    logger.debug("input: {}".format(args.input))

    parser = Parser(args.input)
    code = Code()
    exporter = Export2Hack(args.input)

    while parser.hasMoreCommands():
        parser.advance()
        logger.debug("Type: {} \t|currentCommand: {}".format(parser.currentCommandType, parser.currentCommand))
        retCode = 0b0000000000000000
        if parser.currentCommandType == CommandType.C_COMMAND:
            jumpInst = parser.jump()
            destInst = parser.dest()
            compInst = parser.comp()

            logger.debug("{}: {}={};{}".format(parser.currentCommandType, 
                                            destInst,
                                            compInst,
                                            jumpInst))
            
            retCode |= 0b111<<13
            retCode |= code.jump(jumpInst)<<0
            retCode |= code.dest(destInst)<<3
            retCode |= code.comp(compInst)<<6

            logger.info("{}: {:016b}".format(parser.currentCommandType, retCode))
    
        elif parser.currentCommandType == CommandType.A_COMMAND or parser.currentCommandType == CommandType.L_COMMAND:
            retCode |= int(parser.symbol())  
            logger.info("{}: {:016b}".format(parser.currentCommandType, retCode))
        else:
            logger.fatal("parser.currentCommandType has wrong type. not expected.")
            sys.exit(1)
        exporter.writeCode(retCode)

if __name__ == "__main__":
    args = parse_args()

    logging.basicConfig(filename='main.log',
                    filemode='w',
                    level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s")
    logger = logging.getLogger(__name__)

    main(args)