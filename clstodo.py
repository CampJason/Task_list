import json

class Task:
    counter = 1
    def __init__(self,task='',is_done=False):
        self.task = task
        self.is_done = is_done
        self.number = Task.counter
        Task.counter += 1
    
    def __repr__(self) -> str:
        return f'№ {self.number}: {self.task} {"DONE" if self.is_done else "" }'
    
class Tasklist:
    task_list = []

    def add_task(self,text):
        self.task_list.append(Task(text))

    def print_tasks(self):
        for i in self.task_list:
            print(i)    

    def del_task(self,del_num):
        for num, el in enumerate(self.task_list):
            if el.number == del_num:
                self.task_list.pop(num)

    def done_task(self, mark_num):
        for num, el in enumerate(self.task_list):
            if el.number == mark_num:
                el.is_done = True

    def unmark_task(self, unmark_num):
        for num, el in enumerate(self.task_list):
            if el.number == unmark_num:
                el.is_done = False
    
    def all_done_task(self):
        for num, el in enumerate(self.task_list):
            el.is_done = True

    def unmark_all_task(self):
        for num, el in enumerate(self.task_list):
            el.is_done = False

    def only_done(self):
        t = []
        for num, el in enumerate(self.task_list):
            if el.is_done == True:
                t.append(el)
        print('Successfully!')    
        print(t)

    def only_undone(self):
        t = []
        for num, el in enumerate(self.task_list):
            if el.is_done == False:
                t.append(el)
        print('Successfully!')    
        print(t)

    def fnd_task(self, find):
        temp_task = []
        for num, el in enumerate(self.task_list):
            if el.task in find:
                temp_task.append(el)
                print(temp_task)

    # def s_a_e(self,name):
    #     temp_task = []
    #     for num, el in enumerate(self.task_list):
    #         temp_task.append(el.task)
    #     with open(name+'.json', 'w') as savefile:
    #         json.dump(temp_task, savefile)

    # def ld_file(self,name):
    #     with open(name+'.json', 'r+') as loadfile:
    #         data=json.load(loadfile)
    #         for i in data:
    #             self.task_list.append(Task(i))             

class Saveload(Tasklist):
    def s_a_e(self,name):
        temp_task = []
        for num, el in enumerate(self.task_list):
            temp_task.append(el.task)
        with open(name+format, 'w') as savefile:
            format.dump(temp_task, savefile)
            temp_task.clear()

    def ld_file(self,name):
        with open(name+format, 'r+') as loadfile:
            data=format.load(loadfile)
            for i in data:
                self.task_list.append(Task(i)) 


class SLjson(Saveload):
    def s_a_e(self, name):
        temp_task = []
        for num, el in enumerate(self.task_list):
            temp_task.append(el.task)
        with open(name+'.json', 'w') as savefile:
            json.dump(temp_task, savefile)
            temp_task.clear()

    def ld_file(self,name):
        with open(name+'.json', 'r+') as loadfile:
            data=json.load(loadfile)
            for i in data:
                self.task_list.append(Task(i))    

class SLtxt(Saveload):
    def s_a_e(self, name):
        temp_task = []
        for num, el in enumerate(self.task_list):
            temp_task.append(el.task)
        temp = str(temp_task)
        with open(name+'.txt', 'w') as savefile:
            savefile.write(temp)

    def ld_file(self,name):
        with open(name+'.txt', 'r+') as loadfile:
            for i in loadfile:
                self.task_list.append(Task(i))  
