import sys

# load my modules and functions
sys.path.append('./modules')
sys.path.append('./utils')
import utils.args as arguments

if __name__ == '__main__':
    args = arguments.start_arguments()
    arguments.check_args(args)