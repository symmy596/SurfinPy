import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from surfinpy import utils as ut
from surfinpy import _fig_params
from matplotlib.colors import ListedColormap, BoundaryNorm
import numpy as np

class ChemicalPotentialPlot:
    """Class that plots a phase diagram as a function of chemical potential.

    Parameters
    ----------
    x : :py:attr:`array_like`
        x axis, chemical potential of species x
    y : :py:attr:`array_like`
        y axis, chemical potential of species y
    z : :py:attr:`array_like`
        two dimensional grid, phase info
    labels : :py:attr:`list`
        :py:attr:`list`): of phase labels
    ticks : :py:attr:`list`
        :py:attr:`list`): of phases
    colors : :py:attr:`list`
        :py:attr:`list`): of phases       
    xlabel : :py:attr:`str`
        species name for x axis label
    ylabel : :py:attr:`str`
        species name for y axis label
    """
    def __init__(self, 
                 x,
                 y,
                 z,
                 labels,
                 ticks,
                 colors,
                 xlabel,
                 ylabel):
        self.x = x
        self.y = y
        self.z = z
        self.labels = labels
        self.ticks = ticks
        self.colors = colors
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.levels = ut.get_levels(self.z)
        self.ticky = ut.get_ticks(self.ticks)
        if colors:
            self.cmap = ListedColormap(self.colors)
        else:
            self.cmap = "viridis"

    def plot_phase(self,
                   temperature=None,
                   colourmap=None,
                   set_style=None, 
                   figsize=None):
        """Plots a simple phase diagram as a function of chemical potential.

        Parameters
        ----------
        temperature: :py:attr:`int`
            Temperature. 
        colourmap: :py:attr:`str`
            Colourmap for the plot.
        set_style: :py:attr:`str`
            Plot style
        figsize: :py:attr:`tuple`
            Set a custom figure size.
        """
        if set_style:
            plt.style.use(set_style)
        if colourmap:
            self.cmap = colourmap
        fig = plt.figure(figsize=figsize)
        ax = fig.add_subplot(111)
        CM = ax.contourf(self.x, self.y, self.z, levels=self.levels, cmap=self.cmap)
        ax.set_ylabel("$\Delta \mu_{\mathrm{" + self.xlabel + "}}$" + " (eV)")
        ax.set_xlabel("$\Delta \mu_{\mathrm{" + self.ylabel + "}}$" + " (eV)")
        cbar = fig.colorbar(CM, ticks=self.ticky, pad=0.1)
        cbar.ax.set_yticklabels(self.labels, fontsize=_fig_params.FONTSIZE*0.8)
        plt.tight_layout()
        return ax

    def plot_mu_p(self,
                  temperature,
                  colourmap=None,
                  set_style=None, 
                  cbar_label=None):
        """ Plots a phase diagram  with two sets of axis, one as a function of
        chemical potential and the second is as a function of pressure.

        Parameters
        ----------
        temperature : :py:attr:`int`
            temperature
        colourmap : :py:attr:`str`
            colourmap for the plot
        set_style: :py:attr:`str`
            Plot style
        cbar_label : :py:attr:`str`
            Label for colorbar
        """
        if set_style:
            plt.style.use(set_style)
        if colourmap:
            self.cmap = colourmap

        p1 = ut.pressure(self.x, temperature)
        p2 = ut.pressure(self.y, temperature)
        fig = plt.figure(dpi=96, facecolor='#eeeeee', tight_layout=1)
        ax = fig.add_subplot(121)
        gs = gridspec.GridSpec(1, 2, width_ratios=[.95, .05])
        ax, axR = plt.subplot(gs[0]), plt.subplot(gs[1])
        CM = ax.contourf(self.x, self.y, self.z, levels=self.levels, cmap=self.cmap)
        ax.set_xlabel("$\Delta \mu_{\mathrm{" + self.xlabel + "}}$" + " (eV)")
        ax.set_ylabel("$\Delta \mu_{\mathrm{" + self.ylabel + "}}$" + " (eV)")
        ax2 = ax.twinx()
        ax2.set_ylim(p2[0], p2[-1])
        ax2.set_ylabel("$P_" + "{\mathrm{" + self.ylabel + "}}$" + str(temperature) + " K (bar)")
        ax3 = ax.twiny()
        ax3.set_xlim(p1[0], p1[-1])
        ax3.set_xlabel("$P_" + "{\mathrm{" + self.xlabel + "}}$" + str(temperature) + " K (bar)")
        cbar = fig.colorbar(CM, extend='both', cax=axR, ticks=self.ticky)
        cbar.ax.set_yticklabels(self.labels)
        if cbar_label:
            axR.set_xlabel(cbar_label, fontsize=_fig_params.FONTSIZE*0.8)
        return ax

    def plot_pressure(self, 
                      temperature, 
                      colourmap=None,
                      set_style=None):
        """ Plots a phase diagram as a function of pressure.

        Parameters
        ----------
        temperature : :py:attr:`int`
            temperature
        colourmap : :py:attr:`str`
            colourmap for the plot
        set_style: :py:attr:`str` 
            Plot style
        """
        if set_style:
            plt.style.use(set_style)
        if colourmap:
            self.cmap = colourmap
        p1 = ut.pressure(self.x, temperature)
        p2 = ut.pressure(self.y, temperature)
        fig = plt.figure()
        ax = fig.add_subplot(111)
        CM = ax.contourf(p1, p2, self.z, levels=self.levels, cmap=self.cmap)
        ax.set_ylabel("$P_" + "{\mathrm{" + self.xlabel + "}}$" + " 298 K (bar)")
        ax.set_xlabel("$P_" + "{\mathrm{" + self.ylabel + "}}$" + " 298 K (bar)")
        cbar = fig.colorbar(CM, ticks=self.ticky, pad=0.1)
        cbar.ax.set_yticklabels(self.labels, fontsize=_fig_params.FONTSIZE*0.8)
        plt.tight_layout()
        return ax


