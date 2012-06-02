from PyQt4 import QtGui, QtCore
import client_main
import xml.etree.ElementTree as ET

class Splash(object):
    def __init__(self):
        configurationFile = ET.parse('../conf/clientConf.xml')
        doc = configurationFile.getroot()
        splashConf = doc.find('SplashImage')
        #Fetch location of downloads folder.
        self.confSplashImageLoc = splashConf.find('Location').text
        
    def show_splash(self, path):
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
    splash = Splash()
    app = QtGui.QApplication(sys.argv)
    splash.show_splash(splash.confSplashImageLoc)
    app.quit()
    MainWindow = QtGui.QMainWindow()
    ui = client_main.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
