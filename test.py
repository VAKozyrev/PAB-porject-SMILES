import re

res = re.search("((Cl)|(Br)|[CNIFBOPcno])+(@{0,2}[0-9]{0,1}\({0,1}[\=#\/]{0,1}((Cl)|(Br)|[CNIFBOPcno])+\){0,1}[0-9]{0,1})*", 'CO()O')
print(res.groups())