class MuTPlot():
    """Class that plots a phase diagram as a function of chemical potential and temperature.

    Parameters
    ----------
    x : :py:attr:`array_like`
        x axis, chemical potential of species x
    y : :py:attr:`array_like`
        y axis, chemical potential of species y
    z : :py:attr:`array_like`
        two dimensional grid, phase info
    labels : :py:attr:`list`
        :py:attr:`list`): of phase labels
    ticks : :py:attr:`list`
        :py:attr:`list`): of phases
    colors : :py:attr:`list`
        :py:attr:`list`): of phases       
    xlabel : :py:attr:`str`
        species name for x axis label
    ylabel : :py:attr:`str`
        species name for y axis label
    """
    def __init__(self,
                 x,
                 y,
                 z,
                 labels,
                 ticks,
                 colors,
                 xlabel,
                 ylabel):
        self.x = x
        self.y = y
        self.z = z
        self.labels = labels
        self.ticks = ticks
        self.colors = colors
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.levels = ut.get_levels(self.z)
        self.ticky = ut.get_ticks(self.ticks)
        if colors:
            self.cmap = ListedColormap(self.colors)
        else:
            self.cmap = "viridis"

    def plot_mu_vs_t(self,
                    colourmap=None, 
                    set_style=None, 
                    figsize=None):
        """Plots a simple phase diagram as a function of chemical potential.

        Parameters
        ----------
        colourmap: :py:attr:`str`
            Colourmap for the plot. Default='viridis'
        set_style: :py:attr:`str`
            Plot style
        figsize: :py:attr:`tuple`
            Set a custom figure size.
        """
        if set_style:
            plt.style.use(set_style)
        if colourmap:
            self.cmap = colourmap
        fig = plt.figure(figsize=figsize)
        ax = fig.add_subplot(111)
        CM = ax.contourf(self.x, self.y, self.z, levels=self.levels, cmap=self.cmap)
        ax.set_ylabel("Temperature (K)")
        ax.set_xlabel("$\Delta \mu_{\mathrm{" + self.xlabel + "}}$" + " (eV)")
        cbar = fig.colorbar(CM, ticks=self.ticky, pad=0.1)
        cbar.ax.set_yticklabels(self.labels, fontsize=_fig_params.FONTSIZE*0.8)
        plt.tight_layout()
        return ax

    def plot_p_vs_t(self,
                    temperature,
                    colourmap=None,
                    set_style=None,
                    figsize=None):
        """Plots a simple phase diagram as a function of chemical potential.

        Parameters
        ----------
        temperature: :py:attr:`int`
            Temperature.
        colourmap: :py:attr:`str` 
            Colourmap for the plot. Default='viridis'
        set_style: :py:attr:`str`
            Plot style
        figsize: :py:attr:`tuple` 
            Set a custom figure size.
        """
        p1 = ut.pressure(self.x, temperature)
        if set_style:
            plt.style.use(set_style)
        if colourmap:
            self.cmap = colourmap
        fig = plt.figure(figsize=figsize)
        ax = fig.add_subplot(111)
        CM = ax.contourf(p1, self.y, self.z, levels=self.levels, cmap=self.cmap)
        ax.set_ylabel("Temperature (K)")
        ax.set_xlabel("$P_" + "{\mathrm{" + self.xlabel + "}}$" + str(temperature) + " K (bar)")
        cbar = fig.colorbar(CM, ticks=self.ticky, pad=0.1)
        cbar.ax.set_yticklabels(self.labels, fontsize=_fig_params.FONTSIZE*0.8)
        plt.tight_layout()
        return ax

    def plot_mu_vs_t_vs_p(self,
                          temperature,
                          colourmap=None,
                          set_style=None,
                          figsize=None):
        """Plots a simple phase diagram as a function of chemical potential.

        Parameters
        ----------
        temperature: :py:attr:`int`
            Temperature.
        colourmap: :py:attr:`str` 
            Colourmap for the plot. Default='viridis'
        set_style: :py:attr:`str`
            Plot style
        figsize: :py:attr:`tuple` 
            Set a custom figure size.
        """
        if set_style:
            plt.style.use(set_style)
        if colourmap:
            self.cmap = colourmap
        p1 = ut.pressure(self.x, temperature)

        fig = plt.figure(dpi=96, facecolor='#eeeeee', tight_layout=1)
        ax = fig.add_subplot(121)
        gs = gridspec.GridSpec(1, 2, width_ratios=[.95, .05])
        ax, axR = plt.subplot(gs[0]), plt.subplot(gs[1])
        CM = ax.contourf(self.x, self.y, self.z, levels=self.levels, cmap=self.cmap)
        ax.set_xlabel("$\Delta \mu_{\mathrm{" + self.xlabel + "}}$" + " (eV)")
        ax.set_ylabel("Temperature (K)")
        ax3 = ax.twiny()
        ax3.set_xlim(p1[0], p1[-1])
        ax3.set_xlabel("$P_" + "{\mathrm{" + self.xlabel + "}}$" + str(temperature) + " K (bar)")
        ax3.tick_params(labelsize=10)
        cbar = fig.colorbar(CM, extend='both', cax=axR, ticks=self.ticky)
        cbar.ax.set_yticklabels(self.labels, fontsize=_fig_params.FONTSIZE*0.8)
        return ax

  
class PTPlot:
    """Class for plotting of temperature vs pressure phase diagrams.

    Parameters
    ----------
    x : :py:attr:`array_like`
        x axis
    y : :py:attr:`array_like`
        y axis
    z : :py:attr:`array_like`
        two dimensional array of phases
    """
    def __init__(self,
                 x,
                 y,
                 z):
        self.x = x
        self.y = y
        self.z = z

    def plot(self, colourmap="viridis", set_style=None):
        """plots phase diagram

        Parameters
        ----------
        colourmap : :py:attr:`str`
            colourmap for phase diagram
        set_style: :py:attr:`str`
            Plot style
        """
        if set_style:
            plt.style.use(set_style)
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.contourf(self.x, self.y, self.z, cmap=colourmap)        
        ax.set_xlabel('Temperature (K)')
        ax.set_ylabel("log P (bar)")
        plt.tight_layout()
        return ax
