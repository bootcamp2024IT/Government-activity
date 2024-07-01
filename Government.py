num = []  

def naa_add():
    number = int(input("Enter number: "))
    num.append(number)

def naa_delete():
    num.pop(0)

def wala_add():
    number = int(input("Enter number: "))
    num.insert(0, number)

def wala_delete():
    num.pop() 

while True:
    print("1-Add(Naa), 2-Delete(Naa), 3-Add(Wala), 4-Delete(Wala), 5-Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        naa_add()

    elif choice == "2":
        naa_delete()

    elif choice == "3":
        wala_add()

    elif choice == "4":
        wala_delete()

    elif choice == "5":
        print("bye.")
        break

    else:
        print("Choose properly")

    print("Current list:", num)