from pydantic import BaseModel

class FeedBackdata(BaseModel):
    username: str
    message: str

def feedback(data: FeedBackdata):
    return {"Status": "succes",
            "Note": f"Thankyou for your Feedback {data.username}!",
            "Feedback recieved": f"{data.message}"
    }