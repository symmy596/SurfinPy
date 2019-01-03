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

    def plot(self, output="Phase.png", colourmap="RdBu", set_style="ggplot",
             atmospheric_conditions=[1.0, 298.15]):
        """plots phase diagram

        Parameters
        ----------
        output : str
            output filename
        colourmap : str
            colourmap for phase diagram
        atmospheric_conditions : list
            location of bars showing atmospheric conditions
        """
        plt.style.use(set_style)
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.contourf(self.x, self.y, self.z, cmap=colourmap)        
        ax.set_xlabel('Temperature (K)', fontsize=14)
        ax.set_ylabel("log P (bar)", fontsize=14)
        ax.axhline(y=atmospheric_conditions[0], color="black",
                   linestyle='--', alpha=0.8)
        ax.axvline(x=atmospheric_conditions[1], color="black",
                   linestyle='--', alpha=0.8)
        ax.tick_params(labelsize=14)
        plt.tight_layout()
        plt.savefig(output, dpi=600)
        plt.show()
        plt.close()
