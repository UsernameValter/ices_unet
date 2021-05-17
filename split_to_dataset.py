from PIL import Image 
import numpy as np
import pandas as pd
from PIL import Image
from numpy import asarray
import matplotlib.pyplot as plt
from tqdm import tqdm
 
size = 64 
from PIL import Image
from numpy import asarray

# load the image
file_name = "B5"
image = Image.open(f"{file_name}.png").convert('L')
# convert image to numpy array
data = asarray(image)
print(np.shape(data))
 
tiles = [data[x:x+size, y:y+size] for x in range(0, data.shape[0]-size, 1) for y in range(0, data.shape[1]-size, 1)]

print(np.shape(tiles))
tiles = np.reshape(tiles, (-1, size*size))
size = np.shape(tiles)[0] 

many_parts = 40
if many_parts:
    for i in range(many_parts):
        train_Frame = pd.DataFrame(tiles[size//many_parts*i:size//many_parts*(i+1)]) 

        train_Frame.to_csv(f"{file_name}_Frame_{i}.csv", index=False)
        print(f"{file_name}_Frame_{i} is ready") 
        print(np.shape(train_Frame))
else:
    train_Frame = pd.DataFrame(tiles) 

    train_Frame.to_csv(f"{file_name}_Frame.csv", index=False)
    print(f"{file_name}_Frame is ready")