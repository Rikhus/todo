#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os,sys
home=os.getenv("HOME")
#if(os.path.isfile(home+'/.todo/todo')):
filename=home+'/.todo/todo'
if len(sys.argv)==1:
    todolist=open(filename,'r')
    i=0
    for todo in todolist:
        print(str(i)+'.',todo)
        i+=1
    todolist.close()
    
elif sys.argv[1] == "-a" or sys.argv[1]== "--add":
    todolist=open(filename,'a')
    todo=""
    for word in sys.argv[2:]:
        todo+=word+" "   
    todo+="\n"
    todolist.write(todo)
    todolist.close()
elif sys.argv[1]== "-r" or sys.argv[1]== "--remove":
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
    if int(sys.argv[2])<len(todos):
        for j in range(len(todos)):
            if(j!=int(sys.argv[2])):
                strToDo+=todos[j]
        todolist.write(strToDo)
    else:
        print('Не существует задачи под этим номером')
        for j in range(len(todos)):
            strToDo+=todos[j]
        todolist.write(strToDo)
    todolist.close()
