from os import stat
from get_input import get_input


def date():
    """Returns current date"""
    from datetime import date

    today = date.today()
    return today.strftime("%B %d, %Y")


def time():
    """Returns current time"""
    from datetime import datetime

    now = datetime.now()
    return now.strftime("%H.%M.%S")


def datetime():
    """Returns current date and time"""
    return f"{date()}, {time()}"


def get_data(filepath):
    """Returns item from the filepath as a python dictionary"""
    with open(f'{filepath}', 'rt') as fh:
        values = fh.read().split("\n")
        database = {}
        for each in values:
            if not len(each) < 1:
                stripped = [each.strip()
                            for each in
                            each.strip().strip(",").split(",")]
                id = stripped[0]
                data = stripped[1:]
                database[id] = data
        return database


def display(data):
    """Display all the items from a dictionary in a formatted manner."""

    print()
    for key, value in data.items():
        formatted_item = f"{key:<5} {value[0]:<25} {value[1]:<25} {value[2]:<10} {value[3]:<5} "
        print(formatted_item)
        if key.lower() == "id":
            print("-"*(len(formatted_item)))
    print()


main_file = "books.txt"
database = get_data(main_file)
cart = {"borrowed": [], "returned": []}


def generate_invoice(cart, username, start_time):
    """Generates note"""

    filename = f"Invoice {username} {start_time}.txt"

    with open(f'{filename}', 'wt') as fh:
        fh.write(
            f"================================= INVOICE ===============================\n\n")

        total_amount = 0

        fh.write(f"Customer: {username} \n")
        fh.write(f"Date: {date()}\n")
        fh.write(f"Time: {time()}\n\n")

        for status, items in cart.items():
            if len(items) >= 1:
                fh.write(f"\n\n# Item(s) {status}\n\n")

                total_amount = 0

                formatted_header = f"{'ID':<5} {'Title':<50} {'Price':<5}"
                fh.write(formatted_header + "\n")
                fh.write("-"*len(formatted_header) + "\n")

                for each in items:
                    # [B001, A Game of Thrones, George R. R. Martin, 33, $2]
                    id = each[0]
                    title = each[1]
                    author = each[2]
                    # quantity = each[3]
                    price = each[4]

                    # calculation total amount
                    price_num = float(price.strip("$"))
                    total_amount += price_num

                    formatted_item = f"{id:<5} {title + ' by ' + author:<50} {price:<5}"
                    fh.write(f"{formatted_item}\n")

                fh.write(f"\n\nGrand Total: {total_amount}\n\n")
        fh.write(
            "\n=================================== END =================================\n")


def borrow_book(data, cart):
    while True:
        to_borrow = get_input(
            "\nEnter ID of the item you want to borrow").upper()
        if to_borrow in data.keys():
            item = data[to_borrow]
            name = item[0]
            quantity = item[2]
            if int(quantity) < 1:
                print()
                print(
                    f"[ Out of stock ] {name} is out of stock, please choose another. ")
                print()
            else:
                print("\n# Item borrowed! Thank You!\n")
                updateDatabase(data, to_borrow, do="sub")

                # adding the particular item as list (a with its id at index 0) in the cart
                cart["borrowed"].append([to_borrow] + data[to_borrow])
            break
        else:
            print(
                f"\n[ Error ] Invalid input '{to_borrow}', please try again!\n")
            continue


def return_book(data, cart):
    while True:
        to_return = get_input(
            "\nEnter ID of the item you want to return").upper()
        if to_return in data.keys():
            item = data[to_return]
            print("\n# Item returned! Thank You!\n")
            updateDatabase(data, to_return, do="add")

            # adding the particular item as list (a with its id at index 0) in the cart
            cart["returned"].append([to_return] + data[to_return])
            break
        else:
            print(
                f"\n[ Error ] Invalid input '{to_return}', please try again!\n")
            continue


def updateDatabase(data, key, do="add", qty=1):
    '''Update stock from in a dictionary data using the key.
    Use the do="add"/do="sub" parameter to add or subtract from the stock.'''
    prev_qty = int(data[key][2])

    if do == "add":
        new_qty = prev_qty + qty
    elif do == "sub":
        new_qty = prev_qty - qty

    # updating item quantity
    data[key][2] = str(new_qty)


def updateStock(data, filepath):
    """Updates data (text file) with the most recent data in the dictionary (i.e. data). """

    with open(f'{filepath}', 'wt') as fh:
        for key, value in data.items():
            fh.write(f"{key},")
            for count, each in enumerate(value):
                fh.write(f"{each}{',' if count+1 != len(value) else ''}")
            fh.write("\n")


def main():
    start_time = datetime()
    username = get_input("Enter name").capitalize()
    print()
    print(f"Hi, Mr/s. {username}!")
    print()

    while True:
        options = {
            1: "View available books",
            2: "Borrow a book",
            3: "Return a book",
            4: "Exit (or enter exit)"
        }
        while True:
            print("-"*3)
            for k, v in options.items():
                print(f"Option {k}: {v}")

            user_option = get_input(
                "\nPlease select and choose an option", num=True)
            if user_option in options.keys():

                # print selected option
                formatted_option = f"# Options {user_option}: {options[user_option]}"
                print()
                print(formatted_option)
                print("-"*len(formatted_option))

                if user_option == 1:
                    # 1: "View available books",
                    display(database)
                    break
                elif user_option == 2:
                    # 2: "Borrow a book",
                    display(database)
                    borrow_book(database, cart)
                    updateStock(database, main_file)
                    generate_invoice(cart, username, start_time)
                    break
                elif user_option == 3:
                    # 3: "Return a book",
                    display(database)
                    return_book(database, cart)
                    updateStock(database, main_file)
                    generate_invoice(cart, username, start_time)
                    break
                elif user_option == 4:
                    # 4: "Exit"
                    exit("[ OK ] Exiting...")
            else:
                print(
                    f"[ Invalid input ] Entered value must one of {[i for i in options.keys()]}.\n")


if __name__ == "__main__":
    print("================== WELCOME TO LIBRARY MANAGEMENT SYSTEM ================\n")
    main()
