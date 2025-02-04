import uvicorn
from fastapi import Depends, FastAPI

from .dependencies import get_token_header
from .internal import admin
from .routers import items, users, auth

app = FastAPI(swagger_ui_parameters={
    "syntaxHighlight.theme": "obsidian"
})


app.include_router(users.router)
app.include_router(items.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)
app.include_router(auth.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)