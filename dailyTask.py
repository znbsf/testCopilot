#日常任务
import os.path
import json

filename = "Task.json"

from datetime import date, datetime, timedelta

taskDict = {}

def addTask( task ):
    global taskDict
    print("Add Task ："+task)
    taskDict[task] = False
    with open(filename, "w") as json_file:
        json_dict = json.dump(taskDict, json_file)

def deleteTask( task ):
    global taskDict
    if task in taskDict:
        del taskDict[task]
        with open(filename, "w") as json_file:
            json_dict = json.dump(taskDict, json_file)
    else:
        print("Task not found")

def changeTaskStatus( task ):
    global taskDict
    if task in taskDict:
        taskDict[task] = not taskDict[task]
        with open(filename, "w") as json_file:
            json_dict = json.dump(taskDict, json_file)
    else:
        print("Task not found")

def taskStatus():
    global taskDict
    #打印分割线
    print("-"*50)
    print("Today is "+str(date.today()))
    print("-"*50)
    for i in taskDict:
        if i != "nowDate":
            if taskDict[i] == True:
                print(i+" is done")
            else:
                print(i+" is not done")
    print("-"*50)
    print("Daily Task is done? "+str(taskDict["nowDate"] == str(date.today())))
    print("-"*50)
    print("Task Status:")  #打印任务状态
    for i in taskDict:
        print(i + " is "+str(taskDict[i]))

def dailyInit():
    global taskDict
    if os.path.exists(filename):
        with open(filename, "r") as json_file:
            taskDict = json.load(json_file)
        if "nowDate" in taskDict:
            print("Daily Task already initialized")
            if taskDict["nowDate"] != str(date.today()):
                taskDict["nowDate"] = str(date.today())
                for i in taskDict:
                    if i != "nowDate":
                        taskDict[i] = False
                with open(filename, "w") as json_file:
                    json_dict = json.dump(taskDict, json_file)
        else:
            print("nowDate not found")
            taskDict["nowDate"] = str(date.today())
            print("Daily Task initialized "+str(taskDict))
            with open(filename, "w") as json_file:
                json_dict = json.dump(taskDict, json_file)
    else:
        print("Task.json not found")
        taskDict["nowDate"] = str(date.today())
        with open(filename, "w") as json_file:
            json_dict = json.dump(taskDict, json_file)
            print("Daily Task initialized "+str(taskDict))

if __name__=='__main__':
    dailyInit()
    # addTask("test1")
    taskStatus()
    while True:
        #判断是添加任务还是改变任务状态
        task = input("Please input add , delete, status or change :")
        if task == "":
            break   #输入空字符串退出
        if task == "add":
            task = input("Please input task:")
            addTask(task)   #添加任务
        elif task == "status":
            taskStatus()   #打印任务状态
        elif task == "change":
            task = input("Please input task to be changed:")
            changeTaskStatus(task)   #改变任务状态
        elif task == "delete":
            task = input("Please input task to be deleted:")
            deleteTask(task)
        else:
            print("Invalid input")
            continue    #输入非法字符串继续循环
    print("Daily Task finished")