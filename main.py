#!/usr/bin/env python3
import scapy.all as scapy
from pydub import AudioSegment
from pydub.playback import play

mp3File = "system-fault.mp3"
sound = AudioSegment.from_mp3(mp3File)


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_final = broadcast/arp_request
    answered_list = scapy.srp(arp_final, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process)


def process(pkt):
    if pkt.haslayer(scapy.ARP):
        try:
            real_mac = get_mac(pkt[scapy.ARP].psrc)
            response_mac = pkt[scapy.ARP].hwsrc
            if real_mac != response_mac:
                play(sound)

        except IndexError:
            pass


with open("interface.txt", "r") as f:
    interface = f.readline()
print("ARP-Spoof-Detector 0.01 by Ravehorn")
print("To use different interface, change the value inside interface.txt.")
sniff(interface)
