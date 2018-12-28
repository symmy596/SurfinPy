import matplotlib.pyplot as plt


class PVTPlot:
    """Class for plotting of temperature vs pressure phase diagrams.

    Parameters
    ----------
    x : array like
        x axis
    y : array like
        y axis
    z : array like
        two dimensional array of phases
    """
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def plot(self, output="Phase.png", colourmap="RdBu"):
        """plots phase diagram

        Parameters
        ----------
        output : str
            output filename
        colourmap : str
            colourmap for phase diagram
        """
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.contourf(self.x, self.y, self.z, cmap=colourmap)
        ax.set_xlabel('Temperature (K)', fontsize=14, fontweight="bold")
        ax.set_ylabel("log P (bar)", fontsize=14, fontweight="bold")
        ax.axhline(y=1.01, color="black", linestyle='--', alpha=0.8)
        ax.axvline(x=298.15, color="black", linestyle='--', alpha=0.8)
        ax.tick_params(labelsize=14)
        plt.tight_layout()
        plt.savefig(output, dpi=600)
        plt.show()
        plt.close()
