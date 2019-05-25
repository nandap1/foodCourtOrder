'''
Displays DeAnza's food court menu and produces a bill with the correct orders for students and staff.
'''
#initialize variables
food_1 = 0
food_2 = 0
food_3 = 0 
food_4 = 0
food_5 = 0
flag = True
item = ("")
staff = ("")
exit_loop = False


def display_menu():
    print("DEANZA COLLEGE FOOD COURT MENU:")
    print("1. DeAnza Burger   - $5.25")
    print("2. Bacon Cheese    - $5.75")
    print("3. Mushroom Swiss  - $5.95")
    print("4. Western Burger  - $5.95")
    print("5. Don Cali Burger - $5.95")
    print("6. Exit")

#check if item is between 1 and 5, only then ask for quantity
def get_inputs():
    global food_1, food_2, food_3, food_4, food_5, staff, exit_loop
    while not exit_loop:
        item = input("Enter food:\n").strip()
        #check if item is between 1 and 5, only then ask for quantity
        if int(item) > 0 and int(item) < 6:
            try:
                quantity = input("Enter quantity: ").strip()
                #only when quantity is a positive value, it'll go into loop
                try:
                    if int(quantity) > 0:
                        if item == '1':
                            food_1 += quantity
                        elif item == '2':
                            food_2 += quantity
                        elif item == '3':
                            food_3 += quantity
                        elif item == '4':
                            food_4 += quantity
                        elif item == '5':
                            food_5 += quantity
                    else:
                        print("Invalid quantity, try again.")
                except:
                    print("Invalid entry. Try order again.")
                
            except:
                break
        else:
            if item == '6':
                exit_loop = True
            else:
                print("Invalid entry, try again.")
                
#asking whether staff or student 
    if (food_1 > 0 or food_2 > 0 or food_3 > 0 or food_4 > 0 or food_5 > 0):
        while flag:
            staff = input("Are you a student or a staff:").strip().lower()
            if staff == 'student':
                break
            elif staff == 'staff':
                break
            else:
                print('Invalid entry')

    return food_1, food_2, food_3, food_4, food_5, staff

def compute_bill(food_1, food_2, food_3, food_4, food_5, staff):
    total_after_tax = 0
    tax = 0
    #total for student (default)
    total = (food_1 * 5.25) + (food_2 * 5.75) + (food_3 * 5.95) + (food_4 * 5.95) + (food_5 * 5.95)
    
    if staff == 'staff':
        #factor in tax for staff
        tax = total * 0.09
        
    total_after_tax = total + tax
    return total, tax, total_after_tax

def print_bill(food_1, food_2, food_3, food_4, food_5, total, tax, total_after_tax):
    print("\nDEANZA COLLEGE ORDER BILL:")
    print("Quantity of food item(s)")
    print("DeAnza Burger:  ", food_1)
    print("Bacon Cheese:   ", food_2)
    print("Mushroom Swiss: ", food_3)
    print("Western Burger: ", food_4)
    print("Don Cali Burger:", food_5)
    print("------------------------------------")
    print("Food item(s) and cost")
    print("DeAnza Burger:  ", food_1 * 5.25)
    print("Bacon Cheese:   ", food_2 * 5.75)
    print("Mushroom Swiss: ", food_3 * 5.95)
    print("Western Burger: ", food_4 * 5.95)
    print("Don Cali Burger:", food_5 * 5.95)
    print("------------------------------------")
    print("Total before tax:", round(total,2))
    print("------------------------------------")
    print("Tax amount:", round(tax,2))
    print("------------------------------------")
    print("Total price after tax:", round(total_after_tax,2))

def main():
    #python debugger
    #import pdb; pdb.set_trace()
    display_menu()
    food_1, food_2, food_3, food_4, food_5, staff = get_inputs()
    total, tax, total_after_tax = compute_bill(food_1, food_2, food_3, food_4, food_5, staff)
    print_bill(food_1, food_2, food_3, food_4, food_5, total, tax, total_after_tax)

main()
