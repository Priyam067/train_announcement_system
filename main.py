import tkinter as tk
from tkinter import ttk, messagebox
from all_variables import *
import tkentrycomplete
from playsound import playsound
import sqlite3
import bcrypt


def get_user_data(username):
    global data_db
    connection = sqlite3.connect(data_db)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user_data = cursor.fetchone()
    connection.close()
    return user_data

def store_user_data(username, password):
    global data_db
    connection = sqlite3.connect(data_db)
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT
        )
    ''')
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    connection.commit()
    connection.close()

def eng_announce(data):
    lst = [
        eng_start,
        train_number,
    ]
    lst.extend([eng_num[i] for i in data['train_number']])
    lst.extend([
        train_type[data['train_type']],
        cities[data['source_station']],
        eng_to,
        cities[data['destination_station']],
    ])
    if data['announcement_type'] == "Arrival":
        lst.append(eng_out_arv)
    else:
        lst.append(eng_out_dep_1)
    lst.extend([eng_num[i] for i in data['platform_number']])
    lst.extend([eng_out_dep_2, bell2])
    list_play(lst)


def hindi_announce(data):
    lst = [
        bell_start,
        hindi_start,
        train_number,
    ]
    lst.extend([hindi_num[i] for i in data['train_number']])
    lst.extend([
        cities[data['source_station']],
        hi_se,
        cities[data['destination_station']],
        jane_wali,
        train_type[data['train_type']],
        hindi_out,
    ])
    lst.extend([hindi_num[i] for i in data['platform_number']])
    if data['announcement_type'] == "Arrival":
        lst.extend([hindi_out_arv, bell_end])
    else:
        lst.extend([hindi_out_dep, bell_end])
    list_play(lst)


def mar_announce(data):
    lst = [
        bell_start,
        mar_start,
    ]
    lst.extend([mar_num[i] for i in data['train_number']])
    lst.extend([
        cities[data['source_station']],
        cities[data['destination_station']],
        train_type[data['train_type']],
    ])
    if data['announcement_type'] == "Arrival":
        lst.append(hindi_out)
        lst.extend([mar_num[i] for i in data['platform_number']])
        lst.append(mar_out_arv)
    else:
        lst.append(mar_out)
        lst.extend([mar_num[i] for i in data['platform_number']])
        lst.extend([mar_out_dep, bell_end])
    list_play(lst)


def guj_announce(data):
    lst = [
        bell_start,
        guj_start,
        cities[data['source_station']],
        guj_thi,
        cities[data['destination_station']],
        guj_java_vali,
        train_type[data['train_type']],
        guj_gadi,
    ]
    lst.extend([guj_num[i] for i in data['train_number']])
    lst.append(platform_num_guj)
    lst.extend([guj_num[i] for i in data['platform_number']])
    if data['announcement_type'] == "Arrival":
        lst.append(guj_out_arv)
    else:
        lst.append(guj_out_dep)
    lst.append(bell_end)
    list_play(lst)


def list_play(lst):
    for rec in lst:
        playsound(rec)


def authenticate(username, password):
    user_data = get_user_data(username)
    if user_data and bcrypt.checkpw(password.encode('utf-8'), user_data[2]):
        return True
    else:
        return False

def on_enter(event):
    login()

def on_enter_reg(event):
    submit_registration()

def show_error_popup(message, error_type='Error'):
    messagebox.showerror(error_type, message)


def logout():
    form_frame.grid_forget()  # Hide the main form frame
    label_0.config(text='-: Login  SYSTEM :-')
    root.geometry("525x450")
    login_frame.grid(column=0, row=2)  # Show the login frame


def login_open():
    home_frame.grid_forget()  # Hide the main form frame
    label_0.config(text='-: Login  SYSTEM :-')
    root.geometry("525x450")
    login_frame.grid(column=0, row=2)  # Show the login frame


def login():
    username = username_entry.get()
    password = password_entry.get()
    if authenticate(username, password):
        login_frame.grid_forget()  # Hide the login frame
        root.geometry("920x600")
        label_0.config(text='-: INDIAN  RAILWAYS  ANNOUNCEMENT  SOFTWARE  SYSTEM :-')
        form_frame.grid(column=0, row=2)  # Show the main form frame
        show_error_popup(f"Welcome {username}!", 'Login Successful!')
    else:
        show_error_popup("Invalid username or password")


def register():
    login_frame.grid_forget()  # Hide the login frame
    label_0.config(text="-: Registration System :-")
    root.geometry("450x450")
    registration_frame.grid(column=0, row=2)


def submit_registration():
    global data_db
    connection = sqlite3.connect(data_db)
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT
        )
    ''')
    username = username_entry_reg.get()
    password = password_entry_reg.get()
    if not username or not password:
        show_error_popup("Username and password are required for registration.")
        return
    if get_user_data(username):
        show_error_popup("User with this username already exists.")
        return
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    store_user_data(username, hashed_password)
    registration_frame.grid_forget()  # Hide the main form frame
    label_0.config(text='-: Login  SYSTEM :-')
    root.geometry("525x450")
    login_frame.grid(column=0, row=2)  # Show the login frame
    show_error_popup(f"User registered: {username}", 'registration')


