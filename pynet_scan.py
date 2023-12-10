import sys

# load my modules and functions
sys.path.append('./modules')
sys.path.append('./utils')
import utils.args as arguments
from modules.Visuals import Visuals

# instace objects
vs = Visuals()

if __name__ == '__main__':
    vs.banner()
    
    args = arguments.start_arguments()
    arguments.check_args(args)