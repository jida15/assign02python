#Question 1: Car Class
class Car:
    def __init__(self, brand, model, year):
        self.brand=brand
        self.model=model
        self.year=year
        self.speed=0

    def accelerate(self, amount):
        self.speed+=amount
        print(f"Accelerated by {amount}. Current speed: {self.speed}")

    def brake(self, amount):
        self.speed-=amount
        if self.speed<0:
            self.speed=0
        print(f"Braked by {amount}. Current speed: {self.speed}")

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Speed: {self.speed}")


#Objects and Method Calls
car1=Car("Toyota", "Corolla", 2020)
car2=Car("Tesla", "Model 3", 2023)

car1.accelerate(70)
car1.brake(30)
car1.display_info()

car2.accelerate(80)
car2.brake(20)
car2.display_info()




#Question 2 : Bank Account Class
class BankAccount:
    def __init__(self, account_holder, account_number):
        self.account_holder=account_holder
        self.account_number=account_number
        self.balance=0
        self.transactions=[]

    def deposit(self, amount):
        self.balance+=amount
        self.transactions.append(f"Deposited: {amount}")
        print(f"Deposited {amount}")

    def withdraw(self, amount):
        if amount>self.balance:
            print("Error: Insufficient balance")
        else:
            self.balance-=amount
            self.transactions.append(f"Withdrawn: {amount}")
            print(f"Withdrawn {amount}")

    def get_balance(self):
        print(f"Current Balance: {self.balance}")

    def transaction_history(self):
        print("Transaction History:")
        for t in self.transactions:
            print(t)


#Objects and transactions
acc1 = BankAccount("Sunjida", "A171")
acc2 = BankAccount("sultana", "A172")

acc1.deposit(6000)
acc1.withdraw(2000)
acc1.deposit(2000)
acc1.get_balance()
acc1.transaction_history()

acc2.deposit(8000)
acc2.withdraw(1000)
acc2.withdraw(2000)
acc2.get_balance()
acc2.transaction_history()




#Question 3: Library and Book classes
class Book:
    def __init__(self, title, author, isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.is_available=True


class Library:
    def __init__(self, name):
        self.name=name
        self.books=[]

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn==isbn and book.is_available:
                book.is_available=False
                print(f"Borrowed: {book.title}")
                return
        print("Book not available")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn==isbn:
                book.is_available=True
                print(f"Returned: {book.title}")
                return

    def show_available_books(self):
        print("\nAvailable Calculus Books:")
        for book in self.books:
            if book.is_available:
                print(f"{book.title} by {book.author}")



#Create Library and Calculus Books
library = Library("SEU Library")

book1=Book("Calculus", "James Stewart", "C101")
book2=Book("Thomas' Calculus", "George B. Thomas", "C102")
book3=Book("Advanced Engineering Mathematics", "Erwin Kreyszig", "C103")
book4=Book("Calculus Made Easy", "Silvanus P. Thompson", "C104")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)

#Borrow and return Operations
library.borrow_book("C101")
library.borrow_book("C102")
library.return_book("C101")
library.show_available_books()





#Question 4: Employee Class
class Employee:
    total_employees=0

    def __init__(self, name, employee_id, department, salary):
        self.name=name
        self.employee_id=employee_id
        self.department=department
        self.salary=salary
        Employee.total_employees+=1

    def give_raise(self, percent):
        self.salary+=self.salary * (percent / 100)

    def details(self):
        print(f"Name: {self.name}, ID: {self.employee_id}, Dept: {self.department}, Salary: {self.salary}")


#Objects and Operations
e1=Employee("Sunjida", "E01", "IT", 25000)
e2=Employee("Sultana", "E02", "HR", 30000)
e3=Employee("Munira", "E03", "Finance", 20000)

e1.give_raise(7)
e2.give_raise(8)

e1.details()
e2.details()
e3.details()

print("Total Employees:", Employee.total_employees)





#Question 5: Shopping Cart Class
class ShoppingCart:
    def __init__(self, customer_name):
        self.customer_name=customer_name
        self.items=[]

    def add_item(self, name, price, quantity):
        self.items.append({
            "name": name,
            "price": price,
            "quantity": quantity
        })

    def remove_item(self, name):
        self.items=[item for item in self.items if item["name"] != name]

    def total_price(self):
        total=0
        for item in self.items:
            total+=item["price"] * item["quantity"]
        return total

    def show_cart(self):
        print(f"Shopping Cart for {self.customer_name}")
        for item in self.items:
            print(f"Item: {item['name']}, Price: {item['price']}, Quantity: {item['quantity']}")
        print("Total Price:", self.total_price())


#Creating Objects and Performing Operations
cart1=ShoppingCart("Sunjida")
cart2=ShoppingCart("Sultana")

cart1.add_item("Lipstick", 800, 2)
cart1.add_item("Foundation", 1800, 1)
cart1.add_item("Eyeliner", 450, 2)
cart1.remove_item("Eyeliner")
cart1.show_cart()

cart2.add_item("Compact Powder", 900, 1)
cart2.add_item("Mascara", 1200, 1)
cart2.add_item("Blush", 700, 2)
cart2.remove_item("Blush")
cart2.show_cart()
