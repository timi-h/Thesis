from scapy.all import *

# MQTT PUBLISH Packet - Benign
mqtt_publish = (
    b"\x30"              # MQTT Control Packet Type (PUBLISH)
    b"\x1a"              # Remaining Length
    b"\x00\x0b"          # Topic Name Length
    b"smart/grid"        # Topic Name
    b"\x00\x0d"          # Packet Identifier
    b"power: 500W"       # Payload (Example: Power consumption data)
)

# Send benign packet
send(IP(dst="192.168.226.128")/TCP(dport=1883)/Raw(load=mqtt_publish))
