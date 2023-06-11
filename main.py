from fastapi import FastAPI
import models
from database import engine
from router import employee

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(employee.router)









