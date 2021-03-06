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

# Gets all required data from user
def get_data():
    phone_mac = input("(1/) Enter your phone MAC address: ")
    freepbx_ip_address = input("(2/) Enter your FreePBX IP Address: ")
    ssh_user_id = input("(3/) Enter your SSH User ID: ")
    ssh_password = input("(4/) Enter your SSH password: ")
    time_zone = input("(5/) Enter your time zone (Ex: Eastern Standard/Daylight Time): ")
    olson_time_zone = input("(6/) Enter your Olson Time Zone (Ex: America/New_York): ")
    ntp_server = input("(7/) Enter your NTP Server IP Address: ")
    ethernet_phone_port = input("(8/) Enter your ethernet phone port (default 2000): ")
    sip_port = input("(9/) Enter your SIP port (default 5160): ")
    process_node_name = freepbx_ip_address
    phone_label = ("(10/) Enter your phone label (string at top of phone screen): ")

    number_of_lines = input("(11/) Enter the number of lines you want to add: ")
    number_of_lines = int(number_of_lines)
    if number_of_lines == 1:
        print(" Configuring line 2")
        line_2_feature_label = input("   Enter Line Feature Label: ")
        line_2_name = input("   Enter line name: ")
        line_2_auth_name = input("   Enter line auth name: ")
        line_2_auth_password = input("   Enter line auth password: ")
    else:
        line_var_list = []
        currentLine = {}
        for line in range(number_of_lines):
            print(" Currently configuring line " + str(line + 2))

            #List additions of variable names don't work

            #strFeatureLabel = str(currentLine["line_{0}_feature_label".format(line + 2)])
            #line_var_list.append(strFeatureLabel)
            currentLine["line_{0}_feature_label".format(line + 2)] = input("   Enter Line Feature Label: ")


            currentLine["line_{0}_name".format(line + 2)] = input("   Enter line name: ")
            strLineName = currentLine["line_{0}_name".format(line + 2)]
            line_var_list.append(strLineName)

            currentLine["line_{0}_auth_name".format(line + 2)] = input("   Enter line auth name: ")
            strAuthName = currentLine["line_{0}_auth_name".format(line + 2)]
            line_var_list.append(strAuthName)

            currentLine["line_{0}_auth_password".format(line + 2)] = input("   Enter line auth password: ")
            strAuthPassword = currentLine["line_{0}_auth_password".format(line + 2)]
            line_var_list.append(strAuthPassword)

    load_information = input("(12/) Enter your load information (default SIP42.9-4-2SR3-1S): ")
    directory_url = input("(13/) Enter your FreePBX directory URL (default http://" + freepbx_ip_address + "/directory.xml): ")

    all_data = {'phone_mac': phone_mac,
        'freepbx_ip_address': freepbx_ip_address,
        'ssh_user_id': ssh_user_id,
        'ssh_password': ssh_password,
        'time_zone': time_zone,
        'olson_time_zone': olson_time_zone,
        'ntp_server': ntp_server,
        'ethernet_phone_port': ethernet_phone_port,
        'sip_port': sip_port,
        'process_node_name': process_node_name,
        'phone_label': phone_label,
        #Line information: ,
            # Plan:
                # Add each phone line variable into dictionary in for loop via formatted variable name
                # Will create an item in dictionary of {'formattedVariablename': 'formattedVariableValue'}
        'load_information': load_information,
        'directory_url': directory_url,
        }
    return all_data

print(get_data())

while anotha_one:
    user_input = get_data()
    generate_xml = get_xml(user_input)

    save_xml(generate_xml)
    anotha_one = yes_or_no("Would you like to do another?")