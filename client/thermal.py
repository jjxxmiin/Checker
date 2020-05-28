from Adafruit_AMG88xx import Adafruit_AMG88xx
import pygame
import os
import math
import time

import numpy as np
from scipy.interpolate import griddata

from colour import Color


class Thermal_CAM(object):
	def __init__(self, min_temp=26, max_temp=32, color_depth=1024):
		self.min_temp = min_temp # low range of the sensor (this will be blue on the screen)
		self.max_temp = max_temp # high range of the sensor (this will be red on the screen)
		self.color_depth = color_depth
		
		os.putenv('SDL_FBDEV', '/dev/fb1')
		
		
		
if __name__ == "__main__":
	cam = Thermal_CAM()
