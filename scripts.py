import pandas as pd
import os, csv

# Convert all Custom Index to JSON File
def index_json(index_path):
    # Get List of Custom Indices from folder
    indices_list = os.listdir(index_path)
    for index in indices_list:
        # Read Custom Index
        with open(index_path + index) as f:
            reader = csv.reader(f)
            dfIndex = list(reader)
    # Convert to JSON
    basketOrder = pd.read_json('basketOrder.json')
    print(basketOrder)

# Create JSON File for Kite Basket Order
def kite_basket_order(index_path):
    a = 1


if __name__ == '__main__':
    index_path = os.getcwd() + '/indices/'
    index_json(index_path)