import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os


def cargar_matrius(carpeta, mascara):
    arxius = ['0082.csv']
    matrius = []
    for arxiu in arxius:
        matriu = pd.read_csv(os.path.join(carpeta, arxiu), header=None).to_numpy()
        matriu *= mascara
        matrius.append(matriu)
    matrius_np = np.array(matrius)
    return matrius_np


def construccio_multilayer(GM, RS, FA):
    num_subjs = FA.shape[0]
    num_nodes = FA.shape[1]
    em = np.zeros((num_subjs, num_nodes*2, num_nodes*2), dtype=float)
    for i in range(num_subjs):
                em[i,:76,:76] = GM[i,:,:]
                em[i,76:,76:] = RS[i,:,:]
                em[i,76:,:76] = FA[i,:,:]
                em[i,:76,76:] = FA[i,:,:]
    return em


def construccio_multiplex(GM, RS, FA):
    num_subjs = FA.shape[0]
    num_nodes = FA.shape[1]
    em = np.zeros((num_subjs, num_nodes*3, num_nodes*3), dtype=float)
    diagonal = np.zeros((num_subjs, num_nodes, num_nodes), dtype=float)
    diagonal[:, np.arange(num_nodes), np.arange(num_nodes)] = 1
    for i in range(num_subjs):
                em[i,:76,:76] = GM[i,:,:]
                em[i,76:76*2,76:76*2] = FA[i,:,:]
                em[i,76*2:,76*2:] = RS[i,:,:]
                em[i,76:76*2,:76] = diagonal[i,:,:]
                em[i,76*2:,:76] = diagonal[i,:,:]
                em[i,:76,76:76*2] = diagonal[i,:,:]
                em[i,76*2:,76:76*2] = diagonal[i,:,:]
                em[i,:76,76*2:] = diagonal[i,:,:]
                em[i,76:76*2,76*2:] = diagonal[i,:,:]
    return em

def construccio_monoplex(GM, RS, FA):
    em = (GM + RS + FA) / 3
    return em

GM_path = '/Users/aina/Desktop/TFG/codi/data/GM'
RS_path = '/Users/aina/Desktop/TFG/codi/data/RS'
FA_path = '/Users/aina/Desktop/TFG/codi/data/FA'

mascara_GM = np.load("mascares/mascara_GM.npy")
mascara_RS = np.load("mascares/mascara_RS.npy")
mascara_FA = np.load("mascares/mascara_FA.npy")

GM = cargar_matrius(GM_path, mascara_GM)
RS = cargar_matrius(RS_path, mascara_RS)
FA = cargar_matrius(FA_path, mascara_FA)

multilayer = construccio_multilayer(GM, RS, FA)
multiplex = construccio_multiplex(GM, RS, FA)
monoplex = construccio_monoplex(GM, RS, FA)


fig, axs = plt.subplots(1, 3, figsize=(12, 4))
ims = []
ims.append(axs[0].imshow(multilayer[0], cmap='hot', interpolation='nearest'))
axs[0].set_title('Multilayer')
ims.append(axs[1].imshow(multiplex[0], cmap='hot', interpolation='nearest'))
axs[1].set_title('Multiplex')
ims.append(axs[2].imshow(monoplex[0], cmap='hot', interpolation='nearest'))
axs[2].set_title('Aggregated Monoplex')
fig.colorbar(ims[0], ax=axs, orientation='horizontal', fraction=0.05, pad=0.1)
fig.suptitle("Xarxes Pacient Sa amb Màscara", fontsize=14)
plt.savefig("plots/informe/xarxes_pacient_sa_ambmascara.png") 
plt.show()

