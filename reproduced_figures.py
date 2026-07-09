import numpy as np
import matplotlib.pyplot as plt
from pbh import *

z_grid = np.logspace(np.log10(30), 5, 1000)
fig_masses = [1, 1e2, 1e4]

def figure6():
    plt.figure(figsize=(6.5, 4.8)); vrel = v_rel_eff(z_grid)
    for M in fig_masses:
        yc = epsilon_over_mdot(M, z_grid, "collisional", vrel)
        yp = epsilon_over_mdot(M, z_grid, "photoionization", vrel)
        zp, yp = stop_photo(z_grid, yp, yc)
        line, = plt.plot(z_grid, yc, label=mass_labels[M])
        plt.plot(zp, yp, "--", color=line.get_color())
    setup("YAH'17 Figure 6", r"$\epsilon/\dot m$", (50, 2e4), (1e-7, 3e-3))

def figure7():
    plt.figure(figsize=(6.5, 4.8))
    plt.plot(z_grid, v_B(z_grid)/1e3, ":", label=r"$v_B$")
    plt.plot(z_grid, v_L_rms(z_grid)/1e3, "--", label=r"$\langle v_L^2\rangle^{1/2}$")
    plt.plot(z_grid, v_eff(z_grid)/1e3, label=r"$v_{\rm eff}$")
    setup("YAH'17 Figure 7", r"Velocity [km s$^{-1}$]", (50, 1e5), (3e-1, 8e1))

def figure8():
    plt.figure(figsize=(6.5, 4.8))
    for M in fig_masses:
        yc = average_L(M, z_grid, "collisional") / L_Edd(M)
        yp = average_L(M, z_grid, "photoionization") / L_Edd(M)
        zp, yp = stop_photo(z_grid, yp, yc)
        line, = plt.plot(z_grid, yc, label=mass_labels[M])
        plt.plot(zp, yp, "--", color=line.get_color())
    setup("YAH'17 Figure 8", r"$\langle L\rangle/L_{\rm Edd}$", (50, 1e5), (1e-16, 1e-2))

def figure9():
    plt.figure(figsize=(6.5, 4.8)); vrel = v_rel_eff(z_grid)
    pref = 0.07 * x_e_pbh(z_grid)/(1+x_e_pbh(z_grid)) * m_p*c**2/(k*T_cmb(z_grid))
    for M in fig_masses:
        Lc, Lp = average_L(M, z_grid, "collisional"), average_L(M, z_grid, "photoionization")
        vB, gam = v_B(z_grid, vrel), gamma(M, z_grid, vrel)
        yc = pref * Lc/L_Edd(M) * vB/c * np.sqrt(1 + gam**(2/3))
        yp = pref * Lp/L_Edd(M) * vB/c * np.sqrt(1 + gam**(2/3))
        zp, yp = stop_photo(z_grid, yp, yc)
        line, = plt.plot(z_grid, yc, label=mass_labels[M])
        plt.plot(zp, yp, "--", color=line.get_color())
    plt.axhline(1, linestyle=":", linewidth=1)
    setup("YAH'17 Figure 9", r"$\max(\dot T_{\rm Compt,L}/\dot T)$", (300, 2e4), (1e-8, 1))

def main():
    figure6()
    figure7()
    figure8()
    figure9()
    plt.show()

if __name__ == "__main__":
    main()