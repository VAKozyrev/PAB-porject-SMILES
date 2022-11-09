from smiles_string_class import SmilesString
from smiles_strings_list_class import SmilesStringsList
import constants as c


def read_command(text):
    command = input(str(text))
    return command


def open_file(file_name):
    try:
        with open(str(file_name), 'r') as file_handle:
            return True
    except:
        return False


def read_from_file(file_name):
    with open(str(file_name), 'r') as file_handle:
        smiles_strings_list = file_handle.read()
        return smiles_strings_list


def input_new_smiles(smiles_list):
    string = read_command(c.INPUT_NEW_SMILES)
    smiles_string = SmilesString(string)
    if smiles_string.validate():
        if smiles_string not in smiles_list:
            smiles_list.add_smiles_string(smiles_string)
            print(c.SMILES_INSERTED)
        else:
            print(c.SMILES_ALREADY_LOADED)

    else:
        print(c.SMILES_INVALID)


def obtain_molecular_formula(smiles_list):
    return True
