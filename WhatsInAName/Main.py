import Huffman
from What import*
while True:
    n = input('Name: ')
    first, middle, last = Names(n.split())
    commands = {
        'reverse' : reverse_name(n), 
        'vowel' : vowels_count(n), 
        'consonant' : consonant_count(toLow(n)), 
        'hyphen' : hyphen_count(last),  
        'toup' : toUp(n), 
        'tolow' : toLow(n), 
        'mix' : shuffle_name(n), 
        'palindrome' : IsPalidromd(first), 
        'sort' : Titled(n), 
        'initials' : initials(n.split()), 
        'titled' : Titled(n), 
        'huffman' : Huffman.main(n)}

    while True:
        command = input(f"""{commands.keys()}\nPlease select your command from the list above (or q to quit program): """).lower()
        if command == 'q':
            quit()
        elif command == 'b':
            break
        elif command == 'first':
            print(first)
        elif command == 'middle':
            print(first)
        elif command == 'last':
            print(first)
        else:
            print(commands[command])