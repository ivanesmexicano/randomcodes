# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 15:57:17 2022

@author: Ivan Tonatiuh
"""

from rembg import remove
from PIL import Image
import PIL.Image
if not hasattr(PIL.Image, 'Resampling'):  # Pillow<9.0
    PIL.Image.Resampling = PIL.Image
# Now PIL.Image.Resampling.BICUBIC is always recognized.
  
input_path= 'cl.jpg'
output_path='output.png'
input= Image.open(input_path)
output=remove(input)

output.save(output_path)

