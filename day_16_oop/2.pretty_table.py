from prettytable import PrettyTable

table = PrettyTable()

table.add_column('Pokemon Name',['Pikachu','Squrtile','Charmander'])
table.add_column('Type',['Electric','Water','Fire'])
table.align = 'l'
print(table)