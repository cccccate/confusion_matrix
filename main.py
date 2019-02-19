import matrix
import numpy as np


labels = ["run", "walk", "skip", "jack", "jump","pjump","side","wave2","wave1","bend"]
data = np.array([
  [ 98,    0,      2,      0,      0,      0,    0,    0,    0,    0],
  [0,    100,      0,      0,      0,      0,    0,    0,    0,    0],
  [3,      0,     97,      0,      0,      0,    0,    0,    0,    0],
  [0,      0,      0,    100,      0,      0,    0,    0,    0,    0],
  [0,      0,      0,      0,    100,      0,    0,    0,    0,    0],
  [0,      0,      0,      0,      0,    100,    0,    0,    0,    0],
  [0,      0,      0,      0,      0,      0,  100,    0,    0,    0],
  [0,      0,      0,      0,      0,      0,    0,  100,    0,    0],
  [0,      0,      0,      0,      0,      0,    0,    0,  100,    0],
  [0,      0,      0,      0,      0,      0,    0,    0,    0,  100],
  ])

mx = matrix.Matrix(labels, data)

#Options
mx.cell_size = 25.8 #[mm]
mx.font_size = 14
mx.label_font_size = 7
mx.cell_color = "green" #black, red, yellow, green, blue, purple
mx.label_color = "black" #black, white
mx.line_type = "dot" #normal, dot
mx.percentage = False

mx.draw()