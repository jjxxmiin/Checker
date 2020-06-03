from Adafruit_AMG88xx import Adafruit_AMG88xx
import pygame
import os
import math
import time

import numpy as np
from scipy.interpolate import griddata

from colour import Color

NX = 8
NY = 8


def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))


def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


class Thermal_CAM(object):
        def __init__(self, min_temp=26, max_temp=32, color_depth=1024):
            self.sensor = Adafruit_AMG88xx()

        def cam_setting(self, min_temp=26, max_temp=32, color_depth=1024):
            self.min_temp = min_temp
            self.max_temp = max_temp
            self.color_depth = color_depth

            os.putenv('SDL_FBDEV', '/dev/fb1')
            
            self.points = [(math.floor(i / NX), (i % NY)) for i in range(0, NX * NY)]
            self.grid_x, self.grid_y = np.mgrid[0:NX-1:32j, 0:NY-1:32j]
            
            blue = Color("Indigo")
            colors = list(blue.range_to(Color("red"), self.color_depth))
            
            self.colors = [(int(c.red * 255), int(c.green * 255), int(c.blue * 255)) for c in colors]

            self.lcd = pygame.display.set_mode((NX * 30, NY * 30))
            self.lcd.fill((255,0,0))

            pygame.display.update()
            pygame.mouse.set_visible(False)

            self.lcd.fill((0,0,0))
            
        def show(self):
            pixels = self.sensor.readPixels()
            pixels = [map(p, self.min_temp, self.max_temp, 0, self.color_depth - 1) for p in pixels]

            bicubic = griddata(self.points, pixels, (self.grid_x, self.grid_y), method='cubic')

            for ix, row in enumerate(bicubic):
                for jx, pixel in enumerate(row):
                    pygame.draw.rect(self.lcd, self.colors[constrain(int(pixel), 0, self.color_depth - 1)], (NY * ix, NX * jx, NY, NX))

            pygame.display.update()
	
        def get_thermistor(self):
            return self.sensor.readThermistor()

        def get_pixels(self):
            return self.sensor.readPixels()

if __name__ == "__main__":
        cam = Thermal_CAM()

        print(f"Thermistor : {cam.get_thermistor()}") 
        print(f"MAX Pixel : {max(cam.get_pixels())}")
        print(f"MIN Pixel : {min(cam.get_pixels())}")

