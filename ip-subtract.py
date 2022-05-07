import argparse
import ipaddress
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-n1", help="Netz, von dem subtrahiert werden soll",
                    action="store")
parser.add_argument("-n2", help="Netz, das herausgerechnet werden soll",
                    action="store")
args = parser.parse_args()

if len(sys.argv) < 2:
    parser.print_help(sys.stderr)
else:
    netzwerk1_string = args.n1.replace(" ", "")
    netzwerk2_string = args.n2.replace(" ", "")

    address1 = ipaddress.ip_network(netzwerk1_string)
    address2 = ipaddress.ip_network(netzwerk2_string)

    if address1.version is not address2.version:
        raise Exception("Netze müssen die gleiche Version haben (IPv4/IPv6)")

    if not address1.overlaps(address2):
        print("Netze überlappen nicht")
        parser.print_help()
    else:
        ergebnis = address1.address_exclude(address2)
        ergebnis_compact = ipaddress.collapse_addresses(ergebnis)
        ergebnis_string = (', ').join(map(str, ergebnis_compact))

        print(ergebnis_string)