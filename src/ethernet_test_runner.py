from ethernet_api import EthernetAPI
import sys

def parse_command(line):
    tokens = line.strip().split()
    if not tokens or tokens[0].startswith("#"):
        return None, {}

    cmd = tokens[0]
    args = {}
    for token in tokens[1:]:
        if '=' in token:
            k, v = token.split('=', 1)
            args[k] = v
    return cmd, args

def run_test(file):
    with open(file, 'r') as f:
        for line in f:
            cmd, args = parse_command(line)
            if not cmd:
                continue

            try:
                if cmd == "DetectEthernet":
                    EthernetAPI.DetectEthernet()
                elif cmd == "GetEthernetMetadata":
                    EthernetAPI.GetEthernetMetadata(args["iface"])
                elif cmd == "SetStaticIP":
                    EthernetAPI.SetStaticIP(args["iface"], args["ip"], args["mask"])
                elif cmd == "PingTest":
                    EthernetAPI.PingTest(args["ip"])
                elif cmd == "SpeedTest":
                    EthernetAPI.SpeedTest(args["iface"])
                elif cmd == "ToggleInterface":
                    EthernetAPI.ToggleInterface(args["iface"], args["action"])
                elif cmd == "VerifyConnectivity":
                    EthernetAPI.VerifyConnectivity(args["iface"], args["gateway"])
                elif cmd == "ResetNetwork":
                    EthernetAPI.ResetNetwork(args["iface"])
                elif cmd == "SetDHCP":
                    EthernetAPI.SetDHCP(args["iface"])
                elif cmd == "FrameSizeTest":
                    EthernetAPI.FrameSizeTest(args["iface"], args["size"])
                else:
                    print(f"[ERROR] Unknown command: {cmd}")
            except Exception as e:
                print(f"[ERROR] {cmd} failed: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: sudo python3 ethernet_test_runner.py <test_file.tst>")
        sys.exit(1)

    run_test(sys.argv[1])
