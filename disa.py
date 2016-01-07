#!/usr/bin/env python
# Disa is a visualisation program for braid/lace parts of knitting patterns

import re, sys, os, os.path
from PyQt4 import QtGui, QtCore

# Stuff that shouldn't be hardcoded but still is 
pix_dir = os.path.expanduser('~/gitcode/disa/png')
#input_string = "8r\n1r, 1abk2r, 3r, 1a\n4r, 4a"
#txt_pattern = [[u for u in row.split(", ")] for row in input_string[0]]
pattern_file = os.path.expanduser('~/gitcode/disa/tests/test-keltisk.txt')


# Rudimentary file and text handling
with open(pattern_file, 'r') as f:
    input_string = f.readlines()

# Make a nice string for the label
txt_string = ''
for line in input_string:
    txt_string += line

#print(input_string)
#print('END PATTERN\n\n')
pix_list = os.listdir(pix_dir)
txt_pattern = []
for string_list in input_string:
    # string.remove r'^\d+: '
    # string.remove (\\n)*$
    # string.split(', ')
    string_list = re.sub(r'^\d+: (.*)\n', r'\1', string_list)
    txt_pattern.append(string_list.split(', '))
    print(string_list)
        #string = string.split('\n')[0]
    #txt_pattern += [string.split(', ')]
print(txt_pattern)
#print('END PATTERN\n\n')

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

        re_digit = re.compile("\d+")
        p_array = []

        # units is an array of stitch codes formatted for pixview
        units = list(reversed(txt_pattern))
        #units = list(reversed(input_string))
        for row in units:
            print(row)
            if not row[0] == '#':
                row.reverse()
                widget_row = []
                for u in row:
                    u = re.sub(r'^(\d+)([ar])$', r'\1*\2', u)
                    if '*' in u:    
                        repeat = re_digit.match(u).group()
                        stitch_file = u.split('*')[1] + '.png'
                    else:
                        repeat = 1
                        stitch_file = u + '.png' 
#                    print('{}, {}, {}'.format(u, repeat, stitch_file))
                    if stitch_file in pix_list:
                        for item in range(int(repeat)):
                            widget_row.append(StitchLbl(os.path.join(pix_dir,stitch_file)))
                p_array.append(widget_row)

        pbox = QtGui.QVBoxLayout()
        pbox.setSpacing(0)
        pbox.setAlignment(QtCore.Qt.AlignTop)
        for row in p_array:
            rbox = QtGui.QHBoxLayout()
            rbox.setSpacing(0)
            rbox.setAlignment(QtCore.Qt.AlignLeft)
            for item in row:
                rbox.addWidget(item)
            pbox.addLayout(rbox)

        return pbox


    def initUI(self):

        pix_view = self.initPixview()
        text_view = QtGui.QLabel(txt_string, self)
        text_view.setAlignment(QtCore.Qt.AlignTop)

        topside = QtGui.QWidget(self)
        topside.setLayout(pix_view)
        splitter = QtGui.QSplitter(QtCore.Qt.Vertical)
        splitter.addWidget(topside)
        splitter.addWidget(text_view)
        allbox = QtGui.QVBoxLayout(self)
        allbox.addWidget(splitter)
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
