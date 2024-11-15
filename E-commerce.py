from tabulate import tabulate

customers_list = [["Imie", "Nazwisko"], ["Sebastian", "Kondracki"], ["Piotr", "Nowak"]]

print(tabulate(customers_list, headers="firstrow", tablefmt="html"))


from rich.console import Console
from rich.table import Table

customers = []

customers.append(['2021-02-03', 'Jan Nowak', '2000.00 PLN'])
customers.append(['2021-02-01', 'Anna Kowalska', '1500.00 PLN'])
customers.append(['2021-02-13', 'Ewelina Domag', '500.00 PLN'])

table = Table(title="Sprzedaż Q1-2021")
table.add_column("Data transakcji", justify="right", style="cyan", no_wrap=True)
table.add_column("Klient", style="magenta")
table.add_column("Przychód", justify="right", style="green")

for customer in customers:
    table.add_row(customer[0], customer[1], customer[2])
    
console = Console()
console.print(table)


