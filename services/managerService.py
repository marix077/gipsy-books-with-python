db = []
import os 

class manager : 
    pass

def menu():
    os.system("cls")
    print("1)add user")
    print("2)add tagg")
    print("3)add folder")
    print("4)add book")
    select = input(":")
    return select

def Adduser() :
    os.system("cls")
    Username = {}
    User_name = input("right a username")
    Password = input("set a password")
    db.append(User_name,Password)



    if __name__ == "__main__":
    isalive = True
    while isalive:
        select = menu()
        if select == '1':
            Adduser()
        elif select == '2':
            AddTagg()
        elif select == '3':
            AddFolder()
        elif select == '4':
            AddBook()
        else:
            os.system("cls")
            input("invalid input ; try again")
