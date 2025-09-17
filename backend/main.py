from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import docker, json

itgzImage = 'itzg/minecraft-server'

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
def containers():
    try:
        containers = client.containers.list(all=True, filters={'ancestor': itgzImage})
        
        filtered = []
        for c in containers:
            filtered.append({
                "id": c.id,
                "name": c.name,
                "status": c.status,
                "image": c.image.tags
            })
        
        return filtered
    except Exception as error:
        print("Error catching containers: ", error)

@app.get("/containers/simple")
def containers_simple():
    try:
        running = client.containers.list(filters={'status':'running','ancestor': itgzImage})
        exited = client.containers.list(filters={'status':'exited', 'ancestor': itgzImage})
        paused = client.containers.list(filters={'status':'paused', 'ancestor': itgzImage})
        data = {
            "running": len(running),
            "exited": len(exited),
            "paused": len(paused),
        }

        return data
    except Exception as error:
        print("Error catching simple container data: ", error)