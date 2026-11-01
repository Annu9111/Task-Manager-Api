from fastapi import FastAPI

app = FastAPI()


tasks = [
    {"id": 1, "title": "Learn FastAPI", "done": False},
    {"id": 2, "title": "Push project to GitHub", "done": True},
    {"id": 3, "title": "Build Task Manager API", "done": False},
]


@app.get("/")
def home():
    return {"message":"Hello, Task Manager!"}

@app.get("/tasks")
def get_task():
    return tasks

@app.get("/tasks/{task_id}")
def get_task(task_id:int):
    for task in tasks:
        if task["id"]==task_id:
            return task
    return {"error":"task not found"}

    