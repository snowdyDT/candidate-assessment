import uvicorn
from fastapi import FastAPI

from candidate_assessment import routes

app = FastAPI()
app.include_router(routes.router)

if __name__ == "__main__":
    uvicorn.run(app=app, host="localhost", port=8000)
