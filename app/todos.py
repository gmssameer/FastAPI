

import datetime
from enum import IntEnum


class Priority(IntEnum):
    LOW = 3
    MEDIUM = 2
    HIGH = 1

class Todo:
    id: int
    title: str 
    priority: Priority 
    is_done: bool 
    date: datetime 

    def __init__(self,id,title,priority,is_done):
        self.id = id
        self.title = title
        self.priority = priority
        self.is_done = is_done
        self.date = datetime.datetime.now()

    def __str__(self):
        return f'{"title": {self.title}, "priority": {self.priority}, "is_done": {self.is_done}, "date": {self.date.strftime("%c")}}'

   
class Todo_DB:
    def __init__(self):
        self.todos = []
        

    def add(self,todo:Todo):
        self.todos.append(todo)
        return todo

    def get(self,todo_id:int):
        for todo in self.todos:
            if todo.id == todo_id:
                return todo
        return None

    def get_all(self,first_n=None):
        if first_n is None:
            return self.todos
        else:
            return self.todos[:first_n]

    def edit(self,todo_id,todo_title,priority):
        for todo in self.todos:
            if todo.id == todo_id:
                if todo_title is not None:
                    todo.title = todo_title
                if priority is not None:
                    todo.priority = priority
                return todo
        return None

    def toggle(self,todo_id):
        for todo in self.todos:
            if todo.id == todo_id:
                todo.is_done = not todo.is_done
                return todo
        return None

    def delete(self,todo_id):
        for i in range(len(self.todos)):
            if self.todos[i].id == todo_id:
                return self.todos.pop(i)
        return None

