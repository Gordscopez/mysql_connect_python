from main import DBhelper

def main():
    db = DBhelper()
    while True:
        print('*************WELCOME***********')
        print()
        print("press 1 to insert new user")
        print("press 2 to display all user")
        print("press 3 to delete user")
        print("press 4 to update user")
        print("press 5 to close connection")
        print("press 6 to exit program")
        print()

        try:
            choice = int(input())
            if(choice==1):
                uid = int(input("enter the id of the user"))
                name = input("enter the name of the user")
                phone = input("enter the user phone number")
                db.insert_user(uid, name, phone)
                return 

            elif(choice==2):
                db.fetch_all()
                return

            elif(choice==3):
                id = int(input("enter the id to delete"))
                db.delete_user(id)

            elif(choice==4):
                uid = int(input("enter the id of the user"))
                name = input("enter the name of the user")
                phone = input("enter the user phone number")
                db.update_user(uid, name, phone)

            elif(choice==5):
                db.close_connection()
                break
                
            elif(choice==6):
                break
            else:
                print("Invalid input ! try again")
        except Exception as  e:
                print(e)
                print("Invalid Details ! Try again")

if __name__ == '__main__':
    main()