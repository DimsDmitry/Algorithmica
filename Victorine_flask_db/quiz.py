# -*- coding: utf-8 -*-

from flask import Flask, redirect, url_for, session, request, render_template
from db_scripts import *
from random import randint, shuffle
import os


def quiz_form():
    q_list = get_quizes()
    return render_template('start.html', q_list=q_list)


def index():
    if request.method == 'GET':
        session['quiz_id'] = -1
        return quiz_form()
    if request.method == 'POST':
        session['quiz_id'] = request.form.get("quiz")
        session['last_question'] = 0
        session['total'] = 0
        session['correct'] = 0
        return redirect(url_for('test'))


def question_form(question):
    quest_id, question, *answers_list = question
    shuffle(answers_list)
    return render_template('test.html', question=question, quest_id=quest_id, answers_list=answers_list)


def save_answers():
    answer = request.form.get('ans_text')
    quest_id = request.form.get('q_id')
    session['last_question'] = quest_id
    session['total'] += 1
    if check_answer(quest_id, answer):
        session['correct'] += 1


def test():
    if not ('quiz_id' in session) or int(session['quiz_id']) < 0:
        return redirect(url_for('index'))
    if request.method == "POST":
        save_answers()
    question = get_question_after(session['quiz_id'], session['last_question'])
    print(question)
    if question:
        return question_form(question)
    else:
        return redirect(url_for('result'))


def result():
    return '<h1>Результат викторины</h1><p>Всего: ' + str(session['total']) + '</p><p>Правильно: ' + str(
        session['correct']) + '</p>'


# Создаём объект веб-приложения:
folder = os.getcwd()
app = Flask(__name__, static_folder=folder, template_folder=folder)

app.add_url_rule('/', 'index', index, methods=['POST', 'GET'])
app.add_url_rule('/test', 'test', test, methods=['POST', 'GET'])
app.add_url_rule('/result', 'result', result)
app.config['SECRET_KEY'] = 'DeadMenTellNoSecrets'

if __name__ == "__main__":
    # Запускаем веб-сервер:
    app.run()
