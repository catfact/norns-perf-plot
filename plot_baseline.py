
import matplotlib.pyplot as plt

import csv

def plot_data(infile, outfile=None):
    with open(infile) as csvfile:
        r = csv.reader(csvfile, delimiter=",")
        cpu = []
        xruns = []
        skip = True
        for row in r:
            print(row)
            if skip:
                skip = False
                continue
            cpu.append(float(row[0].strip()))
            xruns.append(float(row[1].strip()))

        print(cpu)
        print(xruns)

        fig1, axs = plt.subplots(2, 2)
        axs[0][0].set_ylim(0, 100)
        axs[0][0].plot(cpu)
        axs[0][0].set_ylabel('CPU load %')
        axs[0][0].grid(True)
        #axs[0][1].boxplot(cpu, notch=True, autorange=True)
        axs[0][1].violinplot(cpu, showmedians=True, showextrema=True)
        axs[0][1].grid(True)
        axs[1][0].set_ylabel('xruns per period')
        axs[1][0].plot(xruns)
        axs[1][0].set_ylim(0, 10)
        axs[1][0].grid(True)
        #axs[1][1].boxplot(xruns, notch=True, autorange=True)
        axs[1][1].violinplot(xruns, showmedians=True, showextrema=True)
        #axs[1][1].set_ylim(0, 10)
        axs[1][1].grid(True)
        if outfile is not None: plt.savefig(outfile, dpi=100)
        plt.show()