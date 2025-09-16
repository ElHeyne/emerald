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
def list_containers():
    try:
        containers = client.containers.list(all=True)
        
        filtered = []
        for c in containers:
            tags = c.image.tags or []
            if any(tag.startswith("itzg") for tag in tags):
                filtered.append({
                    "id": c.id,
                    "name": c.name,
                    "status": c.status,
                    "image": tags
                })
        
        return filtered
    except Exception as error:
        print("Error catching containers: ", error)