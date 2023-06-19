
import socket
import struct
import textwrap

def ddos_detector(source_ip, dest_ip):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
    except socket.error as msg:
        print('Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
        sys.exit()

    packet = s.recvfrom(65565)

    packet = packet[0]
    ip_header = packet[0:20]

    iph = struct.unpack('!BBHHHBBH4s4s' , ip_header)

    version_ihl = iph[0]
    version = version_ihl >> 4
    ihl = version_ihl & 0xF

    iph_length = ihl * 4

    ttl = iph[5]
    protocol = iph[6]
    s_addr = socket.inet_ntoa(iph[8]);
    d_addr = socket.inet_ntoa(iph[9]);

    if protocol == 6 and s_addr == source_ip and d_addr == dest_ip:
        return True
    else:
        return False

def main():
    source_ip = '192.168.1.1'
    dest_ip = '192.168.1.2'

    if ddos_detector(source_ip, dest_ip):
        print('DDoS attack detected from ' + source_ip + ' to ' + dest_ip)
    else:
        print('No DDoS attack detected')

if __name__ == "__main__":
    main()
