from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import cv2
import database
import camera
import filter

class Login(QWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('UI/login.ui', None)
        self.ui.show()

        self.ui.check_btn.clicked.connect(self.check)

    def check(self):
        username = self.ui.username.text()
        password = self.ui.password.text()
        if database.checkPWD(username, password):
            self.ui = MainWindow()
        else:
            self.messageBox('Wrong Username Or Password!')
    
    def messageBox(self, msg):
        message = QMessageBox()
        message.setText(msg)
        message.exec()


class Add_Employee(QWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('UI/add_emp.ui', None)
        self.ui.show()
        self.id = database.counter()

        self.ui.takepicture.clicked.connect(self.takePic)
        self.ui.add_btn.clicked.connect(self.add)
        self.ui.cancel_btn.clicked.connect(self.cancel)

        self.ui.year.clear()
        for i in range(1900, 2023, 1):
            self.ui.year.addItem(str(i))
        
    def takePic(self):
        firstname = self.ui.firstname.text()
        lastname = self.ui.lastname.text()
        self.ui = camera.Camera(firstname+lastname)
    
    def add(self):
        firstname = self.ui.firstname.text()
        lastname = self.ui.lastname.text()
        code = self.ui.code.text()
        day = self.ui.day.currentText()
        month = self.ui.month.currentText()
        year = self.ui.year.currentText()
        birthday = day + ',' + month + ',' + year
        id = self.id + 1
        
        database.add_employee(id, firstname, lastname, birthday, code, img_path=f'{firstname+lastname}.jpg')
        self.ui = MainWindow()

    def cancel(self):
        self.ui = MainWindow()

class Filters(QWindow):
    def __init__(self, img, name):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('UI/filter.ui', None)
        self.ui.show()

        self.name = name
        self.img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.img = cv2.resize(img, (200,200))

        #anime
        self.anime = filter.anime(self.img)
        self.image = QImage(self.anime , self.img.shape[1], self.img.shape[0], QImage.Format_RGB888)
        self.px1 = QPixmap.fromImage(self.image)
        self.ui.img_1.setIcon(QIcon(self.px1))
        self.ui.img_1.setIconSize(QSize(150,150))

        #blur
        self.blur = filter.blur(self.img)
        self.image = QImage(self.blur ,self.img.shape[1], self.img.shape[0], QImage.Format_RGB888)
        self.px1 = QPixmap.fromImage(self.image)
        self.ui.img_2.setIcon(QIcon(self.px1))
        self.ui.img_2.setIconSize(QSize(150,150))

        #red
        self.red = filter.red(self.img)
        self.image = QImage(self.red ,self.img.shape[1], self.img.shape[0], QImage.Format_RGB888)
        self.px1 = QPixmap.fromImage(self.image)
        self.ui.img_3.setIcon(QIcon(self.px1))
        self.ui.img_3.setIconSize(QSize(150,150))

        #anime1
        self.anime1 = filter.anime1(self.img)
        self.image = QImage(self.anime1 ,self.img.shape[1], self.img.shape[0], QImage.Format_RGB888)
        self.px1 = QPixmap.fromImage(self.image)
        self.ui.img_4.setIcon(QIcon(self.px1))
        self.ui.img_4.setIconSize(QSize(150,150))

        #normal
        self.normal = filter.normal(self.img)
        self.image = QImage(self.normal ,self.img.shape[1], self.img.shape[0], QImage.Format_RGB888)
        self.px1 = QPixmap.fromImage(self.image)
        self.ui.img_5.setIcon(QIcon(self.px1))
        self.ui.img_5.setIconSize(QSize(150,150))

        #Hueless
        self.Hueless = filter.Hueless(self.img)
        self.image = QImage(self.Hueless ,self.img.shape[1], self.img.shape[0], QImage.Format_RGB888)
        self.px1 = QPixmap.fromImage(self.image)
        self.ui.img_6.setIcon(QIcon(self.px1))
        self.ui.img_6.setIconSize(QSize(150,150))

        #Greenless
        self.Greenless = filter.Greenless(self.img)
        self.image = QImage(self.Greenless ,self.img.shape[1], self.img.shape[0], QImage.Format_RGB888)
        self.px1 = QPixmap.fromImage(self.image)
        self.ui.img_7.setIcon(QIcon(self.px1))
        self.ui.img_7.setIconSize(QSize(150,150))

        #blueless
        self.Blueless = filter.Blueless(self.img)
        self.image = QImage(self.Blueless ,self.img.shape[1], self.img.shape[0], QImage.Format_RGB888)
        self.px1 = QPixmap.fromImage(self.image)
        self.ui.img_8.setIcon(QIcon(self.px1))
        self.ui.img_8.setIconSize(QSize(150,150))

        #Redless
        self.Redless = filter.Redless(self.img)
        self.image = QImage(self.Redless ,self.img.shape[1], self.img.shape[0], QImage.Format_RGB888)
        self.px1 = QPixmap.fromImage(self.image)
        self.ui.img_9.setIcon(QIcon(self.px1))
        self.ui.img_9.setIconSize(QSize(150,150))

        self.ui.img_1.clicked.connect(self.select)
        self.ui.img_2.clicked.connect(self.select)
        self.ui.img_3.clicked.connect(self.select)
        self.ui.img_4.clicked.connect(self.select)
        self.ui.img_5.clicked.connect(self.select)
        self.ui.img_6.clicked.connect(self.select)
        self.ui.img_7.clicked.connect(self.select)
        self.ui.img_8.clicked.connect(self.select)
        self.ui.img_9.clicked.connect(self.select)
    
    def select(self):
        mode = int(self.sender().objectName().split('_')[-1])
        if mode == 1:
            cv2.imwrite(f'database/db_img/{self.name}.jpg', self.red)
        elif mode == 2:
            cv2.imwrite(f'database/db_img/{self.name}.jpg', self.anime)
        elif mode == 3:
            cv2.imwrite(f'database/db_img/{self.name}.jpg', self.blur)
        elif mode == 4:
            cv2.imwrite(f'database/db_img/{self.name}.jpg', self.anime1)
        elif mode == 5:
            cv2.imwrite(f'database/db_img/{self.name}.jpg', self.normal)
        elif mode == 6:
            cv2.imwrite(f'database/db_img/{self.name}.jpg', self.Hueless)
        elif mode == 7:
            cv2.imwrite(f'database/db_img/{self.name}.jpg', self.Greenless)
        elif mode == 8:
            cv2.imwrite(f'database/db_img/{self.name}.jpg', self.Blueless)
        elif mode == 9:
            cv2.imwrite(f'database/db_img/{self.name}.jpg', self.Redless)
        self.ui = MainWindow()


class Edit_Employee(QWindow):
    def __init__(self, id):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('UI/edit_emp.ui', None)
        self.ui.show()
        self.id = id
        self.employee = database.employee_detail(self.id)[0]

        self.ui.firstname.setText(self.employee[1])
        self.ui.lastname.setText(self.employee[2])
        self.ui.code.setText(str(self.employee[4]))

        self.ui.year.clear()
        for i in range(1900, 2023, 1):
            self.ui.year.addItem(str(i))

        birthday = list(self.employee[3].split(','))
        self.ui.year.setCurrentText(birthday[2])
        self.ui.month.setCurrentText(birthday[1])
        self.ui.day.setCurrentText(birthday[0])

        self.ui.img_eff_btn.clicked.connect(self.effect)
        self.ui.edit_btn.clicked.connect(self.edit)
        self.ui.cancel_btn.clicked.connect(self.cancel)

    def effect(self):
        img = cv2.imread(f'database/db_img/{self.employee[1]+self.employee[2]}.jpg')
        self.ui = Filters(img, self.employee[1]+ self.employee[2])


    def edit(self):
        firstname = self.ui.firstname.text()
        lastname = self.ui.lastname.text()
        code = self.ui.code.text()
        day = self.ui.day.currentText()
        month = self.ui.month.currentText()
        year = self.ui.year.currentText()
        birthday = day + ',' + month + ',' + year
        database.update(self.id, firstname, lastname, birthday, code, img_path=f'{firstname+lastname}.jpg')
        self.ui = MainWindow()

    def cancel(self):
        self.ui = MainWindow()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui =loader.load('UI/emp_list.ui', None)
        self.ui.show()

        self.ui.add_user_btn.clicked.connect(self.add_user)
        self.readFromDataBase()

    def add_user(self):
        self.ui = Add_Employee()
    
    def readFromDataBase(self):
        result = database.employees()
        for i in range(len(result)):
            id_label = QLabel()
            id_label.setText(str(result[i][0]))

            name_label = QLabel()
            name_label.setText(result[i][1] + ' ' + result[i][2])

            edit_btn = QPushButton()
            edit_btn.setStyleSheet('border:0px;')
            edit_btn.setObjectName(f'edit_btn_{result[i][0]}')
            edit_btn.setIcon(QIcon('UI/icon/edit_black.png'))
            edit_btn.clicked.connect(self.edit)

            delete_btn = QPushButton()
            delete_btn.setStyleSheet('border:0px;')
            delete_btn.setObjectName(f'delete_btn_{result[i][0]}')
            delete_btn.setIcon(QIcon('UI/icon/delete.png'))
            delete_btn.clicked.connect(self.delete)

            avr_btn = QPushButton()
            avr_btn.setStyleSheet('max-width: 75px; min height: 75px; border: 0px; border-radius: 30px')
            avr_btn.setIcon(QIcon(f'database/db_img/{result[i][5]}'))
            avr_btn.setIconSize(QSize(75,75))

            self.ui.grid_list.addWidget(id_label, i, 0)
            self.ui.grid_list.addWidget(avr_btn, i, 1)
            self.ui.grid_list.addWidget(name_label, i, 2)
            self.ui.grid_list.addWidget(edit_btn, i, 3)
            self.ui.grid_list.addWidget(delete_btn, i, 4)

    def edit(self):
        id = self.sender().objectName().split('_')[-1]
        self.ui = Edit_Employee(id)

    def delete(self):
        id = self.sender().objectName().split('_')[-1]
        database.delete(id)
        self.clearUI_employee()
        self.readFromDataBase()

    def clearUI_employee(self):
        for i in reversed(range(self.ui.grid_list.count())):
            self.ui.grid_list.itemAt(i).widget().deleteLater()


if __name__ == '__main__':
    app = QApplication([])
    window = Login()
    app.exec()