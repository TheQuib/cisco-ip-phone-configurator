# Cisco IP Phone Configuration File Generator
Sample XML generator | Written in Python
<br>
<br>
## What does this do?
It's simple! The included script 'xml-variable-example.py' just outputs simple xml to the folder 'xml-output'.
<br>
## Yeah that's great, but what does it **do**?
It's actually pretty simple. Python is a great and versatile language, and it has a function for the use of the '%' symbol.
<br>
<br>
Typically, this is used as a modulus (division that returns the remainder). In the case of this script however, it it a function of the string.format class.
<br>
<br>
If you look, you will find this bit of code:
```python
xmlData = xml%fields
```
In this case, 'fields' is a dictionary, and xmlData is a string that contains the contents of 'xml' and formats 'fields' into it.
<br>
<br>
The 'xml' string looks as such:
```python
xml = """<root>
    <user>
        <username>%(username)s</username>
        <password>%(password)s</password>
     </user>
</root>"""
```
So, taking an in depth look here, you will see '%(username)' and '%(password)'. These are both references to the variables 'username' and 'password'. Basically, Python is piping those variables into the string 'xml'.

## Yeah bro, that was confusing.
Well, here is the flow of data:
<br>
*Accept user input* -> *Create string with XML* -> *Place variables into XML string using %variable*