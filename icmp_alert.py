from scapy.all import *

selks_ip = "192.168.226.128"  # Replace with your SELKS IP
spoofed_ip = "8.8.8.8"       # Example of spoofing

# Craft ICMP Echo Request with invalid icode
pkt = IP(src=spoofed_ip, dst=selks_ip) / ICMP(type=8, code=19) / b"MaliciousPayload"
send(pkt)
