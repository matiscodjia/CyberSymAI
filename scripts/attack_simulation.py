from scapy.all import IP, ICMP, TCP, UDP, send
import time
import random
import argparse

def icmp_flood(target_ip, duration):
    print(f"[!] ICMP flood sur {duration}s vers {target_ip}")
    end_time = time.time() + duration
    while time.time() < end_time:
        pkt = IP(dst=target_ip)/ICMP()
        send(pkt, verbose=False)
        time.sleep(random.uniform(0.005, 0.02))

def tcp_scan(target_ip, duration):
    print(f"[!] TCP scan sur {duration}s vers {target_ip}")
    end_time = time.time() + duration
    while time.time() < end_time:
        port = random.randint(20, 1024)
        pkt = IP(dst=target_ip)/TCP(dport=port, flags="S")
        send(pkt, verbose=False)
        time.sleep(random.uniform(0.01, 0.05))

def udp_spam(target_ip, duration):
    print(f"[!] UDP spam sur {duration}s vers {target_ip}")
    end_time = time.time() + duration
    while time.time() < end_time:
        port = random.randint(1024, 65535)
        size = random.randint(10, 200)
        pkt = IP(dst=target_ip)/UDP(dport=port)/bytes([random.randint(0, 255)] * size)
        send(pkt, verbose=False)
        time.sleep(random.uniform(0.01, 0.03))

def normal_traffic(target_ip, duration):
    print(f"[+] Trafic normal sur {duration}s vers {target_ip}")
    end_time = time.time() + duration
    while time.time() < end_time:
        proto = random.choices(['tcp', 'udp', 'icmp'], weights=[0.5, 0.4, 0.1])[0]
        if proto == 'tcp':
            pkt = IP(dst=target_ip)/TCP(dport=random.randint(80, 443), flags="A")
        elif proto == 'udp':
            pkt = IP(dst=target_ip)/UDP(dport=random.randint(1024, 65535))/b"Hello"
        else:
            pkt = IP(dst=target_ip)/ICMP()
        send(pkt, verbose=False)
        time.sleep(random.uniform(0.1, 0.4))

def run_scenario(target_ip, mode, duration):
    if mode == "icmp":
        icmp_flood(target_ip, duration)
    elif mode == "tcp":
        tcp_scan(target_ip, duration)
    elif mode == "udp":
        udp_spam(target_ip, duration)
    elif mode == "normal":
        normal_traffic(target_ip, duration)
    elif mode == "mixed":
        print(f"[+] Scénario mixte sur {duration}s")
        start_time = time.time()
        while time.time() - start_time < duration:
            phase = random.choice(["normal", "icmp", "tcp", "udp"])
            t = random.uniform(2, 6)
            print(f"--> Phase {phase} pendant {t:.1f}s")
            run_scenario(target_ip, phase, t)
    else:
        print("Mode inconnu. Choisir entre: normal, icmp, tcp, udp, mixed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("target", help="IP cible")
    parser.add_argument("mode", help="Mode: normal, icmp, tcp, udp, mixed")
    parser.add_argument("--duration", type=int, default=10, help="Durée (s)")
    args = parser.parse_args()

    run_scenario(args.target, args.mode, args.duration)