# Ethernet Interface Validation Test

DetectEthernet
GetEthernetMetadata iface=eth0

# Use DHCP
SetDHCP iface=eth0
PingTest ip=8.8.8.8

# Assign static IP
SetStaticIP iface=eth0 ip=192.168.1.200 mask=24
PingTest ip=192.168.1.1

# Interface toggling
ToggleInterface iface=eth0 action=down
ToggleInterface iface=eth0 action=up

# Speed check
SpeedTest iface=eth0

# Frame size test (e.g. 1500 = default, 9000 = jumbo frame)
FrameSizeTest iface=eth0 size=1500
FrameSizeTest iface=eth0 size=9000

# Verify gateway
VerifyConnectivity iface=eth0 gateway=192.168.1.1

# Reset back to DHCP
ResetNetwork iface=eth0
