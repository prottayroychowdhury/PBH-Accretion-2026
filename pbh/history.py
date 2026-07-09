import numpy as np
from pathlib import Path
from .constants import rho_crit0, omega_b, omega_rad, c, T0, H0, omega_m, omega_lambda

_data_loaded = False
z_hyrec = xe_hyrec = Tb_hyrec = None
z_hyrec_max = xe_hyrec_max = Tb_hyrec_max = None


def load_history(path=None):
    global _data_loaded, z_hyrec, xe_hyrec, Tb_hyrec, z_hyrec_max, xe_hyrec_max, Tb_hyrec_max
    if path is None:
        root = Path(__file__).resolve().parents[1]
        candidates = [root / "output_xe.dat", root / "output.dat", Path.cwd() / "output_xe.dat", Path.cwd() / "output.dat"]
        path = next((p for p in candidates if p.exists()), None)
        if path is None:
            raise FileNotFoundError("Put output_xe.dat or output.dat in the project folder, or pass load_history(path).")
    data = np.loadtxt(path)
    z, xe, Tb = data[:, 0], data[:, 1], data[:, 2]
    if z[0] > z[-1]: z, xe, Tb = z[::-1], xe[::-1], Tb[::-1]
    z_hyrec, xe_hyrec, Tb_hyrec = z, xe, Tb
    z_hyrec_max, xe_hyrec_max, Tb_hyrec_max = z[-1], xe[-1], Tb[-1]
    _data_loaded = True
    return z_hyrec, xe_hyrec, Tb_hyrec


def _ensure_history():
    if not _data_loaded: load_history()


def x_e(z):
    _ensure_history(); z = np.asarray(z); xe = np.interp(z, z_hyrec, xe_hyrec)
    return np.where(z > z_hyrec_max, xe_hyrec_max, xe)


def x_e_pbh(z):
    return np.minimum(x_e(z), 1.0)


def T_b(z):
    _ensure_history(); z = np.asarray(z); Tb = np.interp(z, z_hyrec, Tb_hyrec)
    Tb_high = Tb_hyrec_max * (1 + z) / (1 + z_hyrec_max)
    return np.where(z > z_hyrec_max, Tb_high, Tb)


def T_cmb(z): return T0 * (1 + z)
def rho_cmb(z): return rho_crit0 * omega_rad * c**2 * (1 + z)**4
def rho_b(z): return rho_crit0 * omega_b * (1 + z)**3
def Hubble(z): return H0 * np.sqrt(omega_rad*(1+z)**4 + omega_m*(1+z)**3 + omega_lambda)
