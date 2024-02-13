import sys
import random
import datetime
from docx import Document
import io

class Decorators:

    def __init__(self,data):
        self.data=data
#1
    def error(self,exc):
        try:
            with open('nonexistent_file.txt', 'r') as f:
                content = f.read()
        except FileNotFoundError:
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            error_message = f"<malki, {current_time}>{e}<Tami&Miri>"
            print(error_message)
        try:
            num = int('abc')
        except ValueError:
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            error_message = f"<malki, {current_time}>{e}<Tami&Miri>"
            print(error_message)
        try:
            my_list = [1, 2, 3]
            print(my_list[4])
        except IndexError:
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            error_message = f"<malki, {current_time}>{e}<Tami&Miri>"
            print(error_message)
        try:
            some_variable = undefined_variable
        except NameError:
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            error_message = f"<malki, {current_time}>{e}<Tami&Miri>"
            print(error_message)
    #2
    def read_docx_file(file_path):
        doc = Document(file_path)
        paragraphs = [para.text for para in doc.paragraphs]
        return paragraphs

#3 לא טוב
    def random(product,count,payment_range):
        sales = random.randint(0, count)
        highest_payment = random.randint(*payment_range)
        return sales, highest_payment
#4
    def print_version(self):
        print(sys.version)
#5
    def handle_parameters(*args,**kwargs):
        for arg in args:
            if isinstance(arg,int):
                print(arg)
        return kwargs

#6
def prints(self,data):
    print("Table")
    for i in range(3):
        for row in self.data:
            prints(row)
    for i in range(3):
            prints(self.data[i])
    for i in range(-2,0):
            prints(self.data[i])
    import random
    random=random.choice(self.data)
    print(random)
#7
def oneLoop(self):
    malki=[item for row in table for item in row if isinstance(item,(int,float))]
    print(malki)
    



