import matplotlib.pyplot as plt
import figures
import self_consistent
import expansion_check

figures.figure6(); figures.figure7(); figures.figure8(); figures.figure9()
self_consistent.plot_luminosity_vs_z(); self_consistent.plot_Meff_ratio_vs_z()
expansion_check.plot_tB_H()
plt.show()
