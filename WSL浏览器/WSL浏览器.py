from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys
import urllib.request
#import strlist#https://ws.imc.re/eaglercraft/single.html#minecraft网页#�#📰
'''class sc:
    def sc(self):
        f1=open('收藏.txt','w')
        sc=StrList.move_str_list(f1.read())
        f1.close()
        return sc
content1="""
content="""
def move_str_list(content):
    #global content1
    #f1=open('help_ImportPackage_move.py','w')
    #f1.write(content1+content)
    #f1.close()
    try:
        import help_ImportPackage_move
    except Exception as e:
        pass
    #import help_ImportPackage_move
    ty=type(help_ImportPackage_move.content)
    print(help_ImportPackage_move.content)
    if str(ty)!="<class 'list'>":
        raise Exception("'content' is not 'List'#请输入正确的内容")
    return help_ImportPackage_move.content
class save:
 url=None
 def Tab_Save(self):
  html = urllib.request.urlopen(self.url).read()
  self.saveHtml("WSL浏览器_下载", html)
  #return html

 def saveHtml(self,file_name, file_content):
  # 注意windows文件命名的禁用符，比如 /
  with open(file_name.replace('/', '_') + ".html", "wb") as f:
   # 写文件用bytes而不是str，所以要转码
   f.write(file_content)'''

class WebView(QWebEngineView):
	def __init__(self, parent):
		super().__init__(parent)
	def createWindow(self, webWindowType):
		return main_demo.browser


