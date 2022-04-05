from whois import whois

from scapy.all import *
from random import randint

def main():
    ans,uans = sr(IP(dst="192.168.82.158")/ICMP())
    for snd,rcv in ans:
        print(rcv.sprintf("%IP.src% is alive now"))
    pass
if __name__ == '__main__':
    main()
