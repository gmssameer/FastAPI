from fastapi import APIRouter,HTTPException,Depends,Request
from fastapi.security import APIKeyHeader
from starlette.authentication import requires

from app.todos import Priority, Todo, Todo_DB

from pydantic import BaseModel


todo_db = Todo_DB()
todo:Todo = Todo(id=1,title="Learn FastAPI",is_done=True,priority=Priority.HIGH)
todo_db.add(todo)



router = APIRouter(
    prefix="/todos",
)

header_scheme = APIKeyHeader(name="Authorization")


@router.get("/")
@requires("authenticated",status_code=404)
def getAllList(request: Request,first_n: int = None) :
    if first_n is None:
        return todo_db.get_all()
    else:
        return todo_db.get_all(first_n)


@router.get("/{todo_id}")
def getTodoById(todo_id: int):
    todo = todo_db.get(todo_id)
    if todo:
        return todo
    raise HTTPException(status_code=404, detail="Todo not found")


class CreateTodo(BaseModel):
    title: str
    is_done: bool = False
    priority: int|None = None


def getPriority (priority_int:int) -> Priority:
    match priority_int:
        case 1:
            priority = Priority.HIGH
        case 2:
            priority = Priority.MEDIUM
        case 3:
            priority = Priority.LOW
        case _:
            priority = Priority.LOW
    return priority


@router.post("/")
def createTodo(todo_obj: CreateTodo):
    new_id = max([todo.id for todo in todo_db.todos]) + 1
    priority = getPriority(todo_obj.priority)
    new_todo = Todo(id=new_id, title=todo_obj.title, is_done=todo_obj.is_done, priority=priority)
    todo_db.add(new_todo)
    return new_todo


class EditTodo(BaseModel):
    title: str|None =None
    priority: int|None = None


@router.put("/{todo_id}")
def editTodo(todo_id:int ,edit_todo: EditTodo):
    if edit_todo.priority is not None:
        priority = getPriority(edit_todo.priority)
    else:
        priority = None
    todo = todo_db.edit(todo_id,edit_todo.title,priority) 
    if todo:
        return todo
    raise HTTPException(status_code=404, detail="Todo not found")


@router.patch("/{todo_id}")
def toggleTodoList(todo_id: int):
    todo = todo_db.toggle(todo_id)
    if todo:
        return todo
    raise HTTPException(status_code=404, detail="Todo not found")

@router.delete("/{todo_id}")
def deleteTodoList(todo_id: int):
    todo = todo_db.delete(todo_id)
    if todo:
        return todo
    raise HTTPException(status_code=404, detail="Todo not found")