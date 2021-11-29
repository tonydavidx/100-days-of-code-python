import pandas

data = pandas.read_csv('./squirrel_data.csv')

fur_colors = data['Primary Fur Color'].value_counts()

gray_squirrel = len(data[data['Primary Fur Color'] == 'Gray'])
cinnamon_squirrel = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrel = len(data[data['Primary Fur Color'] == 'Black'])

my_dict = {
    'colors': ['Gray', 'Cinnamon', 'Black'],
    'Count': [gray_squirrel, cinnamon_squirrel, black_squirrel]
}

df = pandas.DataFrame(my_dict)

df.to_csv('fur_colors.csv')

print(df)
