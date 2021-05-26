
BREAK_LINE = '-'*60

class Colours:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'  # yellow
    FAIL = '\033[91m'  # red color
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    PLAYER1 = '\033[94m'
    PLAYER2 = '\033[96m'

# Value	Description	Behavior
# 0	Default	Returns all attributes to the default state prior to modification
# 1	Bold/Bright	Applies brightness/intensity flag to foreground color
# 4	Underline	Adds underline
# 24	No underline	Removes underline
# 7	Negative	Swaps foreground and background colors
# 27	Positive (No negative)	Returns foreground/background to normal
# 30	Foreground Black	Applies non-bold/bright black to foreground
# 31	Foreground Red	Applies non-bold/bright red to foreground
# 32	Foreground Green	Applies non-bold/bright green to foreground
# 33	Foreground Yellow	Applies non-bold/bright yellow to foreground
# 34	Foreground Blue	Applies non-bold/bright blue to foreground
# 35	Foreground Magenta	Applies non-bold/bright magenta to foreground
# 36	Foreground Cyan	Applies non-bold/bright cyan to foreground
# 37	Foreground White	Applies non-bold/bright white to foreground
# 38	Foreground Extended	Applies extended color value to the foreground (see details below)
# 39	Foreground Default	Applies only the foreground portion of the defaults (see 0)
# 40	Background Black	Applies non-bold/bright black to background
# 41	Background Red	Applies non-bold/bright red to background
# 42	Background Green	Applies non-bold/bright green to background
# 43	Background Yellow	Applies non-bold/bright yellow to background
# 44	Background Blue	Applies non-bold/bright blue to background
# 45	Background Magenta	Applies non-bold/bright magenta to background
# 46	Background Cyan	Applies non-bold/bright cyan to background
# 47	Background White	Applies non-bold/bright white to background
# 48	Background Extended	Applies extended color value to the background (see details below)
# 49	Background Default	Applies only the background portion of the defaults (see 0)
# 90	Bright Foreground Black	Applies bold/bright black to foreground
# 91	Bright Foreground Red	Applies bold/bright red to foreground
# 92	Bright Foreground Green	Applies bold/bright green to foreground
# 93	Bright Foreground Yellow	Applies bold/bright yellow to foreground
# 94	Bright Foreground Blue	Applies bold/bright blue to foreground
# 95	Bright Foreground Magenta	Applies bold/bright magenta to foreground
# 96	Bright Foreground Cyan	Applies bold/bright cyan to foreground
# 97	Bright Foreground White	Applies bold/bright white to foreground
# 100	Bright Background Black	Applies bold/bright black to background
# 101	Bright Background Red	Applies bold/bright red to background
# 102	Bright Background Green	Applies bold/bright green to background
# 103	Bright Background Yellow	Applies bold/bright yellow to background
# 104	Bright Background Blue	Applies bold/bright blue to background
# 105	Bright Background Magenta	Applies bold/bright magenta to background
# 106	Bright Background Cyan	Applies bold/bright cyan to background
# 107	Bright Background White	Applies bold/bright white to background