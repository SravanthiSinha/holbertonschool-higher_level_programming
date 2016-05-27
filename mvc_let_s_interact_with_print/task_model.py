class TaskModel:

    #COnstructor
    def __init__(self, title):
        if title == '' or type(title) is not str:
            raise Exception("title is not a string")
        self.__title = title
        self.__callback_title = None


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
