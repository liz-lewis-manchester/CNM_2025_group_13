import matplotlib.pyplot as plt
import os

def plot_snapshot(x, C, t, outdir="results"):
    os.makedirs(outdir, exist_ok=True)

    plt.figure()
    plt.plot(x, C)
    plt.xlabel("Distance (m)")
    plt.ylabel("Concentration (µg/m³)")
    plt.title(f"Concentration at t={t}s")
    plt.grid()
    plt.tight_layout()
    plt.savefig(f"{outdir}/snapshot_{int(t)}.png")
    plt.close()


def plot_evolution(x, C_hist, times, outdir="results"):
    os.makedirs(outdir, exist_ok=True)

    plt.figure()
    for i, t in enumerate(times):
        plt.plot(x, C_hist[i], label=f"t={t}s")

    plt.xlabel("Distance (m)")
    plt.ylabel("Concentration (µg/m³)")
    plt.title("Pollutant Transport Over Time")
    plt.grid()
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{outdir}/evolution.png")
    plt.close()
