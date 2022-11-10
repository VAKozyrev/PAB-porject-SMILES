from smiles_string_class import SmilesString
from smiles_strings_list_class import SmilesStringsList
import smiles_strings_list_class as s
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


def validate_smiles(smiles_list):
    validated_smiles = []
    for i in smiles_list:
        smiles = SmilesString(i)
        if smiles.validate():
            validated_smiles.append(smiles)
    smiles_list_class = SmilesStringsList(validated_smiles.sort())
    return smiles_list_class

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

def read_substrings_from_file(file_name):
    file_name = read_command(c.PROMPT)
    with open(str(file_name), 'r') as file_handle:
        substring_list = file_handle.read()
        return substring_list

!!!!!!!!!else:
 !!!!!!!       print(c.SMILES_INVALID)


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
        if smiles_string not in smiles_list.smiles_list:
            smiles_list.add_smiles_string(smiles_string)
            print(c.SMILES_INSERTED)
        else:
            print(c.SMILES_ALREADY_LOADED)


def read_from_file(file_name, string_from):
    file_handle = open(str(file_name), 'r')
    all_strings_list = file_handle.readlines()[string_from:] # read from 2nd line
    file_handle.close()
    return all_strings_list


def read_from_terminal(num_of_strings):
    substrings_list = []
    while num_of_strings > 0:
        smiles = read_command(c.PROMPT)
        substrings_list.append(smiles)
    return substrings_list


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




def obtain_molecular_formula(smiles_list):
    for smiles in smiles_list:
        smiles_string = smiles_list.get_smiles_string(smiles)
        molecular_formula = smiles_string.get_molecular_formula()
        result = smiles_string + " " + "is" + " " + molecular_formula
        print(result)


def count_occurances(string, substring):
    counter = 0
    occurances = 0
    while counter < len(string):
        if string[counter: counter + len(substring)] == substring:
            occurances += 1
            counter += len(substring)
        else: counter += 1
    return occurances

def count_occurences_io(smiles_list):
    answer = input(c.INPUT_SOURSE)
    while answer != c.FILE and answer != c.TERMINAL:
        print(c.INVALID_ANSWER)
        answer = input(c.INPUT_SOURSE)
    if answer == c.FILE:
        file_name = input(c.INPUT_FILE_NAME)
        substring_list = read_substrings_from_file(file_name)
    else:
        substring_list = []
        number_of_substrings = int(input('input number of substrings: '))
        for i in range(number_of_substrings):
            substring = input()
            substring_list.append(substring)
    smiles_list.count_substrings(substring_list)


def count_dissimilarity(str1,str2,substring_list):
        branches1 = s.separate_branches(str1)
        branches2 = s.separate_branches(str2)
        dissimilarity = 0
        for i in substring_list:
            occurences1 = 0
            occurences2 = 0
            for k in branches1:
                occurences1 += count_occurances(k, i)
            for k in branches2:
                occurences2 += count_occurances(k,i)
            dissimilarity += (occurences1 - occurences2)**2
        return dissimilarity

def count_dissimilarity_io():
    structure1 = input()
    structure2= input()
    number_of_substrings = int(input('enter number of substrings'))
    substring_list = []
    for i in range(number_of_substrings):
        substring = input()
        substring_list.append(substring)
    dissimilarity = count_dissimilarity(structure1, structure2, substring_list)
    print('dissimilarity =  ', dissimilarity)
