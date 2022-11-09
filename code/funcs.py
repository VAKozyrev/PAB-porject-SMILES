
from smiles_string_class import SmilesString
from smiles_strings_list_class import SmilesStringsList
import constants as c



def smiles_from_file_io():
    file_name = str(input(">"))
    try:
        with open("file_name", "r") as file_handle:
            smiles_strings_list = file_handle.read()
            return (smiles_strings_list)
    except:
        print(c.FAILED_READING)


def smiles_to_file_io(list_smiles):
    file_name = input(c.INPUT_FILE_NAME)
    f = open(file_name, 'w')
    for i in list_smiles.list_smiles:
        f.write(i.smiles + '\n')
    f.close()

def input_new_io(list_smiles):
    s = input(c.INPUT_NEW_SMILES)
    smiles = SmilesString(s)
    if smiles.validate():
        list_smiles.input(smiles)
        print(c.SMILES_INSERTED)
    else:
        print(c.SMILES_INVALID)


def obtain_molecular_formula(smiles_strings_list):
    return True


