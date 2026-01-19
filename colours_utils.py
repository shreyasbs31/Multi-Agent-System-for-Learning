"""
Terminal Color Utilities
========================

ANSI color codes for formatted terminal output.
Provides a simple way to add colors and styling to CLI output.

Usage:
    from colours_utils import Colours
    print(f"{Colours.GREEN}Success!{Colours.RESET}")

Author: Shreyas B S
License: MIT
"""


# ANSI color codes for terminal output
class Colours:
    """ANSI escape codes for terminal text formatting."""
    
    # Text styles
    RESET = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    
    # Foreground colors
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    
    # Background colors
    BG_BLUE = "\033[44m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"