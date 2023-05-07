# Pythy the python -The adventure -  by Allen (very simple python)
print("Pythy - Hi my name is Pythy the Python ")
name = input("Pythy - What is your name: ")
print(f"Pythy - Hi! {name} im Pythy, today's adventure is to get the * ")
age = input("Pythy - what is your age: ")

age = int(age)
print(f"Pythy - You are {age} years old")
while age <= 19:
    print("Pythy - to old for the game")
    break

print("                       *")
print("Pythy - that * is pretty far away")
print("""
    Pythy - legend has it is that if we get the * 
    then we will have all the ice-cream in the world
    but, the difficult thing is, is that there is a
    ice-cream monster names "FROSTBITE" protecting the * 
""")

response1 = input("Pythy - What do you think about 'FROSTBITE'? is he scary, funny or tasty! ").lower()
if response1 == "scary":
    print(f"Pythy - I agree he is {response1}")
elif response1 == "funny":
    print(f"Pythy - HA HA HA HA, i agree he is {response1}")
elif response1 == "tasty" or "tasty!":
    print(f"Pythy - I would imagine us eating FROSTBITE mhmm 😋")

print("Pythy - There are 3 Frostbites around the world pick one")
Destination = input("Pythy - Desert island, France, 1945 Germany 🫡: ").lower()

if Destination == "desert island":
    print("Pythy - Oh there he is ---> 🍨")
    print("Since he is in the Desert he melted")
    print("lets go get the *")
    print("You WON! here is your icecream🍨")

if Destination == "France":
    print("Pythy - Oh there he is ---> 🍨")
    print("Dodge his Brain Freeze attack by clicking M on your keyboard! ")
    Dodge = input("Dodge! ").lower()
    if Dodge == "M":
        print("Pythy - HAYA! ")
        print("I hit him lets go get the *")
        print("You WON! here is your icecream🍨")
    else:
        print("AWW, you lost try again :(")

if Destination == "1945 Germany":
    print("Pythy - Heil HI-")
    print("Pythy - Oh there you are")
    print("Pythy - Oh there he is ---> 🍨!!!")
    print("Dodge his Brain Freeze attack by clicking M on your keyboard! ")
    Dodge = input("Dodge! ").lower()
    if Dodge == "M":
        print("Pythy - HAYA! ")
        print("I hit him lets go get the *")
        print("You WON! here is your icecream🍨")
    else:
        print("AWW, you lost try again :(")

