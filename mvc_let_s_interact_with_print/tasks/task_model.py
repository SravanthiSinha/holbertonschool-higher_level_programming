import json

class TaskModel:

    #COnstructor
    def __init__(self, title):
        if title == '' or type(title) is not str:
            raise Exception("title is not a string")
        self.filename = 'tasks.json'

        self.__title = title
        self.__callback_title = None
        self.__callback_add_task = None
        self.__task = None
        self.__tasks = []
        try:
            with open(self.filename, 'r') as f:
                self.deserialize_tasks()
        except:
            pass
    
        
    def __str__(self):
        return str(self.__title)

    #Getter/Setter
    def get_title(self):
        return self.__title

    def set_callback_title(self,title):
        self.__callback_title = title

    def toggle(self):
        self.__title = self.__title[::-1]
        if self.__callback_title:
            self.__callback_title(self.__title)
            
    def get_tasks(self):
        return self.__tasks

    def set_callback_add_task(self,task):
        self.__callback_add_task = task

    def add_task(self,task):
        self.__tasks.append(task)
        self.__task = task
        self.serialize_tasks()
        if self.__callback_add_task:
            self.__callback_add_task(self.__task)

    def remove_task(self,task):
        self.__tasks.pop(task)
        self.serialize_tasks()

    def serialize_tasks(self):
        with open(self.filename, 'w') as f:
            f.write(json.dumps(self.__tasks))

    def deserialize_tasks(self):
        with open(self.filename, 'r') as f:
            self.__tasks = json.load(f)

