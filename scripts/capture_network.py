import subprocess

def capture(interface='eth0', duration=5, output='../data/pcap/capture.pcap'):
    print(f"Capturing for {duration}s on {interface}")
    subprocess.run(["sudo", "timeout", str(duration), "tcpdump", "-i", interface, "-w", output])

if __name__ == "__main__":
    capture(interface="wlp1s0")
