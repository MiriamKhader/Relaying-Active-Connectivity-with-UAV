""" run the mavsdk server by opening a terminal and entering this:

/home/miriam/.venvs/py39/lib/python3.9/site-packages/mavsdk/bin/mavsdk_server serial:///dev/ttyUSB0:57600

Then open a new terminal and run the virtual environment using:

source ~/.venv/py39/bin/activate py39

and run the script with

python3 scriptName.py

"""


import asyncio
from mavsdk import System
"""
drone = System()

await drone.connect(system_address="serial:///dev/ttyUSB0:57600")

print("Waiting for drone to connect...")
async for state in drone.core.connection_state():
    if state.is_connected:
        print(f"-- Connected to drone!")
        break

print("-- Arming")
await drone.action.arm()

print("-- Taking off")
await drone.action.takeoff()

await asyncio.sleep(10)

await drone.action.land()


"""

async def run():
    drone = System()
    # change port according to the port the telemetry radio has on laptop
    await drone.connect(system_address="serial:///dev/ttyUSB0:57600")

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"-- Connected to drone!")
            break

    print("-- Arming")
    await drone.action.arm()

    print("-- Taking off")
    await drone.action.takeoff()

    await asyncio.sleep(5)

    print("-- Landing")
    await drone.action.land()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())

