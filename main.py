from plot_baseline import *
import glob
import os

datafiles = glob.glob("captures/data_softcut_*.csv")
for datafile in datafiles:
    plotfile = datafile.replace('captures/', 'plots/').replace('csv', 'svg')
    if not os.path.exists(plotfile):
        plot_data(datafile, plotfile)