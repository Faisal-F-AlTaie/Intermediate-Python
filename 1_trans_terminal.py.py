def show_balance():
    print(f"Your balance is ${balance:.2f}")




def deposit ():
    amount = float(input("Enter amount to deposit: "))
    if amount < 0:
        print("Deposit amount must be valid.")
        return 0   
    else:
        return amount



def withdraw ():
    amount = float(input("Enter amount to withdrawn: ")) 
    if amount > balance:
        print("Insufficient funds.")
        return 0
    else:
        return amount



def main():
    balance = 0
    is_running = True



    while is_running:
        print("Banking Program")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            show_balance()
            
        elif choice == '2':
            balance += deposit()
            
        elif choice == '3':
            balance -= withdraw()
        
        elif choice == '4':
            print("Exiting the program.")
            is_running = False
        
        else:
            print("Invalid choice. Please try again.")
            
    print("Thank you for banking with us :)")
    
if __name__ == "__main__":
    main()
            