import tkinter as tk

def send_message():
    message = entry.get()
    if message:
        chat_box.config(state=tk.NORMAL)
        chat_box.insert(tk.END, "You: " + message + "\n")
        chat_box.config(state=tk.DISABLED)
        entry.delete(0, tk.END)

def clear_chat():
    chat_box.config(state=tk.NORMAL)
    chat_box.delete(1.0, tk.END)
    chat_box.config(state=tk.DISABLED)
 
# Create the main window
root = tk.Tk()
root.title("Chat Box")


# Create a Text widget to display the chat history
chat_box = tk.Text(root, state=tk.DISABLED)
chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create an Entry widget for typing messages
entry = tk.Entry(root)
entry.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create a Send button to send messages
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(padx=10, pady=5)

# Create a Clear button to clear the chat history
clear_button = tk.Button(root, text="Clear Chat", command=clear_chat)
clear_button.pack(padx=10, pady=5)



# Start the Tkinter event loop
root.mainloop()
