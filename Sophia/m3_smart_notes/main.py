from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

app = QApplication([])

# окно приложения
notes_win = QWidget()
notes_win.setWindowTitle('Умные заметки')
notes_win.resize(900, 600)

# виджеты окна приложения
list_notes_label = QLabel('Список заметок')
list_notes = QListWidget()
button_note_create = QPushButton('Создать заметку')
button_note_del = QPushButton('Удалить заметку')
button_note_save = QPushButton('Сохранить заметку')

list_tags_label = QLabel('Список тегов')
list_tags = QListWidget()
field_tag = QLineEdit()
field_tag.setPlaceholderText('Введите тег...')

button_tag_add = QPushButton('Добавить к заметке')
button_tag_del = QPushButton('Открепить от заметки')
button_tag_search = QPushButton('Искать заметки по тегу')

field_text = QTextEdit()  # окно для ввода текста

# расположение виджетов по линиям
layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_2 = QVBoxLayout()

# колонка 1
col_1.addWidget(field_text)

# колонка 2
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)

row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)

row_2 = QHBoxLayout()
row_2.addWidget(button_note_save)

col_2.addWidget(row_1)
col_2.addWidget(row_2)

col_2.addWidget(list_tags_label)
col_2.addWidget(list_tags)
col_2.addWidget(field_tag)

row_3 = QHBoxLayout()
row_4 = QHBoxLayout()

row_3.addWidget(button_tag_add)
row_3.addWidget(button_tag_del)
row_4.addWidget(button_tag_search)



