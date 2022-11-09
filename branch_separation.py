'''
ограничения: не считаются циклы и нельзя иметь два разветвления у одного атома
'''

import re


def separate_branches(smiles_string):
    branches_final = []
    main_sequence = smiles_string
    regex = re.compile('[(][CNOBPFIScnos=\/\\@#0-9!]+[)]')
    counter = '!'
    while '(' in main_sequence or ')' in main_sequence:
        branches_found = regex.findall(main_sequence)
        for i in branches_found:
            branches_final.append(counter + i)
        main_sequence = regex.sub(counter,main_sequence)
        counter = counter + '!'
    return main_sequence, branches_final


def get_number_of_sings(string, sign):
    counter = 0
    for i in string:
        if i == sign:
            counter += 1
        else:
            break
    return counter


def clear_sequence(sequence):
    regex = re.compile('[\/\\@0-9!()]')
    return regex.sub('',sequence)


def get_all_sequences(main_sequence, branches):
    all_sequences = [clear_sequence(main_sequence)]
    for i in range(len(branches)-1,-1,-1):
        number_of_signs = get_number_of_sings(branches[i],'!')
        counter = number_of_signs * '!'
        was_found = False
        for j in range(len(main_sequence)-1,-1,-1):
            if main_sequence[j-number_of_signs:j] == counter and not was_found:
                sequence = main_sequence[j-number_of_signs-1] + branches[i][number_of_signs:]
                main_sequence = main_sequence[:j-number_of_signs] + branches[i][number_of_signs:] + main_sequence[j:]
                all_sequences.append(clear_sequence(sequence))
                was_found = True
    return all_sequences, main_sequence


def main():

    smiles_string = 'CC(=O)NC(C)CC1=CNc2c1cc(OCC(ON)C)cc2'
    main_sequence, branches = separate_branches(smiles_string)
    all_sequences, res = get_all_sequences(main_sequence, branches)
    print(smiles_string)
    print(res)
    print(branches)
    print(main_sequence)
    print(all_sequences)


main()
