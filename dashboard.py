import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import *
import platform
import subprocess

servers = []
image_references = []

def check_server_status(server_ip):
    try:
        if selected_os == "Windows":
            command = ["ping", "-n", "1", server_ip]
        elif selected_os == "MacOS" or selected_os == "Linux":
            command = ["ping", "-c", "1", server_ip]
        else:
            return False
        
        result = subprocess.run(command, capture_output=True, text=True, shell=platform.system() == "Windows")
        if result.returncode == 0:
            return True
        else:
            return False  # Return False if ping fails
    except subprocess.CalledProcessError:
        return False  # Return False if an error occurs

def open_start_window():
    start_window = tk.Tk()
    start_window.title("Operating System Selection")
    
    # Combobox with options
    combo = Combobox(start_window)
    combo['values'] = ("Windows", "MacOS", "Linux")
    combo.pack(pady=10)
    
    # Function to close the start window
    def close_start_window():
        global selected_os
        selected_os = combo.get()
        if selected_os:
            start_window.destroy()
            open_login_window(selected_os)
        else:
            messagebox.showwarning("Warning", "Please select an operating system!")
    
    # Start button
    start_button = tk.Button(start_window, text="Start", command=close_start_window)
    start_button.pack(pady=10)
    
    start_window.mainloop()

def open_login_window(selected_os):
    login_window = tk.Tk()
    login_window.title("Login")
    
    # IP address entry field
    ip_label = tk.Label(login_window, text="Server IP Address:")
    ip_label.pack(pady=10)
    ip_entry = tk.Entry(login_window)
    ip_entry.pack(pady=5)
    
    # Server name entry field
    name_label = tk.Label(login_window, text="Server Name:")
    name_label.pack(pady=10)
    name_entry = tk.Entry(login_window)
    name_entry.pack(pady=5)
    
    # Add server button
    def add_server():
        ip = ip_entry.get()
        name = name_entry.get()
        if ip and name:
            servers.append({'ip': ip, 'name': name})
            ip_entry.delete(0, tk.END)
            name_entry.delete(0, tk.END)
            messagebox.showinfo("Information", "IP Address Added")
        else:
            messagebox.showwarning("Warning", "Please enter the IP address and server name!")
    
    add_button = tk.Button(login_window, text="Add", command=add_server)
    add_button.pack(pady=10)
    
    # Run button
    def close_login_window():
        login_window.destroy()
        open_dashboard(selected_os)
    
    run_button = tk.Button(login_window, text="Run", command=close_login_window)
    run_button.pack(pady=10)
    
    login_window.mainloop()

def open_dashboard(selected_os):
    dashboard_window = tk.Tk()
    dashboard_window.title("Dashboard")

    def update_server_status():
        for i, server in enumerate(servers):
            server_name = server['name']
            server_ip = server['ip']
            
            status = check_server_status(server_ip)
            image_path = "green.png" if status else "red.png"
            
            image = tk.PhotoImage(file=image_path)
            image_references[i] = image
            
            image_labels[i].configure(image=image)
            image_labels[i].image = image
            
            server_labels[i].configure(text=f"{server_name}\n{server_ip}", foreground="green" if status else "red")
        
        dashboard_window.update_idletasks()
        dashboard_window.after(5000, update_server_status)
    
    num_servers = len(servers)
    num_columns = 3
    num_rows = (num_servers + num_columns - 1) // num_columns
    
    global server_labels
    global image_labels
    
    server_labels = []
    image_labels = []
    
    for i, server in enumerate(servers):
        server_name = server['name']
        server_ip = server['ip']
        
        subframe = tk.LabelFrame(dashboard_window, text=server_name)
        subframe.grid(row=i // num_columns, column=i % num_columns, padx=10, pady=5)
        
        label = tk.Label(subframe, text="Pinging...")
        label.pack()
        server_labels.append(label)
        
        image_label = tk.Label(subframe)
        image_label.pack(pady=5)
        image_labels.append(image_label)
        
        image = tk.PhotoImage(file="")
        image_references.append(image)
    
    update_server_status()
    
    dashboard_window.mainloop()

open_start_window()
