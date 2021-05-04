from tkinter import *
import sqlite3

win = Tk()
win.title("databse")

#Database

#creating a database or connect to one

conn = sqlite3.connect("address_book.db")

#creating curser
#curser class in an instance using which you can invoke using method that execute SQLITE,
#fetch data  from result sets of queries
curser = conn.cursor()
#
# #creating the table
# curser.execute("""CREATE TABLE student_data(
#                first_name text,
#                last_name text,
#                address text,
#                city text,
#                state text,
#                zipcode integer
# )
# """)
#
# print("table created sucessfully")
#

#creating function

def submit():
    # creating a database or connect to one

    conn = sqlite3.connect("address_book.db")

    curser = conn.cursor()

    curser.execute("INSERT INTO student_data VALUES (:first_name, :last_name, :address, :city, :state, :zipcode)", {
        'first_name': efirst_name.get(),
        'last_name': elast_name.get(),
        'address': eaddress.get(),
        'city': ecity.get(),
        'state': estate.get(),
        'zipcode': ezipcode.get()
    })
    print('Address inserted successfully')


    conn.commit()

    conn.close()

    efirst_name.delete(0,END)
    elast_name.delete(0,END)
    eaddress.delete(0,END)
    ecity.delete(0,END)
    estate.delete(0,END)
    ezipcode.delete(0,END)


def display():
    conn = sqlite3.connect("address_book.db")

    curser = conn.cursor()
    curser.execute("SELECT *, oid FROM student_data")

    records = curser.fetchall()
    print(records)

    print_records=''

    for record in records:
        print_records += str(record[0]) +' ' + str(record[1]) + ' '+ '\t' + str(record[6]) + "\n"


    query_label = Label(win, text = print_records)
    query_label.grid(row=10,column=0,columnspan=2)

    conn.commit()

    conn.close()

def delete():
    conn = sqlite3.connect("address_book.db")

    curser = conn.cursor()
    curser.execute("DELETE from student_data WHERE oid = " + edelete.get())
    print("deleted sucessfully")

    records = curser.fetchall()

    curser.execute("SELECT *, oid FROM student_data")

    records = curser.fetchall()
    print(records)
    conn.commit()

    conn.close()

    print_records = ''

    for record in records:
        print_records += str(record[0]) + ' ' + str(record[1]) + ' ' + '\t' + str(record[6]) + "\n"

    query_label = Label(win, text=print_records)
    query_label.grid(row=11, column=0, columnspan=2)

def update():
    editor =Tk()
    editor.title('update')
    conn = sqlite3.connect("address_book.db")

    curser = conn.cursor()

    record_id = edelete.get()
    curser.execute("SELECT * FROM student_data WHERE oid= " + record_id)

    records = curser.fetchall()

    first_name_editor = Label(editor, text="first_name").grid(row=0, column=0)
    efirst_name_editor = Entry(editor)
    efirst_name_editor.grid(row=0, column=1)

    last_name_editor = Label(editor, text="last_name").grid(row=1, column=0)
    elast_name_editor = Entry(editor)
    elast_name_editor.grid(row=1, column=1)

    address_editor = Label(editor, text="address").grid(row=2, column=0)
    eaddress_editor = Entry(editor)
    eaddress_editor.grid(row=2, column=1)

    city_editor = Label(editor, text="city").grid(row=3, column=0)
    ecity_editor = Entry(editor)
    ecity_editor.grid(row=3, column=1)

    state_editor = Label(editor, text="state").grid(row=4, column=0)
    estate_editor = Entry(editor)
    estate_editor.grid(row=4, column=1)

    zipcode_editor = Label(editor, text="zipcode").grid(row=5, column=0)
    ezipcode_editor = Entry(editor)
    ezipcode_editor.grid(row=5, column=1)

    for record in records:
        efirst_name_editor.insert(0,record[0])
        elast_name_editor.insert(0,record[1])
        eaddress_editor.insert(0,record[2])
        ecity_editor.insert(0,record[3])
        estate_editor.insert(0,record[4])
        ezipcode_editor.insert(0,record[5])



    save = Button(editor, text="SAVE").grid(row=6, columnspan=3, ipady=5, ipadx=40)






#creating desigh


first_name = Label(win,text="first_name").grid(row=0,column=0)
efirst_name = Entry(win)
efirst_name.grid(row=0, column=1)

last_name = Label(win,text="last_name").grid(row=1,column=0)
elast_name= Entry(win)
elast_name.grid(row=1, column=1)

address = Label(win,text="address").grid(row=2,column=0)
eaddress = Entry(win)
eaddress.grid(row=2, column=1)

city = Label(win,text="city").grid(row=3,column=0)
ecity = Entry(win)
ecity.grid(row=3, column=1)

state = Label(win,text="state").grid(row=4,column=0)
estate = Entry(win)
estate.grid(row=4, column=1)

zipcode = Label(win,text="zipcode").grid(row=5,column=0)
ezipcode = Entry(win)
ezipcode.grid(row=5, column=1)

add_record = Button(win, text="addrecords" , command=submit).grid(row=6,columnspan=3,ipady=5,ipadx=40)
display = Button(win, text="display",command = display ).grid(row=7,columnspan=3,ipady=5,ipadx=40)

delete_id = Label(win,text="Delete ID").grid(row=8,column=0)
edelete= Entry(win)
edelete.grid(row=8, column=1)
edelete_button = Button(win, text="DELETE",command=delete).grid(row=9,columnspan=3)
eupdate_button = Button(win, text="update",command=update).grid(row=11,columnspan=3)

# commit chnage
conn.commit()

#close connection
conn.close()



mainloop()
