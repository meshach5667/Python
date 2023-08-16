import tkinter as tk 

class MyGUI:
    def __init__(self):
      

        self.label = tk.Label(self.window,text = "Your message",font=("Arial",18))
        self.label.pack(padx=10,pady=10)
        self.textBox = tk.Text(self.window,height=5,font=("Arial",16))
        self.textBox.pack(padx=10,pady=10)
        self.check_state =tk.IntVar()

        self.button = tk.Button(self.window,text="Show message",font=("Arial",18),command=self.show_message)
        self.button.pack


        self.check = tk.Checkbutton(self.root,text="Show message box",font=("Arial",18))
        self.check.pack(padx=10,pady=10)

       
    #def show_message():
       # print(self.check_state.get())
        self.window = tk.Tk()
        self.window.mainloop()

        