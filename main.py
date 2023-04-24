# Lab Professor: Michael
import sys


# Common Validations and functions
def check_choice(choice):
    try:
        if 1 <= int(choice) <= 5:
            return True
        else:
            return False
    except ValueError:
        return False


def validate_empty(user_input):
    if user_input is None or len(user_input) == 0:
        return False
    else:
        return True


def go_back_menu():
    go_menu = input("Do you want to back to menu? 'yes' to menu / 'no' to exit program: ").lower()
    while go_menu != 'yes' and go_menu != 'no':
        print("Invalid input.")
        go_menu = input("Do you want to back to menu? 'yes' to menu / 'no' to exit program: ").lower()
    else:
        if go_menu == 'yes':
            print("\n"*2)
            menu()
        elif go_menu == 'no':
            sys.exit()


# validation specific for create employee
def validate_id(emp_id):
    if emp_id.isnumeric():
        if any(int(emp_id) in sublist for sublist in employee_list):
            print("The id is already existed! Please enter another id!")
            return False
        else:
            return True
    else:
        print("Invalid input. Please input id in number!")
        return False


def validate_type(emp_type):
    if emp_type.lower() != "manager" and emp_type.lower() != "hourly":
        print("Please enter manager or hourly!")
        return False
    else:
        return True


# validation specific for creating item
def validate_num(item_num):
    if item_num.isnumeric():
        if any(int(item_num) in sublist for sublist in item_list):
            print("The item is already existed! Please enter another number!")
            return False
        else:
            return True
    else:
        print("Invalid input. Please input in number!")
        return False


def validate_dis(dis_num):
    if dis_num.isnumeric():
        if any(int(dis_num) in sublist for sublist in employee_list):
            return True
        else:
            print("Invalid Employee Discount Number. Please input again.")
            return False
    else:
        print("Invalid input. Please input in number!")
        return False


def validate_item(item_num):
    if item_num.isnumeric():
        for sublist in item_list:
            if int(item_num) == sublist[0]:
                return True
        return False
    else:
        print("Invalid input. Please input in number!")
        return False


def get_dis_rate(emp_dis_num):
    dis_rate = 0
    for employee in employee_list:
        if employee[6] == emp_dis_num:
            if employee[2] == "hourly":
                dis_rate += 2
            elif employee[2] == "manager":
                dis_rate += 10

            if employee[3] > 5:
                dis_rate += 10
            else:
                dis_rate += employee[3] * 2
    return dis_rate


def get_dis_accumulated(emp_dis_num):
    for employee in employee_list:
        if employee[6] == emp_dis_num:
            return employee[5]


def get_item_price(item_num):
    for item in item_list:
        if item[0] == item_num:
            return item[2]


def set_total_dis(emp_dis_num, dis_price):
    for employee in employee_list:
        if employee[6] == emp_dis_num:
            employee[5] += dis_price
            return


def set_total_pur(emp_dis_num, price):
    for employee in employee_list:
        if employee[6] == emp_dis_num:
            employee[4] += price
            return


def new_purchase():
    choice = input("Do you want to purchase another item? 'yes' / 'no' ")
    if choice.lower() == 'yes':
        return 1
    elif choice.lower() == 'no':
        return 2
    else:
        return 3


def check_purchase(choice):
    if choice.lower() == 'yes':
        return 1
    elif choice.lower() == 'no':
        return 2
    else:
        return 3


def display_item():
    print("Item Number   |Item Name                |Item Cost      ")
    for items in item_list:
        print("%-14i|%-25s|%-14.2f" % (items[0], items[1], items[2]))


# Sub-menus
def create_employee():
    create_emp = input("Do you want to create new employee? 'YES' / 'NO': ")
    while True:
        if create_emp == 'YES' or create_emp == 'yes':
            emp_id = input("Employee ID: ")
            chk_id = validate_id(emp_id)
            while not validate_empty(emp_id) or not chk_id:
                emp_id = input("Employee ID: ")
                chk_id = validate_id(emp_id)
            emp_id = int(emp_id)

            emp_name = input("Employee Name: ")
            while not validate_empty(emp_name):
                emp_name = input("Employee Name: ")
                validate_empty(emp_name)

            emp_type = input("Employee Type (Manager / Hourly): ").lower()
            chk_type = validate_type(emp_type)
            while not validate_empty(emp_type) or not chk_type:
                emp_type = input("Employee Type (Manager / Hourly): ").lower()
                chk_type = validate_type(emp_type)

            emp_year = input("Years worked: ")
            chk_year = emp_year.isnumeric()
            while not validate_empty(emp_year) or not chk_year:
                print("Invalid input. Please enter year in number!")
                emp_year = input("Years worked: ")
                chk_year = emp_year.isnumeric()
            emp_year = int(emp_year)

            emp_dis_num = input("Employee Discount Number: ")
            chk_num = emp_dis_num.isnumeric()
            while not validate_empty(emp_dis_num) or not chk_num:
                print("Invalid input. Please enter year in number!")
                emp_dis_num = input("Employee Discount Number: ")
                chk_num = emp_dis_num.isnumeric()
            emp_dis_num = int(emp_dis_num)

            temp_list = [emp_id, emp_name, emp_type, emp_year, 0, 0, emp_dis_num]
            employee_list.append(temp_list)
            print("Employee created successful!")
            print("")
            create_employee()

        elif create_emp == 'NO' or create_emp == 'no':
            go_back_menu()
        else:
            print("Invalid input.")
            create_employee()


