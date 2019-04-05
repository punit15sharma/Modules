#!/usr/bin/env /Users/zschillaci/Software/miniconda3/envs/pyenv/bin/python
from header import *

def loadFromCsv(filename):
    with open(filename, 'r') as file:
        rows = [elem for elem in csv.reader(file, delimiter='\t')]
    return rows
def getModuleName(filename):
    return filename[:filename.index('RC') - 1]
def getFilesBySite(files, site):
    site_files = []

    for infile in files:
        for module in SITES[site]:
            if (module in infile):
                site_files.append(infile)
                break

    return site_files

def setPlotStyle():
    plt.style.use('ggplot')
    plt.rcParams['lines.linewidth'] = 2.15
    plt.rcParams['lines.markeredgewidth'] = 0.0
    plt.rcParams['font.size'] = 10
    plt.rcParams['axes.labelsize'] = 12
    plt.rcParams['axes.labelweight'] = 'bold'
    plt.rcParams['axes.facecolor'] = 'whitesmoke'
    plt.rcParams['grid.color'] = 'black'
    plt.rcParams['grid.linestyle'] = '--'
    plt.rcParams['grid.linewidth'] = '0.25'
    plt.rcParams['grid.alpha'] = '0.25'
    plt.rcParams['xtick.labelsize'] = 10
    plt.rcParams['ytick.labelsize'] = 10
    plt.rcParams['legend.fontsize'] = 10
    plt.rcParams['legend.frameon'] = False
    plt.rcParams['figure.titlesize'] = 'large'
    plt.rcParams['figure.titleweight'] = 'bold'
    plt.rcParams['axes.edgecolor'] = 'black'
    plt.rcParams['patch.edgecolor'] = 'none'
    plt.rcParams.update({'figure.max_open_warning': 0})
def savePlot(fname):
    path = RESULTS_DIR + datetime.today().strftime("%Y-%m-%d")
    if not os.path.isdir(path):
        os.makedirs(path)

    plt.savefig(path + '/' + fname + '.pdf')
    plt.close()
def setYlim(ylim,yticks):
    #Set y-limits of plot based upon min. and max. of plots
    low = ylim[0]
    high = ylim[-1]
    tick = abs(yticks[0][1] - yticks[0][0])

    if (low == 0):
        low -= 0.025 * tick
    else:
        low -= 1.05 * tick
    if (high == 0):
        high += 0.025 * tick
    else:
        high += 1.05 * tick

    return low, high
def getAlpha(n):
    return np.max([(1.0 - 0.1 * n), 0.05])
def drawStats(series, ax):
    plt.text(0.7, 0.9, 'Entries: ' + str(round(len(series),0)), ha='center', va='center', transform=ax.transAxes)
    plt.text(0.7, 0.8, 'Mean: ' + str(round(np.mean(series),2)), ha='center', va='center', transform=ax.transAxes)
    plt.text(0.7, 0.7, 'Std. Dev.: ' + str(round(np.std(series),2)), ha='center', va='center', transform=ax.transAxes)
def drawMultiStats(dictOfSeries, ax):
    for n, (key, val) in enumerate(dictOfSeries.items()):
        plt.text(0.75, 0.7 - 0.2 * n, key, weight='bold', ha='center', va='center', transform=ax.transAxes)
        plt.text(0.75, 0.6 - 0.2 * n, "$\mu$: " + str(round(np.mean(val), 2)) + " , $\sigma$: " + str(round(np.std(val), 2)), ha='center', va='center', transform=ax.transAxes)

def getOutputNoise(gain, innse):
    return (gain * innse * (1.6*10**-19) * (10**15))
def getEfficiency(failures, total, printOut=True):
    num = len(failures)
    den = len(total)
    eff = 100 * (1 - num / den)
    if printOut:
        print('Failed channels: ' + str(num))
        print('Total channels: ' + str(den))
        print('Efficiency: ' + str(eff) + ' %')
    return eff

class SingleTestResult(object):
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

        self.dump()

    def dump(self):
        print('----------' + self.label + '----------')
        print('')
        print('Including files: ')
        if (type(self.infile) is not list):
            print(self.infile)
        else:
            print('Num. of files: ' + str(len(self.infile)))
            for infile in self.infile:
                print(infile)
        print('')
        self.whatChannelsFailed()
        print('-----------------------------------')
        print('')

    def whatDoTheCodesMean(self):
        self.meaningOftheCodes = {}
        for i in range(len(self.code)):
            if (self.code[i] not in list(self.meaningOftheCodes.keys())):
                self.meaningOftheCodes[self.code[i]] = self.comm[i]
        self.meaningOftheCodes = collections.OrderedDict(sorted(self.meaningOftheCodes.items(), key=lambda t: t[0]))
        print(self.meaningOftheCodes)

    def whatChannelsFailed(self):
        self.badChannels = collections.OrderedDict()
        self.deadChannels = collections.OrderedDict()

        consecutive_bad, max_consecutive_bad = 0, 0
        consecutive_dead, max_consecutive_dead = 0, 0
        for i in range(len(self.comm)):
            if (self.comm[i] in ALL_BAD_CODES):
                self.badChannels[self.chan[i]] = self.comm[i]
              
                consecutive_bad += 1
                if (consecutive_bad > max_consecutive_bad):
                    max_consecutive_bad = consecutive_bad

                if (self.comm[i] in FAILURE_CODES):
                    self.deadChannels[self.chan[i]] = self.comm[i]

                    consecutive_dead += 1
                    if (consecutive_dead > max_consecutive_dead):
                        max_consecutive_dead = consecutive_dead
                else:
                    consecutive_dead = 0

            else:
                consecutive_bad = 0
                consecutive_dead = 0

        print('----- BAD (NOT-OK) CHANNELS -----')
        print('Max consecutive bad (not-OK) channels: ' + str(max_consecutive_bad))
        getEfficiency(self.badChannels, self.comm)

        print('----- DEAD CHANNELS -----')
        print('Max consecutive dead channels: ' + str(max_consecutive_dead))
        getEfficiency(self.deadChannels, self.comm)

    def Fill(self, i, channels=[], selections=[], unselections=[]):
        fill = False
        if ((self.comm[i] in selections) or (selections == [])):
            if ((self.comm[i] not in unselections) or (unselections == [])):
                if (len(channels) != 2):
                    fill = True
                else:
                    if ((self.chan[i] >= channels[0]) and (self.chan[i] <= channels[1])):
                        fill = True
        return fill

    def Plot(self, **kwargs):
      
        channels = ([] if ('channels' not in kwargs) else kwargs['channels'])
        selections = ([] if ('selections' not in kwargs) else kwargs['selections'])
        unselections = ([] if ('unselections' not in kwargs) else kwargs['unselections'])
      
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
class MultipleTestResults(SingleTestResult):
    def __init__(self, directory, infiles, label, modules = []):
        self.directory = directory
        self.infile = []
        self.name = label
        self.label = label

        self.chan = []
        self.code = []
        self.gain = []
        self.offset = []
        self.innse = []
        self.outnse = []
        self.comm = []

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
                self.infile.append(infile)
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

        self.dump()

