import pandas

data = pandas.read_csv('./squirrel_data.csv')

fur_colors = data['Primary Fur Color'].value_counts()

fur_colors.rename('c')
fur_colors.to_csv('fur_colors.csv')

print(data['Primary Fur Color'].value_counts())
