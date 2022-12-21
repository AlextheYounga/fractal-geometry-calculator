import sys
import colored
from colored import stylize
import os
import sys

# Forcing Python to recognize parent folder.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

# This is some code I reuse for any scripting projects I have.
# It's probably too complex for a project with only one command but it works.

def fractal_calculate_controller(args):
    from fractalgeometrycalculator.fractal_calculate import fractalCalculator
    fractalCalculator()

def main():
    sys.argv.pop(0)

    args = [arg.strip() for arg in sys.argv]

    if (':' in args[0]):
        command = args.pop(0)
        program = command.split(':')[0] + "_controller"
        subroutine = command.split(':')[1]

        globals()[program](subroutine, args)
        return
    else:
        program = args.pop(0) + "_controller"

        globals()[program](args)
        return


if __name__ == '__main__':
    main()
