import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def positius():
    pacients = pd.read_csv('/Users/aina/Desktop/TFG/codi/data/demographics.csv')
    pacients_zero = pacients[pacients["mstype"] >= 0]["ID"].astype(str).str.zfill(4).tolist()
    return pacients_zero


def negatius():
    pacients = pd.read_csv('/Users/aina/Desktop/TFG/codi/data/demographics.csv')
    pacients_zero = pacients[pacients["mstype"] < 0]["ID"].astype(str).str.zfill(4).tolist()
    return pacients_zero


def mitjana_xarxes(path, pacients_zero, mascara):
    matriu = np.zeros((76,76), dtype=float)
    for pacient in os.listdir(path):
        if pacient[:4] in pacients_zero:
            mat = pd.read_csv(os.path.join(path, pacient), header=None).to_numpy() 
            mat *= mascara
            matriu += mat
    matriu /= len(pacients_zero)
    return matriu


GM_path = '/Users/aina/Desktop/TFG/codi/data/GM'
RS_path = '/Users/aina/Desktop/TFG/codi/data/RS'
FA_path = '/Users/aina/Desktop/TFG/codi/data/FA'
mascara_GM = np.load("mascares/mascara_GM.npy")
mascara_RS = np.load("mascares/mascara_RS.npy")
mascara_FA = np.load("mascares/mascara_FA.npy")

pacients_zero = positius()
paceints_un = negatius()

gm_xarxa_zero = mitjana_xarxes(GM_path, pacients_zero, mascara_GM)
rs_xarxa_zero = mitjana_xarxes(RS_path, pacients_zero, mascara_RS)
fa_xarxa_zero = mitjana_xarxes(FA_path, pacients_zero, mascara_FA)

gm_xarxa_un = mitjana_xarxes(GM_path, paceints_un, mascara_GM)
rs_xarxa_un = mitjana_xarxes(RS_path, paceints_un, mascara_RS)
fa_xarxa_un = mitjana_xarxes(FA_path, paceints_un, mascara_FA)


fig1 = plt.figure(figsize=(12, 8))
ax1 = fig1.add_subplot(131, projection='3d')
X, Y = np.meshgrid(np.arange(gm_xarxa_zero.shape[0]), np.arange(gm_xarxa_zero.shape[1]))
ax1.plot_surface(X, Y, gm_xarxa_zero, cmap='hot')
ax1.set_title('GM')

ax2 = fig1.add_subplot(132, projection='3d')
X, Y = np.meshgrid(np.arange(rs_xarxa_zero.shape[0]), np.arange(rs_xarxa_zero.shape[1]))
ax2.plot_surface(X, Y, rs_xarxa_zero, cmap='hot')
ax2.set_title('RS')

ax3 = fig1.add_subplot(133, projection='3d')
X, Y = np.meshgrid(np.arange(fa_xarxa_zero.shape[0]), np.arange(fa_xarxa_zero.shape[1]))
ax3.plot_surface(X, Y, fa_xarxa_zero, cmap='hot')
ax3.set_title('FA')

fig1.suptitle('Mitjana Pacients Malalts Amb Màscara', fontsize=16)
plt.tight_layout()
plt.savefig("mitjana_pacients_malalts_ambmamscara.png")
plt.show()



fig2 = plt.figure(figsize=(12, 8))
ax4 = fig2.add_subplot(131, projection='3d')
X, Y = np.meshgrid(np.arange(gm_xarxa_un.shape[0]), np.arange(gm_xarxa_un.shape[1]))
ax4.plot_surface(X, Y, gm_xarxa_un, cmap='hot')
ax4.set_title('GM')

ax5 = fig2.add_subplot(132, projection='3d')
X, Y = np.meshgrid(np.arange(rs_xarxa_un.shape[0]), np.arange(rs_xarxa_un.shape[1]))
ax5.plot_surface(X, Y, rs_xarxa_un, cmap='hot')
ax5.set_title('RS')

ax6 = fig2.add_subplot(133, projection='3d')
X, Y = np.meshgrid(np.arange(fa_xarxa_un.shape[0]), np.arange(fa_xarxa_un.shape[1]))
ax6.plot_surface(X, Y, fa_xarxa_un, cmap='hot')
ax6.set_title('FA')

fig2.suptitle('Mitjana Pacients Sans Amb Màscara', fontsize=16)
plt.tight_layout()
plt.savefig("mitjana_pacients_sans_ambmamscara.png")
plt.show()

