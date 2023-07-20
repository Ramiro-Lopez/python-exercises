def initialize_balance() -> float:
    """Checks if a 'checkbook.txt` file exists in the current directory"""
    f = open("checkbook.txt", "r")
    balance = float(f.readline().strip())
    f.close()
    if balance == '':
        return 0
    else:
        return balance


def save_balance(current_balance: float) -> None:
    """Saves current balance to file 'checkbook.txt'"""
    f = open("checkbook.txt", "w")
    f.write(str(current_balance))
    f.close()

historical_data = []


def main() -> None:
    print("\n******** Welcome to your terminal checkbook! ********")

    options = "\n\n1) Make a deposit\n2) Make a withdrawl\n3) Check current balance\n4) View history\n5) Exit\n\n"
    
    balance = initialize_balance()

    while True:
        """loop that updates the balance and saves the changes"""
        print(options)
        selection = int(input("What would you like to do? "))
        if selection == 1:
            deposit = float(input("Enter the deposit amount: "))
            balance += deposit
            print("Deposit successful.")
            historical_data.append(f'Deposit: {deposit}')
        elif selection == 2:
            withdrawal = float(input("Enter the withdrawal amount: "))
            if withdrawal > balance:
                print("Insufficient funds.")
            else:
                balance -= withdrawal
                print("Withdrawal successful.")
            historical_data.append(f'Withdrawal: {withdrawal}')
        elif selection == 3:
            print(f"Current balance: {balance}")
        elif selection == 4:
            print(historical_data)
        elif selection == 5:
            print('Thank you! Have a great day.')
            exit()
        else:
            print("Invalid selection.")

        save_balance(balance)
        
        user_cb = input("Would you like to make another transation? (y/n) ")
        if user_cb.lower() != "y":
            print("Thank you! Enjoy your day.")
            break


if __name__ == "__main__":
    main()