import csv

class Item:
     pay_rate = 0.9 #the pay rate after 20% discount
     all = []
    
     def __init__(self,name:str,price:int,quantity=0):
         #if you don't know the exact quantity of item then you pass 0 to the agument "quantity"

         #RUN VALIDATION TO THE RECIEVED ARGUMENT
        assert price >=0, f"price {price} is not >= 0" 
        assert quantity >=0, f"quantity {quantity} is not >= 0"
        #this assert variable is to state the int range
 #it is more like a conditional statement
#you can also print an error message if the output is not true

     #ASSIGN TO SELF OBJECT
        self.name = name    
        self.price = price
        self.quantity = quantity 
       
#acions to execute
        Item.all.append(self)
     def calculate_total_price(self):
         return self.price*self.quantity

     def apply_discount(self):
         self.price = self.price * self.pay_rate
     @classmethod
     def instantiate_from_csv(cls):
        with open("items.csv","r") as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name=item.get("name"),
                price=int(item.get("price")),
             quantity=int(item.get("quantity"))

            )



     def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})"

Item.instantiate_from_csv()

print(Item.all)