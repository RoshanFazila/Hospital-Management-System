from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from datetime import datetime

class HospitalManagementSystem:
   def __init__(self, root):
        self.root = root
        self.Detailsframe = None 
        self.root.title("Hospital Management System")
        self.root.geometry("1520x810+0+0")

        # Heading Frame
        self.heading_frame = Frame(root, bd=20, relief=RIDGE, bg="white")
        self.heading_frame.grid(row=0, column=0, columnspan=5, sticky="nsew")  

        self.heading_label = Label(self.heading_frame, text=" Premium Healthcare Registration", font=("lucida calligraphy", 58, "bold"), bg="white", fg="red")
        self.heading_label.grid(row=0, column=0, columnspan=5)

        # Data Frame
        self.data_frame = Frame(root, bd=10, relief=RIDGE, bg="white")
        self.data_frame.grid(row=1, column=0, sticky="nsew")

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)

        # Initialize Dataframe and DataframeLeft and dataframeright as class attributes
        self.Dataframe = Frame(self.root, bd=15, relief=RIDGE)
        self.Dataframe.place(x=0, y=130, width=1520, height=400)

        self.DataframeLeft = LabelFrame(self.Dataframe, bd=10, relief=RIDGE, padx=10,
                                        font=("times new roman", 12, "bold"), text="  Patient Information  ")
        self.DataframeLeft.place(x=0, y=5, width=970, height=350)

        self.Dataframeright= LabelFrame(self.Dataframe, bd=10, relief=RIDGE, padx=10,
                                        font=("times new roman", 12, "bold"), text="  Bill Details  ")
        self.Dataframeright.place(x=980, y=0, width=500, height=360)

        self.label_patient_name = Label(self.Dataframeright, text="Patient Name:", font=("arial", 12, "bold"))
        self.entry_patient_name = Entry(self.Dataframeright, font=("arial", 12, "bold"), width=20)
        self.label_patientid = Label(self.Dataframeright, text="Patient Id:", font=("arial", 12, "bold"))
        self.entry_patientid = Entry(self.Dataframeright, font=("arial", 12, "bold"), width=20)
        self.label_medical_fees = Label(self.Dataframeright, text="Medical Fees:", font=("arial", 12, "bold"))
        self.entry_medical_fees = Entry(self.Dataframeright, font=("arial", 12, "bold"), width=20)
        self.label_consultation_fees = Label(self.Dataframeright, text="Consultation Fees:", font=("arial", 12, "bold"))
        self.entry_consultation_fees = Entry(self.Dataframeright, font=("arial", 12, "bold"), width=20)
        self.label_other_charges = Label(self.Dataframeright, text="Other Charges Type:", font=("arial", 12, "bold"))
        self.other_charges = ttk.Combobox(self.Dataframeright, font=("arial", 12, "bold"), state="readonly")
        self.other_charges['values'] = ['X-ray', 'Blood Test', 'Scan','None','ECG','MRI','CT']


        self.label_other_charges.grid(row=4, column=2, pady=5, sticky=W)
        self.other_charges.grid(row=4, column=3, pady=5)
        self.label_amt = Label(self.Dataframeright, text="Amount:", font=("arial", 12, "bold"))
        self.amt = Entry(self.Dataframeright, font=("arial", 12, "bold"), width=20)


        self.label_total = Label(self.Dataframeright, text="Total:", font=("arial", 12, "bold"))
        self.entry_total = Entry(self.Dataframeright, font=("arial", 12, "bold"), width=20)

        self.label_patient_name.grid(row=0, column=0, pady=5, sticky=W)
        self.entry_patient_name.grid(row=0, column=1, pady=5)
        self.label_patientid.grid(row=1, column=0, pady=5, sticky=W)
        self.entry_patientid.grid(row=1, column=1, pady=5)
        self.label_medical_fees.grid(row=2, column=0, pady=5, sticky=W)
        self.entry_medical_fees.grid(row=2, column=1, pady=5)
        self.label_consultation_fees.grid(row=3, column=0, pady=5, sticky=W)
        self.entry_consultation_fees.grid(row=3, column=1, pady=5)
        self.label_other_charges.grid(row=4, column=0, pady=5, sticky=W)
        self.other_charges.grid(row=4, column=1, pady=5)
        self.label_amt.grid(row=5, column=0, pady=5, sticky=W)
        self.amt.grid(row=5, column=1, pady=5)
        self.label_total.grid(row=7, column=0, pady=5, sticky=W)
        self.entry_total.grid(row=7, column=1, pady=5)

    

        ########################################################### buttons frame ###################################################################

        self.Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        self.Buttonframe.place(x=0,y=530,width=1530,height=80)

        ######################################################## details frame ###########################################################################

        self.Detailsframe = Frame(self.root,bd=20,relief=RIDGE)
        self.Detailsframe.place(x=0, y=600, width=1520, height=190)

        ######################################################## details frame values ###########################################################################
        self.details_treeview = ttk.Treeview(self.Detailsframe, columns=('Name','Patient Id', 'Age', 'Occupation', 'Medical condition','Gender','Phone','Address',
                                                                         'Admission date','Discharge date','Pulse rate','Blood pressure'))
        self.details_treeview.heading('#0', text='Name')
        self.details_treeview.heading('#1', text='Patient Id')
        self.details_treeview.heading('#2', text='Age')
        self.details_treeview.heading('#3', text='Occupation')
        self.details_treeview.heading('#4', text='Medical condition')
        self.details_treeview.heading('#5', text='Phone')
        self.details_treeview.heading('#6', text='Address')
        self.details_treeview.heading('#7', text='Admission date')
        self.details_treeview.heading('#8', text='Discharge date')
        self.details_treeview.heading('#9', text='Pulse rate')
        self.details_treeview.heading('#10', text='Blood pressure')

        self.details_treeview.column('#0', width=125)
        self.details_treeview.column('#1', width=125)
        self.details_treeview.column('#2', width=125)
        self.details_treeview.column('#3', width=125)
        self.details_treeview.column('#4', width=125)
        self.details_treeview.column('#5', width=125)
        self.details_treeview.column('#6', width=125)
        self.details_treeview.column('#7', width=125)
        self.details_treeview.column('#8', width=125)
        self.details_treeview.column('#9', width=125)
        self.details_treeview.column('#10', width=125)

        self.details_treeview.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
        self.Detailsframe.columnconfigure(0, weight=1)
        self.Detailsframe.rowconfigure(0, weight=1)

        self.setup_ui()
    
   def setup_ui(self):
       
       self.label_name = Label(self.DataframeLeft, text="Name:",font=("arial",12,"bold"))
       self.label_id = Label(self.DataframeLeft, text="Patient id:",font=("arial",12,"bold"))
       self.label_age = Label(self.DataframeLeft, text="Age:",font=("arial",12,"bold"))
       self.label_dob = Label(self.DataframeLeft, text="Date of Birth:",font=("arial",12,"bold"))
       self.label_occ = Label(self.DataframeLeft, text="Occupation:",font=("arial",12,"bold"))
       self.label_medicalcondition = Label(self.DataframeLeft, text="Medical Condition:",font=("arial",12,"bold"))
       self.label_aadhar = Label(self.DataframeLeft, text="Aadhar Number:",font=("arial",12,"bold"))
       self.label_gender = Label(self.DataframeLeft, text="Gender:",font=("arial",12,"bold"))
       self.label_email = Label(self.DataframeLeft, text="Email:",font=("arial",12,"bold"))
       self.label_phone = Label(self.DataframeLeft, text=" Phone:",font=("arial",12,"bold"))
       self.label_maritalstatus = Label(self.DataframeLeft, text=" Marital status:",font=("arial",12,"bold"))
       self.label_address = Label(self.DataframeLeft, text=" Address:",font=("arial",12,"bold"))
       self.label_admidate= Label(self.DataframeLeft, text=" Admission date:",font=("arial",12,"bold"))
       self.label_disdate = Label(self.DataframeLeft, text=" Discharge date:",font=("arial",12,"bold"))
       self.label_attender = Label(self.DataframeLeft, text=" Attender name:",font=("arial",12,"bold"))
       self.label_attnum= Label(self.DataframeLeft, text=" Attender number:",font=("arial",12,"bold"))
       self.label_prate = Label(self.DataframeLeft, text=" Pulse rate:",font=("arial",12,"bold"))
       self.label_bp = Label(self.DataframeLeft, text=" Blood Pressure:",font=("arial",12,"bold"))
      

       self.entry_name = Entry(self.DataframeLeft,font=("arial",12,"bold"),width=35)
       self.entry_id = Entry(self.DataframeLeft,font=("arial",12,"bold"),width=35)
       self.entry_age = Entry(self.DataframeLeft,font=("arial",12,"bold"),width=35)
       self.entry_dob= Entry(self.DataframeLeft,font=("arial",12,"bold"),width=35)
       self.entry_occ = Entry(self.DataframeLeft,font=("arial",12,"bold"),width=35)
       self.entry_medicalcondition = Entry(self.DataframeLeft,font=("arial",12,"bold"),width=35)
       self.entry_aadhar = Entry(self.DataframeLeft,font=("arial",12,"bold"),width=35)
       self.entry_gender = Entry(self.DataframeLeft,font=("arial",12,"bold"),width=35)
       self.entry_email = Entry(self.DataframeLeft,font=("arial",12,"bold"),width=35)
       self.entry_phone = Entry(self.DataframeLeft,font=("arial",12,"bold"),width=35)
       self.entry_maritalstatus = Entry(self.DataframeLeft,font=("arial",12,"bold"),width=35)
       self.entry_address = Entry(self.DataframeLeft,font=("arial",12,"bold"),width=35)
       self.entry_admidate = Entry(self.DataframeLeft,font=("arial",12,"bold"),width=35)
       self.entry_disdate = Entry(self.DataframeLeft,font=("arial",12,"bold"),width=35)
       self.entry_attender = Entry(self.DataframeLeft,font=("arial",12,"bold"),width=35)
       self.entry_attnum = Entry(self.DataframeLeft,font=("arial",12,"bold"),width=35)
       self.entry_prate = Entry(self.DataframeLeft,font=("arial",12,"bold"),width=35)
       self.entry_bp = Entry(self.DataframeLeft,font=("arial",12,"bold"),width=35)
      

        # Buttons with grid
       btn_save = Button(self.Buttonframe, text="Save", bg="green", fg="white", font=("arial", 16, "bold"),
                         width=22, padx=2, pady=5,  command=self.save_to_mysql)
       btn_update= Button(self.Buttonframe, text="update", bg="green", fg="white", font=("arial", 16, "bold"),
                         width=22, padx=2, pady=5, command=self.update_mysql)
       btn_delete = Button(self.Buttonframe, text="delete", bg="green", fg="white", font=("arial", 16, "bold"),
                         width=22, padx=2, pady=5, command=self.delete_from_mysql)
       btn_clear = Button(self.Buttonframe, text="Clear", bg="green", fg="white", font=("arial", 16, "bold"),
                         width=22, padx=2, pady=5, command=self.clear_fields)
       btn_exit = Button(self.Buttonframe, text="Exit", bg="green", fg="white", font=("arial", 16, "bold"),
                         width=22, padx=2, pady=5, command=self.exit_program)
       
       # Submit button
       btn_submit = Button(self.Dataframeright, text="Submit", bg="green", fg="white", font=("arial", 16, "bold"),
                            width=22, padx=2, pady=5, command=self.submit_to_mysql)
       btn_submit.grid(row=6, column=0, columnspan=2, pady=10)


       

        # Grid layout for labels and entries in DataframeLeft
       self.label_name.grid(row=0, column=0, pady=5, sticky=W)
       self.entry_name.grid(row=0, column=1, pady=5)

       self.label_id.grid(row=1, column=0, pady=5, sticky=W)
       self.entry_id.grid(row=1, column=1, pady=5)

       self.label_age.grid(row=2, column=0, pady=5, sticky=W)
       self.entry_age.grid(row=2, column=1, pady=5)

       self.label_dob.grid(row=3, column=0, pady=5, sticky=W)
       self.entry_dob.grid(row=3, column=1, pady=5)

       self.label_occ.grid(row=4, column=0, pady=5, sticky=W)
       self.entry_occ.grid(row=4, column=1, pady=5)

       self.label_medicalcondition.grid(row=5, column=0, pady=5, sticky=W)
       self.entry_medicalcondition.grid(row=5, column=1, pady=5)

       self.label_aadhar.grid(row=6, column=0, pady=5, sticky=W)
       self.entry_aadhar.grid(row=6, column=1, pady=5)

       self.label_gender.grid(row=7, column=0, pady=5, sticky=W)
       self.entry_gender.grid(row=7, column=1, pady=5)

       self.label_email.grid(row=8, column=0, pady=5, sticky=W)
       self.entry_email.grid(row=8, column=1, pady=5)

       self.label_phone.grid(row=0, column=2, pady=5, sticky=W)
       self.entry_phone.grid(row=0, column=3, pady=5)

       self.label_maritalstatus.grid(row=1, column=2, pady=5, sticky=W)
       self.entry_maritalstatus.grid(row=1, column=3, pady=5)

       self.label_admidate.grid(row=2, column=2, pady=5, sticky=W)
       self.entry_admidate.grid(row=2, column=3, pady=5)

       self.label_disdate.grid(row=3, column=2, pady=5, sticky=W)
       self.entry_disdate.grid(row=3, column=3, pady=5)

       self.label_attender.grid(row=4, column=2, pady=5, sticky=W)
       self.entry_attender.grid(row=4, column=3, pady=5)

       self.label_attnum.grid(row=5, column=2, pady=5, sticky=W)
       self.entry_attnum.grid(row=5, column=3, pady=5)

       self.label_address.grid(row=6, column=2, pady=5, sticky=W)
       self.entry_address.grid(row=6, column=3, pady=5)

       self.label_prate.grid(row=7, column=2, pady=5, sticky=W)
       self.entry_prate.grid(row=7, column=3, pady=5)

       self.label_bp.grid(row=8, column=2, pady=5, sticky=W)
       self.entry_bp.grid(row=8, column=3, pady=5)


        # Grid layout for buttons in DataframeLeft
       btn_save.grid(row=9, column=0, pady=10)
       btn_update.grid(row=9, column=1, pady=10)
       btn_delete.grid(row=9, column=2, pady=10)
       btn_clear.grid(row=9, column=3, pady=10)
       btn_exit.grid(row=9, column=4, pady=10)

   def save_to_mysql(self):
    try:
      
        Name = self.entry_name.get()
        id = self.entry_id.get()
        Age = self.entry_age.get()
        Date_of_Birth = self.entry_dob.get()
        occ = self.entry_occ.get()
        medicalcondition = self.entry_medicalcondition.get()
        aadhar = self.entry_aadhar.get()
        gender = self.entry_gender.get()
        email = self.entry_email.get()
        phone = self.entry_phone.get()
        maritalstatus = self.entry_maritalstatus.get()
        address = self.entry_address.get()
        Admidate = self.entry_admidate.get()
        disdate = self.entry_disdate.get()
        attender = self.entry_attender.get()
        attnum = self.entry_attnum.get()
        prate = self.entry_prate.get()
        bp = self.entry_bp.get()
      

        if not all([Name, id, Age, Date_of_Birth, occ, medicalcondition, aadhar, gender, email, phone,
                        maritalstatus, address, Admidate, disdate, attender, attnum, prate, bp]):
                raise ValueError("Please fill all the fields.")
        
        self.details_treeview.insert('', 'end', text='', values=(Name, id, Age, occ, medicalcondition, phone, address, Admidate, disdate,
                                                                prate, bp))

        # Connect to MySQL database (replace with your database credentials)
        conn = mysql.connector.connect(host="localhost", user="root", password="212Ac0619@003", database="program")
        my_cursor = conn.cursor()

        # Insert data into MySQL database
        query = "INSERT INTO sample5 (Name, Patient_Id, Age, Date_of_Birth, Occupation, Medical_condition, Aadhar_number, Gender, Email, Phone, Address, Marital_status, Admission_date, Discharge_date, Attender_name, Attender_number, Pulse_rate, Blood_Pressure) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (Name, id, Age, Date_of_Birth, occ, medicalcondition, aadhar, gender, email, phone, address, maritalstatus, Admidate, disdate, attender, attnum, prate, bp)

        my_cursor.execute(query, values)
        conn.commit()

        conn.close()
        messagebox.showinfo("Success", "Data saved to MySQL!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

        
   def update_mysql(self):
    # Get user inputs
    name = self.entry_name.get()
    id = self.entry_id.get()
    age = self.entry_age.get()
    dob = self.entry_dob.get()
    occ = self.entry_occ.get()
    medicalcondition = self.entry_medicalcondition.get()
    aadhar = self.entry_aadhar.get()
    gender = self.entry_gender.get()
    email = self.entry_email.get()
    phone = self.entry_phone.get()
    marital_status = self.entry_maritalstatus.get()
    address = self.entry_address.get()
    admission_date = self.entry_admidate.get()
    discharge_date = self.entry_disdate.get()
    attender_name = self.entry_attender.get()
    attender_number = self.entry_attnum.get()
    pulse_rate = self.entry_prate.get()
    blood_pressure = self.entry_bp.get()
   

    if not name:
        messagebox.showwarning("Warning", "Please enter the record name to update.")
        return


    # Connect to MySQL database (replace with your database credentials)
    conn = mysql.connector.connect(host="localhost", user="root", password="212Ac0619@003", database="program")
    my_cursor = conn.cursor()

    # Update data in MySQL database
    query = "UPDATE sample5 SET Patient_Id=%s, Age=%s, Date_of_Birth=%s, Occupation=%s, Medical_condition=%s, Aadhar_number=%s, Gender=%s, Email=%s, Phone=%s, Marital_status=%s, Address=%s, Admission_date=%s, Discharge_date=%s, Attender_name=%s, Attender_number=%s, Pulse_rate=%s, Blood_Pressure=%s WHERE Name=%s"
    values = (age, id, dob, occ, medicalcondition, aadhar, gender, email, phone, marital_status, address, admission_date, discharge_date, attender_name, attender_number, pulse_rate, blood_pressure, name)

    my_cursor.execute(query, values)
    conn.commit()

    conn.close()
    messagebox.showinfo("Success", "Data updated in MySQL!")


   def delete_from_mysql(self):
    # Get user input
    name = self.entry_name.get()

    if not name:
        messagebox.showwarning("Warning", "Please enter the record name to delete.")
        return


    # Connect to MySQL database (replace with your database credentials)
    conn = mysql.connector.connect(host="localhost", user="root", password="212Ac0619@003", database="program")
    my_cursor = conn.cursor()

    # Delete data from MySQL database
    query = "DELETE FROM sample5 WHERE name=%s"
    values = (name,)

    my_cursor.execute(query, values)
    conn.commit()

    conn.close()
    messagebox.showinfo("Success", "Data deleted from MySQL!") 
  
   def clear_fields(self):
    self.entry_name.delete(0, END)
    self.entry_id.delete(0, END)
    self.entry_age.delete(0, END)
    self.entry_dob.delete(0, END)
    self.entry_occ.delete(0, END)
    self.entry_medicalcondition.delete(0, END)
    self.entry_aadhar.delete(0, END)
    self.entry_gender.delete(0, END)
    self.entry_email.delete(0, END)
    self.entry_phone.delete(0, END)
    self.entry_maritalstatus.delete(0, END)
    self.entry_address.delete(0, END)
    self.entry_admidate.delete(0, END)
    self.entry_disdate.delete(0, END)
    self.entry_attender.delete(0, END)
    self.entry_attnum.delete(0, END)
    self.entry_prate.delete(0, END)
    self.entry_bp.delete(0, END)
   

   def exit_program(self):
        self.root.destroy()

   def calculate_total(self):
        try:
            medical_fees = float(self.entry_medical_fees.get())
            consultation_fees = float(self.entry_consultation_fees.get())
            other_charges = float(self.amt.get())

            total = medical_fees + consultation_fees + other_charges
            self.entry_total.delete(0, END)
            self.entry_total.insert(0, str(total))
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numerical values for fees.")     

   def submit_to_mysql(self):
    try:
        # Get values from the additional entry boxes
        patient_name = self.entry_patient_name.get()
        doctor_name = self.entry_patientid.get()
        medical_fees = self.entry_medical_fees.get()
        consultation_fees = self.entry_consultation_fees.get()
        other_charges = self.other_charges.get()
        amt = self.amt.get()
        self.calculate_total()

        # Connect to MySQL database (replace with your database credentials)
        conn = mysql.connector.connect(host="localhost", user="root", password="212Ac0619@003", database="program")
        my_cursor = conn.cursor()

        # Insert data into MySQL database
        query = "INSERT INTO sample6 (Patient_name, Patient_id, Medical_fees, consultation_fees, Other_charges, amt, Total) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (patient_name, doctor_name, medical_fees, consultation_fees, other_charges, amt, float(self.entry_total.get()))

        my_cursor.execute(query, values)
        conn.commit()

        conn.close()
        messagebox.showinfo("Success", "Bill details saved to MySQL!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


    def fetch_patient_details(self, patient_name, patient_id):
        try:
            # Connect to MySQL database (replace with your database credentials)
            conn = mysql.connector.connect(host="localhost", user="root", password="212Ac0619@003", database="program")
            my_cursor = conn.cursor()

            # Fetch patient details from MySQL database based on name and id
            query = "SELECT * FROM sample5 WHERE Name=%s AND Patient_Id=%s"
            values = (patient_name, patient_id)

            my_cursor.execute(query, values)
            patient_details = my_cursor.fetchone()

            conn.close()

            if patient_details:
                # Display patient details in dataframeright
                self.display_patient_details(patient_details)
            else:
                messagebox.showinfo("Not Found", "Patient details not found!")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def display_patient_details(self, patient_details):
        # Populate the entry fields in Dataframeright with patient details
        self.entry_patient_name.delete(0, END)
        self.entry_patient_name.insert(0, patient_details[0])

        # Assuming doctor name is stored in the second column of the database
        self.entry_doctor_name.delete(0, END)
        self.entry_doctor_name.insert(0, patient_details[1])

        # Assuming medical fees is stored in the third column of the database
        self.entry_medical_fees.delete(0, END)
        self.entry_medical_fees.insert(0, patient_details[2])

        # Assuming consultation fees is stored in the fourth column of the database
        self.entry_consultation_fees.delete(0, END)
        self.entry_consultation_fees.insert(0, patient_details[3])

        # Assuming other charges is stored in the fifth column of the database
        self.other_charges.set(patient_details[4])

        # Assuming amount is stored in the sixth column of the database
        self.amt.delete(0, END)
        self.amt.insert(0, patient_details[5])

        # Calculate and display the total
        self.calculate_total()

        messagebox.showinfo("Success", "Patient details displayed successfully!")
        


if __name__ == "__main__":
    root = Tk()
    app = HospitalManagementSystem(root)
    root.mainloop()   
 


