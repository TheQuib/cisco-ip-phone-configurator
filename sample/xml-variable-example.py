# xml-variable-example.py
# Generates XML based on given variable values (username,password)
# Prints out result, and saves to file

# Import 'os' library
import os

# Get current working directory of script
cwd = os.getcwd()

# Ask user for input
username = input("Please enter your username:\n")
password = input("Please enter your password:\n")

# Place input variables into 'fields' dictionary
fields = {'username': username, 'password': password}

# Format XML, with 'username' and 'password' in it
xml = """<root>
    <user>
        <username>%(username)s</username>
        <password>%(password)s</password>
     </user>
</root>"""

# Save 'xml' variable as string for later use
xmlData = xml%fields

# Print XML to user
print(xmlData)

# Open/create a file under '/xml-output' called 'userData.xml'
file = open(cwd + "\\sample\\xml-output\\userData.xml", "a")
# Write 'xmlData' variable value to file
file.write(xmlData)
# Close the file
file.close()