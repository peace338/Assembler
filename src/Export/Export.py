import os
import sys

class Export2Hack():
    def __init__(self, inputPath: str):

        self.__file = open(self.__exportFilePath(inputPath), "w")

    def __del__(self):
        if self.__file:
            self.__file.close()

    def writeCode(self, code: int):
        if self.__file.tell() == 0:
            self.__file.write(format(code, '016b'))
        else:
            self.__file.write("\n"+ format(code, '016b'))

    def __exportFilePath(self, inputPath: str) -> str:
        self.__validateInput(inputPath)
        filename = os.path.basename(inputPath).split('.')[0] + '.hack'
        filedir = os.path.dirname(inputPath)
        filepath = os.path.join(filedir, filename)

        return filepath
    
    
    def __validateInput(self, inputPath: str): 

        if os.path.exists(inputPath):
            pass
        else:
            print("The file does not exist in the {}".format(inputPath), file=sys.stderr)
            sys.exit(1) 