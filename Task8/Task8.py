import os
class Task8:
    def aaa(directory,filename):
        path=os.path.join(directory,filename)
        if not os.path.exists(path):
            os.makedirs(directory,exist_ok=True)
            with open(path,'w') as file:
                file.writh("This is created file.")
        with open(path,"r") as file:
            content=file.read()
        return content

    def read_usernames(fileName):
        with open(fileName,'r') as file:
            for line in file:
                username=line.strip()
                yield username


    class RestrictedArray(list):
        def __getitem__(self, item):
            length=len(self)
            if index >=int(length*0.1):
                return super().__getitem__(index)
            else:
                raise IndexError("Access denied")

    usernames = RestrictedArray(
        ["user1", "user2", "user3", "user4", "user5", "user6", "user7", "user8", "user9", "user10", "user11", "user12",
         "user13"])

    try:
        restricted=usernames[:int(len(usernames)*0.9)]
        print(restricted)
    except IndexError as e:
        print(e)
        #4
        #5
    #6
    def return_gmail(list):
        for i in list:
            if i.endswith('@gmail.com'):
                yield i

    #7
    def equal_email_username(file):
        for i in list:
            name,domain=i.split("@")
            if name in domain:
                yield i

    #8
    def check_username(name,list):
        ascii= [ord(char) for char in name]
        is_exist = name in list
        count = name.count("A")
        return is_exist, count

#9
    def Add_name_to_list(list):
        return all(list.isupper() for name in list)

  #10
    def calcuate_sum(customers):
        sum = 0
        group = 0
        x = 0
        for customer in customers:
            if customer % 8 == 0:
                sum += 200
                group += 1
                x = 0
            else:
                x += 1
        sum +=x*50
        return sum




