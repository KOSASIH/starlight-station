# -*- coding: utf-8 -*-

"""
Starlight Station Main Application

This is the main entry point of the Starlight Station application.
It sets up the application, loads the configuration, and starts the server.
"""

import logging
import os
import sys
from typing import Optional

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from app.config import settings
from app.controllers import user_controller, settings_controller, data_controller
from app.models import User, Settings, Data
from app.services import data_service, logging_service, notification_service
from app.utils import helpers, decorators

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set up the application
app = FastAPI(
    title="Starlight Station",
    description="A highly advanced application",
    version="1.0.0",
    contact={
        "name": "John Doe",
        "email": "john.doe@example.com",
        "url": "https://example.com",
    },
    license={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
)

# Set up the static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up the routes
@app.get("/")
async def index(request: Request):
    return JSONResponse(content={"message": "Welcome to Starlight Station"}, media_type="application/json")

@app.get("/users")
async def get_users(request: Request):
    users = user_controller.get_users()
    return JSONResponse(content={"users": users}, media_type="application/json")

@app.get("/settings")
async def get_settings(request: Request):
    settings = settings_controller.get_settings()
    return JSONResponse(content={"settings": settings}, media_type="application/json")

@app.get("/data")
async def get_data(request: Request):
    data = data_controller.get_data()
    return JSONResponse(content={"data": data}, media_type="application/json")

@app.post("/users")
async def create_user(request: Request, user: User):
    user_controller.create_user(user)
    return JSONResponse(content={"message": "User created successfully"}, media_type="application/json")

@app.put("/users/{user_id}")
async def update_user(request: Request, user_id: int, user: User):
    user_controller.update_user(user_id, user)
    return JSONResponse(content={"message": "User updated successfully"}, media_type="application/json")

@app.delete("/users/{user_id}")
async def delete_user(request: Request, user_id: int):
    user_controller.delete_user(user_id)
    return JSONResponse(content={"message": "User deleted successfully"}, media_type="application/json")

# Set up the services
data_service = data_service.DataService()
logging_service = logging_service.LoggingService()
notification_service = notification_service.NotificationService()

# Set up the event handlers
@app.on_event("startup")
async def startup_event():
    logger.info("Application started")
    data_service.start()
    logging_service.start()
    notification_service.start()

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Application stopped")
    data_service.stop()
    logging_service.stop()
    notification_service.stop()

# Run the application
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