def add_announcement():
    # prepare data from gui
    data = {
        'train_number': train_number_entry.get(),
        'source_station': source_station_combobox.get(),
        'destination_station': destination_station_combobox.get(),
        'train_type': train_type_combobox.get(),
        'platform_number': platform_number_entry.get(),
        'announcement_type': announcement_var.get(),
        'repeat_number': repeat_entry.get()
    }

    # add validation for null values
    errors = ''
    for rec in data:
        if not data[rec]:
            errors += f"Enter Valid Value For {rec}." + '\n'
        if rec in ['train_number', 'platform_number', 'repeat_number']:
            try:
                int(data[rec])
            except ValueError:
                errors += f"Enter valid Integer For {rec}." + '\n'
    if errors:
        print('\n', errors, '\n')
        show_error_popup(errors, "ValueError")
        return

    # button disabled while playing announcement
    announcement_button.configure(state="disabled")

    # print Data received from Gui
    print("Train Number:", data['train_number'])
    print("Source Station:", data['source_station'])
    print("Destination Station:", data['destination_station'])
    print("Train type :", data['train_type'])
    print("Platform Number:", data['platform_number'])
    print("Announcement Type:", data['announcement_type'])
    print("repeat for :", data['repeat_number'])

    print("------------------------------------------------")

    # play announcement from received data from Gui
    for i in range(int(data['repeat_number'])):
        guj_announce(data)
        mar_announce(data)
        hindi_announce(data)
        eng_announce(data)

    # button enabled back after playing announcement
    announcement_button.configure(state="normal")


# main Gui
root = tk.Tk()

root.geometry("425x480")
root.title("Train Announcement System")
label_0 = tk.Label(text="-: HOME :-", borderwidth=3, relief="solid",
                   font=("Italic", 20))
label_0.grid(column=0, row=0, sticky=(tk.W, tk.E))

# Train Photo
train_photo_path = image_path
train_photo = tk.PhotoImage(file=train_photo_path)
train_photo_label = tk.Label(root, image=train_photo)
train_photo_label.grid(column=0, row=1, padx=20, pady=20, sticky=(tk.W, tk.E, tk.N, tk.S))

# home frame
home_frame = ttk.Frame(root, padding="20")
home_frame.grid(row=2, column=0)

login_button = ttk.Button(home_frame, text="Login", command=login_open)
login_button.grid(row=2, pady=10)
register_button = ttk.Button(home_frame, text="Register", command=register)
register_button.grid(row=3, pady=10)
exit_button = ttk.Button(home_frame, text="Exit", command=root.destroy)
exit_button.grid(row=4, pady=10)

# Create a frame for the login page
login_frame = ttk.Frame(root, padding="20")
login_frame.columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight=1)

# Username Label and Entry
username_label = ttk.Label(login_frame, text="Username:")
username_label.grid(row=0, column=5, sticky=tk.E, pady=10)
username_entry = ttk.Entry(login_frame, width=30)
username_entry.grid(row=0, column=6, sticky=(tk.W, tk.E), pady=10)

# Password Label and Entry
password_label = ttk.Label(login_frame, text="Password:")
password_label.grid(row=1, column=5, sticky=tk.E, pady=10)
password_entry = ttk.Entry(login_frame, show="*", width=30)
password_entry.grid(row=1, column=6, sticky=(tk.W, tk.E), pady=10)
password_entry.bind("<Return>", on_enter)

# Login Button
login_button = ttk.Button(login_frame, text="Login", command=login)
login_button.grid(row=2, column=4, pady=10)
register_button = ttk.Button(login_frame, text="Register", command=register)
register_button.grid(row=2, column=6, pady=10)
exit_button = ttk.Button(login_frame, text="Exit", command=root.destroy)
exit_button.grid(row=2, column=9, pady=10)

registration_frame = ttk.Frame(root, padding="20")

