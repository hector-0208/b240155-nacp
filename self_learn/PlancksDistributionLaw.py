import matplotlib.pyplot as plt
import numpy as np

C1 = 0.371e-15  # W*m^2 
C2 = 1.439e-2   # m*K

def plancks_law(lam, T):
    # E_lambda = C1 / (lam^5 * (exp(C2 / (lam * T)) - 1))
    numerator = C1
    denominator = (lam**5) * (np.exp(C2 / (lam * T)) - 1)
    return numerator / denominator

# Wavelength range: 0.4 um to 100 um
wavelengths_um = np.linspace(0.4, 100, 1000)
wavelengths_m = wavelengths_um * 1e-6

temperatures = [500, 1000, 1500, 2000] # in K

plt.figure(figsize=(10, 6))

for T in temperatures:
    E_lambda_m = plancks_law(wavelengths_m, T)
    E_lambda_um = E_lambda_m / 1e6 
    
    plt.plot(wavelengths_um, E_lambda_um, label=f'T = {T} K', linewidth=2)

plt.title("Planck's Distribution Law", fontsize=16)
plt.xlabel(r"Wavelength, $\lambda$ ($\mu$m)", fontsize=12)
plt.ylabel(r"Monochromatic Emissive Power, $E_\lambda$ (W/m$^2 \cdot \mu$m)", fontsize=12)

plt.xlim(0, 20) 
plt.ylim(0, max(plancks_law(wavelengths_m, 2000)/1e6) * 1.1)

plt.grid(True, which="both", linestyle="--", alpha=0.6)
plt.legend(fontsize=12)
plt.tight_layout()

plt.show()
