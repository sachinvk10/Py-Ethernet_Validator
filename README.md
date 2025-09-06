  Py-Ethernet_Validator
  ====================

This is a simple DSL-driven Ethernet test suite for Linux. It allows testers to run network validation with no Python knowledge using `.tst` files.

##  Features

- Ethernet interface detection
- Get IP, MAC, link speed
- Static IP & DHCP configuration
- Ping test & connectivity check
- Link speed validation (ethtool)
- Interface toggle (up/down)
- Frame size test (default & jumbo)
- Gateway reachability check
- Full reset to DHCP

## Example use cases:

Verify DHCP or static IP assignment
Validate physical Ethernet ports during manufacturing
Confirm jumbo frame support (9000 MTU)
Detect and debug link drops
Benchmark wired interface reliability


##  Folder Structure

ethernet_test_suite/
├── README.md
├── src/
│ ├── ethernet_api.py
│ └── ethernet_test_runner.py
└── tests/
└── ethernet_validation.tst

##  Running

	#sudo python3 src/ethernet_test_runner.py tests/ethernet_validation.tst
	

## DSL Command Reference

Command									Description
-------                                 -----------
DetectEthernet							Lists Ethernet interfaces
GetEthernetMetadata						Show MAC, IP, speed
SetStaticIP iface= ip= mask=			Assign static IP
SetDHCP iface=							Request IP via DHCP
PingTest ip=							Ping target IP
SpeedTest iface=						Show interface link speed
FrameSizeTest iface= size=				Ping with custom packet size
ToggleInterface iface= action=up/down	Bring interface up/down
VerifyConnectivity iface= gateway=		Ping gateway
ResetNetwork iface=						Reset to DHCP and release configs


## Build Standalone Executable (PyInstaller)

	1. Install PyInstaller:
		#pip install pyinstaller
		
	2. Build it:
		#pyinstaller --onefile src/ethernet_test_runner.py

	3. Copy the binary and .tst file to tester's environment:
		#ethernet_test_runner  tests/ethernet_validation.tst

	4. Run:
		#sudo ./ethernet_test_runner tests/ethernet_validation.tst



