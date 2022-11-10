import re


string = 'Br'
regex = re.compile('((Cl)|(Br)|[CNIFBOPcno])+(@{0,2}[0-9]{0,1}\({0,1}[\=#\/]{0,1}((Cl)|(Br)|[CNIFBOPcno])+\){0,1}[0-9]{0,1})*')

match = regex.match(string)
print(match.group())