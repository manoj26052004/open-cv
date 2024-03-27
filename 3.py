import cv2
import numpy as np

image = cv2.imread(r"C:\Users\sanja\OneDrive\Pictures\anime.jpg")


edges = cv2.Canny(image, threshold1=100, threshold2=200)

cv2.imshow('Original Image', image)
cv2.imshow('Canny Edges', edges)

