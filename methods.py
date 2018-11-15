#!/usr/bin/env /Users/zschillaci/Software/miniconda3/envs/pyenv/bin/python
from header import *

def GetFilesBySite(files):
    LBL_files = []
    SCIPP_files = []

    for f in files:
        for lbl, scipp in zip(LBL_modules, SCIPP_modules):
            if (lbl in f):
                LBL_files.append(f)
                break
            if (scipp in f):
                SCIPP_files.append(f)
                break

    return LBL_files, SCIPP_files

def loadFromCsv(filename):
    with open(filename, 'r') as file:
        list = [elem for elem in csv.reader(file, delimiter='\t')]
    return list

def drawStats(series, ax):
    plt.text(0.7, 0.9, 'Entries: ' + str(round(len(series),0)), ha='center', va='center', transform=ax.transAxes)
    plt.text(0.7, 0.8, 'Mean: ' + str(round(np.mean(series),2)), ha='center', va='center', transform=ax.transAxes)
    plt.text(0.7, 0.7, 'Std. Dev.: ' + str(round(np.std(series),2)), ha='center', va='center', transform=ax.transAxes)

def drawMultiStats(dictOfSeries, ax):
    for n, (key, val) in enumerate(dictOfSeries.items()):
        plt.text(0.75, 0.7 - 0.2 * n, "-----" + key + "-----", weight='bold', ha='center', va='center', transform=ax.transAxes)
        plt.text(0.75, 0.6 - 0.2 * n, "$\mu$: " + str(round(np.mean(val), 2)) + " , $\sigma$: " + str(round(np.std(val), 2)), ha='center', va='center', transform=ax.transAxes)

def getOutputNoise(gain, innse):
    return gain * innse * (1.6*10**-19) * (10**15)
class ABC130_Single_Result(object):
    def __init__(self, directory, infile, label):
        self.directory = directory
        self.infile = infile
        self.name = self.infile[:-4]
        self.label = label

        indata = loadFromCsv(self.directory + self.infile)

        self.chan = []
        self.code = []
        self.gain = []
        self.offset = []
        self.innse = []
        self.outnse = []
        self.comm = []
        for row in indata[1:]:
            self.chan.append(int(row[0]))
            self.code.append(int(row[1]))
            gain = float(row[2])
            self.gain.append(gain)
            self.offset.append(float(row[3]))
            innse = int(row[4])
            self.innse.append(innse)
            self.outnse.append(getOutputNoise(gain, innse))
            self.comm.append(row[5])

        print('-----' + self.name + '-----')
        self.whatDoTheCodesMean()
        self.whatChannelsFailed()

    def whatDoTheCodesMean(self):
        self.meaningOftheCodes = {}
        for i in range(len(self.code)):
            if (self.code[i] not in list(self.meaningOftheCodes.keys())):
                self.meaningOftheCodes[self.code[i]] = self.comm[i]
        self.meaningOftheCodes = collections.OrderedDict(sorted(self.meaningOftheCodes.items(), key=lambda t: t[0]))
        print(self.meaningOftheCodes)

    def whatChannelsFailed(self):
        self.failedChannels = collections.OrderedDict()
        for i in range(len(self.comm)):
            if (self.comm[i] != 'OK'):
                self.failedChannels[self.chan[i]] = self.comm[i]
        print('Failed channels: ' + str(len(self.failedChannels.keys())))

    def Fill(self, i, channels, selections, unselections):
        fill = False
        if ((self.comm[i] in selections) or (selections == [])):
            if ((self.comm[i] not in unselections) or (unselections == [])):
                if (len(channels) != 2):
                    fill = True
                else:
                    if ((self.chan[i] >= channels[0]) and (self.chan[i] <= channels[1])):
                        fill = True
        return fill

    def plot(self, channels = [], selections = [], unselections = []):
        fig = plt.figure("Summary - " + self.name, (12, 8))

        gain = []
        innse = []
        outnse = []
        for i in range(len(self.chan)):
            if self.Fill(i, channels, selections, unselections):
                gain.append(self.gain[i])
                innse.append(self.innse[i])
                outnse.append(self.outnse[i])

        ax1 = fig.add_subplot(221)
        plt.grid(False)
        plt.hist(gain, 50, range=(25,175))
        plt.xlabel('Gain [mV/fC]')
        plt.ylabel('Entries')
        drawStats(gain, ax1)

        ax2 = fig.add_subplot(222)
        plt.grid(False)
        plt.hist(innse, 50, range=(200, 1300))
        plt.xlabel('Input Noise [e$^-$]')
        plt.ylabel('Entries')
        drawStats(innse, ax2)

        ax3 = fig.add_subplot(223)
        plt.grid(False)
        plt.hist(outnse, 50, range=(0, 20))
        plt.xlabel('Output Noise [mV]')
        plt.ylabel('Entries')
        drawStats(outnse, ax3)
        plt.show()

