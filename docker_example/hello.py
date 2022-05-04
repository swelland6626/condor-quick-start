import sys,os
import imageio
import numpy as np

image_path = sys.argv[1]
output_path = sys.argv[2]

os.makedirs(os.path.dirname(os.path.abspath(output_path)),exist_ok=True)

a = imageio.imread(image_path)

with open(output_path,'w') as f:
    f.write(str(np.sum(a))+'\n')
