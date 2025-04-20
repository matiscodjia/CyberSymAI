from scapy.all import rdpcap

packets = rdpcap("../data/pcap/capture.pcap")
for p in packets[:5]:
    print(p.summary())