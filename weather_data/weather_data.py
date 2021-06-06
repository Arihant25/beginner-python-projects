# #  Gets the temperatures from the CSV file using Python's inbuilt CSV module

# import csv

# with open('weather_data.csv') as file:
#     data = csv.reader(file)
#     temperatures = []

#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))

#     print(temperatures)

# # Does the same thing, but using pandas

# import pandas

# data = pandas.read_csv("weather_data.csv")

# print(data)
# print(data["temp"])

# # Calculates the average temperature

import pandas

# data = pandas.read_csv("weather_data.csv")

# # Using Python's methods

# data_dict = data.to_dict()
# temp_list = data['temp'].to_list()

# print("Average temperature is " + str(round(sum(temp_list)/len(temp_list), 2)) + "°C.")

# # Using Pandas in-built method

# print("Average temperature is " + str(round(data['temp'].mean(), 2)) + "°C.")

# # Find the maximum temperature

# print("The maximum temperature is " + str(data['temp'].max()) + "°C.")

# # Find which day had the maximum temperature and print the row

# print(data[data.temp == data.temp.max()])

# # Find the temperature on Monday and convert it to Fahrenheit

# monday = data[data.day == "Monday"].temp
# fahrenheit = monday * 9/5 + 32
# print(fahrenheit)

# # Create a DataFrame from scratch

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# data = pandas.DataFrame(data_dict)

# print(data)

# # Convert DataFrame to CSV file

# data.to_csv('scores.csv')
