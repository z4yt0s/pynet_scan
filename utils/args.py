import ipaddress
from argparse import ArgumentParser
from modules.CustomError import CustomError

def start_arguments():
    """
    Start the arguments and options for pynet_scan
    Returns:
        - Namespace: An object containing the parsed arguments and their values
    """
    # set info principal parser
    parser = ArgumentParser(
        prog='pynet_scan',
        description='Network Scanner in python with offensive plans',
        epilog='created by: zaytos',
        add_help=True
    )
    # subparser for modes [host, net]
    subparser = parser.add_subparsers(dest='mode', help='operation modes:')

    # set global args
    parser.add_argument(
        '-c', '--color',
        action='store_true',
        help='display report colorized format'
    )
    parser.add_argument(
        '-d', '--debug',
        action='store_true',
        help='shows more detailed errors'
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

"""
Funtion to check if the ip address its valid. If its not valid throw error
Args:
    - ip (str): specify the ip with string format
"""
def __check_ip(ip):
    try:
        ipaddress.IPv4Address(ip)
    except ipaddress.AddressValueError as ave:
        try:
            ipaddress.IPv6Address(ip)
        except ipaddress.AddressValueError as ave:
            raise CustomError(f'Invalid IP address', 10) from ave
    
"""
Funtion to check if the arguments and options has been setted correctly
Args:
    - args (Namespace): An object containing the parsed arguments and their values
"""
def check_args(args):
    if args.mode == 'host':
        CustomError.debug = args.debug
        try:
            __check_ip(args.ip)
        except CustomError as ce:
            ce.detect_error_type()