def create_item():
    create_it = input("Do you want to create new item? 'YES' / 'NO': ")
    while True:
        if create_it == 'YES' or create_it == 'yes':
            item_num = input("Item number: ")
            chk_num = validate_num(item_num)
            while not validate_empty(item_num) or not chk_num:
                item_num = input("Item number: ")
                chk_num = validate_num(item_num)
            item_num = int(item_num)

            item_name = input("Item name: ")
            while not validate_empty(item_name):
                item_name = input("Item name: ")
                validate_empty(item_name)

            item_cost = input("Item cost: ")
            chk_cost = item_cost.isnumeric()
            while not validate_empty(item_cost) or not chk_cost:
                print("Invalid input. Please enter cost in number!")
                item_cost = input("Item cost: ")
                chk_cost = item_cost.isnumeric()
            item_cost = int(item_cost)

            temp_list = [item_num, item_name, item_cost]
            item_list.append(temp_list)
            print("Create item successful!")
            print("")
            create_item()

        elif create_it == 'NO' or create_it == 'no':
            go_back_menu()
        else:
            print("Invalid input.")
            create_item()


def purchase():
    display_item()
    while True:
        print("")
        dis_num = input("Please input employee discount number: ")
        chk_dis = validate_dis(dis_num)
        while not chk_dis:
            dis_num = input("Please input employee discount number: ")
            chk_dis = validate_dis(dis_num)
        dis_num = int(dis_num)

        item_num = input("Please input item number: ")
        chk_item = validate_item(item_num)
        while not chk_item:
            print("Invalid Item Number. Please input again.")
            item_num = input("Please input item number: ")
            chk_item = validate_item(item_num)
        item_num = int(item_num)

        choose_purchase = input("Confirm purchase? 'yes' / 'no' :")
        chk_purchase = check_purchase(choose_purchase)
        while chk_purchase == 1:
            # calculate discount and total
            dis_rate = get_dis_rate(dis_num)
            dis_accum = get_dis_accumulated(dis_num)
            item_price = get_item_price(item_num)

            total_discount = round((item_price * dis_rate) / 100, 2)
            if dis_accum < 200 and 200 - dis_accum >= 0:
                diff = 200 - dis_accum
                if diff < total_discount:
                    final_price = item_price - diff
                    set_total_dis(dis_num, diff)
                    set_total_pur(dis_num, final_price)
                # Else use the discount_total got within the purchase
                else:
                    final_price = item_price - total_discount
                    set_total_dis(dis_num, total_discount)
                    set_total_pur(dis_num, final_price)
                print("\nSuccessfully purchased!\n")

            choice = new_purchase()
            while int(choice) == 1:
                purchase()
            while int(choice) == 2:
                summary()
            while int(choice) == 3:
                print("Invalid input. Please enter again.")
                choice = new_purchase()

        while chk_purchase == 2:
            summary()
        while chk_purchase == 3:
            print("Please input again.")
            choose_purchase = input("Confirm purchase? 'yes' / 'no' :")
            chk_purchase = check_purchase(choose_purchase)


def summary():
    print("")
    print("--- All Employee Summary ---")
    print("Employee ID |Employee Name  |Employee Type  |Years Worked  |Total Purchased   |Total Discount  |"
          "Employee Discount Number")
    for employee in employee_list:
        print("%-12i|%-15s|%-15s|%-14i|%-18s|%-16s|%-25i " % (employee[0], employee[1], employee[2], employee[3],
                                                              employee[4], employee[5], employee[6]))
    print("")
    go_back_menu()


# Menu
def menu():
    print("----------------------------")
    print("| 1- Create Employee       |")
    print("| 2- Create Item           |")
    print("| 3- Make Purchase         |")
    print("| 4- All Employee Summary  |")
    print("| 5- Exit                  |")
    print("----------------------------")

    choice = input("Please enter the number of option: ")

    while True:
        chk_choice = check_choice(choice)
        while chk_choice:
            choice = int(choice)
            match choice:
                case 1:
                    create_employee()
                case 2:
                    create_item()
                case 3:
                    purchase()
                case 4:
                    summary()
                case 5:
                    sys.exit()
        while not chk_choice:
            print("Invalid option. You must enter number between 1-5.")
            choice = input("Please enter the number of option: ")
            chk_choice = check_choice(choice)


# initial settings for data
employee_list = [
    [1001, 'John Alber', 'hourly', 8, 0, 0, 22737],
    [1002, 'Sarah Rose', 'manager', 12, 0, 0, 22344],
    [1003, 'Alex Folen', 'manager', 5, 0, 0, 22957],
    [1004, 'Pola Sahari', 'hourly', 17, 0, 0, 22488]
]
item_list = [
    [11526, 'Nike shoes', 120],
    [11849, 'Trampoline', 180],
    [11966, 'Mercury Bicycle', 150],
    [11334, 'Necklace Set', 80]
]

# main program start here
menu()
