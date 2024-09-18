from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import *

class Question:

    def __init__(self, question, right_answer,wrong1, wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

q1 = Question('Государственный язык Бразилии', 'Португальский', 'Английский', 'Испанский','Бразильский')
q2 = Question('Какого цвета нет на флаге России','Зеленый','Красный','Голубой','Белый')
q3 = Question('Какой рукой мешают чай', 'Ложкой','Правой','Левой','Обеими')
q4 = Question('Год основания Москвы','1147','889','1251',"955")


question_list = [q1, q2, q3, q4]

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_ok.setText('Следующий вопрос')


def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_ok.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)


def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()


def check_answer():
    if answers[0].isChecked():
        show_correct('Праильно!')
        window.score += 1
        print(f'Статистика\nВсего вопросов:{window.total}\nПравильных ответов')
    elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct('Непраильно!')
        print(f'Рейтинг: {window.score/window.total*100}%')

def next_question():
    window.total += 1
    print(f'Статистика\nВсего вопросов:{window.total}\nПравильных ответов:{window.score}')
    cur_question = randint(1, len(question_list)-1)
    q = question_list[cur_question]
    ask(q)


def click_OK():
    if btn_ok.text() == 'Ответить':
        check_answer()
    else:
        next_question()


app = QApplication([])
window = QWidget()
window.resize(400,400)
window.setWindowTitle('MemoryCard')


lb_question = QLabel('В каком году основана Москва?')
btn_ok = QPushButton('Ответить')


RadioGroupBox = QGroupBox("Варианты ответов:")
rbtn1 = QRadioButton("Вариант 1")
rbtn2 = QRadioButton("Вариант 2")
rbtn3 = QRadioButton("Вариант 3")
rbtn4 = QRadioButton("Вариант 4")

answers = [rbtn1, rbtn2, rbtn3, rbtn4]


RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)


AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('Прав ты или нет?')
lb_Correct = QLabel('Ответ будет здесь')


layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result)
layout_res.addWidget(lb_Correct)
AnsGroupBox.setLayout(layout_res)



layout_ans1 = QHBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()

layout_ans2.addWidget(rbtn1)
layout_ans2.addWidget(rbtn2)
layout_ans3.addWidget(rbtn3)
layout_ans3.addWidget(rbtn4)


layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)


RadioGroupBox.setLayout(layout_ans1)


layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()


layout_line1.addWidget(lb_question, alignment=Qt.AlignCenter)
layout_line2.addWidget(RadioGroupBox)
layout_line3.addStretch(1)
layout_line3.addWidget(btn_ok, stretch=2)
layout_line3.addStretch(1)
layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_line3.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_line3.addStretch(1)
layout_card.setSpacing(5)



window.score = 0
window.total = 0


btn_ok.clicked.connect(click_OK)
next_question()



window.setLayout(layout_card)
window.show()
app.exec()