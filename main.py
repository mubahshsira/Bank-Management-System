class Account:
    def __init__(self,account_name,account_id,balance=0):

        self.account_name = account_name
        self.account_id = account_id
        self.balance = balance

    def deposit(self,amount):
            self.balance+=amount


    def withdraw(self,amount):
       if  self.balance>=amount:
           self.balance-=amount
       else:
            print("insufficient Balance")

    def display(self):
        print(f"Account ID: {self.account_id}, Account Name: {self.account_name}, Balance: {self.balance}")

class Customer:
    def __init__(self,name,id):
        self.customer_name = name
        self.customer_id = id
    def __str__(self):
        return f"Customer Name: {self.customer_name}, Customer ID: {self.customer_id}"

class bank:
    def __init__(self,bank_name):
        self.bank_name = bank_name
        self.customers=[]
        self.customers_id = []
        self.accounts = []

    def new_customer(self, name, customer_id):
        customer = Customer(name,customer_id)
        self.customers.append(customer)
        print(f"Customer {name} with ID {customer_id} added to {self.bank_name}")

    def add_account(self,account_name,customers_id):
        account = Account(account_name,customers_id)
        self.accounts.append(account)
        print(f"Account {account_name} added for customer ID {customers_id}")

    def deposit(self,name,id,amount):
        if name in self.customers and id in  self.customers_id :
            self.deposit(amount)
            print(f"Deposited {amount} into Account {name}. Current balance: {Account.balance}")
        else:
            print("Customer or Account not found.")
    def withdraw(self,name,id,amount):
      if name in self.customers and id in self.customers_id:
          self.withdraw(amount)
      else:
          print("Customer or Account not found or insufficient balance.")
    def transfer_money(self,from_account,to_account,amount):
        for from_account in self.accounts:
            if from_account == from_account:
                for to_account in self.accounts:
                    if to_account ==to_account:
                        if from_account.balance>=amount:
                            from_account.withdraw(amount)
                            to_account.deposite(amount)
                            print(f"Transferred {amount} from {from_account} to {to_account}.")
                        else:
                            print("Insufficient balance for transfer")
                            break


    def customers_lst(self):
     for customers in self.customers:
       print(customers)




bank_name = "eShikhon Bank PLC"

bank = bank(bank_name)





while True:
    print(f'welcome to {bank.bank_name}\n'
      f'1.add customer\n'
      f'2.add_acc\n'
      f'3.deposite money\n'
      f'4.withdraw money\n'
      f'5 .transfer money\n'
      f'6.customer list\n'
      f'7.Exit')
    num=input('Enter the number:')

    if num == '1':
            name = input("Enter customer name: ")
            id = int(input("Enter customer ID: "))
            bank.new_customer(name, id)

    elif num =='2':
        name = input("Enter customer name: ")
        id = int(input("Enter customer ID: "))
        bank.add_account(name,id)
        print("Your acc has created")


    elif num == '3':
        name=input("enter your name:")
        id = (input("enter your id:"))
        amount = int(input("enter the amount:"))
        deposite_money = (bank.deposit(name,id,amount))
        print(f'{amount} has deposited in your acc')

    elif num == '4':
        name=input("enter your name:")
        id = (input("enter your id:"))
        amount = int(input("enter the amount:"))
        withdraw_money = (bank.withdraw(name,id,amount))


    elif num == "5":
        from_name =input("enter your acc name:")
        to_name =input("enter the  transfer acc name:")
        amount = int(input("enter the transfer amount:"))
        print(f'{amount} tk has transfered from {from_name} to  {to_name}')

    elif num == '6':
        customers_lst = bank.customers_lst()

    elif num =='7':
            print("Finishing.....")
            break
    else:
        ("envalid input")