# Username Label and Entry
username_label_reg = ttk.Label(registration_frame, text="Username:")
username_label_reg.grid(row=0, column=5, sticky=tk.E, pady=10)
username_entry_reg = ttk.Entry(registration_frame, width=30)
username_entry_reg.grid(row=0, column=6, sticky=(tk.W, tk.E), pady=10)

# Password Label and Entry
password_label_reg = ttk.Label(registration_frame, text="Password:")
password_label_reg.grid(row=1, column=5, sticky=tk.E, pady=10)
password_entry_reg = ttk.Entry(registration_frame, show="*", width=30)
password_entry_reg.grid(row=1, column=6, sticky=(tk.W, tk.E), pady=10)
password_entry_reg.bind("<Return>", on_enter_reg)

# Login Button
submit_button_reg = ttk.Button(registration_frame, text="Submit", command=submit_registration)
submit_button_reg.grid(row=2, column=5, sticky=tk.W, pady=10)
exit_button_reg = ttk.Button(registration_frame, text="Exit", command=root.destroy)
exit_button_reg.grid(row=2, column=8, sticky=tk.W, pady=10)

# Create a frame for the form
form_frame = ttk.Frame(root, padding="20")

# Train Type Combobox
train_type_label = ttk.Label(form_frame, text="(2) Train Type:")
train_type_combobox = ttk.Combobox(form_frame, values=lst_train_type, width=27)

# Source Station Combobox
source_station_label = ttk.Label(form_frame, text="(3) Source Station:")
source_station_combobox = tkentrycomplete.AutocompleteCombobox(form_frame, values=city_names, width=27)
source_station_combobox.set_completion_list(city_names)

# Destination Station Combobox
destination_station_label = ttk.Label(form_frame, text="(4) Destination Station:")
destination_station_combobox = tkentrycomplete.AutocompleteCombobox(form_frame, values=city_names, width=27)
destination_station_combobox.set_completion_list(city_names)

# Announcement Type Radiobuttons
announcement_type_label = ttk.Label(form_frame, text="(6) Announcement Type:")
announcement_var = tk.StringVar()
arrival_radio = ttk.Radiobutton(form_frame, text="Arrival", variable=announcement_var, value="Arrival")
departure_radio = ttk.Radiobutton(form_frame, text="Departure", variable=announcement_var, value="Departure")

# Entry widgets and labels
train_number_label = ttk.Label(form_frame, text="(1) Train Number:")
train_number_entry = ttk.Entry(form_frame, width=30)

platform_number_label = ttk.Label(form_frame, text="(5) Platform Number:")
platform_number_entry = ttk.Entry(form_frame, width=30)

repeat_label = ttk.Label(form_frame, text="(7) Repeat For:")
repeat_entry = ttk.Entry(form_frame, width=30)

# Create buttons
announcement_button = ttk.Button(form_frame, text="Announcement", command=add_announcement)
logout_button = ttk.Button(form_frame, text="Logout", command=logout)
exit_button = ttk.Button(form_frame, text="Exit", command=root.destroy)

# Arrange widgets in the form
train_number_label.grid(column=0, row=0, sticky=tk.W, pady=10)
train_number_entry.grid(column=1, row=0, sticky=(tk.W, tk.E), pady=10)

source_station_label.grid(column=0, row=1, sticky=tk.W, pady=10)
source_station_combobox.grid(column=1, row=1, sticky=(tk.W, tk.E), pady=10)

platform_number_label.grid(column=0, row=2, sticky=tk.W, pady=10)
platform_number_entry.grid(column=1, row=2, sticky=(tk.W, tk.E), pady=10)

train_type_label.grid(column=2, row=0, sticky=tk.W, padx=50, pady=10)
train_type_combobox.grid(column=3, row=0, sticky=(tk.W, tk.E), pady=10)

destination_station_label.grid(column=2, row=1, sticky=tk.W, padx=50, pady=10)
destination_station_combobox.grid(column=3, row=1, sticky=(tk.W, tk.E), pady=10)

announcement_type_label.grid(column=2, row=2, sticky=tk.W, padx=50, pady=10)
arrival_radio.grid(column=3, row=2, sticky=tk.W, pady=10)
departure_radio.grid(column=3, row=2, sticky=tk.E, pady=10)

repeat_label.grid(column=1, row=3, padx=20, pady=15)
repeat_entry.grid(column=2, row=3, pady=15)

announcement_button.grid(column=0, row=4, columnspan=2, pady=40, sticky=tk.W)
logout_button.grid(column=2, row=4, columnspan=2, pady=40, sticky=tk.W)
exit_button.grid(column=3, row=4, columnspan=2, pady=40, sticky=tk.E)

# Start the main loop
root.mainloop()
