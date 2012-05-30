from PyQt4 import QtGui, QtCore
import client_main

def show_splash(path):
    image = QtGui.QPixmap(path)
    splash = QtGui.QSplashScreen(image)
    splash.setAttribute(QtCore.Qt.WA_DeleteOnClose)
    splash.setMask(image.mask())
    font = QtGui.QFont(splash.font())
    font.setPointSize(font.pointSize() + 5)
    splash.setFont(font)
    splash.show()
    QtGui.QApplication.processEvents()
    for count in range(1, 6):
        splash.showMessage(splash.tr('Please wait...'),
                           QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft,
                           QtCore.Qt.white)
        QtGui.QApplication.processEvents()
        QtCore.QThread.msleep(1000)

if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    show_splash('images/splash.jpg')
    app.quit()
    MainWindow = QtGui.QMainWindow()
    ui = client_main.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
