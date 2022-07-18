# Define codes
# Steven Dai Chuy
# March 15. 2021

import numpy

def removeRed(img):
  width = len(img)
  height = len(img[0])
  for x in range(width):
    for y in range(height):
      img[x][y][0] = 0
  
  return img

def getAverage(pixel):
  r = pixel[0]
  g = pixel[1]
  b = pixel[2]      

  return (r+g+b)/3.0

def greyScale(img):
  width = len(img)
  height = len(img[0])
  for x in range(width):
    for y in range(height):
      pixel = img[x][y]
      avg = getAverage(pixel)
      for rgb in range(len(img[x][y])):
        img[x][y][rgb] = avg

  return img

def flipVertical(img):
  width = len(img)
  height = len(img[0])
  new_img = numpy.zeros((width, height, 3))
  for x in range(width):
    for y in range(height):
      new_img[x][(height-1)-y] = img[x][y]

  return new_img







