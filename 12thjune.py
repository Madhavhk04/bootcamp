import tkinter as tk

def store_text():
    # Get the text from the textbox
    text = textbox.get("1.0", tk.END).strip()
    # Store it in a variable
    global stored_text
    stored_text = text
    # Print the text to confirm the action
    print(f"Stored text: {stored_text}")

# Initialize the main window
root = tk.Tk()
root.title("Text Storage Example")

# Create a textbox
textbox = tk.Text(root, height=10, width=40)
textbox.pack(pady=10)

# Create a button
button = tk.Button(root, text="Store Text", command=store_text)
button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
