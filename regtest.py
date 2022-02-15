import re

# '\b0*([1-9][0-9]*|0)\b'

mystr = "00009089"

nbr = re.sub( "^0+(?!$)", "" , mystr)

print(nbr)