from tkinter import *
from tkinter import ttk
import mysql.connector


try:
    con = mysql.connector.connect(host='localhost', user='root', password='root', database='Tsering')
    cur = con.cursor()
except mysql.connector.Error as e:
    print(e)

class Std_information:
    def __init__(self, root):

        self.root = root


        #---------Entry---------
        self.id = Entry(self.root)
        self.id.grid(row=0, column=1, padx=15, pady=15)

        self.fname = Entry(self.root)
        self.fname.grid(row=1, column=1, padx=15, pady=15)

        self.lname = Entry(self.root)
        self.lname.grid(row=2, column=1, padx=15, pady=15)

        self.address = Entry(self.root)
        self.address.grid(row=3, column=1, padx=15, pady=15)

        self.degree = Entry(self.root)
        self.degree.grid(row=4, column=1, padx=15, pady=15)

        self.Contact_number = Entry(self.root)
        self.Contact_number.grid(row=5, column=1, padx=15, pady=15)


        #------------frame---------
        self.btn_frame = Frame(self.root, bd=4, bg='navy blue', relief=RIDGE)
        self.btn_frame.place(x=20, y=350, width=600, height=50)

        self.table_frame = Frame(self.root, bd=4, bg='navy blue', relief=RIDGE)
        self.table_frame.place(x=20, y=400, width=600, height=350)

        #-------scrollbar--------
        self.scroll_x = Scrollbar(self.table_frame, orient=HORIZONTAL)
        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y = Scrollbar(self.table_frame, orient=VERTICAL)
        self.scroll_y.pack(side=RIGHT, fill=Y)

        # --------label---------
        self.lblid = Label(self.root, text='ID')
        self.lblid.grid(row=0, column=0, padx=15, pady=15)

        self.lblfname= Label(self.root, text='First Name')
        self.lblfname.grid(row=1, column=0, padx=15, pady=15)

        self.lbllname = Label(self.root, text='Last Name')
        self.lbllname.grid(row=2, column=0, padx=15, pady=15)

        self.lbladdress = Label(self.root, text="Address")
        self.lbladdress.grid(row=3, column=0, padx=15, pady=15)

        self.lbldegree = Label(self.root, text='degree')
        self.lbldegree.grid(row=4, column=0, padx=15, pady=15)

        self.lblContact_number = Label(self.root, text='Contact_number Number')
        self.lblContact_number.grid(row=5, column=0, padx=15, pady=15)


        #----------Table---------
        self.table=ttk.Treeview(self.table_frame, columns=('Id','First_name', 'Last_name','Address', 'degree','Contact_number',),
                                        xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)
        self.table.heading('Id', text='ID')
        self.table.heading('First_name',text='First_name')
        self.table.heading('Last_name', text='Last_name')
        self.table.heading('Address', text='Address')
        self.table.heading('degree', text='Degree')
        self.table.heading('Contact_number', text='Contact_number')
        self.table.pack(fill=BOTH,expand=True)

        self.table['show']='headings'

        self.table.column('Id', width=50)
        self.table.column('First_name',width=80)
        self.table.column('Last_name', width=80)
        self.table.column('Address', width=90)
        self.table.column('degree', width=100)
        self.table.column('Contact_number', width=100)

        self.scroll_x.config(command=self.table.xview)
        self.scroll_y.config(command=self.table.yview)

        self.show()

        self.table.bind('<ButtonRelease-1>',self.pointer)
        self.table.pack(fill=BOTH, expand=True)



        #-----------button--------
        self.addbtn=Button(self.btn_frame, text='Add',command=self.add_info, width=15,height=2)
        self.addbtn.grid(row=5, column=0,padx=10)

        self.upbtn=Button(self.btn_frame,text='Update',command=self.update,width=15,height=2)
        self.upbtn.grid(row=5,column=2,padx=10)
        self.deletebtn=Button(self.btn_frame,text='Delete',command=self.delete,width=15,height=2)
        self.deletebtn.grid(row=5,column=4,padx=10)
        self.clearbtn=Button(self.btn_frame,text='Clear',command=self.clear,width=15,height=2)
        self.clearbtn.grid(row=5,column=6,padx=10)


        self.detail_frame=Frame(self.root,bd=4,relief=RIDGE)
        self.detail_frame.place(x=400,y=15,width=450,height=120)


        self.searchlbl=Label(self.detail_frame,text= 'Search text',width=10,font=('Callibry',10))
        self.searchlbl.grid(row=2,column=0,pady=5)

        self.searchentry=Entry(self.detail_frame,width=20)
        self.searchentry.grid(row=2,column=1,pady=5)

        self.searchbtn=Button(self.detail_frame,text='Search',command=self.search,font=('callibry',10),width=8)
        self.searchbtn.grid(row=2,column=3,pady=15,padx=10)

        self.lblsort = Label(self.detail_frame, text='Sort By', font=('arial', 10))
        self.lblsort.grid(row=1, column=0, pady=5)

        self.sortcombo = ttk.Combobox(self.detail_frame, font=('arial', 10), state='readonly',width=15)
        self.sortcombo['values'] = ('Ascending', 'Descending')
        self.sortcombo.set('Ascending')
        self.sortcombo.grid(row=1, column=1, pady=5, padx=5)

        self.sortcombo.bind("<<ComboboxSelected>>", lambda e: self.sort())


    def add_info(self):
        try:
            id = self.id.get()
            First_name = self.fname.get()
            Last_name = self.lname.get()
            address = self.address.get()
            degree = self.degree.get()
            cont = self.Contact_number.get()

            query = 'insert into student values(%s,%s,%s,%s,%s,%s)'
            values = (id, First_name, Last_name, address, degree, cont,)
            cur.execute(query, values)
            print('1 row inserted')
            con.commit()
            self.show()
            self.clear()
        except ValueError as err:
            print(err)

    def show(self):
        query='select * from student'
        cur.execute(query)
        rows=cur.fetchall()

        if len(rows)!=0:
            self.table.delete(*self.table.get_children())

        for row in rows:
            self.table.insert('',END,values=row)


    def clear(self):
        self.id.delete(0,END)
        self.fname.delete(0,END)
        self.lname.delete(0,END)
        self.address.delete(0,END)
        self.degree.delete(0,END)
        self.Contact_number.delete(0, END)

    def bubbleSort(self, arr):
        n = len(arr)

        if self.sortcombo.get() == "Ascending":
            # Traverse through all array elements
            for i in range(n):

                # Last i elements are already in place
                for j in range(0, n - i - 1):

                    # traverse the array from 0 to n-i-1
                    # Swap if the element found is greater
                    # than the next element
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
        else:
            # Traverse through all array elements
            for i in range(n):

                # Last i elements are already in place
                for j in range(0, n - i - 1):

                    # traverse the array from 0 to n-i-1
                    # Swap if the element found is greater
                    # than the next element
                    if arr[j] < arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]

        return arr

    def sort(self):
        query = 'select * from student'
        cur.execute(query)
        rows = cur.fetchall()

        self.bubbleSort(rows)




        self.table.delete(*self.table.get_children())

        for row in rows:
            self.table.insert('', END, values=row)

    def update(self):
        id = self.id.get()
        First_name = self.fname.get()
        Last_name = self.lname.get()
        address = self.address.get()
        degree = self.degree.get()
        cont = self.Contact_number.get()
        query = 'update student set First_name=%s,Last_name=%s,Address=%s,Degree=%s,contact_number=%s where id=%s'
        values = (First_name, Last_name, address, degree, cont, id)
        cur.execute(query, values)
        con.commit()
        self.clear()
        self.show()


    def pointer(self,event):
        try:
            point = self.table.focus()
            content = self.table.item(point)
            row = content['values']
            self.clear()
            self.id.insert(0, row[0])
            self.fname.insert(0, row[1])
            self.lname.insert(0, row[2])
            self.address.insert(0, row[3])
            self.Contact_number.insert(0, row[5])
            self.degree.insert(0, row[4])
        except IndexError:
            pass


    def delete(self):
        selected_item = self.table.selection()
        self.table.delete(selected_item)

        fname = self.fname.get()
        query = 'delete from student where First_name=%s'
        values=(fname,)
        cur.execute(query,values)
        con.commit()
        self.clear()
        #self.show()


    def search(self, mylist=None):
        if not mylist:
            query = 'select * from student'
            cur.execute(query)
            rows = cur.fetchall()
        else:
            rows = mylist
        found = []
        target = self.searchentry.get()
        for value in rows:
            if target in value:
                found.append(value)

        self.table.delete(*self.table.get_children())

        for row in found:
            self.table.insert('',END,values=row)

        return found


if __name__ == '__main__':
    root = Tk()
    root.geometry('1000x1000+1+1')
    root.title('Student Management Form')
    root.configure(bg='light green')
    gui = Std_information(root)
    root.mainloop()