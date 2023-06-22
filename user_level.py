import json
import time



def load_data_from_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    file.close()
    return data



def gen_bill():
    
    user_id = input("Enter the user ID: ")
    user_name = input("Enter the user name: ")
    id = input("Enter the product ID: ")

    data = load_data_from_file('data.json')

    if id in data:
        prod = data[id]
        quantity = int(input("Enter the quantity: "))

        if quantity <= int(prod['quantity']):
            prod['quantity'] -= quantity
            amount_paid=int(prod['price']) * quantity
            tax=amount_paid*0.18
            date_time=time.ctime()
            print("-----------------------------")
            print("Name of product:", prod['name'])
            print("Category of product:", prod['category'])
            print("Quantity:", quantity)
            print("---------------------------------")
            print("Total sum:",amount_paid)
            print("GST      :18%")
            print("Your bill",amount_paid+tax)
            print("Thanks for visiting")
            
            trasaction=user_id + "," + user_name + "," + user_id + str(quantity) +"," + str(amount_paid) +","+ str(date_time) +"\n"
            f=open("sales.txt",'a')
            f.write(trasaction)
            f.close()
        elif prod['quantity'] > 0:
            print("We have only", prod['quantity'], "pieces.")
            ch = input("If you want to continue with this quantity, press 'y': ")
            if ch.lower() == 'y':
                amount_paid=int(prod['price']) * prod['quantity']
                date_time=time.ctime
                tax=amount_paid*0.18
                
                print("--------------------------------------")
                print("Name of product:", prod['name'])
                print("Category of product:", prod['category'])
                print("Quantity of product:", prod['quantity'])
                print("---------------------------------")
                print("Total sum:", amount_paid)
                print("gst      :18% ")
                print("Your Bill:",amount_paid+tax)
                prod['quantity'] = 0
                print("Thanks for visiting")
                data[id]=prod
                
                trasaction=user_id + "," + user_name + "," +user_id+ str(prod['quantity']) +"," + str(amount_paid) +","+ str(date_time) +"\n"
                f=open("sales.txt",'a')
                f.write(trasaction)
                f.close()
        else:
            print("We don't have any pieces of this product.")
        with open("data.json",'w') as file:
            json.dump(data,file)
        file.close()
        

