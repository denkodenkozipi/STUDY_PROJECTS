import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,  # Текстовая метка
    QPushButton,  # Кнопка
    QLineEdit,  # Поле для ввода текста
    QVBoxLayout,  # Вертикальная компоновка
    QHBoxLayout,  # Горизонтальная компоновка
    QMessageBox,  # Уведомление
)


# noinspection PyUnresolvedReferences
class Window(QWidget):

    def __init__(self):
        super().__init__()

        # параметры окна
        self.setWindowTitle("Авторизация")
        self.resize(400, 350)

        # объявление атрибутов
        self.line_user = None
        self.line_psw = None
        self.button_ok = None

        # присваивание
        self.setLayout(self.interface_manager())

    @staticmethod
    def layout_hello_manager():
        # метка приветствия
        label_hello = QLabel("Добро пожаловать!")
        label_pls = QLabel("Пожалуйста введите данные для авторизации")

        # компоновка преветствия по X
        layout_hello = QHBoxLayout()
        layout_hello.addStretch()
        layout_hello.addWidget(label_hello)
        layout_hello.addStretch()

        # компоновка просьбы по X
        layout_pls = QHBoxLayout()
        layout_pls.addStretch()
        layout_pls.addWidget(label_pls)
        layout_pls.addStretch()

        # компоновка приветствия и просьбы по Y
        layout_hello_pls = QVBoxLayout()
        layout_hello_pls.addStretch()
        layout_hello_pls.addLayout(layout_hello)
        layout_hello_pls.addLayout(layout_pls)

        return layout_hello_pls

    def layout_user_manager(self):
        # метки связанные с user
        label_user = QLabel("Введите имя")
        self.line_user = QLineEdit("Иван")

        # компоновка по таблички "введите имя" по X
        layout_user_h = QHBoxLayout()
        layout_user_h.addStretch()
        layout_user_h.addWidget(label_user)
        layout_user_h.addStretch()

        # компоновка имени и вводного поля по Y
        layout_user_v = QVBoxLayout()
        layout_user_v.addStretch()
        layout_user_v.addLayout(layout_user_h)
        layout_user_v.addWidget(self.line_user)
        layout_user_v.addStretch()

        return layout_user_v

    def layout_psw_manager(self):
        # метки связанные с Password
        label_psw = QLabel("Введите пароль")
        self.line_psw = QLineEdit("12345")

        # компоновка таблички "введите пароль" по X
        layout_psw_h = QHBoxLayout()
        layout_psw_h.addStretch()
        layout_psw_h.addWidget(label_psw)
        layout_psw_h.addStretch()

        # компоновка таблички и вводного поля по Y
        layout_psw_v = QVBoxLayout()
        layout_psw_v.addStretch()
        layout_psw_v.addLayout(layout_psw_h)
        layout_psw_v.addWidget(self.line_psw)
        layout_psw_v.addStretch()

        return layout_psw_v

    def layout_button_manager(self):
        # метка кнопки
        self.button_ok = QPushButton("Подтвердить")

        # компоновка кнопки по X
        layout_button = QHBoxLayout()
        layout_button.addStretch()
        layout_button.addWidget(self.button_ok)
        layout_button.addStretch()

        self.button_ok.clicked.connect(self.check_data)

        return layout_button

    def interface_manager(self):

        # присваивание функций
        layout_hello_pls = self.layout_hello_manager()
        layout_user = self.layout_user_manager()
        layout_psw = self.layout_psw_manager()
        layout_button = self.layout_button_manager()

        # компоновка всех layout по горизонтали
        layout_h = QHBoxLayout()
        layout_h.addStretch()
        layout_h.addLayout(layout_user)
        layout_h.addLayout(layout_psw)
        layout_h.addStretch()

        # конечная компоновка всех layout
        layout_main = QVBoxLayout()
        layout_main.addLayout(layout_hello_pls)
        layout_main.addLayout(layout_h)
        layout_main.addStretch()
        layout_main.addLayout(layout_button)

        return layout_main
    
    def check_data(self):
        # сохранение данные из поля
        data_user = self.line_user.text()
        data_psw = self.line_psw.text()

        # ошибка пустого ввода
        if not data_user or not data_psw:
            QMessageBox.warning(self, "Ошибка!", "Введите данные")
            return

        # если логин и пароль верны, то успешно
        if data_user == "Иван" and data_psw == '12345':
            QMessageBox.information(self, "Успех", "Авторизация прошла успешно!")
            return
        # если логин или пароль не верны ошибка
        else:
            QMessageBox.critical(self, "Ошибка", "Не верный логин или пароль!")
            return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
