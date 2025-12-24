import json
import os
from datetime import datetime

BUDGET_FILE = 'budget.json'

def load_budget():
    try:
        if os.path.exists(BUDGET_FILE):
            with open(BUDGET_FILE, 'r') as file:
                return json.load(file)
#         Opens the file in read mode ("r")
# json.load(file) converts JSON text back to Python dictionary
# Returns the dictionary
        else:
            return {"budget": 0, "transaction": []}
    except:
        print("Error loading budget file.")

def save_budget(data):
    """Save budget data to file"""
    try:
        with open(BUDGET_FILE, "w") as file:
            json.dump(data, file, indent=4)
#             Opens file in write mode ("w")
# Creates file if it doesn't exist
# Overwrites file if it exists
# json.dump() converts Python dictionary to JSON text
# data = what to save
# file = where to save it
# indent=2 = make it readable (pretty formatting)
    except:
        print("Error saving budget file.")

def add_transaction(data, amount, description, trans_type):
    """Add income or expense"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    transaction = {
        "date": timestamp,
        "type": trans_type,
        "amount": amount,
        "description": description
    }
    if "transactions" not in data:
        data["transactions"] = []
        return data
    
    data["transactions"].append(transaction)
    
    if trans_type == "income":
        data["balance"] += amount
    else:
        data["balance"] -= amount
    
    save_budget(data)

def show_balance(data):
    """Display current balance"""
    print(f"\n💰 Current Balance: ${data['balance']:.2f}")

def show_transactions(data):
    """Show all transactions"""
    if len(data["transactions"]) == 0:
        print("\n📭 No transactions yet")
        return
    
    print("\n📊 Transaction History:")
    for t in data["transactions"]:
        symbol = "+" if t["type"] == "income" else "-"
        print(f"{t['date']} | {symbol}${t['amount']:.2f} | {t['description']}")

print("💰 BUDGET TRACKER 💰\n")

budget_data = load_budget()

if "transactions" not in budget_data:
    budget_data["transactions"] = []
if "balance" not in budget_data:
    budget_data["balance"] = 0

while True:
    print("\n1. Add Income")
    print("2. Add Expense")
    print("3. View Balance")
    print("4. View Transactions")
    print("5. Quit")
    
    choice = input("\nChoose (1-5): ")
    
    if choice == "1":
        try:
            amount = float(input("Amount: $"))
            desc = input("Description: ")
            add_transaction(budget_data, amount, desc, "income")
            print("✅ Income added!")
        except ValueError:
            print("❌ Invalid amount")
    
    elif choice == "2":
        try:
            amount = float(input("Amount: $"))
            desc = input("Description: ")
            add_transaction(budget_data, amount, desc, "expense")
            print("✅ Expense added!")
        except ValueError:
            print("❌ Invalid amount")
    
    elif choice == "3":
        show_balance(budget_data)
    
    elif choice == "4":
        show_transactions(budget_data)
    
    elif choice == "5":
        print("👋 Goodbye!")
        break
    
    else:
        print("❌ Invalid choice")


    
