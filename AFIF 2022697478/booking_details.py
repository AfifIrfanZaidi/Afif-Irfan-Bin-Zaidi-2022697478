import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector  

mydb = mysql.connector.connect(
    host ="localhost",
    user ="root",
    password = "", 
    database="futsal_booking")

mycursor=mydb.cursor()

def insert_data():
    #try:
        label_name = name_entry.get()
        label_time_starting = time_starting_entry.get()
        label_time_ending = time_ending_entry.get()
        booking_date= booking_date_combobox.get()
        label_duration = duration_entry.get()
        #label_hours = hours_combobox.get()
        label_place = place_entry.get()
        
        # Perform any calculations or data processing here

        print("Name:", label_name)
        print("Time Starting:", label_time_starting)
        print("Time Ending:", label_time_ending)
        print(" booking date:", booking_date)
        print("Duration:", label_duration) 
        print("Place:", label_place)
        
        # calculation
        playing_time_value = int(playing_time.get())
        price_value = int(price.get())
        total_price_button = playing_time_value * price_value

        tk.messagebox.showinfo("total", f"total(RM): {total_price_button}")
        print("Revenue data inserted into the 'price' table.")
        print("------------------------------------------")
        print("Playing Time:", playing_time_value, "Price:", price_value)
        print("Total Revenue (RM):", total_price_button)
        print("------------------------------------------")
        
        sql=("INSERT INTO booking_details (NAME,START,END,DATE,DURATION_PRICE,PLACE,PLAYING_TIME,PRICE, TOTAL_PRICE ) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        val=(label_name, label_time_starting, label_time_ending, booking_date, label_duration, label_place, playing_time_value, price_value, total_price_button)
    
        mycursor.execute(sql,val)
        mydb.commit()


# Tkinter GUI
root = tk.Tk()
root.title("FUTSAL BOOKING")
root.geometry("750x750")
root.configure(bg="#030303")

label_name = tk.Label(root, text="FUTSAL BOOKING", font=("Imprint MT Shadow", 18))
label_name.grid(row=0, column=2, padx=5, pady=5)

label_name = tk.Label(root, text="Name booking",bg="#030303", fg="#ECF0F1", font=("Imprint MT Shadow", 18))
label_name.grid(row=1, column=2, padx=5, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=2, column=2, padx=5, pady=5)

label_time_starting = tk.Label(root, text="Time Starting",bg="#030303", fg="#ECF0F1", font=("Imprint MT Shadow", 18))
label_time_starting.grid(row=3, column=1, padx=5, pady=5)
time_starting_entry = ttk.Combobox(root, values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"])
time_starting_entry.grid(row=4, column=1, padx=5, pady=5)

label_time_ending = tk.Label(root, text="Time Ending", bg="#030303", fg="#ECF0F1", font=("Imprint MT Shadow", 18))
label_time_ending.grid(row=3, column=3, padx=10, pady=10)
time_ending_entry = ttk.Combobox(root, values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"])
time_ending_entry.grid(row=4, column=3, padx=5, pady=5)


label_duration = tk.Label(root, text="Duration", bg="#030303", fg="#ECF0F1", font=("Imprint MT Shadow", 18))
label_duration.grid(row=8, column=1, padx=10, pady=10)
duration_entry = ttk.Combobox(root, values=["AM RM50 per hour", "PM RM70 per hour"])
duration_entry.grid(row=9, column=1, padx=5, pady=5)

#label_hours = tk.Label(root, text="Hours", bg="#030303", fg="#ECF0F1", font=("Imprint MT Shadow", 18))
#label_hours.grid(row=8, column=3, padx=5, pady=5)
#hours_combobox = ttk.Combobox(root, values=["1", "2", "3","4","5","6", "7","8","9","10"])
#hours_combobox.grid(row=9, column=3, padx=5, pady=5)

booking_date = tk.Label(root, text="    Booking date    :",font =("Imprint MT Shadow", 18), bg="#030303", fg="#ECF0F1")
booking_date.grid(row=6, column=2, padx=5, pady=5)
booking_date_combobox = tk.Entry(root) 
booking_date_combobox.grid(row=7, column=2, padx=5, pady=5)

label_place = tk.Label(root, text="Place", bg="#030303", fg="#ECF0F1", font=("Imprint MT Shadow", 18))
label_place.grid(row=8, column=3, padx=5, pady=5)
place_entry = ttk.Combobox(root, values=["", "D Futsal", "Derga Futsal", "WNS Futsal"])
place_entry.grid(row=9, column=3, padx=5, pady=5)

price_for_booking = tk.LabelFrame(root, text="Price for Booking", bg="#030303", fg="#ECF0F1", font=('Imprint MT Shadow', 18,))
price_for_booking.grid(row=13, column=2, sticky="news", padx=30, pady=30)

playing_time_label = tk.Label(price_for_booking, text="Playing Time",bg="#030303", fg="#ECF0F1", font=('Imprint MT Shadow', 18,))
playing_time_label.grid(row=0, column=0, padx=10, pady=10)
playing_time = tk.Entry(price_for_booking)
playing_time.grid(row=0, column=1, padx=10, pady=10)

price_label = tk.Label(price_for_booking, text="Price:", bg="#030303", fg="#ECF0F1", font=('Imprint MT Shadow', 18,))
price_label.grid(row=2, column=0, padx=10, pady=10)
price = tk.Entry(price_for_booking)
price.grid(row=2, column=1, padx=10, pady=10)

# Buttons to perform operations
total_price_button = tk.Button(price_for_booking, text="Total price", command=insert_data, bg="#030303", fg="#ECF0F1", font=('Imprint MT Shadow', 18,))
total_price_button .grid(row=4, column=0, columnspan=2, pady=5)
result_label = tk.Label(price_for_booking, text='')

root.mainloop()