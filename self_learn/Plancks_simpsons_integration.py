import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simpson

C1 = 3.742e-16  # W*m^2
C2 = 1.4388e-2  # m*K
sigma_actual = 5.67e-8 # W/(m^2 * K^4) (Stefan-Boltzmann Constant)

def plancks_law(lam, T):
    numerator = C1
    denominator = (lam**5) * (np.exp(C2 / (lam * T)) - 1)
    return numerator / denominator

# Wavelength range: 0.1 um to 1000 um
wavelengths_um = np.logspace(-1, 3, 1000) 
wavelengths_m = wavelengths_um * 1e-6

temperatures = [100, 500, 1000] # in K

plt.figure(figsize=(10, 6))

for T in temperatures:
    E_lambda_m = plancks_law(wavelengths_m, T)
    E_lambda_um = E_lambda_m / 1e6 # Convert from W/m³ to W/(m²·µm)
    plt.plot(wavelengths_um, E_lambda_um, label=f'T = {T} K', linewidth=2)

plt.title(r"Planck's Distribution Law", fontsize=16)
plt.xlabel(r"Wavelength, $\lambda$ ($\mu$m)", fontsize=12)
plt.ylabel(r"Monochromatic Emissive Power, $E_\lambda$ (W/m² · $\mu$m)", fontsize=12)

plt.xscale('log')
plt.yscale('log')
plt.xlim(0.1, 1000)
plt.ylim(1e-4, 1e5)
plt.grid(True, which="both", linestyle="--", alpha=0.6)
plt.legend(fontsize=12)
plt.tight_layout()
plt.show()

T_int = 1000 # K

# For Simpson's rule, We generate 10,001 points (an odd number)
lam_m_int = np.linspace(0.1e-6, 1000e-6, 10001) 
E_lam_int = plancks_law(lam_m_int, T_int)

# Integral of E_b(lambda) d(lambda)
K = simpson(y=E_lam_int, x=lam_m_int)

sigma_calc = K / (T_int**4)

print("Integration Range: 0.1 µm to 1000 µm")
print(f"Temperature (T): {T_int} K\n")
print(f"Calculated Total Emissive Power (K): {K:.2f} W/m²")
print(f"Calculated Stefan-Boltzmann Constant (sigma): {sigma_calc:.4e} W/(m²·K^4)")
print(f"Theoretical Stefan-Boltzmann Constant:           {sigma_actual:.4e} W/(m²·K^4)")

error = abs(sigma_calc - sigma_actual) / sigma_actual * 100
print(f"Percentage Error: {error:.4f}%")