class ABC130_Site_Results(ABC130_Single_Result):
    def __init__(self, directory, infiles, label, modules = []):
        self.directory = directory
        self.name = 'Multiple'
        self.label = label

        self.chan = []
        self.code = []
        self.gain = []
        self.offset = []
        self.innse = []
        self.outnse = []
        self.comm = []

        print('----------------------')
        print('Grouping: ' + label)
        print('Including files: ')
        for infile in infiles:
            include = False
            if (modules == []):
                include = True
            else:
                for module in modules:
                    if (module in infile):
                        include = True
                        break
            if include:
                print(infile)
                indata = loadFromCsv(self.directory + infile)
                for row in indata[1:]:
                    self.chan.append(int(row[0]))
                    self.code.append(int(row[1]))
                    gain = float(row[2])
                    self.gain.append(gain)
                    self.offset.append(float(row[3]))
                    innse = int(row[4])
                    self.innse.append(innse)
                    self.outnse.append(getOutputNoise(gain, innse))
                    self.comm.append(row[5])

def plotMultiple(allResults, extension, channels = [], selections = [], unselections = []):
    fig = plt.figure("Summary", (12, 8))

    dictOfSeries = collections.OrderedDict()

    ax1 = fig.add_subplot(221)
    plt.grid(False)
    alpha = 1.0
    for result in allResults:
        gain = []
        for i in range(len(result.chan)):
            if result.Fill(i, channels, selections, unselections):
                gain.append(result.gain[i])
        plt.hist(gain, 50, range=(25, 175), alpha=alpha, label=result.label)
        alpha -= 0.25
        plt.xlabel('Gain [mV/fC]')
        plt.ylabel('Entries')
        dictOfSeries[result.label] = gain
    drawMultiStats(dictOfSeries, ax1)
    plt.legend(loc=1)

    ax2 = fig.add_subplot(222)
    plt.grid(False)
    alpha = 1.0
    for result in allResults:
        innse = []
        for i in range(len(result.chan)):
             if result.Fill(i, channels, selections, unselections):
                innse.append(result.innse[i])
        plt.hist(innse, 50, range=(200, 1300), alpha=alpha, label=result.label)
        alpha -= 0.25
        plt.xlabel('Input Noise [e$^-$]')
        plt.ylabel('Entries')
        dictOfSeries[result.label] = innse
    drawMultiStats(dictOfSeries, ax2)
    plt.legend(loc=1)

    ax3 = fig.add_subplot(223)
    plt.grid(False)
    alpha = 1.0
    for result in allResults:
        outnse = []
        for i in range(len(result.chan)):
            if result.Fill(i, channels, selections, unselections):
                outnse.append(result.outnse[i])
        plt.hist(outnse, 50, range=(0, 20), alpha=alpha, label=result.label)
        alpha -= 0.25
        plt.xlabel('Output Noise [mV]')
        plt.ylabel('Entries')
        dictOfSeries[result.label] = outnse
    drawMultiStats(dictOfSeries, ax3)
    plt.legend(loc=1)

    fname = 'ABC130_Results_Comparison-' + extension
    # if ((selections == []) and (unselections == [])):
    #     fname += '-all'
    # else:
    #     for selection in selections:
    #         fname += '-' + selection
    #     for unselection in unselections:
    #         fname += '-!' + unselection

    plt.savefig(fname + '.pdf')
    plt.close()
    
