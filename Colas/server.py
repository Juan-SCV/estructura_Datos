from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from paquete.cola import Cola

class Item(BaseModel):
    nombre: str
    productos: List[str]

app = FastAPI()
cola = Cola()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/estado")
def estado():
    elementos = cola.contar()
    return {"status": "ok", "elementos": elementos}

@app.post("/encolar")
def encolar(item: dict):
    cola.encolar(item)
    return {"status": "ok"}

@app.get("/desencolar")
def desencolar():
    elemento = cola.desencolar()
    return {"status": "ok", "elemento": elemento}

@app.get("/ver_todos")
def ver_todos():
    elementos = cola.ver_listado()
    return {"status": "ok", "elementos": elementos}

@app.get("/ver_primero")
def ver_primero():
    elemento = cola.ver_primero()
    if elemento:
        return {"status": "ok", "elemento": elemento}    


@app.get("/ver_ultimo")
def ver_ultimo():
    elemento = cola.ver_ultimo()
    if elemento:
        return {"status": "ok", "elemento": elemento}

@app.get("/cancelar_pedido/{mensaje_id}")
def cancelar_pedido(mensaje_id: int):
    elemento = cola.desencolar_id(mensaje_id)
    if elemento is not None:
        return {"status": "ok", "message_id": mensaje_id, "message": "Pedido cancelado"}
    else:
        return {"status": "error", "message_id": mensaje_id, "message": "Pedido no encontrado"}
