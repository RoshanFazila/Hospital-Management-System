import tkinter as tk
from tkinter import PhotoImage
from tkinter import simpledialog
from ADMIN import AdminLoginApp
from patient_login import PatientLoginApp
import webbrowser
from appointment import AppointmentApp

class MyApp:
    def __init__(self, root):
        self.root = root
        self.Detailsframe = None 
        self.root.title("Premium Healthcare")
        self.root.configure(bg="black")

        # Load the background image
        self.bg_image = PhotoImage(file="image.png") 
        bg_label = tk.Label(root, image=self.bg_image)
        bg_label.place(relwidth=1, relheight=1)

        # Heading label
        heading_label = tk.Label(root,bd=20,relief=tk.RIDGE,  text="Welcome to Premium Healthcare", font=("lucida calligraphy", 40), bg="white", fg="black")
        heading_label.place(relx=0.5, rely=0.1, anchor="center")

        # Address label
        address_label = tk.Label(root, text="Sathy Road, Kurumbapalayam, Coimbatore - 641107",
                                 font=("lucida calligraphy", 18), bg="white", fg="black")
        address_label.place(relx=0.5, rely=0.2, anchor="center")

        # Admin Login button
        btn_admin = tk.Button(root, text="Admin Login", bg="#2a575d", fg="white", font=("arial", 16, "bold"),
                              width=22, command=self.admin_login)
        btn_admin.place(relx=0.3, rely=0.3, anchor="center")

        # Patient Login button
        btn_patient = tk.Button(root, text="Patient Login", bg="#2a575d", fg="white", font=("arial", 16, "bold"),
                                width=22, command=self.patient_login)
        btn_patient.place(relx=0.7, rely=0.3, anchor="center")

        btn_location = tk.Button(root, text="Location", bg="#2a575d", fg="white", font=("arial", 16, "bold"),
                                 width=22, command=self.show_location)
        btn_location.place(relx=0.5, rely=0.4, anchor="center")

        btn_app = tk.Button(root, text=" Book an Appointment", bg="#2a575d", fg="white", font=("arial", 16, "bold"),
                                 width=22, command=self.appointment)
        btn_app.place(relx=0.5, rely=0.5, anchor="center")

    def admin_login(self):
        # Ask for administrator's password
        password = simpledialog.askstring("Admin Login", "Enter Administrator Password:", show='*')

        # Check if the password is correct
        if password == "ADMIN@123":  # Replace "your_admin_password_here" with the actual password
            # Create an instance of AdminLoginApp and show it
            ADMIN_window = tk.Toplevel(self.root)
            AdminLoginApp(ADMIN_window)

            screen_width = ADMIN_window.winfo_screenwidth()
            screen_height = ADMIN_window.winfo_screenheight()
            ADMIN_window.geometry(f"{screen_width}x{screen_height}")
        else:
            # Password incorrect, notify the user
            tk.messagebox.showerror("Error", "Incorrect password. Access denied.")

    def patient_login(self):
        # Create an instance of PatientLoginApp and show it
        patient_login_window = tk.Toplevel(self.root)
        PatientLoginApp(patient_login_window)

        screen_width = patient_login_window.winfo_screenwidth()
        screen_height = patient_login_window.winfo_screenheight()
        patient_login_window.geometry(f"{screen_width}x{screen_height}")

    def appointment(self):
        # Create an instance of PatientLoginApp and show it
        appointment_window = tk.Toplevel(self.root)
        AppointmentApp(appointment_window)   

        screen_width = appointment_window.winfo_screenwidth()
        screen_height = appointment_window.winfo_screenheight()
        appointment_window.geometry(f"{screen_width}x{screen_height}")
 

    def show_location(self):
        latitude = "11.114109300119873"
        longitude = "77.02817577784423"
        google_maps_url = f"https://www.google.com/maps/place/{latitude},{longitude}"

        webbrowser.open(google_maps_url)

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
