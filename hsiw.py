import numpy as np
import os
os.system('clear')
gt = [77,101,114,114,121,32,67,104,114,105,115,116,109,97,115]
text = np.random.rand(15)*120
while np.sum(np.square(text-gt))>1e-5:
    text -= 1e-2*(text-gt)
print(''.join(chr(int(i)) for i in np.round(text)))
