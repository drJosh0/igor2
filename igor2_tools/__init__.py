import re

def _init_prompt():
    user = input(
'''\nActive instance of IGOR: What would you like to do??
d - download new data from SEC?
s - search existing local files?
t - test BETA tools
q - quit program
\n''')
    return user