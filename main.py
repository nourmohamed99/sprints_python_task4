# This is a sample Python script.
import csv
import datetime

contact_book = f"contact_book_{datetime.datetime.now().strftime('%Y_%m_%d')}.csv"

# the input function print choices and takes input from user
def Input():
    print("1.Add contact")
    print("2.Update contact")
    print("3.Delete contact")

    choice = int(input("Please enter your choice: "))
    if choice == 1:
        create()
    elif choice == 2:
        update()
    elif choice == 3:
        delete()
    else:
        print("incorrect input please try again!")
        Input()


# the create function add new contact to you contact book and write them in a file
def create():
    # take inputs from user and call save function
    name = input("Enter Name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter Email address: ")
    address = input("Enter Address: ")
    current_date = datetime.datetime.now().strftime('%d-%m-%Y- %H:%M:%S')
    save(name, phone_number, email, address, current_date)
    Input()


# save inputs into a file called contact_book
def save(name, phone_number, email, address, current_date):
    with open(contact_book, "a", newline='') as file:
        save = csv.writer(file)
        save.writerow([name, phone_number, email, address, current_date])
    with open("contact_book.csv", "a", newline='') as file:
        save = csv.writer(file)
        save.writerow([name, phone_number, email, address, current_date])
        print("saved successfully!")


# update function let the user decide what field they want to update then
# write the name of the contact that they want to change
# if the name entered is not in the file it will print "name not found"
# else it will update
def update():
    options = input("please select the field you want to update\n"
                    "1. name\n"
                    "2. phone number\n"
                    "3. email\n"
                    "4. address\n"
                    "5. cancel\n"
                    "enter: ")
    if options.isdigit() and 0 < int(options) <= 5:
        if int(options) < 5:
            with open("contact_book.csv", "r") as file:
                reader = csv.reader(file)
                rows = list(reader)
            search_name = input("enter name you want to update: ")
            if valid_name(rows, search_name):
                for row in rows:
                    if row[0] == search_name:
                        if int(options) == 1:
                            new_value = input("Enter new name: ")
                            row[0] = new_value
                        elif int(options) == 2:
                            new_value = input("Enter new phone_number: ")
                            row[1] = new_value
                        elif int(options) == 3:
                            new_value = input("Enter new email: ")
                            row[2] = new_value
                        elif int(options) == 4:
                            new_value = input("Enter new address: ")
                            row[3] = new_value
                with open("contact_book.csv", "w", newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(rows)
                print("updated successfully!")
                Input()
            else:
                print("name not found please try again")
                update()

        elif int(options) == 5:
            Input()
        else:
            print("incorrect input please try again!")
            update()


# the delete function let the user enter the name in his contact to delete it
# if the name does not exist it will print "name not found"
def delete():
    with open("contact_book.csv", "r", newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)
    name = input("enter the name you want to delete: ")
    if valid_name(rows, name):
        for row in rows:
            if row[0].strip().lower() == name:
                rows.remove(row)
        with open("contact_book.csv", "w") as file:
            adder = csv.writer(file)
            adder.writerow(rows)
        print("contact deleted successfully!")
        Input()
    else:
        print("name not found ty again!")
        again = int(input("to try again enter 1 \n"
                          "to go back enter 0 \n"
                          "enter input here: "))
        if again == 1:
            delete()
        elif again == 0:
            Input()
        else:
            print("incorrect input try again")
            delete()


def valid_name(rows, name):
    for row in rows:
        if row[0].strip().lower() == name:
            return True
    return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Contact Book")
    print("please select one of the above")
    Input()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
