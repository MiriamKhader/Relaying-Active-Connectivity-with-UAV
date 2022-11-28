import time as time

import flight
import readRSSI
from datetime import datetime
import asyncio
from mavsdk import System

port = "/dev/ttyACM0"
running = True
with open("/home/miriam/Relaying-Active-Connectivity-with-UAV/rssi5.csv", "w") as csvFile:
    while running:
        rssi = readRSSI.RSSI(port)

        #print(rsswith open("/home/miriam/Desktop/rssis.csv", "w") as csvFile:i)

        rssiSplit = rssi.split(",")
        if len(rssiSplit) > 1:
            value = int(rssiSplit[4][5:])
            print(value)
            curr_time = datetime.now().strftime("%S")
            print(curr_time)
            csvFile.write('{}'.format(value))
            csvFile.write('{}'.format(", "))
            csvFile.write('{}'.format(curr_time))
            csvFile.write('{}'.format('\n'))

        """
        if value < -80:
            print("flying")
            
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

                await asyncio.sleep(10)

                print("-- Landing")
                await drone.action.land()


            if __name__ == "__main__":
                loop = asyncio.get_event_loop()
                loop.run_until_complete(run())
            """
   # running = False


