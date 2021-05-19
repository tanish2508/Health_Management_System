import datetime
def gettime():
    return datetime.datetime.now()
def take(k):
    if k==1:
        c=int(input("enter 1 for excersise and 2 for food"))
        if(c==1):
            value=input("type here\n")
            with open("tanish-ex.txt","a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("successfully written")
        elif(c==2):
            value = input("type here\n")
            with open("tanish-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif(k==2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("mayank-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("mayank-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif(k==3):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("shivam-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("shivam-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    else:
        print("plz enter valid input (1(tanish),2(mayank),3(shivam)")
def retrieve(k):
    if k==1:
        c=int(input("enter 1 for excersise and 2 for food"))
        if(c==1):
            with open("tanish-ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif(c==2):
            with open("tanish-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif(k==2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("mayank-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("mayank-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif(k==3):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("shivam-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("shivam-food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("plz enter valid input (tanish,mayank,shivam)")
print("health management system: ")
a=int(input("press 1 for lock the value and 2 for retrieve "))

if a==1:
    b = int(input("press 1 for tanish, 2 for mayank, 3 for shivam "))
    take(b)
else:
    b = int(input("press 1 for tanish, 2 for mayank, 3 for shivam "))
    retrieve(b)
