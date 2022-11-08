from smiles_string_class import SmilesString
from smiles_strings_list_class import SmilesStringsList

INPUT_NEW_SMILES = 'Enter new smiles '
SMILES_INVALID   = 'SMILES invalid'
SMILES_INSERTED  = 'SMILES Inserted'
#def smiles_from_file_io():


#def smiles_to_file_io():

def input_new_io(list_smiles):
    s = input(INPUT_NEW_SMILES)
    smiles = SmilesString(s)
    if smiles.validate():
        list_smiles.input(smiles)
        print(SMILES_INSERTED)
    else:
        print(SMILES_INVALID)

