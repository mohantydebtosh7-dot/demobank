customer = {}
def add_customer(account_number, name, account_type, balance):
    if account_number in customer:
        print("Customer already exist!")
    else:
        customer[account_number] = {"name":name,"account_type":account_type,"balance":balance}
        print(f"Customer {account_number} added successfully!")

def view_customer():
    print("------All Customer Details-----")
    for account_number,info in customer.items():
        print(f"account_number:{account_number} |name:{info["name"]}|account_type : {info["account_type"]}|balance:{info["balance"]}")

def search_customer(account_number):
    print("------Customer Details using account number-----")
    if account_number in customer:
        print(f"name:{customer[account_number]["name"]}|account_type : {customer[account_number]["account_type"]}|balance:{customer[account_number]["balance"]}")
    else:
        print("customer is not exist!!!")



def main():
    while True:
        print("1.Add Customer\n2.View Customer Table\n3.Search Customer\n4.Exit")

        choose_number = int(input("Choose what you want to do : "))
        if choose_number == 1:
            add_customer(101, "John", "Saving" , 200)
            add_customer(102, "Elina", "Saving" , 20000)
            add_customer(103, "Bob", "Saving" , 200)
            add_customer(104, "Rahul", "Saving" , 20000)
        if choose_number == 2:
            view_customer()
        if choose_number == 3:
            account_number = int(input("Enter account number: "))
            search_customer(account_number)
        if choose_number == 4:
            break
def main():
    customers = []

    while True:
        print("\n--- Customer Management System ---")
        print("1. Add Customer")
        print("2. View All Customers")
        print("3. Search Customer")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")

        if choice == '1':
            # ADD CUSTOMER
            name = input("Enter Name: ")
            phone = input("Enter Phone: ")
            email = input("Enter Email: ")
            customer = {"name": name, "phone": phone, "email": email}
            customers.append(customer)
            print(f"Customer '{name}' added successfully!")

        elif choice == '2':
            # VIEW CUSTOMERS
            print("\n--- All Customers ---")
            if not customers:
                print("No customers found.")
            else:
                for idx, c in enumerate(customers, 1):
                    print(f"{idx}. Name: {c['name']} | Phone: {c['phone']} | Email: {c['email']}")

        elif choice == '3':
            # SEARCH CUSTOMER
            search_name = input("Enter the name to search for: ").lower()
            found = False
            for c in customers:
                if search_name in c['name'].lower():
                    print(f"Found: Name: {c['name']}, Phone: {c['phone']}, Email: {c['email']}")
                    found = True
            if not found:
                print("No customer matching that name was found.")

        elif choice == '4':
            print("Exiting system. Goodbye!")
            break
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()