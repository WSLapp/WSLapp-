from PyQt5.Qt import *
from PyQt5.QtWebEngineWidgets import *
class WebView(QWebEngineView):
    def __init__(self, parent):
        super().__init__(parent)
    def createWindow(self, webWindowType):
        return main_demo.browser


class Main(QMainWindow):
    def __init__(self,Title='',Web=''):
        super(Main, self).__init__()
        self.browser = WebView(self)
        self.tabs = QTabWidget()
        self.urlbar = QLineEdit()
        self.setWindowTitle(Title)#'Windows7')
        self.web = QWebEngineView()
        self.setCentralWidget(self.web)
        qurl=QUrl(Web)
        self.web.load(QUrl(Web))#'https://win7simu.visnalize.com/'))
        self.browser.urlChanged.connect(lambda qurl, browser=self.browser: self.renew_urlbar(qurl, self.browser))
    # 将当前网页的链接更新到地址栏
    def renew_urlbar(self, url, browser=None):
        # 非当前窗口不更新URL
        if browser != self.tabs.currentWidget():
            return
        #self.add_new_tab()
        self.urlbar.setText(url.toString())
        self.urlbar.setCursorPosition(0)

def open_file(name,file):
    app = QApplication([])
    win = Main(name,file)
    win.show()
    app.exec()
if __name__ == '__main__':
    open_file('a','https://www.baidu.com/')#'https://win7simu.visnalize.com/')

