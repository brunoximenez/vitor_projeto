from lib_mod import plot, matrix_calculation, save_file
import numpy as np

# Roda essas duas linhas se vc quiser brincar com a parte do plot
# file = 'data.txt'
# plot(file, scale=100)

# //.......................................//
# //..........VARIAVES DE ENTRADA..........//
# //.......................................//
Kcal = 76.8  # Modulo Bulk dos minerais (calcita, dolomita, quartzo)
Kdol = 95.0
Kqtz = 37.0
Gcal = 32.0  # Modulo Shear dos minerais (calcita, dolomita, quartzo)
Gdol = 45.0
Gqtz = 45.0
Rcal = 2.71  # Densidade dos minerais (calcita, dolomita, quartzo)
Rdol = 2.85
Rqtz = 2.65


# //.......................................//
# //..........VARIAVES AUXILIARES..........//
# //.......................................//
K = np.array([Kcal, Kdol, Kqtz])  # Modulo Bulk maximo e minimo
G = np.array([Gcal, Gdol, Gqtz])
R = np.array([Rcal, Rdol, Rqtz])
prop = (['Effective bulk modulus (GPa)', 'Effective shear modulus (GPa)', 'Velocity ratio (frac)', 'Acoustic impedance (Pa.s/m)'])

KHS_M, GHS_M, VPVS_M, AI_M = matrix_calculation(K, G, R)

save_file('KHS_ternary.txt', KHS_M)
save_file('GHS_ternary.txt', GHS_M)
save_file('VPVS_ternary.txt', VPVS_M)
save_file('AI_ternary.txt', AI_M)

plot('KHS_ternary.txt', 100, 35, 95, prop[0])
plot('GHS_ternary.txt', 100, 30, 45, prop[1])
plot('VPVS_ternary.txt', 100, 1.45, 1.95, prop[2])
plot('AI_ternary.txt', 100, 16000, 21000, prop[3])