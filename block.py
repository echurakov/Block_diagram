
from PyQt5 import * 
from PyQt5.QtWidgets import *
import sys
from PyQt5 import QtWidgets , QtCore
from PyQt5.QtGui import QPixmap


class Begin(QtWidgets.QWidget):
    def __init__(self, parent = None, text = "", node_child = ""):
        """
        Метод определяет блок "Начало", его атрибуты: text - текстовое поле, node_child - для связи с нижеследующим блоком 
        """
        super().__init__(parent)
        self.setWindowTitle("Begin")
        self.text = text
        self.node_child = node_child
        self.label = QLabel(self.text, self)
        self.pic = QLabel("Begin", self)

        self.pic.setGeometry(50,50,50,50)
        self.pic.setPixmap(QPixmap("D:\\Новая папка\\rectangle"))

  #  def resizeEvent(self, a0):
  #      set.pic.setGeometry(0, 0, set.width(), set.height())
    
    def set_child(self, node_child):
        self.node_child = node_child

    """def set_child(self, node_child)
        begin.set_child(Action)
    """


class Cond(QtWidgets.QWidget):
    def __init__(self, parent = None, text = "", node_parents = [], node_child0 = "", node_child1 = ""):
        """
        Метод определяет блок "Условие", его атрибуты: text - текстовое поле; node_child0, node_child1 - для связи с нижеследующими блоками
        """
        super().__init__(parent)
        self.setWindowTitle("Condition")
        self.text = ""
        self.node_parents = node_parents
        self.node_child0 = ""
        self.node_child1 = ""
        self.label = QLabel(self.text, self)
        self.pic = QLabel("Condition", self)

        self.pic.setGeometry(50,50,50,50)
        self.pic.setPixmap(QPixmap("D:\\Новая папка\\romb"))

    #def resizeEvent(self, a0):
    #    set.pic.setGeometry(0, 0, set.width(), set.height())

    def add_parents(self, node_parents):
        self.node_parents.append(node_parents)

    def delete_parents(self, node_parents):
        self.node_parents.remove(node_parents)  
    
        """ 
    def set_parent(self, node_parents):
        self.node_parents = node_parents
        """

    def set_child0(self, node_child0):
        self.node_child0 = node_child0

    def set_child1(self, node_child1):
        self.node_child1 = node_child1
    
    def resizeEvent(self, a):
        self.pic.setGeometry(50,50, self.width() -100 , self.height() - 100)
        

class Action(QtWidgets.QWidget):
    def __init__(self, text = "", parent = None, node_parents = [], node_child = ""):
        """
        Метод определяет блок "Операция", его атрибуты: text - текстовое поле; 
        node_child - для связи с нижеследующим блоком; 
        node_parents - для связи с предыдущим (верхним) блоком
        """
        super().__init__(parent)
        self.setWindowTitle("Action")
        self.text = ""
        self.node_parents = []
        self.node_child = ""
        self.label = QLabel(self.text, self)
        self.pic = QLabel("Action", self)

        self.pic.setGeometry(50,50,50,50)
        self.pic.setPixmap(QPixmap("D:\\Новая папка\\rectangle"))

    def resizeEvent(self, a0):
        self.pic.setGeometry(0, 0, self.width(), self.height())

    def add_parents(self, node_parents):
        self.node_parents.append(node_parents)

    def delete_parents(self, node_parents):
        self.node_parents.remove(node_parents)  
    """def set_parent(self, node_parents):
        self.node_parents = node_parents
    """
    def set_child(self, node_child):
        self.node_child = node_child


class Cycle(QtWidgets.QWidget):
    def __init__(self, parent = None, text = "", node_child = "", node_parents = []):
        """
        Метод определяет блок "Цикл", его атрибуты: text - текстовое поле; 
        node_parent0, node_parent1 - для связи с предыдущими блоками (верхними, боковыми); 
        node_child - для связи с нижеследующим блоком
        """
        super().__init__(parent)
        self.setWindowTitle("Cycle")
        self.text = ""
        self.node_parents = node_parents
        self.node_child0 = ""
        self.node_child1 = ""
        self.label = QLabel(self.text, self)
        self.pic = QLabel("Cycle", self)

        self.pic.setGeometry(50,50,50,50)
        self.pic.setPixmap(QPixmap("D:\\Новая папка\\hexagon"))

    def resizeEvent(self, a0):
        set.pic.setGeometry(0, 0, set.width(), set.height())

    def add_parents(self, node_parents):
        self.node_parents.append(node_parents)

    def delete_parents(self, node_parents):
        self.node_parents.remove(node_parents)   

    """ def set_parent0(self, node_parent0):
        self.node_parent0 = node_parent0

    def set_parent1(self, node_parent1):
        self.node_parent1 = node_parent1
    """
    def set_child0(self, node_child0):
        self.node_child0 = node_child0

    def set_child1(self, node_child1):
        self.node_child1 = node_child1


class End(QtWidgets.QWidget):
    def __init__(self, parent = None, text = "", node_parents = []):
        """
        Метод определяет блок "Конец", его атрибуты: text - текстовое поле;
        node_child - для связи с предыдущим (верхним) блоком
        """
        super().__init__(parent)
        self.setWindowTitle("End")
        self.text = text
        self.node_parents = node_parents
        self.label = QLabel(self.text, self)  
        self.pic = QLabel("Cycle", self)

        self.pic.setGeometry(50,50,50,50)
        self.pic.setPixmap(QPixmap("D:\\Новая папка\\hexagon"))

    def resizeEvent(self, a0):
        set.pic.setGeometry(0, 0, set.width(), set.height())

    def add_parents(self, node_parents):
        self.node_parents.append(node_parents)

    def delete_parents(self, node_parents):
        self.node_parents.remove(node_parents)   
   

    def print_all_parents(self):
        print(self.parent.text)
        self.parent.print_all_parents()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Блок-схема")
        self.setCentralWidget

# class Pix(QWidget):
#     def __init__(self, image_path, parent=None):
#         super().__init__(parent)

        
#         label = QLabel(self)
#         pixmap = QPixmap(image_path)
#         label.setPixmap(pixmap)
        
#         self.setWindowTitle("Pix")
#         self.pix = QPixmap("rombos.png")

        



if __name__ == "__main__":
    # QtCore.QCoreApplication.addLibraryPath("./")
    app = QApplication(sys.argv)
    window = MainWindow()
    # window.show()
    # pic = Pix(sys.argv)/
    # pic.show()

    begin = Begin()
    begin.show()
    cond = Cond()
    action1 = Action()
    action2 = Action()
    cycle = Cycle()
    end = End()
    # end.show()
    cond.show()
    begin.set_child(cond)
    cond.set_child0(action1)
    cond.set_child1(cycle)
    cond.add_parents(begin)
    action1.add_parents(cond)
    action1.set_child(action1)
    cycle.add_parents(cond)
    cycle.add_parents(action2)
    cycle.set_child0(action2)
    cycle.set_child1(end)
    action2.set_child(cycle)
    action2.add_parents(cycle)
    end.add_parents(cycle)
    end.add_parents(action1)

    begin.text = "Начало"
    cond.text = "14"
    action1.text = "Начать процесс дегидрации"
    action2.text = "Ничего не делать"
    end.text = "Конец"

    # widget.show()
    app.exec()