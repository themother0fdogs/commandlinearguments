import sys
lst = sys.argv

print(lst[1], ": Check Balance")
print(lst[2], ": Withdraw Cash")
print(lst[3], ": Deposit Cash")
print(lst[4], ": Deposit Check")

accBalance = 10000

while True:
    userInput = int(input("Enter option number: "))
    if userInput == 1:
        print("Current Balance: ", accBalance)
    elif userInput == 2:
        withdrawal = int(input("How much would you like to withdraw? "))
        accBalance = accBalance - withdrawal
        print("Current Balance: ", accBalance)
    elif userInput == 3:
        depositCash = int(input("How much cash would you like to deposit? "))
        accBalance = accBalance + depositCash
        print("Current Balance: ", accBalance)
    elif userInput == 4:
        depositCheck = int(input("What is the amount of the check deposit? "))
        accBalance = accBalance + depositCheck
        print("Current Balance: ", accBalance)
    else: print("Option does not exist")

    choice = input("Would you like to choose another option? [Yes | No] ")
    choiceCase = choice.lower()
    if choiceCase == "no":
        break










