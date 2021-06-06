import pandas

# Read the data
data = pandas.read_csv('squirrel_data.csv')


# Count the number of squirrels of each color
gray = len(data[data["Primary Fur Color"] == "Gray"])
red = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])

# Create a dictionary of the data
data_dict = {
    "Fur Color": ['gray', 'red', 'black'],
    "Count": [gray, red, black]
}

# Convert the dictionary to a DataFrame
dataframe = pandas.DataFrame(data_dict)

# Export the data as a CSV file
dataframe.to_csv('squirrel_count.csv')
