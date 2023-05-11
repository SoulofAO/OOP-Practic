from PyQt5 import QtWidgets

# создаем приложение
app = QtWidgets.QApplication([])

# создаем окно
window = QtWidgets.QWidget()

# создаем QComboBox
combo_box = QtWidgets.QComboBox()

# добавляем элементы в QComboBox
combo_box.addItem("Option 1")
combo_box.addItem("Option 2")
combo_box.addItem("Option 3")

# добавляем QComboBox на окно
layout = QtWidgets.QVBoxLayout(window)
layout.addWidget(combo_box)

# показываем окно
window.show()

# получаем выбранный элемент из QComboBox
selected_item = combo_box.currentText()
print(selected_item)

# запускаем главный цикл приложения
app.exec_()
