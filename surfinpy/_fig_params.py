"""
Plot formatting
"""

# Copyright (c) Adam R. Symington
# Distributed under the terms of the MIT License
# author: Adam R. Symington

from collections import OrderedDict
from matplotlib import rcParams, cycler
import seaborn as sns

sns.set_palette('colorblind')
colors = sns.palettes.SEABORN_PALETTES['colorblind']

FONTSIZE = 15
NEARLY_BLACK = "#161616"
LIGHT_GREY = "#F5F5F5"
WHITE = "#ffffff"

MASTER_FORMATTING = {
    "axes.formatter.limits": (-3, 3),
    "xtick.major.pad": 7,
    "ytick.major.pad": 7,
    "ytick.color": NEARLY_BLACK,
    "xtick.color": NEARLY_BLACK,
    "axes.labelcolor": NEARLY_BLACK,
    "axes.spines.bottom": True,
    "axes.spines.left": True,
    "axes.spines.right": True,
    "axes.spines.top": True,
    "axes.axisbelow": True,
    "legend.frameon": False,
    'axes.edgecolor': NEARLY_BLACK,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
    "mathtext.fontset": "custom",
    "font.size": FONTSIZE,
    "font.family": "sans-serif",
    "font.serif" : "Arial",
    "savefig.bbox": "tight",
    "axes.facecolor": LIGHT_GREY,
    "axes.labelpad": 10.0,
    "axes.labelsize": FONTSIZE,
    "axes.titlepad": 20,
    "axes.titlesize": FONTSIZE,
    "axes.grid": False,
    "grid.color": WHITE,
    "lines.markersize": 7.0,
    "lines.scale_dashes": False,
    "xtick.labelsize": FONTSIZE,
    "ytick.labelsize": FONTSIZE,
    "legend.fontsize": FONTSIZE * 0.8,
    "lines.linewidth": 2,
}

for k, v in MASTER_FORMATTING.items():
    rcParams[k] = v