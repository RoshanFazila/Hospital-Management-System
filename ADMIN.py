import tkinter as tk
from tkinter import PhotoImage
from new_registration import HospitalManagementSystem
from patient_history import PatientHistoryApp


class AdminLoginApp:
    def __init__(self, master):
        self.master = master
        master.title("Admin's Login")

        # Load the background image
        self.bg_image = PhotoImage(file="image.png")
        bg_label = tk.Label(master, image=self.bg_image)
        bg_label.place(relwidth=1, relheight=1)

        # Create the heading label
        heading_label = tk.Label(master, bd=25, relief=tk.RIDGE, text="Admin's Login", font=("lucida calligraphy", 45), bg="white")
        heading_label.pack(pady=(50, 30))

        # Create the buttons
        new_registration_button = tk.Button(master, text="New Registration", command=self.new_registration, font=("lucida calligraphy", 25), bg="#646F7B")
        new_registration_button.pack(pady=10)

        patient_history_button = tk.Button(master, text="Patient History", command=self.patient_history, font=("lucida calligraphy", 25), bg="#646F7B")
        patient_history_button.pack(pady=10)

    def new_registration(self):
        # Create an instance of HospitalManagementSystem and show it
        new_registration_window = tk.Toplevel(self.master)
        HospitalManagementSystem(new_registration_window)

    def patient_history(self):
        patient_history_window = tk.Toplevel(self.master)
        PatientHistoryApp(patient_history_window)

if __name__ == "__main__":
    root = tk.Tk()
    app = AdminLoginApp(root)
    root.mainloop()
