from random import choice
first = """local
roasted
grilled
garlic mashed
oven dried
spiced
stewed
assorted
iced
sliced
braised
free-range
baby
teriyaki glazed
steamed"""

secound = """cauliflower
tilapia fillet
pork loin
green beans
basmati rice
rainbow carrots
fingerling potatoes
three color squash
potatoes
eggplant
drumstick
short rib
duck breast
eye round of beef
baguette"""
third = """with fennel
gratin
bengali style
with peas
pizza
with balsamico
with garlic and olive oil
with pigeon peas
with minted yogurt
soup
chutney
salad
with tropical fruit salsa
over sticky rice
au jus"""
first = first.split("\n")
secound = secound.split("\n")
third = third.split("\n")
menuRepeat = []
menuToPrint = []
while True:
    try:
        while True:
            menuItems = int(input("How many items? "))
            if menuItems >= 3375:
                continue
            else:
                break
        break
    except:
        pass
for a in range(menuItems):
    while True:
        menu = (choice(first), choice(secound), choice(third))
        if menu in menuRepeat:
            continue
        else:
            menuRepeat.append(menu)
            menuToPrint.append(menu)
            break
for a in menuToPrint:
    repeat = menuToPrint.index(a)
    print(f"{repeat + 1}: {a[0]} {a[1]} {a[2]}")