from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import docker

app = FastAPI()
client = docker.from_env()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Change to server's specific
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/containers")
def list_containers(all: bool = True):
    containers = client.containers.list(all=all)
    return [
        {
            "id": c.id,
            "name": c.name,
            "status": c.status,
            "image": c.image.tags
        }
        for c in containers
    ]