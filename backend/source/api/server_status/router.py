import time
from fastapi import APIRouter, BackgroundTasks

router = APIRouter(
    prefix="/server-status",
    tags=["server-status"],
)

@router.get("/")
def server_status():
    return {"endpoint_name":"server-status"}

@router.get("/temperature")
async def server_temperature(background_tasks: BackgroundTasks):
    def get_server_temperature():
        time.sleep(5)
        temperature_info = {"PC1":"hot", "PC2":"cold", "PC3":"unavailable"}
        print(temperature_info)
        return temperature_info

    background_tasks.add_task(get_server_temperature)
    return {"msg": "Task recieved for temperature fetching"}