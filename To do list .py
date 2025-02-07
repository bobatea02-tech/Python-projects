
#create the GUI elements
import tkinter
import tkinter.messagebox
import random

#create root window
root = tkinter.Tk()

#change root window
root.config(bg='white')

#change the title
root.title('MY SUPER TO_DO_LIST')

#change the window size
root.geometry('250x275')

#create an empty list

tasks = []
#define functions

def update_listbox():
    #clear current list
    clear_listbox()
    #populate listbox
    for task in tasks:
        lb_tasks.insert('end',task)

def clear_listbox():
    lb_tasks.delete(0,'end')

def add_text():
    #get the task to add
    task = txt_input.get()
    #make sure the task is not empty
    if task != '':
    #append to the list
        tasks.append(task)
        #update the listbox
        update_listbox()
    else:
        tkinter.messagebox.showwarning("warning",'Please enter a task!!!')
    txt_input.delete(0,'end')

def delete():
    #get the text of currently selected one deleted
    task = lb_tasks.get('active')
    if task in tasks:
        tasks.remove(task)
    #update the listbox
    update_listbox()

def sort_ascen():
    #sort the list
    tasks.sort()
    #update the list
    update_listbox()

def sort_desen():
    tasks.sort()
    tasks.reverse()
    update_listbox()

def random_choose():
    task =random.choice(tasks)
    lbl_display["text"]= task

def no_of_tasks():
    number_of_tasks = len(tasks)
    msg = "Number of tasks is %s" %number_of_tasks
    #display the message
    lbl_display['text']= msg

def delete_all():
    confirmed = tkinter.messagebox.askyesno('Please confirm', "DO you really want to delete?")
    if confirmed:
        #Clear the tasks list
        global tasks
        tasks=[]
        update_listbox()
        
def quite():
    exit()
    
#GUI generations
lbl_title = tkinter.Label(root,text="TO-DO-LIST" , bg="white")
lbl_title.grid(row=0,column= 0)

lbl_display = tkinter.Label(root,text="" , bg="white")
lbl_display.grid(row=0,column=1)

txt_input = tkinter.Entry(root, width=15)
txt_input.grid(row=1,column=1)

btn_add_task = tkinter.Button(root, text="ADD TASK",fg="green",bg="white",command=add_text)
btn_add_task.grid(row=1,column=0)

btn_delete_all = tkinter.Button(root, text="DELETE ALL",fg="green",bg="white",command=delete_all)
btn_delete_all.grid(row=2,column=0)

btn_delete = tkinter.Button(root, text="DELETE",fg="green",bg="white",command=delete)
btn_delete.grid(row=3,column=0)

btn_sort_asc = tkinter.Button(root, text="SORT(ASC)",fg="green",bg="white",command=sort_ascen)
btn_sort_asc.grid(row=4,column=0)

btn_sort_desc = tkinter.Button(root, text="SORT(DESC)",fg="green",bg="white",command=sort_desen)
btn_sort_desc.grid(row=5,column=0)

btn_choose_random = tkinter.Button(root, text="RANDOM CHOOSE",fg="green",bg="white",command=random_choose)
btn_choose_random.grid(row=6,column=0)

btn_no_of_tasks = tkinter.Button(root, text="NO. OF TASK",fg="green",bg="white",command=no_of_tasks)
btn_no_of_tasks.grid(row=7,column=0)

btn_exit = tkinter.Button(root, text="EXIT",fg="green",bg="white",command=quite)
btn_exit.grid(row=8,column=0)

lb_tasks = tkinter.Listbox(root)
lb_tasks.grid(row=2,column=1, rowspan = 7)

#start the main events loop
root.mainloop()






