import sys
import matplotlib as mpl
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, qApp
import time
import datetime
from functions import get_latest_file, file_approval, order_file, \
    find_ori, treat_ori_for_lpv, listing_lpv, approved_corks, get_latest_cspfile, cspFile, orderCSP, listCSP

mpl.use('Qt5Agg')
from Control_DS100plusv8 import Ui_MainWindow


class MainWindow(QMainWindow):
    def selectFolder(self):
        folder_path = str(
            QFileDialog.getExistingDirectory(self, 'Select Folder')
        )
        self.ui.label_6.setText(folder_path)
        try:
            if len(folder_path) > 1:
                self.start_worker_1()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("You didn't choose a folder.")
                msg.setInformativeText('Choose again!')
                msg.setWindowTitle("Error!")
                msg.exec_()
                return
        except Exception as error:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Verify the folder!")
            msg.setInformativeText('Error: {}'.format(error))
            msg.setWindowTitle("Error!")
            msg.exec_()
            return

    def start_worker_1(self):
        folder_path = self.ui.label_6.text()
        self.thread[1] = ThreadClass(parent=None, folder_path=folder_path, index=1)
        self.thread[1].start()
        self.thread[1].any_signal.connect(self.get_latest_file_thread)

    def get_latest_file_thread(self, file_name):
        cnt = file_name
        first_text = self.ui.label_2.text()
        aux_text = self.ui.label_2.text()
        filename = cnt.split('\\')[1]
        index = self.sender().index
        if cnt != aux_text:
            if index == 1:
                self.ui.label_2.setText(first_text + filename)
                self.listen_for_file(cnt)

    def _connectActions(self):
        self.ui.action_Exit.triggered.connect(qApp.quit)
        self.ui.actionSelect_Folder_2.triggered.connect(self.selectFolder)
        self.ui.listWidget.itemClicked.connect(self.clicked_item)
        self.ui.listWidget_2.itemClicked.connect(self.clicked_itemCSP)

    def list_signals(self, _cycles):
        self.ui.listWidget.clear()
        self.ui.listWidget.addItems(_cycles)

    def listCSPsignals(self, _cycles):
        self.ui.listWidget_2.clear()
        self.ui.listWidget_2.addItems(_cycles)

    def listen_for_file(self, cnt):
        file = cnt
        folder_path = self.ui.label_6.text()
        if len(folder_path) < 10:
            return
        else:
            while True:
                if file_approval(file):
                    try:
                        filename = file.split('\\')[1]
                        self.ui.label_2.setText('File: ' + filename)
                        Plot_values = order_file(file)
                        global lpv_plots
                        lpv_plots = Plot_values[0]
                        global signal_plots
                        signal_plots = Plot_values[1]
                    except Exception as error:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Critical)
                        msg.setText("Error obtaining LPV's and Signals! Check if file is well formatted!")
                        msg.setInformativeText('Error: {}'.format(error))
                        msg.setWindowTitle("Error!")
                        msg.exec_()
                        return
                    try:
                        ori_gets = find_ori(file, self.ui.label_6.text())
                        global ori
                        ori = ori_gets[0]
                        ori_name = ori_gets[1]
                        self.ui.label_3.setText('ORI: ' + ori_name)
                        ori_lpv = treat_ori_for_lpv(ori, lpv_plots)
                    except Exception as error:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Critical)
                        msg.setText("Error obtaining ORI! Check if ORI is in the folder!")
                        msg.setInformativeText('Error: {}'.format(error))
                        msg.setWindowTitle("Error!")
                        msg.exec_()
                        return
                    try:
                        self.ui.widget.plot(lpv_plots, ori_lpv)
                    except Exception as error:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Critical)
                        msg.setText("Error on LPV Graph")
                        msg.setInformativeText('Error: {}'.format(error))
                        msg.setWindowTitle("Error!")
                        msg.exec_()
                        return
                    try:
                        self.ui.widget_2.plot_signal(signal_plots, ori)
                        listing = listing_lpv(lpv_plots, signal_plots, ori)
                    except Exception as error:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Critical)
                        msg.setText("Error on Signal Graph")
                        msg.setInformativeText('Error: {}'.format(error))
                        msg.setWindowTitle("Error!")
                        msg.exec_()
                        return
                    try:
                        variables = approved_corks(lpv_plots, ori)
                        stats = variables[0]
                        count = variables[1]
                        gl_rj = variables[2]

                        # Color if above 20% rejection red if below green
                        if gl_rj > 20:
                            self.ui.label_rj_gl.setStyleSheet('background-color: red')
                        else:
                            self.ui.label_rj_gl.setStyleSheet('background-color: rgb(0, 255, 0)')
                        if stats[0] > 20:
                            self.ui.taxa_1.setStyleSheet('background-color: red')
                        else:
                            self.ui.taxa_1.setStyleSheet('background-color: rgb(0, 255, 0)')
                        if stats[1] > 20:
                            self.ui.taxa_2.setStyleSheet('background-color: red')
                        else:
                            self.ui.taxa_2.setStyleSheet('background-color: rgb(0, 255, 0)')
                        if stats[2] > 20:
                            self.ui.taxa_3.setStyleSheet('background-color: red')
                        else:
                            self.ui.taxa_3.setStyleSheet('background-color: rgb(0, 255, 0)')
                        if stats[3] > 20:
                            self.ui.taxa_4.setStyleSheet('background-color: red')
                        else:
                            self.ui.taxa_4.setStyleSheet('background-color: rgb(0, 255, 0)')
                        if stats[4] > 20:
                            self.ui.taxa_5.setStyleSheet('background-color: red')
                        else:
                            self.ui.taxa_5.setStyleSheet('background-color: rgb(0, 255, 0)')
                        if stats[5] > 20:
                            self.ui.taxa_6.setStyleSheet('background-color: red')
                        else:
                            self.ui.taxa_6.setStyleSheet('background-color: rgb(0, 255, 0)')
                        if stats[6] > 20:
                            self.ui.taxa_7.setStyleSheet('background-color: red')
                        else:
                            self.ui.taxa_7.setStyleSheet('background-color: rgb(0, 255, 0)')
                        if stats[7] > 20:
                            self.ui.taxa_8.setStyleSheet('background-color: red')
                        else:
                            self.ui.taxa_8.setStyleSheet('background-color: rgb(0, 255, 0)')

                        self.ui.label_corks.setText(str(count))
                        self.ui.label_rj_gl.setText('{}%'.format(str(round(gl_rj, 2))))
                        self.ui.taxa_1.setText('{}%'.format(str(round(stats[0], 2))))
                        self.ui.taxa_2.setText('{}%'.format(str(round(stats[1], 2))))
                        self.ui.taxa_3.setText('{}%'.format(str(round(stats[2], 2))))
                        self.ui.taxa_4.setText('{}%'.format(str(round(stats[3], 2))))
                        self.ui.taxa_5.setText('{}%'.format(str(round(stats[4], 2))))
                        self.ui.taxa_6.setText('{}%'.format(str(round(stats[5], 2))))
                        self.ui.taxa_7.setText('{}%'.format(str(round(stats[6], 2))))
                        self.ui.taxa_8.setText('{}%'.format(str(round(stats[7], 2))))
                        self.list_signals(listing)
                        HOUR = datetime.datetime.now().hour
                        MINUTE = datetime.datetime.now().minute
                        self.ui.scan_date.setText(('Last scan at {}:{}'.format(str(HOUR), str(MINUTE))))

                    except Exception as error:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Critical)
                        msg.setText("Error on statistics!")
                        msg.setInformativeText('Error: {}'.format(error))
                        msg.setWindowTitle("Error!")
                        msg.exec_()
                    try:
                        controllerCSPFile = get_latest_cspfile(folder_path)
                        Vars = cspFile(controllerCSPFile)
                        signalsCSP = Vars[0]
                        channelsCSP = Vars[1]
                        timesCSP = Vars[2]
                        global plotCSP
                        plotCSP = orderCSP(signalsCSP, channelsCSP, timesCSP)
                        cyclesCSP = listCSP(plotCSP)
                        self.listCSPsignals(cyclesCSP)
                        self.ui.widget_3.plotCSP_signal(plotCSP)
                        return signal_plots, ori

                    except Exception as error:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Critical)
                        msg.setText("Error on Log File Aquisition!")
                        msg.setInformativeText('Error: {}'.format(error))
                        msg.setWindowTitle("Error!")
                        msg.exec_()

                        return

                time.sleep(60)

    def clicked_item(self, item):
        item_text = item.text()
        item_rep = int(item_text[6:len(item_text)]) - 1
        self.ui.widget_2.update_signal_plot(signal_plots, ori, item_rep, lpv_plots)
        return

    def clicked_itemCSP(self, item):
        item_text = item.text()
        item_rep = int(item_text[6:len(item_text)]) - 1
        self.ui.widget_3.updateCSP_plot(plotCSP, item_rep)
        return

    def __init__(self):
        super(MainWindow, self).__init__()
        self.main_win = QMainWindow()
        self.main_win.setWindowIcon(QIcon('FILDAN_Icon.ico'))
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.thread = {}
        self._connectActions()

    def show(self):
        self.main_win.showMaximized()


class ThreadClass(QtCore.QThread):
    any_signal = QtCore.pyqtSignal(str)

    def __init__(self, folder_path, parent=None, index=0):
        super(ThreadClass, self).__init__(parent)
        self.index = index
        self.is_running = True
        self.folder_path = folder_path

    def run(self):
        print('Starting thread...', self.index)
        cnt = 0

        while True:
            cnt = get_latest_file(self.folder_path)
            self.any_signal.emit(cnt)
            time.sleep(60)


if __name__ == '__main__':
    global signal_plots
    global lpv_plots
    global ori
    global plotCSP
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
