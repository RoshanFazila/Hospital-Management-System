import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter import ttk
import mysql.connector

class PatientLoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Patient Login")

        # Load the background image
        self.bg_image = PhotoImage(file="image.png")  
        bg_label = tk.Label(root, image=self.bg_image)
        bg_label.place(relwidth=1, relheight=1)

        # Create the heading label
        self.heading_label = tk.Label(root, bd=25, relief=tk.RIDGE, text="Patient Login", font=("lucida calligraphy", 30), bg="white")
        self.heading_label.pack(pady=(50, 30))

        # Create labels, entries, and submit button for patient name and ID
        self.name_label = tk.Label(root, text="Enter Patient Name:", font=("lucida calligraphy", 18), bg="white")
        self.name_label.pack(pady=10)

        self.name_entry = tk.Entry(root, font=("lucida calligraphy", 12))
        self.name_entry.pack(pady=10)

        self.id_label = tk.Label(root, text="Enter Patient ID:", font=("lucida calligraphy", 18), bg="white")
        self.id_label.pack(pady=10)

        self.id_entry = tk.Entry(root, font=("Helvetica", 18))
        self.id_entry.pack(pady=10)

        self.submit_button = tk.Button(root, text="Submit", fg="white", command=self.submit, font=("lucida calligraphy", 18), bg="#646F7B")
        self.submit_button.pack(pady=10)

       

    def submit(self):
        try:
            # Get the entered patient name and ID
            patient_name = self.name_entry.get()
            patient_id = self.id_entry.get()

            # Connect to MySQL database (replace with your database credentials)
            conn = mysql.connector.connect(host="localhost", user="root", password="212Ac0619@003", database="program")
            my_cursor = conn.cursor()

            # Query to fetch patient details based on name and ID
            query = "SELECT * FROM sample6 WHERE Patient_name = %s AND Patient_id = %s"
            values = (patient_name, patient_id)

            my_cursor.execute(query, values)
            patient_details = my_cursor.fetchone()  # Fetch the first matching record

            conn.close()

            if patient_details:
                # Display the details in a messagebox
                details_str = f"Patient Name: {patient_details[0]}\nPatient ID: {patient_details[1]}\nMedical Fees: {patient_details[2]}\nConsultation Fees: {patient_details[3]}\nOther Charges: {patient_details[4]}\nAmount: {patient_details[5]}\nTotal: {patient_details[6]}"
                messagebox.showinfo("Patient Details", details_str)
            else:
                messagebox.showinfo("Patient Details", "No matching patient found.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
if __name__ == "__main__":
    root = tk.Tk()
    app = PatientLoginApp(root)
    root.mainloop()
