#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os,sys
home=os.getenv("HOME")
#if(os.path.isfile(home+'/.todo/todo')):
filename=home+'/.todo/todo'
try:
    test=open(filename,'r')
    test.close()
except:
    os.mkdir(home+'/.todo')
    test=open(filename,'w')
    test.close()

def returnTodo(filename):
    todolist=open(filename,'r')
    i=0
    s=''
    for todo in todolist:
        s+=str(i)+'. '+todo+'\n'
        i+=1
    todolist.close()
    return s

def addTodo(filename,todoForAdd):
    todolist=open(filename,'a')
    todo=""
    for word in todoForAdd:
        todo+=word 
    todo+="\n"
    todolist.write(todo)
    todolist.close()

def removeTodo(filename,todoToRemove):
    todolist=open(filename,'r')
    i=0
    todos=[]
    for todo in todolist:
        todos.append(todo)
        i+=1
    todolist.close()
    todolist=open(filename,'w')
    strToDo=""
    #print(todos)
    if int(todoToRemove)<len(todos):
        for j in range(len(todos)):
            if(j!=int(todoToRemove)):
                strToDo+=todos[j]
        todolist.write(strToDo)
        return True
    else:
        print('Cannot find this index')
        for j in range(len(todos)):
            strToDo+=todos[j]
        todolist.write(strToDo)
        return False
    todolist.close()

def commandLine(filename):
    print('***Select the action***\nl-print your ToDo\'s  a-add ToDo  d-delete ToDo  e-exit')
    command=input('>>> ')
    if command=='a':
        todoForAdd=str(input('write your ToDo: '))        
        if todoForAdd!='':
            addTodo(filename,todoForAdd)
            print('Added')
        else:
            print('Blank text!')
    elif command=='l':
        print(returnTodo(filename))
    elif command=='d':
        i=int(input('type the ToDo\'s index:'))
        removeTodo(filename,i)
        print('Removed')
    elif command=='e':
        exit(0)
    else:
        print('Incorrect command!')

while True:
    commandLine(filename)