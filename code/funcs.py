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
    validated_smiles = []
    with open(str(file_name), 'r') as file_handle:
        all_strings_list = file_handle.readlines()[1:] # read from 2nd line
        for i in all_strings_list:
            smiles = SmilesString(i)
            if smiles.validate():
                validated_smiles.append(smiles)
        smiles_list = SmilesStringsList(validated_smiles.sort())
        return smiles_list


def write_to_file(smiles_list):
    file_name = read_command(c.INPUT_FILE_NAME)
    f = open(str(file_name), 'w')
    for i in smiles_list.smiles_list:
        f.write(i.smiles + '\n')
    f.close()



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
    for elem in smiles_list:
        smiles_string = smiles_list.get_smiles_string(elem)
        molecular_formula = smiles_string.get_molecular_formula()
        result = smiles_string + " " + "is" + " " + molecular_formula
        print(molecular_formula)