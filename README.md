# Cisco IP Phone Configuration File Generator
XML configuration file generator for Cisco IP Phones | Written in Python

## Requirements
- SIP firmware installed on phone
- FreePBX instance as PBX for phone
- TFTP server with DHCP option 66 (TFTP server) set to it

## Python Requirements
- None! This will run with a base install of Python

### Usage
All you need to do is run generate-xml.py. It will ask you to enter required information, and create a folder under /config with the name of the MAC address of your phone.