class MainDemo(QMainWindow):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		#sc1=sc()
		#f1=open('收藏.txt','r')
		#print(f1.read())
		#shoucang=strlist.sc#strlist.move_str_list(f1.read())#move_str_list(f1.read())
                #sc=StrList.move_str_list(f1.read())
		#f1.close()
		#shoucang=sc1.sc()
		#self.tab_save=save()
		self.setWindowTitle('WSL浏览器')
		self.setWindowIcon(QIcon('icons/penguin.png'))
		self.resize(800, 500)
		self.show()
		# 添加URL地址栏
		self.urlbar = QLineEdit()
		# 让地址栏支持输入地址回车访问
		self.urlbar.returnPressed.connect(self.navigate_to_url)#renew_urlbar1
		# 添加标签栏
		""
		#正方形标签
		self.tabs = QTabWidget()
		self.tabs.setDocumentMode(True)
		#标签形状
		"""梯形"""
		self.tabs.setTabShape(QTabWidget.Triangular)
		#设置可拖动页面
		#help(self.tabs)
		self.tabs.setMovable(True)
		#self.tabs.setMovable(bool)#setMoveable(bool)
		#
		self.tabs.tabBarDoubleClicked.connect(self.tab_open)
		self.tabs.currentChanged.connect(self.current_tab_changed)
		"""
		#梯形标签
		self.tabs = QTabWidget()
		self.tabs.setTabShape(QTabWidget.Triangular)
		self.tabs.setDocumentMode(True)
		self.tabs.setMovable(True)
		self.tabs.setTabsClosable(True)
                #self.tabWidget.tabCloseRequested.connect(self.close_Tab)
		self.setCentralWidget(self.tabs)
		"""
		# 允许关闭标签
		self.tabs.setTabsClosable(True)
		# 设置关闭按钮的槽
		self.tabs.tabCloseRequested.connect(self.close_current_tab)
		#self.add_new_tab(QUrl('https://www.baidu.com/'), 'Homepage')
		# 设置浏览器
		self.browser = WebView(self)
		self.browser.load(QUrl('https://www.baidu.com/'))
		# 为标签添加索引方便管理
		i = self.tabs.addTab(self.browser, 'Homepage')
		self.tabs.setCurrentIndex(i)
		qurl=QUrl('https://www.baidu.com/')
		#self.tab_save.url='https://www.baidu.com/'
		self.browser.urlChanged.connect(lambda qurl, browser=self.browser: self.renew_urlbar(qurl, self.browser))
		#self.browser.urlChanged.connect(lambda qurl, browser=self.browser: self.renew_urlbar1(qurl, self.browser))
		# 将标签标题改为网页相关的标题
		self.browser.loadFinished.connect(lambda _, i=i, browser=self.browser: self.tabs.setTabText(i, self.browser.page().title()))
		self.setCentralWidget(self.tabs)
		new_tab_action = QAction(QIcon('icons/add_page.png'), 'New Page', self)
		new_tab_action.triggered.connect(self.add_new_tab)
		# 添加导航栏
		navigation_bar = QToolBar('Navigation')
		self.addToolBar(navigation_bar)
		# 设定图标大小
		navigation_bar.setIconSize(QSize(16, 16))
		self.addToolBar(navigation_bar)
		# 添加前进、后退、停止加载和刷新的按钮
		"""
		back_button = QAction(QIcon('icons/back.png'), '后退', self)
		forward_button = QAction(QIcon('icons/forward.png'), '前进', self)
		stop_button = QAction(QIcon('icons/stop.png'), '停止加载', self)
		reload_button = QAction(QIcon('icons/renew.png'), '重新加载', self)
		new_button=QAction(QIcon('icons/add_page.png'), '新增网页', self)
		"""
		back_button = QAction(QIcon('icons/houtui.png'), '后退', self)
		forward_button = QAction(QIcon('icons/qianjin.png'), '前进', self)
		stop_button = QAction(QIcon('icons/close.png'), '停止加载', self)
		reload_button = QAction(QIcon('icons/shuaxin.png'), '重新加载', self)
		new_button=QAction(QIcon('icons/new.png'), '新增网页', self)
		home_button=QAction(QIcon('icons/home.png'), '首页', self)#新窗口.png
		new_windows_button=QAction(QIcon('icons/新窗口.png'), '在新窗口中打开', self)
		#save_button=QAction(QIcon('icons/tab_save.png'), '保存网页', self)
		""
		back_button.triggered.connect(self.tabs.currentWidget().back)
		forward_button.triggered.connect(self.tabs.currentWidget().forward)
		stop_button.triggered.connect(self.tabs.currentWidget().stop)
		reload_button.triggered.connect(self.tabs.currentWidget().reload)
		new_button.triggered.connect(self.add_new_tab)
		home_button.triggered.connect(self.home)
		#save_button.triggered.connect(self.tab_save.Tab_Save)
		# 将按钮添加到导航栏上
		navigation_bar.addAction(back_button)
		navigation_bar.addAction(forward_button)
		navigation_bar.addAction(stop_button)
		navigation_bar.addAction(reload_button)
		#navigation_bar.addAction(new_windows_button)
		navigation_bar.addAction(home_button)
		navigation_bar.addAction(new_button)
		#navigation_bar.addAction(home_button)
		#navigation_bar.addAction(save_button)
		navigation_bar.addSeparator()
		navigation_bar.addWidget(self.urlbar)

	
	# 响应回车按钮，将浏览器当前访问的URL设置为用户输入的URL
	def navigate_to_url(self):
		current_url = QUrl(self.urlbar.text())
		if current_url.scheme() == '':
			current_url.setScheme('http')
		#self.tab_save.url=self.urlbar.text()
		self.tabs.currentWidget().load(current_url)
	def home(self):#https://www.hao123.com/?tn=88093251_99_hao_pg
		#current_url = QUrl('https://www.baidu.com/')
		current_url = QUrl('https://www.monknow.com/zh-CN')
		if current_url.scheme() == '':
			current_url.setScheme('http')
		#self.tab_save.url=self.urlbar.text()
		self.tabs.currentWidget().load(current_url)


	# 将当前网页的链接更新到地址栏
	def renew_urlbar(self, url, browser=None):
		# 非当前窗口不更新URL
		if browser != self.tabs.currentWidget():
			return
		#self.add_new_tab()
		self.urlbar.setText(url.toString())
		self.urlbar.setCursorPosition(0)
	# 将当前网页的链接更新到地址栏
	def renew_urlbar1(self, url, browser=None):
		# 非当前窗口不更新URL
		if browser != self.tabs.currentWidget():
			return
		self.add_new_tab()
		current_url = QUrl(self.tabs.currentWidget())#'https://www.hao123.com/?tn=88093251_99_hao_pg')
		if current_url.scheme() == '':
			current_url.setScheme('http')
		self.tab_save.url=self.urlbar.text()
		self.tabs.currentWidget().load(current_url)
		#self.urlbar.setText(url.toString())
		#self.urlbar.setCursorPosition(0)


	# 添加新的标签页
	def add_new_tab(self):
		# 设置浏览器
		self.browser = WebView(self)
		self.browser.load(QUrl('https://www.monknow.com/zh-CN'))#chrome://newtab
		#self.browser.load(QUrl('chrome://newtab'))
		# 为标签添加索引方便管理
		i = self.tabs.addTab(self.browser, 'Blank')
		self.tabs.setCurrentIndex(i)
		qurl=QUrl('https://www.monknow.com/zh-CN')
		#self.tab_save.url='https://www.hao123.com/?tn=88093251_99_hao_pg'
		self.browser.urlChanged.connect(lambda qurl, browser=self.browser: self.renew_urlbar(qurl, self.browser))
		# 将标签标题改为网页相关的标题
		self.browser.loadFinished.connect(lambda _, i=i, browser=self.browser: self.tabs.setTabText(i, self.browser.page().title()))
	# 双击标签栏打开新页面
	def tab_open(self, i=-1):
		if i == -1:
			self.add_new_tab()
	def current_tab_changed(self, i):
		qurl = self.tabs.currentWidget().url()
		self.renew_urlbar(qurl, self.tabs.currentWidget())
	def close_current_tab(self, i):
		# 若当前标签页只有一个则不关闭
		if self.tabs.count() < 2:
                        #sys.exit(0)
			#exit()
			sys.exit(0)
			#return
		self.tabs.removeTab(i)



if __name__ == '__main__':
	my_application = QApplication(sys.argv) #创建QApplication类的实例
	main_demo = MainDemo()
	main_demo.show()
	my_application.exec_()
