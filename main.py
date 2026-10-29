print("Welcome to my chore planner program")
name=input("Enter your name: ")
chorenumb=int(input("Enter the number of chores you have to complete: "))
print(name, "you have", chorenumb, "number of chores")
numofchore=0
cmch=[]
while numofchore<chorenumb:
    chore=input("What chores do you have to do? ")
    comchore=input("Have you completed the chore " + chore + "? ").lower()
    while comchore!="yes":
        print("Complete the current chore you are doing")
        comchore=input("Have you completed the chore " + chore + "? ").lower()
    cmch.append(chore)
    numofchore+=1
    storedch=chorenumb-numofchore
    print(" Well done ", name, "you have ", storedch, "chores left ")
print("Today you have completed",numofchore, "And you have ", storedch, "Number of chores remaining.")