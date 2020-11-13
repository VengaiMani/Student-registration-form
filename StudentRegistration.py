from tkinter import *
from tkcalendar import DateEntry

form=Tk()
form.title("Student registration form")
form.geometry("800x800")

Label(form,text="Student Registration form",font=("Freestyle Script",30),bg="powder blue",pady=10).pack()

#Name
name_frame=Frame(form,pady=15)
Label(name_frame,text="First Name").grid(row=0,column=0)
first_name=Entry(name_frame,width=30).grid(row=0,column=1)
Label(name_frame,text="Last Name",pady=10).grid(row=1,column=0)
last_name=Entry(name_frame,width=30).grid(row=1,column=1)
name_frame.pack()

#Roll number
roll_frame=Frame(form,pady=15)
Label(roll_frame,text="Roll number").grid(row=0,column=0)
roll_number=Entry(roll_frame,width=20).grid(row=0,column=1)
roll_frame.pack()

#Date of birth
date_frame=Frame(form,pady=15)
Label(date_frame,text="Date of Birth").grid(row=0,column=0)
date_of_birth=DateEntry(date_frame,year=1999).grid(row=0,column=1)
date_frame.pack()

#Gender
gender_frame=Frame(form,pady=15)
Label(gender_frame,text="Gender").grid(row=0,column=0)
gender=IntVar()
Radiobutton(gender_frame,text="Male",variable=gender,value=1).grid(row=1,column=0)
Radiobutton(gender_frame,text="Female",variable=gender,value=2).grid(row=1,column=1)
Radiobutton(gender_frame,text="Other",variable=gender,value=3).grid(row=1,column=2)
gender_frame.pack()

#Parents details
parent_frame=Frame(form,pady=15)
Label(parent_frame,text="Father's name").grid(row=0,column=0)
father_name=Entry(parent_frame,width=30).grid(row=0,column=1)
Label(parent_frame,text="Mother's name").grid(row=1,column=0)
mother_name=Entry(parent_frame,width=30).grid(row=1,column=1)
parent_frame.pack()



#Department and year of study
dept_year_frame=Frame(form,pady=15)
Label(dept_year_frame,text="Department").grid(row=0,column=0)
department=StringVar()
DEPARTMENTS=["Computer science and engineering",
             "Information Technology",
             "Mechanical engineering",
             "Electronics and communication engineering",
             "Electrical and electronics engineering",
             "Civil engineering",
             "Electronics and instrumentation engineering"]
OptionMenu(dept_year_frame,department,*DEPARTMENTS).grid(row=0,column=1)
STUDY_YEAR=["First year","Second year","Third year","Fourth year"]
year_of_study=StringVar()
Label(dept_year_frame,text="Year of study",pady=10).grid(row=1,column=0)
OptionMenu(dept_year_frame,year_of_study,*STUDY_YEAR).grid(row=1,column=1)
dept_year_frame.pack()

#Email address
mail_frame=Frame(form,pady=15)
Label(mail_frame,text="Email address").grid(row=0,column=0)
email=Entry(mail_frame,width=30).grid(row=0,column=1)
mail_frame.pack()

#Phone number
phone_frame=Frame(form,pady=15)
Label(phone_frame,text="Phone number").grid(row=0,column=0)
phone_number=Entry(phone_frame,width=20).grid(row=0,column=1)
phone_frame.pack()

#Address
address_frame=Frame(form,pady=15)
Label(address_frame,text="Address").grid(row=0,column=0)
address=Text(address_frame,width=30,height=5).grid(row=0,column=1)
address_frame.pack()

#Register button
register_button=Button(form,text="Register",font=("Script MT Bold",20,"bold"),fg="blue",bg="orange")
register_button.pack()

form.mainloop()