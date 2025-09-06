import subprocess
import re

class EthernetAPI:

    @staticmethod
    def DetectEthernet():
        print("[DetectEthernet] Scanning Ethernet interfaces...")
        output = subprocess.check_output(["ip", "-o", "link", "show"]).decode()
        interfaces = [
            line.split(":")[1].strip()
            for line in output.strip().split("\n")
            if "ether" in line
        ]
        print(f"[DetectEthernet] Found interfaces: {interfaces}")
        return interfaces

    @staticmethod
    def GetEthernetMetadata(iface):
        print(f"[GetEthernetMetadata] Getting metadata for {iface}...")
        try:
            ip_addr = subprocess.getoutput(f"ip addr show {iface}")
            mac = re.search(r"link/ether ([0-9a-f:]+)", ip_addr)
            inet = re.search(r"inet ([0-9\.]+)", ip_addr)

            speed_output = subprocess.getoutput(f"ethtool {iface}")
            speed = re.search(r"Speed: (.+)", speed_output)

            print(f"  Interface: {iface}")
            print(f"  MAC: {mac.group(1) if mac else 'N/A'}")
            print(f"  IP: {inet.group(1) if inet else 'N/A'}")
            print(f"  Speed: {speed.group(1) if speed else 'N/A'}")
        except Exception as e:
            print(f"[GetEthernetMetadata] Error: {e}")

    @staticmethod
    def SetStaticIP(iface, ip, mask):
        print(f"[SetStaticIP] Assigning static IP {ip}/{mask} to {iface}...")
        subprocess.run(["sudo", "ip", "addr", "flush", "dev", iface])
        subprocess.run(["sudo", "ip", "addr", "add", f"{ip}/{mask}", "dev", iface])
        subprocess.run(["sudo", "ip", "link", "set", iface, "up"])
        print("[SetStaticIP] Static IP set.")

    @staticmethod
    def PingTest(ip):
        print(f"[PingTest] Pinging {ip}...")
        result = subprocess.run(["ping", "-c", "4", ip], stdout=subprocess.PIPE)
        output = result.stdout.decode()
        if "0% packet loss" in output:
            print("[PingTest]  Ping successful")
        else:
            print("[PingTest]  Ping failed or packet loss detected")

    @staticmethod
    def SpeedTest(iface):
        print(f"[SpeedTest] Checking link speed for {iface}...")
        output = subprocess.getoutput(f"ethtool {iface}")
        match = re.search(r"Speed: (.+)", output)
        if match:
            print(f"[SpeedTest] Speed: {match.group(1)}")
        else:
            print("[SpeedTest] Could not determine speed.")

    @staticmethod
    def ToggleInterface(iface, action):
        print(f"[ToggleInterface] Setting interface {iface} {action}...")
        subprocess.run(["sudo", "ip", "link", "set", iface, action])
        print(f"[ToggleInterface] Interface {iface} is now {action}.")

    @staticmethod
    def VerifyConnectivity(iface, gateway):
        print(f"[VerifyConnectivity] Checking connectivity to {gateway} from {iface}...")
        result = subprocess.run(["ping", "-I", iface, "-c", "3", gateway], stdout=subprocess.PIPE)
        if "0% packet loss" in result.stdout.decode():
            print("[VerifyConnectivity]  Gateway reachable")
        else:
            print("[VerifyConnectivity]  Gateway unreachable or packet loss")

    @staticmethod
    def ResetNetwork(iface):
        print(f"[ResetNetwork] Resetting interface {iface} to DHCP...")
        subprocess.run(["sudo", "dhclient", "-r", iface])
        subprocess.run(["sudo", "dhclient", iface])
        print("[ResetNetwork] DHCP reconfigured.")

    @staticmethod
    def SetDHCP(iface):
        print(f"[SetDHCP] Enabling DHCP on {iface}...")
        subprocess.run(["sudo", "dhclient", "-v", iface])
        print("[SetDHCP] DHCP enabled.")

    @staticmethod
    def FrameSizeTest(iface, size):
        print(f"[FrameSizeTest] Testing frame size {size} on {iface}...")
        result = subprocess.run(["ping", "-M", "do", "-s", str(int(size) - 28), "-c", "3", "8.8.8.8", "-I", iface], stdout=subprocess.PIPE)
        print(result.stdout.decode())
