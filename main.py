'''student management system project in python using tkinter and mysql'''
from functools import partial
from tkinter import *
from tkinter import messagebox
import pymysql
import credentials as cr


class Management:
    def __init__(self, root):
        self.window = root
        self.window.title("Student Result Management System")
        self.window.geometry("780x480")
        self.window.config(bg="white")

        # Customization
        self.color_1 = "deep sky blue"
        self.color_2 = "gray95"
        self.color_3 = "black"
        self.color_4 = "white"
        self.font_1 = "times new roman"
        self.font_2 = "helvetica"

        # User Credentials
        self.host = cr.host
        self.user = cr.user
        self.password = cr.password
        self.database = cr.database

        # Left Frame
        self.frame_1 = Frame(self.window, bg=self.color_1)
        self.frame_1.place(x=0, y=0, width=540, relheight=1)

        # Right Frame
        self.frame_2 = Frame(self.window, bg=self.color_2)
        self.frame_2.place(x=540, y=0, relwidth=1, relheight=1)

        # Buttons
        self.add_bt = Button(self.frame_2, text='Add New', font=(self.font_1, 12), bd=2, command=self.AddStudent,
                             cursor="hand2", bg=self.color_2, fg=self.color_3).place(x=68, y=40, width=100)
        self.view_bt = Button(self.frame_2, text='View Result', font=(self.font_1, 12), bd=2,
                              command=self.GetResult_View, cursor="hand2", bg=self.color_2, fg=self.color_3).place(
            x=68, y=100, width=100)
        self.update_bt = Button(self.frame_2, text='Update', font=(self.font_1, 12), bd=2,
                                command=self.GetPRN_Update, cursor="hand2", bg=self.color_2, fg=self.color_3).place(
            x=68, y=160, width=100)
        self.delete_bt = Button(self.frame_2, text='Delete', font=(self.font_1, 12), bd=2,
                                command=self.GetPRN_Delete, cursor="hand2", bg=self.color_2, fg=self.color_3).place(
            x=68, y=220, width=100)
        self.clear_bt = Button(self.frame_2, text='Clear', font=(self.font_1, 12), bd=2, command=self.ClearScreen,
                               cursor="hand2", bg=self.color_2, fg=self.color_3).place(x=68, y=280, width=100)
        self.exit_bt = Button(self.frame_2, text='Exit', font=(self.font_1, 12), bd=2, command=self.Exit,
                              cursor="hand2", bg=self.color_2, fg=self.color_3).place(x=68, y=340, width=100)

    '''Widgets for adding student data'''

    def AddStudent(self):
        self.ClearScreen()

        self.name = Label(self.frame_1, text="Name", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,
                                                                                                                  y=30)
        self.name_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.name_entry.place(x=40, y=60, width=200)

        self.prn = Label(self.frame_1, text="PRN", font=(self.font_2, 15, "bold"), bg=self.color_1).place(
            x=300, y=30)
        self.prn_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.prn_entry.place(x=300, y=60, width=200)

        self.branch = Label(self.frame_1, text="Branch", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,
                                                                                                                y=100)
        self.branch_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.branch_entry.place(x=40, y=130, width=200)

        self.no_of_subjects = Label(self.frame_1, text="No. of subjects", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,
                                                                                                                  y=100)
        self.no_of_subjects_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.no_of_subjects_entry.place(x=300, y=130, width=200)

        self.semester = Label(self.frame_1, text="Semester", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40, y=170)
        self.semester_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.semester_entry.place(x=40, y=200, width=200)

        self.total_marks = Label(self.frame_1, text="Total Marks", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300, y=170)
        self.total_marks_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.total_marks_entry.place(x=300, y=200, width=200)

        self.gender = Label(self.frame_1, text="Gender", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,
                                                                                                                y=240)
        self.gender_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.gender_entry.place(x=40, y=270, width=200)

        self.dob = Label(self.frame_1, text="DOB", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,
                                                                                                                 y=240)
        self.dob_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.dob_entry.place(x=300, y=270, width=200)

        self.contact_no = Label(self.frame_1, text="Contact No.", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,
                                                                                                                  y=310)
        self.contact_no_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.contact_no_entry.place(x=40, y=340, width=200)

        self.email = Label(self.frame_1, text="Email ID", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,
                                                                                                              y=310)
        self.email_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.email_entry.place(x=300, y=340, width=200)

        self.submit_bt_1 = Button(self.frame_1, text='Submit', font=(self.font_1, 12), bd=2, command=self.Submit,
                                  cursor="hand2", bg=self.color_2, fg=self.color_3).place(x=200, y=389, width=100)

    '''Get the contact number to show a student details'''

    def GetResult_View(self):
        self.ClearScreen()

        self.getInfo = Label(self.frame_1, text="Enter PRN", font=(self.font_2, 18, "bold"),
                             bg=self.color_1).place(x=140, y=70)
        self.getInfo_entry = Entry(self.frame_1, font=(self.font_1, 12), bg=self.color_4, fg=self.color_3)
        self.getInfo_entry.place(x=163, y=110, width=200, height=30)
        self.submit_bt_2 = Button(self.frame_1, text='Submit', font=(self.font_1, 10), bd=2,
                                  command=self.CheckResult_View, cursor="hand2", bg=self.color_2,
                                  fg=self.color_3).place(x=220, y=150, width=80)

    '''To update a student details, get the contact number'''

    def GetPRN_Update(self):
        self.ClearScreen()

        self.getInfo = Label(self.frame_1, text="Enter PRN", font=(self.font_2, 18, "bold"),
                             bg=self.color_1).place(x=140, y=70)
        self.getInfo_entry = Entry(self.frame_1, font=(self.font_1, 12), bg=self.color_4, fg=self.color_3)
        self.getInfo_entry.place(x=163, y=110, width=200, height=30)
        self.submit_bt_2 = Button(self.frame_1, text='Submit', font=(self.font_1, 10), bd=2,
                                  command=self.CheckResult_Update, cursor="hand2", bg=self.color_2,
                                  fg=self.color_3).place(x=220, y=150, width=80)

    '''Get the contact number to delete a student record'''

    def GetPRN_Delete(self):
        self.ClearScreen()

        self.getInfo = Label(self.frame_1, text="Enter PRN", font=(self.font_2, 18, "bold"),
                             bg=self.color_1).place(x=140, y=70)
        self.getInfo_entry = Entry(self.frame_1, font=(self.font_1, 12), bg=self.color_4, fg=self.color_3)
        self.getInfo_entry.place(x=163, y=110, width=200, height=30)
        self.submit_bt_2 = Button(self.frame_1, text='Submit', font=(self.font_1, 10), bd=2, command=self.DeleteData,
                                  cursor="hand2", bg=self.color_2, fg=self.color_3).place(x=220, y=150, width=80)

    '''Remove all widgets from the frame 1'''

    def ClearScreen(self):
        for widget in self.frame_1.winfo_children():
            widget.destroy()

    '''Exit window'''

    def Exit(self):
        self.window.destroy()

    '''
    Checks whether the contact number is available or not. If available, 
    the function calls the 'ShowDetails' function to display the result.
    '''

    def CheckResult_View(self):
        if self.getInfo_entry.get() == "":
            messagebox.showerror("Error!", "Please enter your PRN", parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=self.host, user=self.user, password=self.password,
                                             database=self.database)
                curs = connection.cursor()
                curs.execute("select * from student_register where prn=%s", self.getInfo_entry.get())
                row = curs.fetchone()

                if row == None:
                    messagebox.showerror("Error!", "PRN doesn't exist", parent=self.window)
                else:
                    self.ShowDetails(row)
                    connection.close()
            except Exception as e:
                messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

    '''
    Checks whether the contact number is available or not. If available, 
    the function calls the 'GetUpdateDetails' function to get the new data to perform
    update operation.
    '''

    def CheckResult_Update(self):
        if self.getInfo_entry.get() == "":
            messagebox.showerror("Error!", "Please enter your PRN", parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=self.host, user=self.user, password=self.password,
                                             database=self.database)
                curs = connection.cursor()
                curs.execute("select * from student_register where prn=%s", self.getInfo_entry.get())
                row = curs.fetchone()

                if row == None:
                    messagebox.showerror("Error!", "PRN doesn't exist", parent=self.window)
                else:
                    self.GetUpdateDetails(row)
                    connection.close()
            except Exception as e:
                messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

    '''Clears a student record'''

    def DeleteData(self):
        if self.getInfo_entry.get() == "":
            messagebox.showerror("Error!", "Please enter your PRN", parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=self.host, user=self.user, password=self.password,
                                             database=self.database)
                curs = connection.cursor()
                curs.execute("select * from student_register where prn=%s", self.getInfo_entry.get())
                row = curs.fetchone()

                if row == None:
                    messagebox.showerror("Error!", "PRN doesn't exist", parent=self.window)
                else:
                    curs.execute("delete from student_register where prn=%s", self.getInfo_entry.get())
                    connection.commit()
                    messagebox.showinfo('Done!', "The data has been deleted")
                    connection.close()
                    self.ClearScreen()
            except Exception as e:
                messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

    '''Gets the data that the user wants to update to perform the update operation'''

    def GetUpdateDetails(self, row):
        self.ClearScreen()

        self.name = Label(self.frame_1, text="Name", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,
                                                                                                                  y=30)
        self.name_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.name_entry.insert(0, row[0])
        self.name_entry.place(x=40, y=60, width=200)

        self.branch = Label(self.frame_1, text="Branch", font=(self.font_2, 15, "bold"), bg=self.color_1).place(
            x=300, y=30)
        self.branch_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.branch_entry.insert(0, row[1])
        self.branch_entry.place(x=300, y=60, width=200)

        self.no_of_subjects = Label(self.frame_1, text="No. of subjects", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,
                                                                                                                y=100)
        self.no_of_subjects_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.no_of_subjects_entry.insert(0, row[2])
        self.no_of_subjects_entry.place(x=40, y=130, width=200)

        self.semester = Label(self.frame_1, text="Semester", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,
                                                                                                                  y=100)
        self.semester_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.semester_entry.insert(0, row[3])
        self.semester_entry.place(x=300, y=130, width=200)

        self.gender = Label(self.frame_1, text="Gender", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40, y=170)
        self.gender_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.gender_entry.insert(0, row[4])
        self.gender_entry.place(x=40, y=200, width=200)

        self.total_marks = Label(self.frame_1, text="Total Marks", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300, y=170)
        self.total_marks_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.total_marks_entry.insert(0, row[5])
        self.total_marks_entry.place(x=300, y=200, width=200)

        self.contact_no = Label(self.frame_1, text="Contact No.", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,
                                                                                                                y=240)
        self.contact_no_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.contact_no_entry.insert(0, row[6])
        self.contact_no_entry.place(x=40, y=270, width=200)

        self.email = Label(self.frame_1, text="Email ID", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,
                                                                                                                 y=240)
        self.email_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.email_entry.insert(0, row[7])
        self.email_entry.place(x=300, y=270, width=200)

        self.dob = Label(self.frame_1, text="DOB", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,
                                                                                                              y=310)
        self.dob_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.dob_entry.insert(0, row[9])
        self.dob_entry.place(x=300, y=340, width=200)

        self.submit_bt_1 = Button(self.frame_1, text='Submit', font=(self.font_1, 12), bd=2,
                                  command=partial(self.UpdateDetails, row), cursor="hand2", bg=self.color_2,
                                  fg=self.color_3).place(x=160, y=389, width=100)
        self.cancel_bt = Button(self.frame_1, text='Cancel', font=(self.font_1, 12), bd=2, command=self.ClearScreen,
                                cursor="hand2", bg=self.color_2, fg=self.color_3).place(x=280, y=389, width=100)

    '''Within frame 1, it displays information about a student'''

    def ShowDetails(self, row):
        self.ClearScreen()
        name = Label(self.frame_1, text="Name", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40, y=30)
        name_data = Label(self.frame_1, text=row[0], font=(self.font_1, 10)).place(x=40, y=60)

        branch = Label(self.frame_1, text="Branch", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300, y=30)
        branch_data = Label(self.frame_1, text=row[1], font=(self.font_1, 10)).place(x=300, y=60)

        no_of_subjects = Label(self.frame_1, text="No. of subjects", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40, y=100)
        no_of_subjects_data = Label(self.frame_1, text=row[2], font=(self.font_1, 10)).place(x=40, y=130)

        semester = Label(self.frame_1, text="Semester", font=(self.font_2, 15, "bold"),
                               bg=self.color_1).place(x=300, y=100)
        semester_data = Label(self.frame_1, text=row[3], font=(self.font_1, 10)).place(x=300, y=130)

        gender = Label(self.frame_1, text="Gender", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,
                                                                                                               y=170)
        gender_data = Label(self.frame_1, text=row[4], font=(self.font_1, 10)).place(x=40, y=200)

        total_marks = Label(self.frame_1, text="Total Marks", font=(self.font_2, 15, "bold"), bg=self.color_1).place(
            x=300, y=170)
        total_marks_data = Label(self.frame_1, text=row[5], font=(self.font_1, 10)).place(x=300, y=200)

        percentage = int(row[5]) / int(row[2])  # Calculate percentage
        pass_fail = "Pass" if percentage >= 33 else "Fail"  # Determine pass/fail status

        percentage_label = Label(self.frame_1, text="Percentage", font=(self.font_2, 15, "bold"),
                                 bg=self.color_1).place(x=40, y=240)
        percentage_data = Label(self.frame_1, text=f"{percentage}%", font=(self.font_1, 10)).place(x=40, y=270)

        pass_fail_label = Label(self.frame_1, text="Pass/Fail", font=(self.font_2, 15, "bold"), bg=self.color_1).place(
            x=300, y=240)
        pass_fail_data = Label(self.frame_1, text=pass_fail, font=(self.font_1, 10)).place(x=300, y=270)

        email = Label(self.frame_1, text="Email ID", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40, y=310)
        email_data = Label(self.frame_1, text=row[7], font=(self.font_1, 10)).place(x=40, y=340)

        dob = Label(self.frame_1, text="DOB", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40, y=380)
        dob_data = Label(self.frame_1, text=row[9], font=(self.font_1, 10)).place(x=40, y=410)


    '''Updates student data'''

    def UpdateDetails(self, row):
        if self.name_entry.get() == "" or self.branch_entry.get() == "" or self.no_of_subjects_entry.get() == "" or self.semester_entry.get() == "" or self.gender_entry.get() == "" or self.total_marks_entry.get() == "" or self.contact_no_entry.get() == "" or self.email_entry.get() == "" or self.dob_entry.get() == "":
            messagebox.showerror("Error!", "Sorry!, All fields are required", parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=self.host, user=self.user, password=self.password,
                                             database=self.database)
                curs = connection.cursor()
                curs.execute("select * from student_register where prn=%s", row[8])
                row = curs.fetchone()

                if row == None:
                    messagebox.showerror("Error!", "The PRN doesn't exist", parent=self.window)
                else:
                    curs.execute(
                        "update student_register set name=%s, branch=%s, no_of_subjects=%s, semester=%s, gender=%s, total_marks=%s, contact_no=%s, email=%s, dob=%s where prn=%s",
                        (
                            self.name_entry.get(),
                            self.branch_entry.get(),
                            self.no_of_subjects_entry.get(),
                            self.semester_entry.get(),
                            self.gender_entry.get(),
                            self.total_marks_entry.get(),
                            self.contact_no_entry.get(),
                            self.email_entry.get(),
                            self.dob_entry.get(),
                            row[8]
                        ))
                    connection.commit()
                    connection.close()
                    messagebox.showinfo('Done!', "The data has been updated")
                    self.ClearScreen()
            except Exception as e:
                messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

    '''It adds the information of new students'''

    def Submit(self):
        if self.name_entry.get() == "" or self.prn_entry.get() == "" or self.branch_entry.get() == "" or self.no_of_subjects_entry.get() == "" or self.semester_entry.get() == "" or self.total_marks_entry.get() == "" or self.gender_entry.get() == "" or self.dob_entry.get() == "" or self.contact_no_entry.get() == "" or self.email_entry.get() == "":
            messagebox.showerror("Error!", "Sorry!, All fields are required", parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=self.host, user=self.user, password=self.password,
                                             database=self.database)
                curs = connection.cursor()
                curs.execute("select * from student_register where prn=%s", self.contact_no_entry.get())
                row = curs.fetchone()

                if row != None:
                    messagebox.showerror("Error!",
                                         "This PRN already exists, please try again with another number",
                                         parent=self.window)
                else:
                    curs.execute(
                        "insert into student_register (name,prn,branch,no_of_subjects,semester,total_marks,gender,dob,contact_no,email) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (
                            self.name_entry.get(),
                            self.prn_entry.get(),
                            self.branch_entry.get(),
                            self.no_of_subjects_entry.get(),
                            self.semester_entry.get(),
                            self.total_marks_entry.get(),
                            self.gender_entry.get(),
                            self.dob_entry.get(),
                            self.contact_no_entry.get(),
                            self.email_entry.get()
                        ))
                    connection.commit()
                    connection.close()
                    messagebox.showinfo('Done!', "The data has been submitted")
                    self.reset_fields()
            except Exception as e:
                messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

    '''Reset all the entry fields'''

    def reset_fields(self):
        self.name_entry.delete(0, END)
        self.prn_entry.delete(0, END)
        self.branch_entry.delete(0, END)
        self.no_of_subjects_entry.delete(0, END)
        self.semester_entry.delete(0, END)
        self.total_marks_entry.delete(0, END)
        self.gender_entry.delete(0, END)
        self.dob_entry.delete(0, END)
        self.contact_no_entry.delete(0, END)
        self.email_entry.delete(0, END)


# The main function
if __name__ == "__main__":
    root = Tk()
    obj = Management(root)
    root.mainloop()