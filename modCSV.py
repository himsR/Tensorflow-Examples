import csv
import numpy
import cv2
import matplotlib.pyplot as plt
import glob
import os

b = open('test.csv', 'a')
writer = csv.writer(b)
for i in range(2000,2972):
  writer.writerows([[i,0]])

