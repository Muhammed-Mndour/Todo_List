from datetime import datetime, timedelta
from math import log10, isinf
from posixpath import split
import math
from traceback import print_tb
from typing import runtime_checkable

import numpy as np
from numpy.compat import contextlib_nullcontext


class Task:

    def __init__(self, title, description, priority, category, deadline):
        self.id = 0
        self.title = title
        self.description = description
        self.status = 'Pending'
        self.priority = priority
        self.category = category
        self.created = datetime.now()
        self.is_deleted = False
        self.deadline = deadline

    def __repr__(self):
        return (f'* title: {self.title}\n'
                f'* description: {self.description}\n'
                f'* status: {self.status}\n'
                f'* priority: {self.priority}\n'
                f'* category: {self.category}\n'
                f'* created: {self.created}\n'
                f'* Id: {self.id}\n'
                f'* deadline: {self.deadline}\n')


class Todo:

    def __init__(self):
        self.x = 1
        self.tasks = []
        self.cnt = 0

    def __getitem__(self, index):
        out = self.tasks[index]
        return out

    def __setitem__(self, index, value):
        self.tasks[index] = value

    def __len__(self):
        return len(self.tasks)

    def __repr__(self):
        x = 0;
        for i in self.tasks:
            if (i.is_deleted == True):
                continue
            else:
                x = x + 1
                print(f'Task Number{x}:\n{i}')

        return ''

    def AddTasks(self, task):
        task.id = self.cnt
        self.cnt = self.cnt + 1
        self.tasks.append(task)
        return True

    # return the correct index in todo list
    # one based
    def Search_by_index(self, number):
        for task in self.tasks:
            if task.is_deleted == True:
                continue
            else:
                number = number - 1
                if number == 0:
                    return task.id
                    break
        return -1

    def Delete_Task(self, number):
        index = self.Search_by_index(number)
        try:
            self.tasks[index].is_deleted = True
            return True
        except IndexError:
            return False

    def Search_Task_by_Title(self, title):
        for i in range(self.tasks.__len__()):
            if self.tasks[i].title == title:
                return self.tasks[i]
        return False

    def Show_Missed_Tasks(self):
        missed = Todo()
        now = datetime.now()  # Capture the current time once
        for task in self.tasks:
            if task.deadline < now and not task.is_deleted:
                missed.AddTasks(task)
        return missed

    def Sort(self, type):
        # Status
        if type == 1:
            for task in self.tasks:
                if (task.status == 'Pending'): print(task)
            for task in self.tasks:
                if (task.status == 'In progress'): print(task)
            for task in self.tasks:
                if (task.status == 'Completed'): print(task)
        # Priority
        elif type == 2:
            for task in self.tasks:
                if (task.priority == 'High'): print(task)
            for task in self.tasks:
                if (task.priority == 'Medium'): print(task)
            for task in self.tasks:
                if (task.priority == 'Low'): print(task)
        # Creation date
        elif type == 3:
            sortedList = self.tasks
            sortedList.sort(key=lambda task: task.created)
            for task in sortedList: print(task)

        elif type == 4:
            sortedList = self.tasks
            sortedList.sort(key=lambda task: task.deadline)
            for task in sortedList: print(task)

    def Filster(self, filter):
        # Status
        if filter == 1:
            while 1:
                x = input('1-Pending 2-In progress 3-Completed  4-Exit\n')
                try:
                    x = int(x)
                except ValueError:
                    print('Invalid Input')
                    continue

                if x < 1 or x > 4:
                    print('Invalid Input')
                    continue

                if x == 4:
                    print('Exit')
                    break

                cnt = int(0)
                if x == 1:
                    for task in self.tasks:
                        if (task.status == 'Pending'):
                            print(task)
                            cnt = cnt + 1
                elif x == 2:
                    for task in self.tasks:
                        if (task.status == 'In progress'):
                            print(task)
                            cnt = cnt + 1
                elif x == 3:
                    for task in self.tasks:
                        if (task.status == 'Completed'):
                            print(task)
                            cnt = cnt + 1

                if cnt == 0: print('Empty List')
                break
        # Priority
        else:
            while 1:
                x = input('1-High 2-Medium 3-Low  4-Exit\n')
                try:
                    x = int(x)
                except ValueError:
                    print('Invalid Input')
                    continue

                if x < 1 or x > 4:
                    print('Invalid Input')
                    continue

                if x == 4:
                    print('Exit')
                    break

                cnt = int(0)
                if x == 1:
                    for task in self.tasks:
                        if (task.priority == 'High'):
                            print(task)
                            cnt = cnt + 1
                elif x == 2:
                    for task in self.tasks:
                        if (task.priority == 'Medium'):
                            print(task)
                            cnt = cnt + 1
                elif x == 3:
                    for task in self.tasks:
                        if (task.priority == 'Low'):
                            print(task)
                            cnt = cnt + 1

                if cnt == 0: print('Empty List')
                break


