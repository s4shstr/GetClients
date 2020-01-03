#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import io
import codecs
import html2text
import codecs
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os
from getpass import getpass
import pyautogui,time


BLOCKSIZE = 1048576
str1 = '['
str2 = '.'
k = 0
firstClient = 'textzgdfnzfgn'
flag = False
temppath = os.getenv('TEMP')


#get html web-page
br = webdriver.Chrome('C:\chromedriver.exe')
br.get('https://wiki.itfb.ru/display/CLIEN/Clients')

pyautogui.keyDown('alt')
time.sleep(.2)
pyautogui.press('tab')
time.sleep(.2)
pyautogui.keyUp('alt')

s_username = br.find_element_by_id('os_username')
s_password = br.find_element_by_id('os_password')
s_continue = br.find_element_by_id('loginButton')
s_username.send_keys(str(input('Введите логин: ')))
s_password.send_keys(str(getpass('Введите пароль: ')))
s_continue.click()

page = br.page_source
file = codecs.open(temppath + '/clients.html', 'w', encoding = 'utf-8')
file.write(page)
file.close()
br.quit()


#conversion html to txt
html = codecs.open(temppath + '/clients.html', 'r', 'utf-8')
f = html.read()
w = open(temppath + '/Clients.txt', 'w')
w.write(html2text.html2text(f))
html.close()
w.close()


#conversion to utf-8
with codecs.open(temppath + '/Clients.txt', 'r', 'cp1251') as sourceFile:
    with codecs.open(temppath + '/Clients_new.txt', 'w', 'utf8') as targetFile:
        while True:
            contents = sourceFile.read(BLOCKSIZE)
            if not contents:
                break
            targetFile.write(contents)  


#finding clients on txt file
with io.open(temppath + '/Clients_new.txt', encoding='utf-8') as file:
    for line in file:
        if flag == True:
            break
        if str1 in line:
            for i in range(len(line)):
                if str1 == line[i]:
                    if str2 == line[i + 4] and firstClient != line[i + 1 : i + 4]:
                        k = k + 1
                        if k == 1:
                            firstClient = line[i + 1 : i + 4]
                        print(line[i + 1 : i + 4])
                    if str2 == line[i + 5] and firstClient != line[i + 1 : i + 5]:
                        k = k + 1
                        if k == 1:
                            firstClient = line[i + 1 : i + 5]
                        print(line[i + 1 : i + 5])
                if (firstClient == line[i + 1 : i + 4] or firstClient == line[i + 1 : i + 5]) and k > 1:
                    flag = True
                    break
print("Колическо компаний: " + str(k))