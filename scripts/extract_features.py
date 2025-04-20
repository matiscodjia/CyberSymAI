import csv
from datetime import datetime
from scapy.all import rdpcap
import sys
print("👾 Python utilisé :", sys.executable)

def extract_features(pcap_file):
    packets = rdpcap(pcap_file)
    features = {
        'timestamp': datetime.now().isoformat(),
        'total': len(packets),
        'tcp': sum(1 for p in packets if p.haslayer('TCP')),
        'udp': sum(1 for p in packets if p.haslayer('UDP')),
        'icmp': sum(1 for p in packets if p.haslayer('ICMP')),
    }
    return features

def save_features_to_csv(features, csv_path="../data/processed/features.csv"):

    fieldnames = ['timestamp', 'total', 'tcp', 'udp', 'icmp']
    # Crée le fichier avec en-tête s’il n’existe pas
    try:
        with open(csv_path, 'r') as f:
            header_exists = True
    except FileNotFoundError:
        header_exists = False

    with open(csv_path, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not header_exists:
            writer.writeheader()
        writer.writerow(features)

if __name__ == "__main__":
    pcap_path = "../data/pcap/capture.pcap"  # <-- modifie ici si besoin
    features = extract_features(pcap_path)
    save_features_to_csv(features)
    print("✅ Features saved to CSV:")
    print(features)
