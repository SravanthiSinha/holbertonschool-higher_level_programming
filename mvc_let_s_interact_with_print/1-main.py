import Tkinter as tk

from task_model import TaskModel
from task_view import TaskView


root = tk.Tk()
root.withdraw()
tv = TaskView(root)
tv.update_title("Finish this funny project")
root.mainloop()
