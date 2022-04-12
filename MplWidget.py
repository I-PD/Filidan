# Imports
from PyQt5 import QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib
import numpy as np

# Ensure using PyQt5 backend
matplotlib.use('QT5Agg')


# Matplotlib canvas class to create figure
class MplCanvas(FigureCanvas):
    def __init__(self):
        # figsize=(18.1, 8.8),
        self.fig = Figure(figsize=(14.1, 6.8), facecolor='#f0f0f0')
        self.ax = self.fig.subplots(2, 4)
        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        FigureCanvas.updateGeometry(self)

    # Matplotlib widget


# figsize=(14.5, 4.8),
class MplWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)  # Inherit from QWidget
        self.canvas = MplCanvas()  # Create canvas object
        self.vbl = QtWidgets.QVBoxLayout()  # Set box for plotting
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)
        self.canvas.ax[0, 0].set_title('Channel 1')
        self.canvas.ax[0, 1].set_title('Channel 2')
        self.canvas.ax[0, 2].set_title('Channel 3')
        self.canvas.ax[0, 3].set_title('Channel 4')
        self.canvas.ax[1, 0].set_title('Channel 5')
        self.canvas.ax[1, 1].set_title('Channel 6')
        self.canvas.ax[1, 2].set_title('Channel 7')
        self.canvas.ax[1, 3].set_title('Channel 8')

        toolbar = NavigationToolbar(self.canvas, self)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(self.canvas)

    def plot(self, _data, _ori_data):
        data = _data
        if len(data[0]) > 0:
            x1 = np.arange(1, len(data[0]) + 1)
        if len(data[1]) > 0:
            x2 = np.arange(1, len(data[1]) + 1)
        if len(data[2]) > 0:
            x3 = np.arange(1, len(data[2]) + 1)
        if len(data[3]) > 0:
            x4 = np.arange(1, len(data[3]) + 1)
        if len(data[4]) > 0:
            x5 = np.arange(1, len(data[4]) + 1)
        if len(data[5]) > 0:
            x6 = np.arange(1, len(data[5]) + 1)
        if len(data[6]) > 0:
            x7 = np.arange(1, len(data[6]) + 1)
        if len(data[7]) > 0:
            x8 = np.arange(1, len(data[7]) + 1)

        # clear previous graph
        self.canvas.ax[0, 0].cla()
        self.canvas.ax[0, 1].cla()
        self.canvas.ax[0, 2].cla()
        self.canvas.ax[0, 3].cla()
        self.canvas.ax[1, 0].cla()
        self.canvas.ax[1, 1].cla()
        self.canvas.ax[1, 2].cla()
        self.canvas.ax[1, 3].cla()

        self.canvas.ax[0, 0].set_title('Channel 1')
        self.canvas.ax[0, 1].set_title('Channel 2')
        self.canvas.ax[0, 2].set_title('Channel 3')
        self.canvas.ax[0, 3].set_title('Channel 4')
        self.canvas.ax[1, 0].set_title('Channel 5')
        self.canvas.ax[1, 1].set_title('Channel 6')
        self.canvas.ax[1, 2].set_title('Channel 7')
        self.canvas.ax[1, 3].set_title('Channel 8')

        # plot
        if len(data[0]) > 0:
            self.canvas.ax[0, 0].plot(x1, data[0], marker='o')
        if len(data[1]) > 0:
            self.canvas.ax[0, 1].plot(x2, data[1], marker='o')
        if len(data[2]) > 0:
            self.canvas.ax[0, 2].plot(x3, data[2], marker='o')
        if len(data[3]) > 0:
            self.canvas.ax[0, 3].plot(x4, data[3], marker='o')
        if len(data[4]) > 0:
            self.canvas.ax[1, 0].plot(x5, data[4], marker='o')
        if len(data[5]) > 0:
            self.canvas.ax[1, 1].plot(x6, data[5], marker='o')
        if len(data[6]) > 0:
            self.canvas.ax[1, 2].plot(x7, data[6], marker='o')
        if len(data[7]) > 0:
            self.canvas.ax[1, 3].plot(x8, data[7], marker='o')

        # xticks
        # self.canvas.ax[0, 0].set_xticks(x1)
        # self.canvas.ax[0, 1].set_xticks(x2)
        # self.canvas.ax[0, 2].set_xticks(x3)
        # self.canvas.ax[0, 3].set_xticks(x4)
        # self.canvas.ax[1, 0].set_xticks(x5)
        # self.canvas.ax[1, 1].set_xticks(x6)
        # self.canvas.ax[1, 2].set_xticks(x7)
        # self.canvas.ax[1, 3].set_xticks(x8)

        # for i, txt in enumerate(data[0]):
        #    self.canvas.ax[0, 0].annotate(data[0][i], (x1[i], data[0][i]), horizontalalignment='center',
        #                                  annotation_clip=True)

        # ORI
        if len(data[0]) > 0:
            self.canvas.ax[0, 0].hlines(y=int(_ori_data[0][0]), xmin=1, xmax=len(data[0]), linewidth=2, color='r')
        if len(data[1]) > 0:
            self.canvas.ax[0, 1].hlines(y=int(_ori_data[1][0]), xmin=1, xmax=len(data[1]), linewidth=2, color='r')
        if len(data[2]) > 0:
            self.canvas.ax[0, 2].hlines(y=int(_ori_data[2][0]), xmin=1, xmax=len(data[2]), linewidth=2, color='r')
        if len(data[3]) > 0:
            self.canvas.ax[0, 3].hlines(y=int(_ori_data[3][0]), xmin=1, xmax=len(data[3]), linewidth=2, color='r')
        if len(data[4]) > 0:
            self.canvas.ax[1, 0].hlines(y=int(_ori_data[4][0]), xmin=1, xmax=len(data[4]), linewidth=2, color='r')
        if len(data[5]) > 0:
            self.canvas.ax[1, 1].hlines(y=int(_ori_data[5][0]), xmin=1, xmax=len(data[5]), linewidth=2, color='r')
        if len(data[6]) > 0:
            self.canvas.ax[1, 2].hlines(y=int(_ori_data[6][0]), xmin=1, xmax=len(data[6]), linewidth=2, color='r')
        if len(data[7]) > 0:
            self.canvas.ax[1, 3].hlines(y=int(_ori_data[7][0]), xmin=1, xmax=len(data[7]), linewidth=2, color='r')

        self.canvas.draw()

    def plot_signal(self, _data, _ori):
        data = _data
        ori = _ori
        self.canvas.ax[0, 0].cla()
        self.canvas.ax[0, 1].cla()
        self.canvas.ax[0, 2].cla()
        self.canvas.ax[0, 3].cla()
        self.canvas.ax[1, 0].cla()
        self.canvas.ax[1, 1].cla()
        self.canvas.ax[1, 2].cla()
        self.canvas.ax[1, 3].cla()

        self.canvas.ax[0, 0].set_facecolor('#ffffff')
        self.canvas.ax[0, 1].set_facecolor('#ffffff')
        self.canvas.ax[0, 2].set_facecolor('#ffffff')
        self.canvas.ax[0, 3].set_facecolor('#ffffff')
        self.canvas.ax[1, 0].set_facecolor('#ffffff')
        self.canvas.ax[1, 1].set_facecolor('#ffffff')
        self.canvas.ax[1, 2].set_facecolor('#ffffff')
        self.canvas.ax[1, 3].set_facecolor('#ffffff')

        self.canvas.ax[0, 0].set_title('Channel 1')
        self.canvas.ax[0, 1].set_title('Channel 2')
        self.canvas.ax[0, 2].set_title('Channel 3')
        self.canvas.ax[0, 3].set_title('Channel 4')
        self.canvas.ax[1, 0].set_title('Channel 5')
        self.canvas.ax[1, 1].set_title('Channel 6')
        self.canvas.ax[1, 2].set_title('Channel 7')
        self.canvas.ax[1, 3].set_title('Channel 8')

        for i in range(len(data[0])):
            self.canvas.ax[0, 0].plot(data[0][i][0], data[0][i][1])
        for i in range(len(data[1])):
            self.canvas.ax[0, 1].plot(data[1][i][0], data[1][i][1])
        for i in range(len(data[2])):
            self.canvas.ax[0, 2].plot(data[2][i][0], data[2][i][1])
        for i in range(len(data[3])):
            self.canvas.ax[0, 3].plot(data[3][i][0], data[3][i][1])
        for i in range(len(data[4])):
            self.canvas.ax[1, 0].plot(data[4][i][0], data[4][i][1])
        for i in range(len(data[5])):
            self.canvas.ax[1, 1].plot(data[5][i][0], data[5][i][1])
        for i in range(len(data[6])):
            self.canvas.ax[1, 2].plot(data[6][i][0], data[6][i][1])
        for i in range(len(data[7])):
            self.canvas.ax[1, 3].plot(data[7][i][0], data[7][i][1])

        self.canvas.ax[0, 0].vlines(x=int(ori[0][1]), ymin=0, ymax=6100, linewidth=2, color='r')
        self.canvas.ax[0, 0].vlines(x=int(ori[0][2]), ymin=0, ymax=6100, linewidth=2, color='r')
        self.canvas.ax[0, 1].vlines(x=int(ori[1][1]), ymin=0, ymax=6100, linewidth=2, color='r')
        self.canvas.ax[0, 1].vlines(x=int(ori[1][2]), ymin=0, ymax=6100, linewidth=2, color='r')
        self.canvas.ax[0, 2].vlines(x=int(ori[2][1]), ymin=0, ymax=6100, linewidth=2, color='r')
        self.canvas.ax[0, 2].vlines(x=int(ori[2][2]), ymin=0, ymax=6100, linewidth=2, color='r')
        self.canvas.ax[0, 3].vlines(x=int(ori[3][1]), ymin=0, ymax=6100, linewidth=2, color='r')
        self.canvas.ax[0, 3].vlines(x=int(ori[3][2]), ymin=0, ymax=6100, linewidth=2, color='r')
        self.canvas.ax[1, 0].vlines(x=int(ori[4][1]), ymin=0, ymax=6100, linewidth=2, color='r')
        self.canvas.ax[1, 0].vlines(x=int(ori[4][2]), ymin=0, ymax=6100, linewidth=2, color='r')
        self.canvas.ax[1, 1].vlines(x=int(ori[5][1]), ymin=0, ymax=6100, linewidth=2, color='r')
        self.canvas.ax[1, 1].vlines(x=int(ori[5][2]), ymin=0, ymax=6100, linewidth=2, color='r')
        self.canvas.ax[1, 2].vlines(x=int(ori[6][1]), ymin=0, ymax=6100, linewidth=2, color='r')
        self.canvas.ax[1, 2].vlines(x=int(ori[6][2]), ymin=0, ymax=6100, linewidth=2, color='r')
        self.canvas.ax[1, 3].vlines(x=int(ori[7][1]), ymin=0, ymax=6100, linewidth=2, color='r')
        self.canvas.ax[1, 3].vlines(x=int(ori[7][2]), ymin=0, ymax=6100, linewidth=2, color='r')
        self.canvas.draw()

    def update_signal_plot(self, _data, _ori, _rep, _lpv):
        data = _data
        ori = _ori
        rep = _rep
        self.canvas.ax[0, 0].cla()
        self.canvas.ax[0, 1].cla()
        self.canvas.ax[0, 2].cla()
        self.canvas.ax[0, 3].cla()
        self.canvas.ax[1, 0].cla()
        self.canvas.ax[1, 1].cla()
        self.canvas.ax[1, 2].cla()
        self.canvas.ax[1, 3].cla()

        self.canvas.ax[0, 0].set_title('Channel 1')
        self.canvas.ax[0, 1].set_title('Channel 2')
        self.canvas.ax[0, 2].set_title('Channel 3')
        self.canvas.ax[0, 3].set_title('Channel 4')
        self.canvas.ax[1, 0].set_title('Channel 5')
        self.canvas.ax[1, 1].set_title('Channel 6')
        self.canvas.ax[1, 2].set_title('Channel 7')
        self.canvas.ax[1, 3].set_title('Channel 8')

        if int(rep) + 1 <= len(data[0]):
            self.canvas.ax[0, 0].plot(data[0][rep][0], data[0][rep][1])
            self.canvas.ax[0, 0].vlines(x=int(ori[0][1]), ymin=0, ymax=6100, linewidth=2, color='r')
            self.canvas.ax[0, 0].vlines(x=int(ori[0][2]), ymin=0, ymax=6100, linewidth=2, color='r')
            if _lpv[0][rep] >= int(ori[0][3]):
                self.canvas.ax[0, 0].set_facecolor('#ffd34c')
            else:
                self.canvas.ax[0, 0].set_facecolor('#8fff5f')

        if int(rep) + 1 <= len(data[1]):
            self.canvas.ax[0, 1].plot(data[1][rep][0], data[1][rep][1])
            self.canvas.ax[0, 1].vlines(x=int(ori[1][1]), ymin=0, ymax=6100, linewidth=2, color='r')
            self.canvas.ax[0, 1].vlines(x=int(ori[1][2]), ymin=0, ymax=6100, linewidth=2, color='r')
            if _lpv[1][rep] >= int(ori[1][3]):
                self.canvas.ax[0, 1].set_facecolor('#ffd34c')
            else:
                self.canvas.ax[0, 1].set_facecolor('#8fff5f')

        if int(rep) + 1 <= len(data[2]):
            self.canvas.ax[0, 2].plot(data[2][rep][0], data[2][rep][1])
            self.canvas.ax[0, 2].vlines(x=int(ori[2][1]), ymin=0, ymax=6100, linewidth=2, color='r')
            self.canvas.ax[0, 2].vlines(x=int(ori[2][2]), ymin=0, ymax=6100, linewidth=2, color='r')
            if _lpv[2][rep] >= int(ori[2][3]):
                self.canvas.ax[0, 2].set_facecolor('#ffd34c')
            else:
                self.canvas.ax[0, 2].set_facecolor('#8fff5f')

        if int(rep) + 1 <= len(data[3]):
            self.canvas.ax[0, 3].plot(data[3][rep][0], data[3][rep][1])
            self.canvas.ax[0, 3].vlines(x=int(ori[3][1]), ymin=0, ymax=6100, linewidth=2, color='r')
            self.canvas.ax[0, 3].vlines(x=int(ori[3][2]), ymin=0, ymax=6100, linewidth=2, color='r')
            if _lpv[3][rep] >= int(ori[3][3]):
                self.canvas.ax[0, 3].set_facecolor('#ffd34c')
            else:
                self.canvas.ax[0, 3].set_facecolor('#8fff5f')

        if int(rep) + 1 <= len(data[4]):
            self.canvas.ax[1, 0].plot(data[4][rep][0], data[4][rep][1])
            self.canvas.ax[1, 0].vlines(x=int(ori[4][1]), ymin=0, ymax=6100, linewidth=2, color='r')
            self.canvas.ax[1, 0].vlines(x=int(ori[4][2]), ymin=0, ymax=6100, linewidth=2, color='r')
            if _lpv[4][rep] >= int(ori[4][3]):
                self.canvas.ax[1, 0].set_facecolor('#ffd34c')
            else:
                self.canvas.ax[1, 0].set_facecolor('#8fff5f')

        if int(rep) + 1 <= len(data[5]):
            self.canvas.ax[1, 1].plot(data[5][rep][0], data[5][rep][1])
            self.canvas.ax[1, 1].vlines(x=int(ori[5][1]), ymin=0, ymax=6100, linewidth=2, color='r')
            self.canvas.ax[1, 1].vlines(x=int(ori[5][2]), ymin=0, ymax=6100, linewidth=2, color='r')
            if _lpv[5][rep] >= int(ori[5][3]):
                self.canvas.ax[1, 1].set_facecolor('#ffd34c')
            else:
                self.canvas.ax[1, 1].set_facecolor('#8fff5f')

        if int(rep) + 1 <= len(data[6]):
            self.canvas.ax[1, 2].plot(data[6][rep][0], data[6][rep][1])
            self.canvas.ax[1, 2].vlines(x=int(ori[6][1]), ymin=0, ymax=6100, linewidth=2, color='r')
            self.canvas.ax[1, 2].vlines(x=int(ori[6][2]), ymin=0, ymax=6100, linewidth=2, color='r')
            if _lpv[6][rep] >= int(ori[6][3]):
                self.canvas.ax[1, 2].set_facecolor('#ffd34c')
            else:
                self.canvas.ax[1, 2].set_facecolor('#8fff5f')

        if int(rep) + 1 <= len(data[7]):
            self.canvas.ax[1, 3].plot(data[7][rep][0], data[7][rep][1])
            self.canvas.ax[1, 3].vlines(x=int(ori[7][1]), ymin=0, ymax=6100, linewidth=2, color='r')
            self.canvas.ax[1, 3].vlines(x=int(ori[7][2]), ymin=0, ymax=6100, linewidth=2, color='r')
            if _lpv[7][rep] >= int(ori[7][3]):
                self.canvas.ax[1, 3].set_facecolor('#ffd34c')
            else:
                self.canvas.ax[1, 3].set_facecolor('#8fff5f')

        self.canvas.draw()
        return

    def plotCSP_signal(self, _data):
        data = _data
        self.canvas.ax[0, 0].cla()
        self.canvas.ax[0, 1].cla()
        self.canvas.ax[0, 2].cla()
        self.canvas.ax[0, 3].cla()
        self.canvas.ax[1, 0].cla()
        self.canvas.ax[1, 1].cla()
        self.canvas.ax[1, 2].cla()
        self.canvas.ax[1, 3].cla()

        self.canvas.ax[0, 0].set_facecolor('#ffffff')
        self.canvas.ax[0, 1].set_facecolor('#ffffff')
        self.canvas.ax[0, 2].set_facecolor('#ffffff')
        self.canvas.ax[0, 3].set_facecolor('#ffffff')
        self.canvas.ax[1, 0].set_facecolor('#ffffff')
        self.canvas.ax[1, 1].set_facecolor('#ffffff')
        self.canvas.ax[1, 2].set_facecolor('#ffffff')
        self.canvas.ax[1, 3].set_facecolor('#ffffff')

        self.canvas.ax[0, 0].set_title('Channel 1')
        self.canvas.ax[0, 1].set_title('Channel 2')
        self.canvas.ax[0, 2].set_title('Channel 3')
        self.canvas.ax[0, 3].set_title('Channel 4')
        self.canvas.ax[1, 0].set_title('Channel 5')
        self.canvas.ax[1, 1].set_title('Channel 6')
        self.canvas.ax[1, 2].set_title('Channel 7')
        self.canvas.ax[1, 3].set_title('Channel 8')

        for i in range(len(data[0])):
            self.canvas.ax[0, 0].plot(data[0][i][1], data[0][i][0])
        for i in range(len(data[1])):
            self.canvas.ax[0, 1].plot(data[1][i][1], data[1][i][0])
        for i in range(len(data[2])):
            self.canvas.ax[0, 2].plot(data[2][i][1], data[2][i][0])
        for i in range(len(data[3])):
            self.canvas.ax[0, 3].plot(data[3][i][1], data[3][i][0])
        for i in range(len(data[4])):
            self.canvas.ax[1, 0].plot(data[4][i][1], data[4][i][0])
        for i in range(len(data[5])):
            self.canvas.ax[1, 1].plot(data[5][i][1], data[5][i][0])
        for i in range(len(data[6])):
            self.canvas.ax[1, 2].plot(data[6][i][1], data[6][i][0])
        for i in range(len(data[7])):
            self.canvas.ax[1, 3].plot(data[7][i][1], data[7][i][0])

        self.canvas.draw()
        return

    def updateCSP_plot(self, _data, _rep):
        data = _data
        rep = _rep
        self.canvas.ax[0, 0].cla()
        self.canvas.ax[0, 1].cla()
        self.canvas.ax[0, 2].cla()
        self.canvas.ax[0, 3].cla()
        self.canvas.ax[1, 0].cla()
        self.canvas.ax[1, 1].cla()
        self.canvas.ax[1, 2].cla()
        self.canvas.ax[1, 3].cla()

        self.canvas.ax[0, 0].set_title('Channel 1')
        self.canvas.ax[0, 1].set_title('Channel 2')
        self.canvas.ax[0, 2].set_title('Channel 3')
        self.canvas.ax[0, 3].set_title('Channel 4')
        self.canvas.ax[1, 0].set_title('Channel 5')
        self.canvas.ax[1, 1].set_title('Channel 6')
        self.canvas.ax[1, 2].set_title('Channel 7')
        self.canvas.ax[1, 3].set_title('Channel 8')

        if int(rep) + 1 <= len(data[0]):
            self.canvas.ax[0, 0].plot(data[0][rep][1], data[0][rep][0])

        if int(rep) + 1 <= len(data[1]):
            self.canvas.ax[0, 1].plot(data[1][rep][1], data[1][rep][0])

        if int(rep) + 1 <= len(data[2]):
            self.canvas.ax[0, 2].plot(data[2][rep][1], data[2][rep][0])

        if int(rep) + 1 <= len(data[3]):
            self.canvas.ax[0, 3].plot(data[3][rep][1], data[3][rep][0])

        if int(rep) + 1 <= len(data[4]):
            self.canvas.ax[1, 0].plot(data[4][rep][1], data[4][rep][0])

        if int(rep) + 1 <= len(data[5]):
            self.canvas.ax[1, 1].plot(data[5][rep][1], data[5][rep][0])

        if int(rep) + 1 <= len(data[6]):
            self.canvas.ax[1, 2].plot(data[6][rep][1], data[6][rep][0])

        if int(rep) + 1 <= len(data[7]):
            self.canvas.ax[1, 3].plot(data[7][rep][1], data[7][rep][0])

        self.canvas.draw()
        return
