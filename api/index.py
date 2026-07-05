from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

# Serve your HTML file
@app.get("/")
async def read_index():
    return FileResponse('public/index.html')

# This is where you would put your AI logic if you decide to use an API
