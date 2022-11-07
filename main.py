from class_LIST_SMILES import ListSmiles
from class_SMILES import Smiles

''' 
    What is smiles and list_smiles:
        
    class SMILES:
        def __init__(self, smiles):             smiles = str
            self.smiles = smiles
    
    class LIST_SMILES:
        def __init__(self, list_smiles):        list_smiles = [SMILES]
            self.list_smiles = list_smiles
'''
#COMMANDS#
COUNT_SUBSTRINGS  = 'C'
MOLECULAR_FORMULA = 'M'
DISSIMILARITY     = 'D'
INPUT_NEW_SMILES  = 'I'
HELP              = 'H'
QUIT              = 'Q'
NO                = 'N'
YES               = 'Y'

#INTERACTIONS#
LOAD_SOURSE     = 'Load input from file (Y/N)?'
INPUT_COMMAND   = 'Input command to execute:' 
INPUT_SOURSE    = 'Input sourse (F/T)'
INPUT_FILE_NAME = 'Input file name: '
SAVE_SMILES     = 'Save SMILES list to file (Y/N)?' 
GOODBYE         = 'Goodbye!'
LIST_IS_EMPTY   = 'SMILES list empty'
f = open('helpmessage.txt', 'r', encoding="utf-8")
HELP_MESSAGE    = f.read()
f.close()

#ERRORS#
FAILED_READING  = 'Failed reading file '
INVALID_ANSWER  = 'Answer invalid'
LIST_EMPTY      = 'SMILES list empty'
INVALID_COMMAND = 'Command invalid'
SMILES_INVALID  = 'SMILES invalid'

          
def main():
    
    list_smiles = ListSmiles([])
   '''Firs step, program asks if you want to load SMILES strings from file or 
   not. Repeat question untill answer != Y or N. If answer is NO program do 
   nothing and print list of all commands. If answer is YES program ask for
   file name.
   '''

    answer = input(LOAD_SOURSE)
        while answer != YES and answer != NO:
            print(INVALID_ANSWER)
            answer = input(LOAD_SOURSE)
        
   '''SMILES_from_file(): function which ask user to enter name of file 
   for reading, if file can't be read print 'Failed reading file + 'file name'
   else: read only valid SMILES and return oject LIST_SMILES with 
   valid SMILES from the file.
   '''

    if answer == YES:
        list_SMILES = SMILES_from_file_io()
        if list_SMILES.list_SMILES == []:
            print(LIST_IS_EMPTY)
    if answer == NO:
        list_SMILES = LIST_SMILES([])
    
    '''Second step, program print list of all commands
    '''

    print(HELP_MESSAGE)
        
    '''Fird step, main loop with all commands.
    '''

    command = input()                    
    while command.upper() != QUIT:
        
        if command == COUNT_SUBSTRINGS:
            
        if command == MOLECULAR_FORMULA:
            
        if command == DISSIMILARITY:
    
        if command == INPUT_NEW_SMILES:
        
        if command == HELP:
            print(HELP_MESSAGE)
        
        command = input()
    
    '''Forth step, program ask if you want to save SMILES to file or not. If answer
    is NO program do nothing and close. If answer is YES program ask for a file name. 
    '''

    answer = input(SAVE_SMILES)          
    while answer != YES and answer != NO:
        print(INVALID_ANSWER)
        answer = input(SAVE_SMILES)
    
    '''SMILES_to_file_io(list_SMILES): function that asks user for file name, If program 
    can't open the file, print 'Failed open file + 'file name'. Else, program 
    write SMILES from list_SMILES to the file, if that SMILES is not already 
    in the file. 
    '''
    if answer == YES:
        SMILES_to_file_io(list_SMILES)
    
    
    print(GOODBYE)
    
    
    
    
main()