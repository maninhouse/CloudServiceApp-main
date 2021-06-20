from app import app
from flask import render_template,request
import tkinter as tk
from tkinter import Message, filedialog
import os
import random


@app.route('/')
def index():
    return render_template('public/index.html',message = '')

@app.route('/', methods=['POST']) 
def send_ans():
    level = request.form.get('level_selector')
    print('level:',level)
    ans = request.values.get('input_password')
    keys = ['H', 'B', 'D']
    
    if level == '1':
        if ans == 36 or ans == '36':
            correct_message = '恭喜通過第{LEVEL}關! 這關的key是「{KEY}」'.format(LEVEL=level,KEY=keys[int(level)-1])
            return render_template('public/index.html', message = correct_message)            
    elif level == '2':
        if ans == 'B聖誕節':
            correct_message = '恭喜通過第{LEVEL}關! 這關的key是「{KEY}」'.format(LEVEL=level,KEY=keys[int(level)-1])
            return render_template('public/index.html', message = correct_message)        
    elif level == '3':
        if ans == 'C':
            correct_message = '恭喜通過第{LEVEL}關! 這關的key是「{KEY}」'.format(LEVEL=level,KEY=keys[int(level)-1])
            return render_template('public/index.html', message = correct_message)
    return render_template('public/index.html', message = '密碼輸入錯誤喔!再試試看吧!')

@app.route('/I_told_you')
def cute():
    img_num = random.randint(1,9)

    return render_template('public/cute.html',message = img_num)

@app.route('/hidden_mission')
def mission():
    return render_template('public/index_hidden.html')

@app.route('/hidden_mission', methods=['POST']) 
def check_pwd():
    ans = request.values.get('input_password')
    if ans == "HBD" or ans == "hbd":
        return render_template('public/letter.html')
    return render_template('public/index_hidden.html', message = '密碼輸入錯誤喔!再試試看吧!')
