from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from agents.planner import create_plan
from agents.executor import execute_plan
from agents.verifier import verify_and_format

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/run")
def run_task(query: str):
    plan = create_plan(query)
    results = execute_plan(plan)
    final_output = verify_and_format(results)
    return final_output
