import json
import random
import string
from pathlib import Path


class Bank:
    database = Path("Bank-Systeam(PY)\deta1.json")  #  file will be created in same folder
    data = []

    #  Load data safely
    @classmethod
    def load_data(cls):
        if cls.database.exists():
            try:
                content = cls.database.read_text().strip()
                if content:
                    cls.data = json.loads(content)
                else:
                    cls.data = []
            except Exception:
                cls.data = []
        else:
            cls.data = []

    #  Save data safely
    @classmethod
    def save_data(cls):
        cls.database.write_text(json.dumps(cls.data, indent=4))

    @classmethod
    def accountNoGenerator(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=6)
        ac = num + alpha
        return "".join(ac)

    def create_account(self):
        name = input("Enter Your Name: ")
        age = int(input("Enter Your Age: "))
        if age <= 18:
            print("❌ Sorry! Age must be above 18.")
            return
        email = input("Enter Your Email: ")
        pin = input("Enter 4 Digit Pin: ")
        if len(pin) != 4 or not pin.isdigit():
            print("❌ Pin must be exactly 4 digits.")
            return

        info = {
            "name": name,
            "age": age,
            "email": email,
            "pin": int(pin),
            "accountNo.": Bank.accountNoGenerator(),
            "balance": 0
        }

        Bank.data.append(info)
        Bank.save_data()

        print("\n✅ Account Created Successfully!")
        print("===Your Account Details===")
        for k, v in info.items():
            if k != "pin":
                print(f"  {k} : {v}")
        print("⚠️ Save your Account Number safely!")

    def deposit_money(self):
        account = input("\n Enter Your Account Number: ")
        password = input("Enter Your Pin: ")

        if not password.isdigit():
            print("❌ Pin must be numeric.")
            return

        user = None
        for i in Bank.data:
            if i["accountNo."] == account and i["pin"] == int(password):
                user = i
                break

        if user is None:
            print("❌ Account not found / Wrong pin!")
            return

        amount = int(input("Enter Amount To Deposit: "))

        if amount <= 0:
            print("❌ Amount must be greater than 0.")
            return

        if amount > 10000:
            print("❌ You can only deposit up to 10000.")
            return

        user["balance"] += amount
        Bank.save_data()

        print(f"✅ Deposited {amount}")
        print(f"💰 New Balance: {user['balance']}")
    
    def withdraw_money(self):
        account = input("\nEnter Your Account Number: ")
        password = input("Enter Your Pin: ")

        if not password.isdigit():
            print("❌ Pin must be numeric.")
            return

        user = None
        for i in Bank.data:
            if i["accountNo."] == account and i["pin"] == int(password):
                user = i
                break

        if user is None:
            print("❌ Account not found / Wrong pin!")
            return

        amount = int(input("Enter Amount To Withdraw: "))

        if amount <= 0:
            print("❌ Amount must be greater than 0.")
            return

        if amount > i["balance"]:
            print("❌ You can only withdraw within your Account Balance .")
            return

        user["balance"] -= amount
        Bank.save_data()

        print(f"✅ Withdraw {amount}")
        print(f"💰 New Balance: {user['balance']}")
    
    def show_details(self):
         account = input("\nEnter Your Account Number: ")
         password = input("Enter Your Pin: ")

         if not password.isdigit():
            print("❌ Pin must be numeric.")
            return

         user = None
         for i in Bank.data:
            if i["accountNo."] == account and i["pin"] == int(password):
                user = i
                break

         if user is None:
            print("❌ Account not found / Wrong pin!")
            return
         
         for i in user:
             print(f"{i}  : {user[i]}")



# Load stored data first
Bank.load_data()
user = Bank()
rep = True
while rep :
    print("\n====== BANK SYSTEM ======")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. withdraw Money")
    print("4. Show Details")
    print("5. For Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        user.create_account()
    elif choice == 2:
        user.deposit_money()
    elif choice == 3:
        user.withdraw_money()
    elif choice == 4:
        user.show_details()
    elif choice == 5:
        choice=0
        print("\n====== THANK YOU FOR USING BANK SYSTEM ======")
        break
    else:
        print("❌ Invalid Choice")

