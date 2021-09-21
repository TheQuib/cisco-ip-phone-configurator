# generate-xml.py
# Generates configuration files for a Cisco IP Phone for use on FreePBX

import os

# Get current working directory of script
cwd = os.getcwd()

# Welcome message
print("\n\nWelcome! This script will generate XML files for Cisco 49xx phones.\n\n")

# Initialize default variables
phone_index = 1
anotha_one = True

# Ask a yes or no question
def yes_or_no(question):
    reply = str(input(question + ' (y/n): ')).lower().strip()
    if reply[0] == 'y':
        return True
    if reply[0] == 'n':
        return False
    else:
        return yes_or_no("Uhhhh, that wasn't an answer... please enter ")

# Gets all required data from user
def get_data():
    phone_mac = input("\n Enter phone " + str(phone_index) + "'s MAC address ")
    phone_name = input("\n Enter phone" + str(phone_index) + "'s Name ")

    all_data = {'phone_mac': phone_mac, 'phone_name': phone_name}
    return all_data

# Generates XML in variable 'xml_current'
def get_xml(all_data):
    xml_current = """<xml>
        <stuff>
            Yes
        </user>
    </xml>"""
    xml_data = xml_current%all_data
    return xml_data

# Saves the generated XML in a file under /config
def save_xml(xml_data):
    file = open(cwd + "\\generate-xml\\config\\file1.xml", "a")
    file.write(xml_data)
    file.close()

while anotha_one:
    user_input = get_data()
    generate_xml = get_xml(user_input)

    save_xml(generate_xml)
    anotha_one = yes_or_no("Would you like to do another?")