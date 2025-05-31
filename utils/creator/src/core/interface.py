try: 
    from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget, QFrame, QPushButton, QLabel, QLineEdit, QComboBox, QProgressBar, QDialog, QDialogButtonBox, QRadioButton, QCheckBox, QSpinBox, QSlider, QMenuBar, QTableWidget, QTreeWidget, QMessageBox, QTextEdit, QFileDialog, QScrollArea, QMenu, QScrollArea
    from PyQt5.QtGui import QIcon, QPixmap, QCursor, QScreen, QMouseEvent  
    from PyQt5.QtCore import Qt, QPoint 
except:
    pass

from utils.creator.src.core import File

class Interface:
    from typing import Type
    window: Type[QMainWindow]
    
    widgets = []
    
    
    class Scrollable(QScrollArea):
        def __init__(self, parent=None):
            super().__init__(parent)
            self.setWidgetResizable(True)
            self.setMouseTracking(True)
            self._last_mouse_pos = None
            self._hand_scrolling = False

        def mousePressEvent(self, event: QMouseEvent):
            if event.button() == Qt.LeftButton:
                self._last_mouse_pos = event.pos()
                self._hand_scrolling = True
                self.setCursor(Qt.ClosedHandCursor)
            super().mousePressEvent(event)

        def mouseMoveEvent(self, event: QMouseEvent):
            if self._hand_scrolling and self._last_mouse_pos:
                delta = event.pos() - self._last_mouse_pos
                self._last_mouse_pos = event.pos()
                self.horizontalScrollBar().setValue(self.horizontalScrollBar().value() - delta.x())
                self.verticalScrollBar().setValue(self.verticalScrollBar().value() - delta.y())
            super().mouseMoveEvent(event)

        def mouseReleaseEvent(self, event: QMouseEvent):
            if event.button() == Qt.LeftButton:
                self._hand_scrolling = False
                self.setCursor(Qt.ArrowCursor)
            super().mouseReleaseEvent(event)
    
    @classmethod
    def setup(cls, window: QMainWindow):
        cls.window = window  
        cls.screen_width, cls.screen_height = cls.get_screen_size() 
        cls.window.resizeEvent = cls.display
    #     cls.window.wheelEvent = cls.wheelEvent
        
    # @classmethod
    # def wheelEvent(cls, event): 
    #     if event.angleDelta().y() > 0:
    #         cls.scale_factor *= 1.1  # Zoom avant
    #     else:
    #         cls.scale_factor /= 1.1  # Zoom arrière
    #     cls.window.update()
    
    @classmethod
    def get_window_size(cls): 
        return cls.window.width(), cls.window.height()
    
    @classmethod
    def get_screen_size(cls):
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableSize() 
        return screen_geometry.width(), screen_geometry.height() 
    
    def add(widget:QWidget, **kwargs):
        position  = kwargs.get("position", (0, 0))
        width = kwargs.get("width", None)
        height = kwargs.get("height", width) 
        style = kwargs.get("style", None) 
        display = kwargs.get("display", False)  
        scrollable = kwargs.get("scrollable", False)  
        min_width = kwargs.get("min_width", False)
        min_heigth = kwargs.get("min_heigth", False)
        max_width = kwargs.get("max_width", False)
        max_heigth = kwargs.get("max_heigth", False)
        
        if min_width:
            widget.setMinimumWidth(min_width)
        if min_heigth:
            widget.setMinimumHeight(min_heigth)
        if max_width:
            widget.setMaximumWidth(max_width)
        if max_heigth:
            widget.setMaximumHeight(max_heigth)
            
        if scrollable:
            widget = Interface.scrollable(widget)
        if style:
            widget.setProperty("class", style) 
            
            
        Interface.widgets.append({
            "widget": widget,
            "position": position,
            "width": width,
            "height": height,
            "display": display,
            # "min_width": min_width,
            # "min_height": min_heigth,
            # "max_width": max_width,
            # "max_height": max_heigth,
            # "scrollable": scrollable,
            # "style": style
        })

    @classmethod
    def display(cls, event): 
        for item in cls.widgets: 
            widget:QWidget = item["widget"]
            x, y = item["position"]
            width = item["width"]  
            height = item["height"]
            display = item["display"]
            
            
            x, y = cls.responsive(x, y)
            
                
            if width:
                if display == "center":
                    x = (widget.parentWidget().width() - width) // 2
                    y = (widget.parentWidget().height() - height) // 2
                width, height = cls.responsive(width, height)
                widget.setGeometry(x, y, width, height)
            else:
                if display == "center":
                    x = widget.parentWidget().width() // 2
                    y = widget.parentWidget().height() // 2
                widget.move(x, y)
                # widget.resize()
                
        super(QMainWindow, cls.window).resizeEvent(event)
        

    @classmethod
    def responsive(cls, width, height):
        new_width, new_height = cls.get_window_size()  
        scale_width = new_width / cls.screen_width
        scale_height = new_height / cls.screen_height 
        width = width * scale_width
        height = height * scale_height
        return int(width), int(height) 
    
    
        
        
    @classmethod
    def body(cls, **kwargs):
        style = kwargs.get("style", "")
        body = QWidget(cls.window)
        cls.window.stacked_widget.addWidget(body)
        body.setProperty("class", style)
        cls.window.setCentralWidget(body) 
        return body
        
    @classmethod
    def title(cls, title:str) -> None:
        cls.window.setWindowTitle(title)
        
    @classmethod
    def resize(cls, width:int, height:int) -> None:
        cls.window.resize(width, height)
        
    @classmethod
    def style(cls, path) -> None:
        styles = File.load(path)
        cls.window.setStyleSheet(styles) 
        
    def favicon(cls, icon) -> None:
        cls.window.setWindowIcon(QIcon(icon))
        
    def scrollable(child:QWidget):
        scroll = Interface.Scrollable(child.parentWidget())
        scroll.setWidget(child)
        scroll.setWidgetResizable(True)
        return scroll 
    
    def card(parent, **kwargs): 
        card = QFrame(parent)  
        Interface.add(card, **kwargs)
        return card
    
    def label(title, parent, **kwargs): 
        label = QLabel(title, parent) 
        Interface.add(label, **kwargs)
        return label
    
    def button(title, parent, action=None, **kwargs): 
        button = QPushButton(title, parent) 
        button.setCursor(QCursor(Qt.PointingHandCursor)) 
        Interface.add(button, **kwargs)
        if action:
            button.clicked.connect(action)
        return button
    
    def input(parent, **kwargs):
        x, y  = kwargs.get("position", (0, 0))
        width = kwargs.get("width", 200)
        style = kwargs.get("style", "")
        line_edit = QLineEdit(parent)
        line_edit.setProperty("class", style)
        line_edit.setGeometry(x, y, width, 30)
        return line_edit
    
    def combo_box(parent, items, **kwargs):
        x, y  = kwargs.get("position", (0, 0))
        width = kwargs.get("width", 200)
        style = kwargs.get("style", "")
        combo_box = QComboBox(parent)
        combo_box.setProperty("class", style)
        combo_box.setGeometry(x, y, width, 30)
        combo_box.addItems(items)
        return combo_box

    def progress_bar(parent, **kwargs):
        x, y  = kwargs.get("position", (0, 0))
        width = kwargs.get("width", 200)
        style = kwargs.get("style", "")
        progress_bar = QProgressBar(parent)
        progress_bar.setProperty("class", style)
        progress_bar.setGeometry(x, y, width, 20)
        return progress_bar
    
    def dialog(title, parent, **kwargs):
        width = kwargs.get("width", 300)
        height = kwargs.get("height", 200)
        style = kwargs.get("style", "")
        dialog = QDialog(parent)
        dialog.setWindowTitle(title)
        dialog.setProperty("class", style)
        dialog.setFixedSize(width, height)
        return dialog

    def dialog_buttons(dialog, **kwargs):
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, dialog)
        buttons.setGeometry(kwargs.get("position", (100, 150))[0], kwargs.get("position", (100, 150))[1], kwargs.get("width", 100), kwargs.get("height", 30))
        return buttons
    
    def radio_button(title, parent, **kwargs):
        x, y  = kwargs.get("position", (0, 0))
        style = kwargs.get("style", "")
        radio_button = QRadioButton(title, parent)
        radio_button.setProperty("class", style)
        radio_button.move(x, y)
        return radio_button

    def check_box(title, parent, **kwargs):
        x, y  = kwargs.get("position", (0, 0))
        style = kwargs.get("style", "")
        check_box = QCheckBox(title, parent)
        check_box.setProperty("class", style)
        check_box.move(x, y)
        return check_box
    
    def spin_box(parent, **kwargs):
        x, y  = kwargs.get("position", (0, 0))
        width = kwargs.get("width", 100)
        style = kwargs.get("style", "")
        spin_box = QSpinBox(parent)
        spin_box.setProperty("class", style)
        spin_box.setGeometry(x, y, width, 30)
        return spin_box
    
    def slider(parent, **kwargs):
        x, y  = kwargs.get("position", (0, 0))
        width = kwargs.get("width", 200)
        style = kwargs.get("style", "")
        slider = QSlider(Qt.Horizontal, parent)
        slider.setProperty("class", style)
        slider.setGeometry(x, y, width, 30)
        return slider
    
    def menu_bar(parent:QMainWindow, **kwargs):
        menu_bar = QMenuBar(parent)
        file_menu = QMenu("File", parent)
        file_menu.addAction("Open")
        file_menu.addAction("Save")
        file_menu.addAction("Exit")
        menu_bar.addMenu(file_menu)
        parent.setMenuBar(menu_bar)
        return menu_bar
    
    def table_widget(parent, **kwargs):
        rows = kwargs.get("rows", 5)
        columns = kwargs.get("columns", 3)
        style = kwargs.get("style", "")
        table = QTableWidget(parent)
        table.setRowCount(rows)
        table.setColumnCount(columns)
        table.setProperty("class", style)
        return table
    
    def tree_widget(parent, **kwargs):
        style = kwargs.get("style", "")
        tree = QTreeWidget(parent)
        tree.setProperty("class", style)
        return tree
    
    def context_menu(parent, **kwargs):
        menu = QMenu(parent)
        action1 = menu.addAction("Option 1")
        action2 = menu.addAction("Option 2")
        action3 = menu.addAction("Option 3")
        return menu
    
    def message_box(parent, title, message, icon=QMessageBox.Information, **kwargs):
        msg_box = QMessageBox(parent)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(icon)
        msg_box.exec_()

    def text_edit(parent, **kwargs):
        x, y  = kwargs.get("position", (0, 0))
        width = kwargs.get("width", 400)
        height = kwargs.get("height", 300)
        style = kwargs.get("style", "")
        text_edit = QTextEdit(parent)
        text_edit.setProperty("class", style)
        text_edit.setGeometry(x, y, width, height)
        return text_edit

    def image(path, parent:QWidget, **kwargs):
        image = QLabel(parent)  
        pixmap = QPixmap(path)
        image.setPixmap(pixmap)
        image.setScaledContents(True) 
        Interface.add(image, **kwargs)
        return image


    def file_dialog(parent, **kwargs):
        file_dialog = QFileDialog(parent)
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        file_dialog.setViewMode(QFileDialog.List)
        file_dialog.setProperty("class", kwargs.get("style", ""))
        return file_dialog


    # def scroll(parent, **kwargs):
    #     scroll = QScrollArea(parent)
    #     style = kwargs.get("style", "")
    #     scroll.setProperty("class", style)
    #     return scroll
    
    def icon(path):
        return QIcon(path)



class Window(QMainWindow):
    def __init__(self, **kwargs):
        title = kwargs.get("title", "Creator") 
        super().__init__() 
        self.stacked_widget = QStackedWidget()
        
        self.setWindowTitle(title)
    def resizeEvent(self, event):
        super().resizeEvent(event) 
