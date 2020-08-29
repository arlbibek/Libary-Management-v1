# imporing date
import datetime

# Library Management System
file1 = open('books.txt', 'r')  # opening file
lines = file1.read()
file1.close()  # closing files
list1 = lines.split('\n')  # spliting by '\n'


list2 = []  # an empty list
for each_item in list1:  # iterating with each item in the 'list1'
    list2.append(each_item.split(','))  # spliting item by ','

Library = {}
for each_item in list2:
    key = each_item[0]
    values = []
    for each in range(1, len(each_item)):
        values.append(each_item[each])
        Library[key] = values


now = datetime.datetime.now()

print('\n')
print("\t{|| Aryal Library ||}")
print("\t^^^^^^^^^^^^^^^^^^^^^")
print("___________________________")
Name = input("Please state your full name: ")
print("\n\tWelcome Mr/Ms.", Name.title())

# function to view every items


def all_items():
    print("............................................................................")
    print("\tBook Lists")
    print("\t==========")
    for key, values in Library.items():
        print("\tBook ID  : ", key)
        print("\n\tBook Name: ", values[0], "by", values[1], "@", values[-1] +
              "\n\t--------------------------------------------------------------------")


borrowed = {}  # empty dictonary to store borrowed items as global variable
returned = {}  # empty dictonary to store returned items as global variable

infnite = True  # to run the program until user choose to exit
while infnite:
    try:
        print("\t____________________________________\n\t>>>Press '1' to view available Books.\n\t>>>Press '2' to borrow Books.\n\t>>>Press '3' to return Books.\n\t>>>Press '4' to Exit.\n_______________________")
        user_input = int(input(">>>Please enter here: "))
        if user_input == 1:
            print("\nOption '1'\nThese Books are available for now.")
            all_items()
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        elif user_input == 2:
            error2 = True
            while error2:
                try:
                    all_items()
                    print(
                        "\nOption '2'\nChoose what to borrow.\nWhich book would you like to borrow today? Mr/Ms.", Name)
                    to_borrow = str(input(">>> Please Enter Book ID: "))
                    # book id milo ki milena vanera
                    for key, values in Library.items():
                        if to_borrow == key:
                            if int(values[2]) > 0:
                                print("\n" + values[0], "by", values[1] +
                                      '\n' + "~~Wow!! Intresting choice.~~\n")
                                # decereasing quantity
                                new_quantity = int(values[2]) - 1
                                values[2] = str(new_quantity)
                                borrowed[key] = values
                                # decreasing values in main library
                                Library[key] = values
                                # Writing Borrow Note
                                total = 0
                                file1 = open("Borrow Book Note.txt", 'w')
                                file1.write("Borrow Records.\n")
                                file1.write("===============\n")
                                file1.write("Name:" + Name + "\t\t\t\t\tDate:" + str(now.year) +
                                            "/" + str(now.month) + "/" + str(now.day) + "\n")
                                file1.write(
                                    "-------------------------------------------------------------------\n")
                                file1.write(
                                    "Name:" + '\t\t\t\t' + "\t\tPrice\n")
                                for values in borrowed.values():
                                    # removing '$'
                                    dollar = values[-1]
                                    no_dollar = dollar.replace('$', '')
                                    total = float(no_dollar) + float(total)
                                    # adding '$' back
                                    total1 = "$" + str(total)
                                    dollar1 = "$" + str(no_dollar)
                                    file1.write(values[0] + '\t\t\t' +
                                                '\t\t' + str(dollar1) + '\n')
                                file1.write("Grand Total" + '\t\t\t\t\t' +
                                            str(total1) + '\n')
                                file1.write(
                                    "___________________________________________________________________\n")
                                file1.write(
                                    "___________________________________________________________________\n")
                                file1.write(
                                    ">\t\t Aryal's borrowed \t\t<\n###################################################################\n")
                                file1.close()
                                # noteing....
                                file1 = open("books.txt", 'w')
                                for key, values in Library.items():
                                    file1 = open("books.txt", 'a')
                                    file1.write(key + ",")
                                    for each in values:
                                        file1.write(str(each + ','))
                                    file1.write('\n')
                                file1.close()
                            else:
                                print("\n\t***Sorry! The book '",
                                      values[0], "' is out of stock!\n")
                            error2 = False
                except Exception:
                    print("***Wrong Book Id!! Please re-enter Book ID***")
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        elif user_input == 3:
            error3 = True
            while error3 == True:
                all_items()
                print(
                    "Option 3\n========\nWhich book would you like to return today? Mr/Ms.", Name)
                to_return = str(input(">>>Please Enter Book ID: "))
                for key, values in Library.items():
                    if to_return == key:
                        error3_a = True
                        while error3_a == True:
                            try:
                                days_kept = int(
                                    input("How many days did you kept the book for yourself?: "))
                                error3_a = False
                            except Exception:
                                print("***Please enter a number***")
                        new_quantity = int(values[2]) + 1
                        values[2] = str(new_quantity)
                        values.append(days_kept)
                        returned[key] = values
                        print("\n\tThank you for returing",
                              values[0], "by", values[1])
                        # returning book note
                        total_amt = 0.0
                        total_fine = 0.0
                        file1 = open("Return Book Note.txt", 'w')
                        file1.write("Return Records.\n")
                        file1.write("===============\n")
                        file1.write("Name:" + Name + "\t\t\t\t\tDate:" + str(now.year) +
                                    "/" + str(now.month) + "/" + str(now.day) + "\n")
                        file1.write(
                            "________________________________________________________________\n")
                        file1.write("Name:\t\t\t\tDays\t\tPrice\tFine\t\n")
                        for values in returned.values():
                            days = int(values[-1])
                            # removing '$'
                            dollar = values[-2]
                            no_dollar = dollar.replace('$', '')
                            # calculating fine
                            if days >= 10:
                                fine_ = round((0.1 * float(no_dollar))
                                              * float(days - 10), 2)
                                total_fine += float(fine_)
                                total_fine = round(total_fine, 2)
                                fine_ = "$" + str(fine_)
                            else:
                                fine_ = '$0.0'
                            # calculating fine
                            total_amt = float(no_dollar) + total_amt
                            # adding '$' back
                            total_fine1 = '$' + str(total_fine)
                            dollar1 = "$" + str(no_dollar)
                            total_amt1 = "$" + str(total_amt)
                            file1.write(values[0] + '\t\t\t' + str(days) +
                                        '\t\t' + str(dollar) + '\t' + str(fine_) + '\n')
                            values.pop()
                        file1.write(
                            "___________________________________________________________________\n")
                        file1.write("Total" + '\t\t\t\t\t\t' + str(total_amt1) + '\t' + str(
                            total_fine1) + '\n-------------------------------------------------------------------\n')
                        file1.write("Grand Total\t\t\t\t\t$" +
                                    str(float(total_amt) + float(total_fine)) + "\n")
                        file1.write(
                            "-------------------------------------------------------------------\n")
                        file1.write(">\t\t\t Aryal's Library \t\t\t<\n")
                        file1.write(
                            "###################################################################\n")
                        file1.close()
                        # noteing....
                        file1 = open("Books(Updated).txt", 'w')
                        for key, values in Library.items():
                            file1.write(key + ",")
                            for each in values:
                                file1.write(str(each + ','))
                            file1.write('\n')
                        file1.close()
                        error3 = False
        elif user_input == 4:
            print(
                "\tSorry to see you go. :( \n\tPlease visit us again.\n\tThank You\n\t\n\tExiting...")
            exit()
    except Exception:
        print("\n***Please enter a number from given option!!***")
