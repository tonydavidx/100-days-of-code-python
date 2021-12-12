
import csv
import pandas

# with open('./weather_data.csv', 'r') as wd:
#     data = csv.reader(wd)
#     tempratures = []
#     for row in data:
#         if row[1] != 'temp':
#             tempratures.append(int(row[1]))

#     tempratures.pop(0)


# reading csv with pandas
data = pandas.read_csv('./weather_data.csv')

# data_dict = data.to_dict()

# temp_list = data['temp'].to_list()


# max_temp = data['temp'].max()

# # get average temprature from list
# average_temp = data['temp'].mean()

# max_temp_row = data[data.temp == data.temp.max()]


# monday = data[data.day == 'Monday']

# monday_temp = monday.temp


# def celcius_convert(temp):
#     c = (temp * 9/5) + 32
#     return c


# mon_temp_f = (monday_temp * 9/5) + 32

# generate dictionary with names and scores
my_dict = {
    'name': ['angela', 'leo', 'frodo'],
    'scores': [10, 10, 25]
}

data = pandas.DataFrame(my_dict)

data.to_csv('new_dict.csv')