a = Task('t1', 'task1', 'High', 'Work', datetime.now() + timedelta(days=6))
b = Task('t2', 'task2', 'Medium', 'Personal', datetime.now() + timedelta(days=6))
c = Task('t3', 'task3', 'Low', 'Work', datetime.now())
d = Task('t4', 'task4', 'High', 'Personal', datetime.now() + timedelta(days=6))
e = Task('t5', 'task5', 'Medium', 'Personal', datetime.now() + timedelta(days=5))
f = Task('t6', 'task6', 'Low', 'Personal', datetime.now())
todo = Todo()
todo.AddTasks(a)
todo.AddTasks(b)
todo.AddTasks(c)
todo.AddTasks(d)
todo.AddTasks(e)
todo.AddTasks(f)
while 1:
    print("How could i help u ")
    print('1- add task')
    print('2- delete task')
    print('3- edit task')
    print('4- show tasks')
    print('5- Search for task')
    print('6- Show Missed Tasks')
    print('7- Sort')
    print('8- Filter')
    print('9- exit program')

    x = int(input())
    # add task
    if x == 1:
        title = input('Enter Task Title: ')
        description = input('Enter Task Description: ')

        # Priority
        while 1:
            priority = input('Enter Task Priority: '
                             '1- High    2-Medium   3-Low\n')
            try:
                priority = int(priority)
            except ValueError:
                print('Invalid Priority')
                continue

            if priority >= 1 and priority <= 3:
                if priority == 1:
                    priority = 'High'
                elif priority == 2:
                    priority = 'Medium'
                elif priority == 3:
                    priority = 'Low'
                break
            print('Invalid Priority')

        # Category
        while 1:
            category = input('Enter Task Category: '
                             '1- Work  2- Personal\n')
            try:
                category = int(category)
            except ValueError:
                print('Invalid Category')
                continue

            if category >= 1 and category <= 2:
                if category == 1:
                    category = 'Work'
                else:
                    category = 'Personal'
                break
            print('Invalid Category')

        # Deadline
        while 1:
            days = input('How many days do you want from now? : ')
            try:
                days = int(days)
            except ValueError:
                print('Invalid Days')
                continue
            deadline = datetime.now() + timedelta(days=days)
            break

        a = Task(title, description, priority, category, deadline)
        todo.AddTasks(a)
        print('Add task Completed')
    # delete task
    elif x == 2:
        print(todo)
        while 1:
            number = input('Enter Task Number: ')
            try:
                number = int(number)
            except ValueError:
                print('Invalid Number')
                continue

            if (todo.Delete_Task(number)):
                print('Deleted Successfully')
                break
            else:
                print('Not fount')
                continue

    # Edit task
    elif x == 3:
        print(todo)

        while 1:
            number = input('Enter Task Number: ')
            try:
                number = int(number)
            except ValueError:
                print('Invalid Number')
                continue

            index = todo.Search_by_index(number)
            try:
                task = todo[index]
            except IndexError:
                print('Not found')
                continue
            break

        while 1:
            op = input('1- Title\n'
                       '2- Description\n'
                       '3- Status\n'
                       '4- Priority\n'
                       '5- Category\n'
                       '6- Deadline\n'
                       '7- Exit Program\n')
            if op < '1' or op > '7':
                print('Invalid Operation')
                continue

            if (op == '1'):
                title = input('Enter Task Title: ')
                task.title = title

            elif (op == '2'):
                description = input('Enter Task Description: ')
                task.description = description
            # Status
            elif (op == '3'):
                # Pending, Completed, or In progress
                while 1:
                    status = input('Enter Task Status: '
                                   '1- Pending    2-Completed   3-In progress\n')
                    try:
                        status = int(status)
                    except ValueError:
                        print('Invalid Status')
                        continue

                    if status >= 1 and status <= 3:
                        if status == 1:
                            status = 'Pending'
                        elif status == 2:
                            status = 'Completed'
                        elif status == 3:
                            status = 'In progress'
                        task.status = status
                        break
                    print('Invalid Priority')


            elif (op == '4'):
                while 1:
                    priority = input('Enter Task Priority: '
                                     '1- High    2-Medium   3-Low\n')
                    try:
                        priority = int(priority)
                    except ValueError:
                        print('Invalid Priority')
                        continue

                    if priority >= 1 and priority <= 3:
                        if priority == 1:
                            priority = 'High'
                        elif priority == 2:
                            priority = 'Medium'
                        elif priority == 3:
                            priority = 'Low'
                        task.priority = priority
                        break
                    print('Invalid Priority')
            # Category
            elif (op == '5'):
                while 1:
                    category = input('Enter Task Category: '
                                     '1- Work  2- Personal\n')
                    try:
                        category = int(category)
                    except ValueError:
                        print('Invalid Category')
                        continue

                    if category >= 1 and category <= 2:
                        if category == 1:
                            category = 'Work'
                        else:
                            category = 'Personal'
                        task.category = category
                        break
                    print('Invalid Category')
            # Deadline
            elif (op == '6'):
                while 1:
                    days = input('How many days Do u want to add: ')
                    try:
                        days = int(days)
                    except ValueError:
                        print('Invalid Days')
                        continue
                    deadline = task.deadline + timedelta(days=days)
                    break
                task.deadline = deadline

            elif (op == '7'):
                break
            else:
                print('Invalid Input')
                continue

            todo[index] = task
            print('Edit Completed')
            print(task)

    # show tasks
    elif x == 4:
        print(todo)

    # Search for task
    elif x == 5:
        title = input('Enter Task Title: ')
        task = todo.Search_Task_by_Title(title)
        if task == False:
            print('Not found')
        else:
            print(task)
    # Show Missed Tasks
    elif x == 6:
        missed = todo.Show_Missed_Tasks()
        if missed.__len__() == 0:
            print('No Missed Tasks')
        else:
            print('Missed Tasks\n')
            print(missed)
    # Sort
    elif x == 7:
        while 1:
            sort_by = input('Enter Task Filter: \n'
                            '1-Status 2-Priority 3-Creation Date 4-Deadline 5-Exit\n')
            try:
                sort_by = int(sort_by)
            except ValueError:
                print('Invalid Filter')
                continue
            if sort_by < 1 or sort_by > 5:
                print('Invalid Filter')
                continue

            if sort_by == 5:
                break

            todo.Sort(sort_by)

    # Filter
    elif x == 8:
        while 1:
            filter = input('Enter Task Filter: \n'
                           '1-Status 2-Priority 3-Exit\n')
            try:
                filter = int(filter)
            except ValueError:
                print('Invalid Filter')
                continue
            if filter < 1 or filter > 3:
                print('Invalid Filter')
                continue

            if filter == 3:
                break

            todo.Filster(filter)

    elif x == 9:
        break

    else:
        print('Invalid Input')

# Core Features:
# Add Tasks: Allow the user to add tasks to the to-do list.
# View Tasks: Display all tasks in the to-do list.
# Mark Tasks as Completed: Let users mark tasks as done.
# Delete Tasks: Enable users to remove tasks from the list.
# Edit Tasks: Provide an option to update a task description.
# Search for Tasks: Search for tasks by title.
# Due Dates: Add deadlines or due dates for tasks.
# Task Sorting: Sort tasks by priority, status, or due date.
# Interactive Menu: Display a menu for the user to select actions easily.


# Save and Load: Save tasks to a file and load them when the app starts.


# task Variables:
#     Title
#     Description
#     Status: Pending, Completed, or In progress.
#     Priority: (High, Medium, Low).
#     Creation Date
#     Category:  Work, Personal.
#     deadline
