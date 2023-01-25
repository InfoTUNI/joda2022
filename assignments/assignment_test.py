import pickle
import pandas as pd

df = pickle.load(open('out.pkl', mode='rb'))

print(len(df)==3)