def plotMultiple(TestResults, extension, **kwargs):

    channels = ([] if ('channels' not in kwargs) else kwargs['channels'])
    selections = ([] if ('selections' not in kwargs) else kwargs['selections'])
    unselections = ([] if ('unselections' not in kwargs) else kwargs['unselections'])
    annotate = (True if ('annotate' not in kwargs) else kwargs['annotate'])

    fig = plt.figure("Summary", (12, 8))
    fig.suptitle(extension, fontsize=14)

    dictOfSeries = collections.OrderedDict()

    ax1 = fig.add_subplot(221)
    plt.grid(False)
    for n, result in enumerate(TestResults):
        gain = []
        for i in range(len(result.chan)):
            if result.Fill(i, channels, selections, unselections):
                gain.append(result.gain[i])
        plt.hist(gain, 50, range=(25, 175), alpha=getAlpha(n), label=result.label)
        dictOfSeries[result.label] = gain
    if annotate:
        drawMultiStats(dictOfSeries, ax1)
    plt.xlabel('Gain [mV/fC]')
    plt.ylabel('Entries')
    plt.legend(loc=1)

    ax2 = fig.add_subplot(222)
    plt.grid(False)
    for n, result in enumerate(TestResults):
        innse = []
        for i in range(len(result.chan)):
             if result.Fill(i, channels, selections, unselections):
                innse.append(result.innse[i])
        plt.hist(innse, 50, range=(200, 1300), alpha=getAlpha(n), label=result.label)
        dictOfSeries[result.label] = innse
    if annotate:
        drawMultiStats(dictOfSeries, ax2)
    plt.xlabel('Input Noise [e$^-$]')
    plt.ylabel('Entries')
    plt.legend(loc=1)

    ax3 = fig.add_subplot(223)
    plt.grid(False)
    for n, result in enumerate(TestResults):
        outnse = []
        for i in range(len(result.chan)):
            if result.Fill(i, channels, selections, unselections):
                outnse.append(result.outnse[i])
        plt.hist(outnse, 50, range=(0, 20), alpha=getAlpha(n), label=result.label)
        dictOfSeries[result.label] = outnse
    if annotate:
       drawMultiStats(dictOfSeries, ax3)
    plt.xlabel('Output Noise [mV]')
    plt.ylabel('Entries')
    plt.legend(loc=1)

    fname = 'ABC130_Comparison-' + extension
    
    if (selections != []):
        for selection in selections:
            fname += '-' + selection
    if (unselections != []):
        for unselection in unselections:
            fname += '-' + unselection

    savePlot(fname)
def plotMultipleVsChannel(TestResults, extension, channels=[0, 2560]):
    fig = plt.figure("Summary", (12, 8))
    fig.suptitle(extension, fontsize=14)

    ax1 = fig.add_subplot(221)
    plt.grid(False)
    for n, result in enumerate(TestResults):
        plt.plot(result.chan, result.gain, 'o', alpha=getAlpha(n), label=result.label, markersize=3)
    plt.xlim(channels[0], channels[1])
    low, high = setYlim(plt.ylim(), plt.yticks())
    plt.ylim(low, high)
    plt.xlabel('Channel')
    plt.ylabel('Gain [mV/fC]')
    plt.legend(loc=1)

    ax2 = fig.add_subplot(222)
    plt.grid(False)
    for n, result in enumerate(TestResults):
        plt.plot(result.chan, result.innse, 'o', alpha=getAlpha(n), label=result.label, markersize=3)
    plt.xlim(channels[0], channels[1])
    low, high = setYlim(plt.ylim(), plt.yticks())
    plt.ylim(low, high)
    plt.xlabel('Channel')
    plt.ylabel('Input Noise [e$^-$]')
    plt.legend(loc=1)

    ax3 = fig.add_subplot(223)
    plt.grid(False)
    for n, result in enumerate(TestResults):
        plt.plot(result.chan, result.outnse, 'o', alpha=getAlpha(n), label=result.label, markersize=3)
    plt.xlim(channels[0], channels[1])
    low, high = setYlim(plt.ylim(), plt.yticks())
    plt.ylim(low, high)
    plt.xlabel('Channel')
    plt.ylabel('Output Noise [mV]')
    plt.legend(loc=1)

    fname = 'ABC130_ComparisonVsChannel-' + extension
    savePlot(fname)
