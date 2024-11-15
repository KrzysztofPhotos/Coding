class Complex:
    def __init__(self, realpart, imagpart): 
        self.r = realpart
        self.i = imagpart
    def conjugate(self):
        self.i = -self.i
        
x = Complex(2.0, -1.0)
a = x.r # 2.0
b = x.i # -1.0
x.conjugate()
print(x.i) # 1.0




class Customer:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        
    def __str__(self):
        return "Klient [imię: " + self.first_name + ", nazwisko: " + self.last_name + ", email: " + self.email + "]"
    
    def short_name(self):
        return self.first_name[0] + self.last_name[0]
    
customer1 = Customer("Jan","Nowak","jan.nowak@gmail.com")
customer2 = Customer("Anna","Kowalska","anna.kowalska@gmail.com")

print(customer1)
print(customer2)

print(customer1.short_name())


class Company:
    def __init__(self, company_name, nip, mail):
        self.company_name = company_name
        self.nip = nip
        self.mail = mail
        
    def print_label(self):
        print('Company name: ' + self.company_name + "; NIP: " + self.nip)
        
company1 = Company("Cisco", "502876485", "contact@cisco.com")

company1.print_label()



class Book:
    def __init__(self, title, author, release_date, availability):
        self.title = title
        self.author = author
        self.release_date = release_date
        self.availability = availability
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Release Date: {self.release_date}, Availability: {self.availability}"


# class Library:
#     def __init__(self) -> None:
#         pass
#     def add()

book1 = Book("Example Book", "John Author", "2022-01-01", True)
print(book1)