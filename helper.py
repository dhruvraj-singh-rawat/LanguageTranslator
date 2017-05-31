## Importing the Library's
import os
import pickle
import copy
import numpy as np

CODES ={'<PAD>':0,'EOS':1,'UNK':2,'GO'+:3}

def load_data(path):
	input_file=os.path.join(path)
	with open(input_file,"r",encoding='utf-8',errors='ignore') as f:
		data=f.read()
	return data