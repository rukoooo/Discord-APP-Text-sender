import tkinter as tk
import requests
import threading
import time

def send_message():
    webhook_url = webhook_entry.get()
    message = message_entry.get("1.0", "end-1c")
    
    payload = {"content": message}
    response = requests.post(webhook_url, json=payload)
    
    if response.status_code == 204:
        status_label.config(text="Message sent successfully!", fg="green")
    else:
        status_label.config(text="Failed to send message.", fg="red")

def spam_message():
    webhook_url = webhook_entry.get()
    message = message_entry.get("1.0", "end-1c")
    
    while spamming:
        payload = {"content": message}
        response = requests.post(webhook_url, json=payload)
        if response.status_code != 204:
            status_label.config(text="Failed to send message.", fg="red")
        time.sleep(0.01)  # Decreased sleep time for faster spamming

def start_spam():
    global spamming
    spamming = True
    threading.Thread(target=spam_message).start()

def stop_spam():
    global spamming
    spamming = False

# Create main window
root = tk.Tk()
root.title("Rukos App sender")
root.configure(bg="black")

# Webhook entry
webhook_label = tk.Label(root, text="Enter Webhook:", fg="white", bg="black", font=("Courier", 12, "bold"))
webhook_label.grid(row=0, column=0, sticky="w", padx=10, pady=(20,5))

webhook_entry = tk.Entry(root, width=50, bg="black", fg="white", bd=2, insertbackground="white", font=("Courier", 12))
webhook_entry.grid(row=0, column=1, padx=10, pady=(20,5))

# Message entry
message_label = tk.Label(root, text="Enter Message:", fg="white", bg="black", font=("Courier", 12, "bold"))
message_label.grid(row=1, column=0, sticky="w", padx=10, pady=(5,5))

message_entry = tk.Text(root, width=40, height=5, bg="black", fg="white", bd=2, insertbackground="white", font=("Courier", 12))
message_entry.grid(row=1, column=1, padx=10, pady=(5,5))

# Send button
send_button = tk.Button(root, text="Send", command=send_message, bg="black", fg="white", bd=2, font=("Courier", 12, "bold"))
send_button.grid(row=2, column=1, pady=(5,20))

# Spam button
spam_button = tk.Button(root, text="Spam", command=start_spam, bg="black", fg="white", bd=2, font=("Courier", 12, "bold"))
spam_button.grid(row=2, column=1, padx=10, pady=(5,20), sticky="e")

# Stop button
stop_button = tk.Button(root, text="Stop", command=stop_spam, bg="black", fg="white", bd=2, font=("Courier", 12, "bold"))
stop_button.grid(row=2, column=1, padx=10, pady=(5,20), sticky="w")

# Status label
status_label = tk.Label(root, text="", fg="white", bg="black", font=("Courier", 12, "bold"))
status_label.grid(row=3, column=1, pady=5)

root.mainloop()
