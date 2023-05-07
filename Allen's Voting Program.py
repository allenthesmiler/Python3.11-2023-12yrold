#Allen's Voting Program
print("Welcome to ALLEN's VOTING PROGRAM") #(this is not legitimate)

print(">To vote we need to ask your age? ")

age = input(">What is your age? ")

age = int(age)

if age >= int(18):
    print(f"You are eligible to vote because you are {age} Years old and are a adult")
    voted_ = input(">have you voted yet? ")
    if voted_ == "yes":
        print("ok thank you for voting and using Allen's Voting Program")
    elif voted_ == "no":
        print("Vote quick")
    else:
        print("I dont understand that")
        print("please say if you have voted yet if you have voted yet, answer the next question.")
        voted_ = input(">have you voted yet?")
if age < int(18):
    print(f"You are not eligible to vote because you are {age} Years old and are not a adult")
    print("Please vote as soon as you are 18!")
if age == str:
    print("Please say your numerical age, I dont understand that")
    age = float(input(">What is your age? "))