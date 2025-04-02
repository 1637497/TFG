
import numpy as np
import pandas as pd

pacients = pd.read_csv('/Users/aina/Desktop/TFG/codi/data/demographics.csv')

multilayer = pacients['mstype'].to_numpy()
multilayer = np.tile(multilayer, 2)
multiplex = pacients['mstype'].to_numpy()
multiplex = np.tile(multiplex, 3)
monoplex = pacients['mstype'].to_numpy()

print(multilayer.shape)
print(multiplex.shape)
print(monoplex.shape)

np.save("etiquetes/etiquetes_multilayer.npy", multilayer)
np.save("etiquetes/multiplex.npy", multiplex)
np.save("etiquetes/monoplx.npy", monoplex)
