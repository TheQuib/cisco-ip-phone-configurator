# Cisco IP Phone Configuration File Generator
XML configuration file generator for Cisco IP Phones | Written in Python
<br>
<br>
## PLEAE NOTE:
This is not a complete project. I am putting my progress up on GitHub as a way to track it, and for others to follow up if they so choose. Please do not use these files until I release them officially via this repository's releases.
<br>
<br>

## Requirements
- SIP firmware installed on phone
  - Instructions below
- FreePBX instance on same network as phones
- Cisco IP Phone 79xx phones
- TFTP server on same network as phones
- DHCP option 66 set to the IP/DNS of TFTP server

## Python Requirements
**None!** This will run with a base install of Python

## Usage
All you need to do is run generate-xml.py. It will ask you to enter required information, and create a directory under /config with the name of the MAC address of your phone.
