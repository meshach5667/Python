class Music:
    def __init__(self,name:str,amount:int,price:int):
        

         self.name = name
         self.amount = amount
         self.price = price
         

    def musical_instruments(self):
        return self.amount * self.price

guitar = Music(input("Enter the type of instrument you want: "), input("Enter amount: "),200)
piano = Music(input("Enter the type of instrument you want: "),input("Enter amount: "),400)


print(guitar.musical_instruments())
print(piano.musical_instruments())



        

        
       
     



