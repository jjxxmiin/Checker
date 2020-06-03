import sys
import datetime
import requests
from thermal import Thermal_CAM
from multiprocessing import Process, Queue
from threading import Thread

URL = ''


def input_barcode(): 
    while True:
        barcode = input("Barcode : ")
        
        print(f"Your Barcode : {barcode}")

        now = datetime.datetime.now()
        now_timestamp = now.timestamp()

        param = {'timestamp': now_timestamp, 'code': barcode, 'location': 1}

        response = requests.get(URL, param)

        print(response)


if __name__ == "__main__":
    cam = Thermal_CAM()
    cam.cam_setting()

    th1 = Thread(target=input_barcode)
    th1.start()

    while True:
        cam.show()
