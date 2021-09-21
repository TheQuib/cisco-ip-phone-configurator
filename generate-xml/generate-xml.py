# generate-xml.py
# Generates configuration files for a Cisco IP Phone for use on FreePBX

print("\n\nWelcome! This script will generate XML files for Cisco 49xx phones.\n\n")

#Initialize current phone index number for visuals
phone_index = 1

def get_data():
    #Get user input
    phone_mac = input(" Enter phone " + str(phone_index) + "'s MAC address\n")
    phone_name = input(" Enter phone" + str(phone_index) + "'s Name")

