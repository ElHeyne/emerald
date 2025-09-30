from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import docker
import asyncio
import threading

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
                "short_id": c.short_id,
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

@app.get("/container/{container_id}")
def container(container_id: str):
    try:
        container = client.containers.get(container_id)
        return {
            "id": container.id,
            "short_id": container.short_id,
            "name": container.name,
            "status": container.status,
            "image": container.image.tags,
        }
    except Exception as error:
        print("Error cathing container info: ", error)

@app.post("/container/{container_id}/start")
def container_start(container_id: str):
    try:
        container = client.containers.get(container_id)
        container.start()
        print("start: ", container_id)
        data = {"status": "success", "message": "Server started", "container_name": container.name, "container_sid": container.short_id}
    except docker.errors.NotFound:
        print("Error carching container: ", error)
        data = {"status": "error", "message": "Docker Not Found"}
    except Exception as error:
        print("Error starting the container: ", error)
        data = {"status": "error", "message": "Error starting server", "container_name": container.name, "container_sid": container.short_id}
    finally:
        return data

@app.post("/container/{container_id}/stop")
def container_start(container_id: str):
    try:
        container = client.containers.get(container_id)
        container.stop()
        print("stop: ", container_id)
        data = {"status": "success", "message": "Server stopped", "container_name": container.name, "container_sid": container.short_id}
    except docker.errors.NotFound:
        print("Error carching container: ", error)
        data = {"status": "error", "message": "Docker Not Found"}
    except Exception as error:
        print("Error stopping the container: ", error)
        data = {"status": "error", "message": "Error stopping server", "container_name": container.name, "container_sid": container.short_id}
    finally:
        return data

@app.post("/container/{container_id}/restart")
def container_start(container_id: str):
    try:
        print("restart: ", container_id)
    except Exception as error:
        print("Error restarting the container: ", error)

@app.delete("/container/{container_id}")
def container_start(container_id: str):
    try:
        print("delete: ", container_id)
    except Exception as error:
        print("Error deleting the container: ", error)
    
@app.websocket("/ws")
async def docker_websocket(websocket: WebSocket):
    await websocket.accept()

    loop = asyncio.get_event_loop()

    def docker_events():
        for event in client.events(decode=True):
            status = event.get("status", "")
            if status in {"start", "stop", "restart", "die", "destroy"}:
                asyncio.run_coroutine_threadsafe(websocket.send_json(event), loop)
                print("Docker event: ", event)

    threading.Thread(target=docker_events, daemon=True).start()

    try:
        while True:
            await asyncio.sleep(1)
    except Exception as error:
        print("Websocket error / disconection: ", error)