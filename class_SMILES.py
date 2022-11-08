import re

class Smiles:
    def __init__(self, smiles):
        self.smiles = smiles

    def validate(self):
        expression = '((Cl)|(Br)|[CNIFBOPcno])+(@{0,2}[0-9]{0,1}\({0,1}[\=#\/]{0,1}((Cl)|(Br)|[CNIFBOPcno])+\){0,1}[0-9]{0,1})*'
        match = re.match(expression, self.smiles)
        return match.group() == self.smiles