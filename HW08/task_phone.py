
from csv import DictReader, DictWriter
from os.path import exists

def create_file():
    with open("Phone.csv", "w", encoding= "utf-8")  as data:
        f_writer = DictWriter(data, fieldnames= ['Фамилия', 'Имя', 'Номер'])
        f_writer.writeheader()

def get_info():
    info = ['Иванов', 'Иван', '12-18-18']
    return info

def read_file(file_name):
    with open(file_name, encoding= "utf-8")  as data:
        f_reader = DictReader(data)
        res = list(f_reader)
    return res

def write_file(file_name, lst):
    with open(file_name, encoding= "utf-8")  as data:
        f_reader = DictReader(data)
        res = list(f_reader)
    obj = {"Фамилия": lst[0], "Имя": lst[1], "Номер": lst[2]}
    res.append(obj)
    with open("Phone.csv", "w", encoding= "utf-8")  as data:
        f_writer = DictWriter(data, fieldnames= ['Фамилия', 'Имя', 'Номер'])
        f_writer.writeheader()
        f_writer.writerows(res)

def main():
    while True:
        command = input("Введите команду: ")
        if command == "q":
            break
        elif command == "r":
            if not exists("Phone.csv"):
                break
            print(read_file("Phone.csv"))
        elif command == "w":
            if not exists("Phone.csv"):
                create_file()
            get_info()
            write_file()

main()
