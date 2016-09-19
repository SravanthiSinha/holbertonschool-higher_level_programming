import Tkinter as tk
from Tkinter import *

class TaskView(tk.Toplevel):

    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.protocol('WM_DELETE_WINDOW', self.master.destroy)

        if not isinstance(master, tk.Tk):
            raise Exception("master is not a tk.Tk()")

        self.listbox = tk.Listbox(self)

        self.__title_var = tk.StringVar()
        self.__title_label = tk.Label(self, textvariable=self.__title_var)
        self.toggle_button = tk.Button(self, text="Reverse")
        
        self.toggle_button.pack(fill=X)
        self.__title_label.pack(fill=X)
        
        self.__L1 = tk.Label(self, text="Add task")
        self.__L1.pack(fill=X)

        self.__task = StringVar()
        self.add_entry = tk.Entry(self,textvariable=self.__task)
        self.add_entry.pack(fill=X)
        
        self.listbox.pack(fill=BOTH)

        self.remove_button = tk.Button(self, text="Remove Task")
        self.remove_button.pack(fill=X)
        self.__callback_add_task = None
        self.__callback_remove_task = None

    def update_title(self, title):
        if not isinstance(title, str):
            raise Exception("title is not a string")
        self.__title_var.set(title)
        
    def display_tasks(self,items):
        if items:
            for item in items:
                self.listbox.insert(END, item)

    def set_task(self,*args):
        self.__task.set(self.add_entry.get())
        if self.__callback_add_task:
            self.__callback_add_task(self.__task.get())
        
    def add_task(self,task):
        self.listbox.insert(END, task)
        self.listbox.pack(fill=BOTH)

    def set_callback_add_task(self,task):
        self.__callback_add_task = task
        
    def set_callback_remove_task(self,index):
        self.__callback_remove_task = index
        
    def remove_task(self):
        indexes = list(self.listbox.curselection())
        indexes.sort(reverse=True)
        for index in indexes:
            self.listbox.delete(index)
        self.listbox.pack(fill=BOTH)
        if self.__callback_remove_task:
            self.__callback_remove_task(index)
        
        
        
       
       
