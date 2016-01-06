#!/usr/bin/env python
# Disa is a visualisation program for braid/lace parts of knitting patterns

import re, sys, os, os.path
from PyQt4 import QtGui, QtCore

pix_dir = os.path.expanduser('~/gitcode/disa/png')
input_string = "8r\n1r, 3a, 3r, 1a\n4r, 4a"

pix_list = os.listdir(pix_dir)

# Should handle number + letter(s)
#stitch_dict = {"r": "-", "a": "x"}

re_digit = re.compile("\d+")




#output_string = ""


txt_pattern = [[u for u in row.split(", ")] for row in input_string.split("\n")]

#print("START\n{}END".format(output_string))

#widgetlist = []
#for item in mylist: widgetlist.append(mincoolawidget(args))


class StitchLbl(QtGui.QLabel):

    def __init__(self, stitch_path):
        super().__init__()
        pixmap = QtGui.QPixmap(stitch_path)
        self.setPixmap(pixmap)


class MainWindow(QtGui.QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initPixview(self):

        p_array = []

        # units is an array of stitch codes formatted for pixview
        units = list(reversed(txt_pattern))
        for row in units:
            row.reverse()
            widget_row = []
            for u in row:
                repeat = re_digit.match(u).group()
                stitch_file = u.split(repeat)[1] + '.png'
                if stitch_file in pix_list:
                    for item in range(int(repeat)):
                        widget_row.append(StitchLbl(os.path.join(pix_dir,stitch_file)))
            p_array.append(widget_row)

        pbox = QtGui.QVBoxLayout()
        for row in p_array:
            rbox = QtGui.QHBoxLayout()
            for item in row:
                rbox.addWidget(item)
            pbox.addLayout(rbox)

        return pbox


    def initUI(self):

        pix_view = self.initPixview()
        text_view = QtGui.QLabel(input_string, self)

        #splitter = QtGui.QSplitter(QtCore.Qt.Vertical)
        #splitter.addLayout(pix_view)
        #splitter.addWidget(text_view)

        #hbox = QtGui.QHBoxLayout(self)
        #hbox.addWidget(splitter)
        
        allbox = QtGui.QVBoxLayout(self)
        allbox.addLayout(pix_view)
        allbox.addWidget(text_view)

        self.setLayout(allbox)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('plastique'))

        self.setWindowTitle('disa')

        self.show()


def main():

    myApp = QtGui.QApplication(sys.argv)
    mainwin = MainWindow()
    sys.exit(myApp.exec_())


if __name__ == '__main__':
    main()
