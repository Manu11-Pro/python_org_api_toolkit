from fastapi import FastAPI
from src.api_toolkit.api_fetch.latest_version_fetch import get_py_latest_version
from src.api_toolkit.api_fetch.news_and_blogs_fetch import get_py_news_and_blogs
from src.api_toolkit.api_fetch.jobs_fetch import get_py_jobs
from src.api_toolkit.api_fetch.feedback_fetch import FeedBackdata, feedback

app = FastAPI(title="Python.org API Toolkit")

@app.get("/")
def home():
    return {
        "Message": "Welcome to the Python.org API Toolkit",
        "Endpoints": ["/py_latest_version", "/py_news_and_blogs", "/py_jobs"],
        "": ["/feedback"],
        "Docs": "/docs"
    }

@app.get("/py_latest_version")
def read_py_latest_version():
    return get_py_latest_version()

@app.get("/py_news_and_blogs")
def read_py_news_and_blogs():
    return get_py_news_and_blogs()

@app.get("/py_jobs")
def read_py_jobs():
    return get_py_jobs()

@app.post("/feedback")
def send_feedback(data: FeedBackdata):
    return feedback(data)