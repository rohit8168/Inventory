import pandas as pd
import json

def load_data_from_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def save_data_to_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)

def displa():
    data = load_data_from_file('data.json')
    df = pd.DataFrame(data.values(), index=data.keys())
    print(df)

def specific():
    data = load_data_from_file('data.json')
    order_id = input("Enter the order ID you want to find: ")
    if order_id in data:
        order_data = data[order_id]
        df = pd.DataFrame([order_data], index=[order_id])
        print(df)
    else:
        print("Invalid order ID")

def add():
    data = load_data_from_file('data.json')
    order_id = int(input("Enter the order ID: "))
    dict2 = {}
    dict2['name'] = input("Enter the name: ")
    dict2['price'] = float(input("Enter the price: "))
    dict2['category'] = input("Enter the category: ")
    dict2['quantity'] = int(input("Enter the quantity: "))
    dict2['date'] = input("Enter the date: ")
    data[order_id] = dict2
    save_data_to_file(data, 'data.json')

def delete():
    data = load_data_from_file('data.json')
    order_id = input("Enter the order ID of the product you want to delete: ")
    if order_id in data:
        del data[order_id]
        save_data_to_file(data, 'data.json')
    else:
        print("Invalid order ID")

def update():
    data = load_data_from_file('data.json')
    order_id = input("Enter the order ID you want to update: ")
    if order_id in data:
        update_type = int(input("Enter 0 to update the whole data, or 1 for a specific attribute: "))
        if update_type == 0:
            for key in data[order_id]:
                data[order_id][key] = input(f"Enter the value for {key}: ")
        elif update_type == 1:
            attribute = input("Enter the attribute name: ")
            if attribute in data[order_id]:
                if attribute == 'price' or attribute == 'quantity':
                    data[order_id][attribute] = int(input(f"Enter the value for {attribute}: "))
                else:
                    data[order_id][attribute] = input(f"Enter the value for {attribute}: ")
            else:
                print("Invalid attribute")
        else:
            print("Invalid update type")
        save_data_to_file(data, 'data.json')
    else:
        print("Invalid order ID")

def del_all():
    data = {}
    save_data_to_file(data, 'data.json')



