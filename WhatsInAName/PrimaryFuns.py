from random import shuffle
reverse_name = lambda string: string[::-1]
vowels_count = lambda string: consonant_count(string, True)
def consonant_count(string, vowel=False):
    frequencies = {}
    letters = 'bcdfghjklmnpqrstvwxz' if not vowel else 'aeiou'
    for char in string: 
        if char in letters:
            if char in frequencies:
                frequencies[char] += 1
            else:
                frequencies[char] = 1
    return frequencies
Titled = lambda string: bool([i for i in  ('Dr.', "Sir", "Esq", "Phd.") if i in string])
hyphen_count = lambda name: bool(name.count('-')) 
def Names(List):
    splitList = List
    first = splitList[0]
    last = splitList[-1] if len(splitList) > 1 else 0
    try:
        del splitList[0], splitList[-1]
        middle = splitList 
    except IndexError: middle = 0
    return first, middle, last
toUp = lambda string: ''.join([chr(ord(a) - 32) if ord(a) not in range(65, 90) else a for a in string])
toLow = lambda string: ''.join([chr(ord(a) + 32) if ord(a) not in range(97, 122) else a for a in string])
IsPalidromd = lambda string: True if reverse_name(string) == string else False
initials = lambda split: [a[0] for a in split if a]
def shuffle_name(name):
    new = list(name)
    shuffle(new)
    return ''.join(new)