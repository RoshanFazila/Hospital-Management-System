import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import mysql.connector

class AppointmentApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Book Your Appointment")

        # Set background color for the root window
        self.master.configure(background="#6fdcdc")

    # Create a frame with a ridge border
        self.frame = ttk.Frame(self.master, relief="ridge", borderwidth=25)
        self.frame.grid(row=0, column=0, padx=20, pady=20, sticky="n")  

    # Define font style
        self.heading_font_style = ("Lucida Calligraphy", 24, "bold")
        self.info_font_style = ("Arial", 12)

    # Create a label for the heading
        self.heading_label = tk.Label(self.frame, text="BOOK YOUR APPOINTMENT", font=self.heading_font_style, fg="blue")
        self.heading_label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

    # Create labels and entry widgets for patient information
        self.name_label = tk.Label(self.frame, text="Name:", font=self.info_font_style)
        self.name_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.name_entry = tk.Entry(self.frame, font=self.info_font_style)
        self.name_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        self.age_label = tk.Label(self.frame, text="Age:", font=self.info_font_style)
        self.age_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.age_entry = tk.Entry(self.frame, font=self.info_font_style, width=5)
        self.age_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        self.gender_label = tk.Label(self.frame, text="Gender:", font=self.info_font_style)
        self.gender_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.gender_entry = tk.Entry(self.frame, font=self.info_font_style, width=5)
        self.gender_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        self.medical_condition_label = tk.Label(self.frame, text="Medical condition:", font=self.info_font_style)
        self.medical_condition_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.medical_condition_entry = tk.Entry(self.frame, font=self.info_font_style, width=5)
        self.medical_condition_entry.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        self.address_label = tk.Label(self.frame, text="Address:", font=self.info_font_style)
        self.address_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.address_entry = tk.Entry(self.frame, font=self.info_font_style, width=5)
        self.address_entry.grid(row=5, column=1, padx=10, pady=5, sticky="w")

        self.phone_label = tk.Label(self.frame, text="Phone no:", font=self.info_font_style)
        self.phone_label.grid(row=6, column=0, padx=10, pady=5, sticky="w")
        self.phone_entry = tk.Entry(self.frame, font=self.info_font_style, width=5)
        self.phone_entry.grid(row=6, column=1, padx=10, pady=5, sticky="w")

        self.email_label = tk.Label(self.frame, text="Email:", font=self.info_font_style)
        self.email_label.grid(row=7, column=0, padx=10, pady=5, sticky="w")
        self.email_entry = tk.Entry(self.frame, font=self.info_font_style)
        self.email_entry.grid(row=7, column=1, padx=10, pady=5, sticky="w")

    # Add a preferred timing drop-down menu
        self.timing_label = tk.Label(self.frame, text="Preferred Timing:", font=self.info_font_style)
        self.timing_label.grid(row=8, column=0, padx=10, pady=5, sticky="w")
        self.timing_var = tk.StringVar()
        self.timing_combobox = ttk.Combobox(self.frame, font=self.info_font_style, textvariable=self.timing_var, state="readonly")
        self.timing_combobox["values"] = ("Morning", "Afternoon", "Evening")
        self.timing_combobox.grid(row=8, column=1, padx=10, pady=5, sticky="w")

        self.date_label = tk.Label(self.frame, text="Date:", font=self.info_font_style)
        self.date_label.grid(row=9, column=0, padx=10, pady=5, sticky="w")
        self.date_entry = tk.Entry(self.frame, font=self.info_font_style)
        self.date_entry.grid(row=9, column=1, padx=10, pady=5, sticky="w")

   
    # Create a button to submit the appointment
        self.submit_button = ttk.Button(self.frame, text="Submit Appointment", command=self.submit_appointment)
        self.submit_button.grid(row=10, column=0, columnspan=2, pady=10)

    # Configure row and column weights to make the frame expandable
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)


    def submit_appointment(self):
        # Fetch patient information
        name = self.name_entry.get()
        age = self.age_entry.get()
        gender = self.gender_entry.get()  
        medical_condition = self.medical_condition_entry.get()  
        address = self.address_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        preferred_timing = self.timing_var.get()
        selected_date = self.date_entry.get()

        try:
            # Connect to MySQL database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="212Ac0619@003",
                database="program"
            )
            
            # Create cursor object
            mycursor = mydb.cursor()

            # SQL query to insert patient details into appointments table
            sql = "INSERT INTO appointments (name, age, gender, medical_condition, address, phone, email, preferred_timing, selected_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (name, age, gender, medical_condition, address, phone, email, preferred_timing, selected_date)
            
            # Execute SQL query
            mycursor.execute(sql, values)

            # Commit changes
            mydb.commit()

            # Close connection
            mydb.close()

            # Send email notification to the patient
            self.send_email_notification(name, email, "Appointment Confirmation", f"Dear {name},\n\nYour appointment has been confirmed.\n\nDate: {selected_date}\nTime: {preferred_timing}\n\nThank you.")
        
        except mysql.connector.Error as error:
            print("Failed to insert record into MySQL table:", error)

    def send_email_notification(self, recipient_name, recipient_email, subject, message):
        try:
        # Setup the MIME
            email_message = MIMEMultipart()
            email_message['From'] = "roshanfazila.mi@gmail.com"  # Replace with your email address
            email_message['To'] = recipient_email
            email_message['Subject'] = subject

        # Add body to email
            email_message.attach(MIMEText(message, 'plain'))

        # Create SMTP session for sending the mail
            session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
            session.starttls()  # enable security
            session.login("roshanfazila.mi@gmail.com", "hkin gelk stjm witn")  # login with mail_id and password
            text = email_message.as_string()
            session.sendmail("miruthula249@gmail.com", recipient_email, text)
            session.quit()
            print('Mail Sent')
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AppointmentApp(root)
    root.mainloop()
