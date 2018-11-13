from netaddr import *


def in_range(your_ip, start, end):
    """Check ip to return True if belong to given range, otherwise return False"""

    ips = IPAddress(your_ip)
    if ips in iter_iprange(IPAddress(start), IPAddress(end), step=1):
        # print("{} in range {} - {}".format(ips, start, end))
        return True
    else:
        # print("{} out range {} - {}".format(ips, start, end))
        return False


if __name__ == '__main__':
    while True:
        try:
            # my_ip = IPAddress(input("enter your ip eg. 10.0.0.200> "))
            start_ip = IPAddress(input("enter your start ip eg. 10.0.0.1> "))
            end_ip = IPAddress(input("enter your end ip eg. 10.0.0.250> "))
        except AddrFormatError as e:  # netaddr.core.AddrFormatError:
            print(e)
            continue
        else:
            break

    filename = input("enter your ip list file name here> ")
    for line in open(filename):
        my_ip = line.strip()
        try:
            if in_range(my_ip, start_ip, end_ip):
                print("{} belong to {} - {}".format(my_ip, start_ip, end_ip), file=open("ip_result.txt", "a"))
            else:
                print("{} out of {} - {}".format(my_ip, start_ip, end_ip), file=open("ip_result.txt", "a"))
        except AddrFormatError as e:
            print("{} is not fucking an ip address".format(my_ip), file=open("ip_result.txt", "a"))
            continue
    else:
        print("\nFinished checking ip in range !")
