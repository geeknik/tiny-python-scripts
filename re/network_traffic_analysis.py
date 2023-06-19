
import socket
from scapy.all import *

def network_traffic_analysis(target_ip):
    # Create a raw socket and bind it to the public interface
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    s.bind((target_ip, 0))

    # Include IP headers
    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    # Receive all packages
    s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    # Receive a packet
    while True:
        packet = s.recvfrom(65565)

        # Packet string from tuple
        packet = packet[0]

        # Parse IP header
        ip_header = packet[0:20]

        # Unpack the packet 
        iph = unpack('!BBHHHBBH4s4s' , ip_header)

        # Protocol field
        protocol = iph[6]

        # Continue parsing for ICMP, TCP, and UDP
        if protocol == 1:
            unpack_icmp(packet)
        elif protocol == 6:
            unpack_tcp(packet)
        elif protocol == 17:
            unpack_udp(packet)

    # Disabled promiscuous mode
    s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

def unpack_icmp(packet):
    # Unpack ICMP packet
    u = IP(packet)
    if u.haslayer(ICMP):
        icmp_layer = u.getlayer(ICMP)
        print("ICMP Packet: ", icmp_layer.summary())

def unpack_tcp(packet):
    # Unpack TCP packet
    u = IP(packet)
    if u.haslayer(TCP):
        tcp_layer = u.getlayer(TCP)
        print("TCP Packet: ", tcp_layer.summary())

def unpack_udp(packet):
    # Unpack UDP packet
    u = IP(packet)
    if u.haslayer(UDP):
        udp_layer = u.getlayer(UDP)
        print("UDP Packet: ", udp_layer.summary())
