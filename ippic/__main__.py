import argparse, netaddr, sys
from .ipv6 import _ipv6
from .ipv4 import _ipv4


def main():
    parser = argparse.ArgumentParser(description="Create an image from an IP")
    parser.add_argument("ip", action="store", help="IP")
    parser.add_argument("-d", action="store_true", help="debug")
    args = parser.parse_args()

    if netaddr.valid_ipv6(args.ip):
        _ipv6(ip=args.ip, debug=args.d)
    elif netaddr.valid_ipv4(args.ip):
        _ipv4(ip=args.ip, debug=args.d)
    else:
        sys.stderr.write("Please provide a valid IP address.\n")


if __name__ == "__main__":
    main()
