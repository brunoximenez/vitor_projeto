import ternary
import numpy as np


def save_file(file_name, data):
    file = open(file_name, 'w+')
    np.savetxt(file_name, data, fmt="%2.3f")
    # with open(file_name, 'w') as f:
    #     for line in data:
    #         print line
    #         np.savetxt(f, line, fmt='%.2f')
    file.close()


def matrix_calculation(K, G, R):
    auxKmax = 4 * np.amax(G) / 3
    auxKmin = 4 * np.amin(G) / 3
    auxGmax = (np.amax(G) / 6) * ((9 * np.amax(K)) + (8 * np.amax(G))) / (np.amax(K) + (2 * np.amax(G)))
    auxGmin = (np.amin(G) / 6) * ((9 * np.amin(K)) + (8 * np.amin(G))) / (np.amin(K) + (2 * np.amin(G)))

    RHO = np.array([])
    KHSsup = np.array([])
    KHSinf = np.array([])
    GHSsup = np.array([])
    GHSinf = np.array([])
    KHS = np.array([])
    GHS = np.array([])
    M = np.array([])
    imax = 100
    for i in range(0, imax, 1):  # i = concentracao do mineral calcita em % (for nao aceita i float)
        jmax = imax - i
        for j in range(0, jmax, 1):  # j = concentracao do mineral dolomita
            k = 1 - i * 1e-2 - j * 1e-2  # k = concentracao mineral quartzo
            a = np.array([i, j, k * 1e2])
            if len(M) == 0:
                M = np.array(a)  # concentration in %
            else:
                M = np.vstack((M, a))  # concentration in %
            # Limite superior de Hashin-Shtrikman para o modulo bulk
            x = -auxKmax + 1 / ((i * 1e-2 / (K[0] + auxKmax)) + (j * 1e-2 / (K[1] + auxKmax)) + (k / (K[2] + auxKmax)))
            KHSsup = np.append(KHSsup, x)
            # Limite inferior de Hashin-Shtrikman para o modulo bulk
            x = -auxKmin + 1 / ((i * 1e-2 / (K[0] + auxKmin)) + (j * 1e-2 / (K[1] + auxKmin)) + (k / (K[2] + auxKmin)))
            KHSinf = np.append(KHSinf, x)
            # Limite superior de Hashin-Shtrikman para o modulo shear
            x = -auxGmax + 1 / ((i * 1e-2 / (G[0] + auxGmax)) + (j * 1e-2 / (G[1] + auxGmax)) + (k / (G[2] + auxGmax)))
            GHSsup = np.append(GHSsup, x)
            # Limite inferior de Hashin-Shtrikman para o modulo shear
            x = -auxGmin + 1 / ((i * 1e-2 / (G[0] + auxGmin)) + (j * 1e-2 / (G[1] + auxGmin)) + (k / (G[2] + auxGmin)))
            GHSinf = np.append(GHSinf, x)
            # Densidade
            x = (R[0] * i * 1e-2) + (R[1] * j * 1e-2) + (R[2] * k)
            RHO = np.append(RHO, x)

    KHS = (KHSinf + KHSsup) / 2
    GHS = (GHSinf + GHSsup) / 2
    VPVS = np.sqrt(((KHS / GHS) + (4 / 3)))
    AI = RHO * np.sqrt(((KHS * 1e+9 + (4 * GHS * 1e+9 / 3)) / (1000 * RHO)))
    RHO = np.vstack(RHO)
    KHS = np.vstack(KHS)
    GHS = np.vstack(GHS)
    VPVS = np.vstack(VPVS)
    AI = np.vstack(AI)
    RHO_M = np.append(M, RHO, axis=1)
    KHS_M = np.append(M, KHS, axis=1)
    GHS_M = np.append(M, GHS, axis=1)
    VPVS_M = np.append(M, VPVS, axis=1)
    AI_M = np.append(M, AI, axis=1)
    return KHS_M, GHS_M, VPVS_M, AI_M, RHO_M


def plot(file, scale, vmin, vmax, prop):
    ## Boundary and Gridlines
    figure, tax = ternary.figure(scale=scale)
    tax.ax.axis("off")
    figure.set_facecolor('w')
    # Draw Boundary and Gridlines
    tax.boundary(linewidth=1.0)
    tax.gridlines(color="black", multiple=scale / 10, linewidth=0.1, ls='-')

    # Set Axis labels and Title
    fontsize = 15
    tax.left_axis_label("          Calcite (%)", fontsize=fontsize, offset=0.15)
    tax.right_axis_label("Dolomite (%)        ", fontsize=fontsize, offset=0.15)
    tax.bottom_axis_label("   Quartz (%)", fontsize=fontsize, offset=0.09)

    # Set ticks
    tax.ticks(axis='brl', linewidth=1, multiple=scale / 10, offset=0.025)

    # Scatter some points
    # file = 'data.txt'
    data = np.loadtxt(file, usecols=[0, 1, 2])
    c = np.loadtxt(file, usecols=[3])

    cb_kwargs = {"shrink": 0.8,
                 "orientation": "horizontal",
                 "fraction": 0.1,
                 "pad": 0.05,
                 "aspect": 15}

    tax.scatter(data, marker='o', c=c, edgecolor='k', s=scale / 4, linewidths=0.0,
                vmin=vmin, vmax=vmax, colorbar=True, colormap='jet', cbarlabel=prop,
                cb_kwargs=cb_kwargs, zorder=0)
    
    tax._redraw_labels()
    ternary.plt.show()
    return 0
