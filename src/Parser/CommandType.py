from enum import Enum

class CommandType(Enum):
    A_COMMAND = 'A_COMMAND'  # For @xxx where xxx is a symbol or a decimal number
    C_COMMAND = 'C_COMMAND'  # For dest=comp;jump
    L_COMMAND = 'L_COMMAND'  # For (xxx) where xxx is a symbol