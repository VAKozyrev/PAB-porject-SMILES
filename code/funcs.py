from smiles_string_class import SmilesString
from smiles_strings_list_class import SmilesStringsList
import constants as c



def print_help_message():
    mes = ['C: count the number of times each sub-string from an external list (given file) occurs in the SMILES strings of the list.',
            'M: Count the number of times each atomic element occurs in the strings in the list and obtain the molecular formula (number of atoms of each element, e.g., C8NO2). The output of the command should appear in the terminal and be in lexicographic order.',
            'D: compare a given pair of molecules from their SMILES representation (calculate their dissim- ilarity, i.e., sum of squared differences between the number of occurrences of the sub-strings in two SMILES).',
            'S: select all SMILES strings in the list containing a given (set of) sub-structure(s). The set may be given by the user or read from a file (one substructure per line). The output of the command should appear in the terminal and be in lexicographic order.',
            'I: input a new SMILES string to be added to the current list, if valid (if not, the application reports it found a problem and waits for the user’s to input a new command).']

    for str in mes:
        print(str)


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