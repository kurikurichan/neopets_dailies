from neobot import NeoBot
from login import username, pw

# Run dailies through each username & password provided
for idx, un in enumerate(username):
    NeoBot(un, pw[idx])


# Needs to run with an IP address for the virtual machine
# works locally because it's pulling fromt he internet
