import argparse
import logging
import os
import sys

from .Parser.Parser import Parser
from .Parser.CommandType import CommandType
from .Code.Code import Code
from .Export.Export import Export2Hack
from .SymbolTable.SymbolTable import SymbolTable

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
    symbolTable = SymbolTable()
    logger.info("Starting first pass")
    while parser.hasMoreCommands():
        
        parser.advance()

        if parser.currentCommandType == CommandType.L_COMMAND:   
            logger.debug("CommandType.L_COMMAND is detected.")
            symbol = parser.symbol()

            if not symbolTable.contains(symbol):
                symbolTable.addEntry(symbol, parser.getLineCount())

            logger.debug("add {} with address {}.".format(symbol, parser.getLineCount()))
        else:
            parser.lineCount()

    parser.resetParser()

    logger.info("Starting second pass")
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
            
            exporter.writeCode(retCode)

        elif parser.currentCommandType == CommandType.A_COMMAND:
            symbol = parser.symbol()
            logger.debug("parsed symbol: {}".format(symbol))
            if symbol.isdigit():
                retCode |= int(symbol)  
            else:
                if not symbolTable.contains(symbol):
                    symbolTable.addEntry(symbol, parser.getAddrCount())
                    parser.addrCount()
                retCode |= symbolTable.getAddress(symbol)
            logger.info("{}: {:016b}".format(parser.currentCommandType, retCode))

            exporter.writeCode(retCode)

        elif parser.currentCommandType == CommandType.L_COMMAND:
            pass
        else:
            logger.fatal("parser.currentCommandType has wrong type. not expected.")
            sys.exit(1)
        

if __name__ == "__main__":
    args = parse_args()

    logging.basicConfig(filename='main.log',
                    filemode='w',
                    level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d \n\t- %(message)s")
    logger = logging.getLogger(__name__)

    main(args)