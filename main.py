import lib
import numpy as np

'''

Roda essas duas linhas se vc quiser brincar com a parte do plot
file = 'data.txt'
plot(file, scale=100)

'''
# //.......................................//
# //..........VARIAVES DE ENTRADA..........//
# //.......................................//
Kcal = 76.8  # Modulo Bulk dos minerais (calcita, dolomita, quartzo)
Kdol = 95.0
Kqtz = 37.0
Gcal = 32.0  # Modulo Shear dos minerais (calcita, dolomita, quartzo)
Gdol = 45.0
Gqtz = 45.0


# //.......................................//
# //..........VARIAVES AUXILIARES..........//
# //.......................................//
K = np.array([Kcal, Kdol, Kqtz])  # Modulo Bulk maximo e minimo
G = np.array([Gcal, Gdol, Gqtz])

KHS_M, GHS_M = lib.matrix_calculation(K, G)

lib.save_file('KHS_ternary.txt', KHS_M)
lib.save_file('GHS_ternary.txt', GHS_M)

# file, scale (x+y+z=scale), color scale min, color scale  max
lib.plot('KHS_ternary.txt', 100, 35, 95)
lib.plot('GHS_ternary.txt', 100, 32, 45)
