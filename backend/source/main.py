from fastapi import FastAPI

from api.hello_world.router import router as hello_world_router

app = FastAPI()

# App routing
app_routes = [
    hello_world_router,
]

for route in app_routes:
    app.include_router(route)