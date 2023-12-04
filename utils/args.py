# PSEUDO CODE
# Set up the info, modes and general arguments
# We check modes and based on the value we set the specific arguments of that mode
# Return both args [global && specific]
from argparse import ArgumentParser

def start_arguments():
    """ Return the arguments setted by the user
    Returns:
        tuple: A tuple with global args and specific mode args
            - global_args: general arguments of the tool
            - specific_mode_args: arguments of specific mode
    """
    # set info principal parser
    parser = ArgumentParser(
        prog='pynet_scan',
        description='Network Scanner in python with offensive plans',
        epilog='created by: zaytos',
        add_help=False
    )
    # subparser for modes [host, net]
    subparser = parser.add_subparsers(dest='mode', help='operation modes:')

    # set global args
    parser.add_argument(
        '-c', '--color',
        action='store_true',
        help='display report colorized format'
    )

    # set mode 'HOST' and him args
    host_parser = subparser.add_parser('host', help='scan a specific host')
    host_parser.add_argument(
        'ip',
        action='store', type=str,
        help='specify de ip of target'
    )
    
    # set mode 'NET' and him args
    net_parser = subparser.add_parser('net', help='scan a specific network')
    net_parser.add_argument(
        'network_ip',
        action='store', type=str,
        help='specify the network address'
    )
    net_parser.add_argument(
        '-m', '--mask',
        action='store', type=str,
        help='specify the mask of the network'
    )
    return parser.parse_args()