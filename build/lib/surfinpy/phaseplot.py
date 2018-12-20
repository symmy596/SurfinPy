import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedFormatter
import matplotlib.gridspec as gridspec
from matplotlib.ticker import FormatStrFormatter
import matplotlib.ticker as ticker

def get_levels(X):

    a = np.amax(X) + 1
    b = np.amin(X) - 1
    levels = np.arange(b, a, 1)

    return levels

def get_ticks(X):

    t = np.arange(X.size)
    t = t - 0.5
    ticky = t.tolist()
    return ticky

def plot_phase(x, y, phase, t, labels, XL, YL, temperature, output):
    
    levels = get_levels(phase)
    ticky = get_ticks(t)
    t_lab = str(temperature) + " K"
    XLab = "$\Delta \mu_{" + XL + "}$" + " (eV)"
    YLab = "$\Delta \mu_{" + YL + "}$" + " (eV)"

    fig = plt.figure()
    ax = fig.add_subplot(111)
    fontsize = 10

    CM = ax.contourf(x, y, phase, levels=levels, cmap="RdBu")

    ax.set_ylabel(YLab, fontsize=14)
    ax.set_xlabel(XLab, fontsize=14)
    ax.text(0.1, 0.95, t_lab,  fontsize=15, color="white", horizontalalignment='center', verticalalignment='center', transform = ax.transAxes)
    ax.tick_params(labelsize=12)

    cbar = fig.colorbar(CM, ticks=ticky, pad=0.1)
    cbar.ax.set_yticklabels(labels)
    plt.tight_layout()
    plt.savefig(output, dpi=600)
    plt.show()
 
def plot_mu_p(x, y, phase, p1, p2, t, labels, XL, YL, temperature, output):
    
    levels = get_levels(phase)
    ticky = get_ticks(t)
    fontsize = 10
    X1Lab = "$\Delta \mu_{" + XL + "}$" + " (eV)"
    Y1Lab = "$\Delta \mu_{" + YL + "}$" + " (eV)"
    X2Lab = "Log $P_" + "{" + XL + "}$" + " 298 K (bar)"
    Y2Lab = "Log $P_" + "{" + YL + "}$" + " 298 K (bar)"
    temp = str(temperature)
    temp = temp + " K"

    fig = plt.figure(dpi=96, facecolor='#eeeeee', tight_layout=1)
    ax = fig.add_subplot(121)

    gs = gridspec.GridSpec(1, 2, width_ratios=[.95, .05] )
    ax, axR = plt.subplot(gs[0]), plt.subplot(gs[1])
    
    CM = ax.contourf(x, y, phase, levels=levels, cmap="RdBu")

    ax.set_xlabel(X1Lab, fontsize=14)
    ax.set_ylabel(Y1Lab, fontsize=14)       
    ax2 = ax.twinx()
    ax2.set_ylim(p2[0], p2[-1])
    ax2.set_ylabel(Y2Lab, fontsize=13)
    ax3 = ax.twiny()
    ax3.set_xlim(p1[0], p1[-1])
    ax3.set_xlabel(X2Lab, fontsize=12)
    ax.tick_params(labelsize=10)
    ax2.tick_params(labelsize=10)
    ax3.tick_params(labelsize=10)
    ax.text(0.13, 0.95, temp,  fontsize=15, color="white", horizontalalignment='center', 
            verticalalignment='center', transform = ax.transAxes)
    cbar = fig.colorbar(CM, extend='both', cax=axR, ticks=ticky)
    cbar.ax.set_yticklabels(labels)
    axR.set_xlabel('$H_2O$ $nm^{-2}$', fontsize=12)
    plt.savefig(output, dpi=600)
    plt.show()

def plot_pressure(x, y, phase, t, labels, XL, YL, temperature, output):
    
    levels = get_levels(phase)
    ticky = get_ticks(t)
    t_lab = str(temperature) + " K"
    XLab = "Log $P_" + "{" + XL + "}$" + " 298 K (bar)"
    YLab = "Log $P_" + "{" + YL + "}$" + " 298 K (bar)"

    fig = plt.figure()
    ax = fig.add_subplot(111)
    fontsize = 10
    rc('axes', linewidth=2) 

    CM = ax.contourf(x, y, phase, levels=levels, cmap="RdBu") 
    ax.set_ylabel(YLab, fontsize=14)
    ax.set_xlabel(XLab, fontsize=14)
    ax.text(0.1, 0.95, t_lab,  fontsize=15, color="white", horizontalalignment='center', 
            verticalalignment='center', transform = ax.transAxes)
    ax.tick_params(labelsize=12)
    cbar = fig.colorbar(CM, ticks=ticky, pad=0.1)
    cbar.ax.set_yticklabels(labels)
    plt.tight_layout()
    plt.savefig(output, dpi=600)
    plt.show()  

def tvp_plot(x, y, z, t, labels=None, output="Phase.png"):

    fig = plt.figure()
    ax = fig.add_subplot(111)
    fontsize = 10
    rc('axes', linewidth=2) 
    
    CM = ax.contourf(x, y, z, cmap="RdBu")
    ax.set_xlabel('Temperature (K)', fontsize=14, fontweight="bold")
    ax.set_ylabel("log P (bar)", fontsize=14, fontweight="bold")
    ax.axhline(y=1.01, color="black", linestyle='--', alpha=0.8)
    ax.axvline(x=298.15, color="black", linestyle='--', alpha=0.8)
    ax.tick_params(labelsize=14)
    plt.tight_layout()
    plt.savefig(output, dpi=600)
    plt.show()
    plt.close()   