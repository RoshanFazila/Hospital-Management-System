import tkinter as tk
from tkinter import ttk, messagebox, PhotoImage
import mysql.connector

class PatientHistoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Patient History")

        # Load the background image
        self.bg_image = PhotoImage(file="image.png")  # Replace with your image file
        bg_label = tk.Label(root, image=self.bg_image)
        bg_label.place(relwidth=1, relheight=1)

        # Create the heading label
        self.heading_label = tk.Label(root, bd=25, relief=tk.RIDGE, text="Patient History", font=("lucida calligraphy", 30), bg="white")
        self.heading_label.pack(pady=10)

        # Create label, entry, and submit button for patient ID
        self.patient_id_label = tk.Label(root, text="Enter your Patient ID:", font=("lucida calligraphy", 18), bg="white")
        self.patient_id_label.pack(pady=10)

        self.patient_id_entry = tk.Entry(root, font=("Helvetica", 18))
        self.patient_id_entry.pack(pady=10)

        self.submit_button = tk.Button(root, text="Submit", fg="white", command=self.submit, font=("lucida calligraphy", 18), bg="#646F7B")
        self.submit_button.pack(pady=10)

        # Create Treeview to display patient data
        self.columns = ('Name', 'Patient Id', 'Age', 'Medical condition', 'Phone', 'Address', 'Admission date', 'Discharge date', 'Pulse rate', 'Blood pressure')
        self.tree = ttk.Treeview(root, columns=self.columns, show='headings')
        self.column_widths = [100, 100, 50, 150, 100, 150, 120, 120, 80, 120]  # Adjust these values as needed

        for col, width in zip(self.columns, self.column_widths):
            self.tree.column(col, width=width)
            self.tree.heading(col, text=col)

        self.tree.pack(pady=10)

    def submit(self):
        # Get the patient ID from the entry
        patient_id = self.patient_id_entry.get()

        # Clear the Treeview
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Connect to MySQL database (replace with your database credentials)
        conn = mysql.connector.connect(host="localhost", user="root", password="212Ac0619@003", database="program")
        my_cursor = conn.cursor()

        # Fetch specific columns from MySQL based on patient ID
        query = "SELECT Name, Patient_Id, Age, Medical_condition, Phone, Address, Admission_date, Discharge_date, Pulse_rate, Blood_Pressure FROM sample5 WHERE Patient_Id = %s"
        values = (patient_id,)
        my_cursor.execute(query, values)
        patient_data = my_cursor.fetchone()

        conn.close()

        # Display data in the Treeview
        if patient_data:
            self.tree.insert('', 'end', values=patient_data)
        else:
            messagebox.showinfo("Patient History", f"No data found for Patient ID {patient_id}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PatientHistoryApp(root)
    root.mainloop()
