rider1age = int(input("What is the age of the first rider?"))
rider1height = int(input("What is the height of the first rider?"))

#golden ticket
if rider1age >= 12 & rider1age <= 17:
    if input("Do you have a golden passport (yes/no)?") == "yes":
        rider1age = 18

if str(input("Is there a second rider (yes/no)?")) == "no":
    if rider1height < 36:
        print("Sorry you cannot ride")
    else:
        if rider1age > 18 & rider1height > 62:
          print("You may ride!")
else:
    rider2age = input("What is the age of the second rider?")
    rider2height = input("What is the height of the second rider?")

    #golden ticket
    if rider2age >= 12 & rider2age <= 17:
        if input("Do you have a golden passport (yes/no)?") == "yes":
            rider2age = 18

    if rider1age >= 18 | rider2age >= 18 :
        print("You may ride!")
    elif rider1age >= 12 & rider2age >= 12 & rider1height >= 52 & rider2height >= 52:
        print("You may ride!")
    elif rider1age >= 16 & rider2age >= 14 | rider1age >= 14 & rider2age >= 16 :
        print("You may ride!")
    else:
        print("You cannot ride")