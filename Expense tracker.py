import os

# File to store transactions
FILE_NAME = "expenses.txt"

def load_transactions():
    transactions = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                date, type_, amount, category = line.strip().split(",")
                transactions.append({
                    "date": date,
                    "type": type_,
                    "amount": float(amount),
                    "category": category
                })
    return transactions

def save_transaction(transaction):
    with open(FILE_NAME, "a") as file:
        file.write(f"{transaction['date']},{transaction['type']},{transaction['amount']},{transaction['category']}\n")

def add_transaction():
    date = input("Enter date (YYYY-MM-DD): ")
    type_ = input("Type (income/expense): ").lower()
    amount = float(input("Amount: "))
    category = input("Category (food, rent, etc.): ")
    transaction = {
        "date": date,
        "type": type_,
        "amount": amount,
        "category": category
    }
    save_transaction(transaction)
    print("Transaction saved!\n")

def show_transactions(transactions):
    if not transactions:
        print("No transactions found.")
        return
    print("\n--- All Transactions ---")
    for t in transactions:
        print(f"{t['date']} - {t['type'].capitalize()} - ₹{t['amount']} ({t['category']})")
    print()

def show_balance(transactions):
    income = sum(t["amount"] for t in transactions if t["type"] == "income")
    expenses = sum(t["amount"] for t in transactions if t["type"] == "expense")
    balance = income - expenses
    print(f"\nTotal Income: ₹{income}")
    print(f"Total Expenses: ₹{expenses}")
    print(f"Current Balance: ₹{balance}\n")

def main():
    while True:
        print("------ Expense Tracker ------")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. View Balance")
        print("4. Exit")
        choice = input("Choose an option: ")

        transactions = load_transactions()

        if choice == "1":
            add_transaction()
        elif choice == "2":
            show_transactions(transactions)
        elif choice == "3":
            show_balance(transactions)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.\n")

if __name__ == "__main__":
    main()
  
