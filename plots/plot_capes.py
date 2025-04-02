import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os


def cargar_matrius(carpeta, mascara):
    arxius = ['0082.csv']
    matrius = []
    for arxiu in arxius:
        matriu = pd.read_csv(os.path.join(carpeta, arxiu), header=None).to_numpy()
        #matriu *= mascara
        matrius.append(matriu)
    matrius_np = np.array(matrius)
    return matrius_np

GM_path = '/Users/aina/Desktop/TFG/codi/data/GM'
RS_path = '/Users/aina/Desktop/TFG/codi/data/RS'
FA_path = '/Users/aina/Desktop/TFG/codi/data/FA'

mascara_GM = np.load("mascares/mascara_GM.npy")
mascara_RS = np.load("mascares/mascara_RS.npy")
mascara_FA = np.load("mascares/mascara_FA.npy")

GM = cargar_matrius(GM_path, mascara_GM)
RS = cargar_matrius(RS_path, mascara_RS)
FA = cargar_matrius(FA_path, mascara_FA)


fig, axs = plt.subplots(1, 3, figsize=(12, 4))
ims = []
ims.append(axs[0].imshow(GM[0], cmap='hot', interpolation='nearest'))
axs[0].set_title('GM')
ims.append(axs[1].imshow(FA[0], cmap='hot', interpolation='nearest'))
axs[1].set_title('FA')
ims.append(axs[2].imshow(RS[0], cmap='hot', interpolation='nearest'))
axs[2].set_title('RS')
fig.colorbar(ims[0], ax=axs, orientation='horizontal', fraction=0.05, pad=0.1)
fig.suptitle("Pacient Sa Sense Màscara", fontsize=14)
plt.savefig("plots/informe/Pacient_sa_sensemascara.png") 
plt.show()

