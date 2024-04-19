import getpass
import sys
import datetime
from math import pi
import calendar
from datetime import date
import os.path
import struct
import platform
import os
import site
from os import listdir
from os.path import isfile, join
import getpass
import time
from math import sqrt


def get_string_formatted():
    print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are")

def get_sys_version():
    print("Python Version: ",sys.version)
    print("Version Info: ",sys.version_info)

def get_datetime():
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))

def get_radius():
    r = float(input("Radius: "))
    area = pi * (r ** 2)
    print("Area: ",area)

def get_fullname():
    fname = input("First Name: ")
    lname = input("Last Name: ")
    print(lname +str(" ")+ fname)

def get_numbers():
    numbers = input("Input a sequence of comma-separated numbers: ")
    numbers_list = numbers.split(",")
    numbers_tuple = tuple(numbers_list)
    print("List: ",numbers_list)
    print("Tuple: ",numbers_tuple)

def get_extension():
    filename = input("Filename: ")
    extension = filename.split(".")
    print("The extension of file is " + repr(extension[-1]))

def get_color_list():
    color_list = ["Red","Green","White" ,"Black"]
    print("%s %s" % (color_list[0], color_list[-1]))

def get_exam_st_date():
    exam_st_date = (11, 12, 2014)
    print("The examination will start from: %s-%s-%s" % (exam_st_date))

def compute_n():
    n = int(input("Input an integer: "))
    n1 = int("%s" % (n))
    n2 = int("%s%s" % (n,n))
    n3 = int("%s%s%s" % (n,n,n))
    ans = n1 + n2 + n3
    print(ans)

def get_calendar():
    year = int(input("Year: "))
    month = int(input("Month: "))
    print(calendar.month(year, month))

def get_no_escape():
    print("""a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example""")

def get_days():
    start_date = date(2014, 7, 2)
    end_date = date(2014, 7, 11)
    count = end_date - start_date
    print(count.days)
    print(count)

def get_diff():
    n = int(input("Input a number: "))
    diff = abs(17 - n)
    if n > 17:
        return diff * 2
    else:
        return diff

def get_sum():
    n1 = int(input("n1: "))
    n2 = int(input("n2: "))
    n3 = int(input("n3: "))
    sum = n1 + n2 + n3
    if n1 == n2 and n2 == n3 and n1 == n3:
        return sum * 3
    else:
        return sum

def get_is_string(text):
    new_text = ""
    if text[:2] == "Is":
        print(text)
    else:
        print("Is", text)

def get_copied_str(text,n):
    new_text = ""
    for i in range(n):
        new_text = new_text + text
    print(new_text)

def odd_or_even(n):
    if not isinstance(n,int) and not(isinstance(n,float)):
        print("Please input valid number")
    elif n % 2 == 0:
        print(n ,"is even number")
    elif n % 2 != 0:
        print(n ,"is an odd number")

def get_count(list):
    count = 0
    for i in list:
        if i == 4:
            count = count + 1
    print(count)

def get_char_2copy(text,n):
    new_text = ""
    if len(text) < 2:
        return text
    else:
        for i in range(n):
            new_text = new_text + text[:2]
        return new_text

def check_vowel(char):
    if char.lower() in ('aeiou'):
        print(char, "is vowel")
    else:
        print(char, "is not vowel")

def check_value(list, n):
    for i in list:
        if i == n:
            return True
    return False

def histogram(list):
    for i in list:
        print(i * "&")

def concat_list(list):
    new_text = ""
    for i in list:
        new_text = new_text + str(i)
    return new_text

def print_even():
    numbers = [
        386, 462, 47, 418, 907, 344, 236, 237, 823, 566, 597, 978, 328, 615, 953, 345,
        399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
        815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
        958, 743, 527
    ]
    for i in numbers:
        if i == 237:
            break
        elif i % 2 == 0:
            print(i)

def compare_color_list():
    color_list_1 = set(["White", "Black", "Red"])
    color_list_2 = set(["Red", "Green"])
    print(color_list_1.difference(color_list_2))
    print(color_list_2.difference(color_list_1))

def triangle_area(base, height):
    area = 1 / 2 * base * height
    print("Area:",area)

def get_sum_3int(n1,n2,n3):
    if n1 == n2 or n1 == n3 or n2 == n3:
        return 0
    else:
        return n1 + n2 + n3

def get_sum_2int(n1,n2):
    sum = n1 + n2
    if sum >= 15 and sum <= 20:
        return 20
    else:
        return sum

def get_true_false(n1,n2):
    if n1 == n2 or (n1+n2) == 5 or abs(n1-n2) == 5:
        return True
    else:
        return False
def get_add_object(n1,n2):
    sum = n1 + n2
    if isinstance(n1,int) and isinstance(n2,int):
        return sum
    else:
        return ("Please input 2 integers")

def get_personal_details():
    name = "Kah Yan"
    age = 24
    address = "Johor Jaya, Johor, Malaysia"
    print("Name: " +str(name)+ "\nAge: " +str(age)+ "\nAddress: "+str(address))

def solve_equation(x,y):
    ans = (x + y) ** 2
    print("Ans:",ans)

def check_file_exist(file):
    print(os.path.isfile(file))

def check_bit():
    print(struct.calcsize("P") * 8)

def get_os():
    print("Name of OS:",os.name)
    print("Name of OS system:",platform.system())
    print("Version of OS:",platform.release())

def get_site():
    print(site.getsitepackages())

def get_current_dir():
    print("Current File Name: ", os.path.realpath(__file__))

def get_cpu_count():
    print(os.cpu_count())

def str_to_num(text):
    int1 = int(float(text))
    float1 = float(text)
    print("Integer:",int1)
    print("Float:",float1)

def get_dir():
    files_list = [f for f in listdir(r'C:\Users\user\Desktop\GitHub\Python\python_basic_part1') if isfile(join(r'C:\Users\user\Desktop\GitHub\Python\python_basic_part1', f))]
    print(files_list)

def get_no_space(n):
    for i in range(n):
        print(i * "&", end="")

def get_username():
    print(getpass.getuser())

def get_exe_time(n):
    sum = 0
    start_time = time.time()
    for i in range(n):
        sum = sum + i
    end_time = time.time()
    timetake = end_time - start_time
    return sum,timetake

def convert_height():
    height = float(input("Height: "))
    unit = input("Feet(f) or Inches(i): ")
    if unit.lower() == "f":
        f_to_cm = height * 30.48
        return str(f_to_cm) + " cm"
    elif unit.lower() == "i":
        i_to_cm = height * 2.54
        return str(i_to_cm) + " cm"


def hypotenuse(a,b):
    c = sqrt((a ** 2) + (b ** 2))
    print(c)

def convert_to_s():
    days = float(input("Days: "))
    hours = float(input("Hours: "))
    minutes = float(input("Minutes: "))
    seconds = float(input("Seconds: "))
    time_in_s = (days * 24 * 60 * 60) + (hours * 60 * 60) + (minutes * 60) + seconds
    print(time_in_s)



def get_datetime_creation(filename):
    print("Created:",time.ctime(os.path.getctime(filename)))
    print("Modified",time.ctime(os.path.getmtime(filename)))

def bmi(weight,height):
    bmi = weight / (height ** 2)
    print("BMI:",round(bmi,2))

def sum_of_digits(n):
    n1 = n // 1000
    n2 = (n - n1 * 1000) // 100
    n3 = (n - n1 * 1000 - n2 * 100) // 10
    n4 = (n - n1 * 1000 - n2 * 100 - n3 * 10)
    return "The sum of " +str(n1)+"+"+str(n2)+"+"+str(n3)+"+"+str(n4)+"="+str(n1+n2+n3+n4)

def sort_numbers(n1,n2,n3):
    max_num = max(n1,n2,n3)
    min_num = min(n1,n2,n3)
    middle_num = (n1+n2+n3) - max_num - min_num
    return "Min: " +str(min_num)+"\nMiddle: "+str(middle_num)+"\nMax: "+str(max_num)

def copyright():
    print("Python Copyright Information:\n"+str(sys.copyright))
def join_colors():
    list_of_colors = ['Red','White','Black']
    colors = '-'.join(list_of_colors)
    print("All colors: "+str(colors))

def get_count_char(text,n):
    print(text.count(n))

def get_path(path):
    if os.path.isdir(path):
        print("It's a directory")
    elif os.path.isfile(path):
        print("It's a file")
    else:
        print("It's a special file")

def ascii(n):
    print(ord(n))

def get_filesize(path):
    filesize = os.path.getsize(path)
    print("The size of " +str(path)+ " is " +str(filesize)+" "+str("Bytes"))

def get_sum_and_print(x,y):
    sum = x + y
    print(str(x)+"+"+str(y)+"="+str(sum))

def print_1_or_null(n):
    if n == 1:
        print("First day of a Month!")

def swap_variables(a,b):
    print("Before swap: a = %d , b = %d" % (a,b))
    a,b = b,a
    print("After swap: a = %d, b = %d" % (a,b))

def string_or_number(n):
    if str(n).isdigit():
        print("The input is number")
    else:
        print("The input is not number")

def get_current_datetime():
    print(time.ctime())
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print(datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p"))

def get_multiplication(n1,n2):
    n1 = float(n1)
    n2 = float(n2)
    sum = n1 * n2
    print("The multiplication of {0} and {1} is {2}".format(n1,n2,sum))

get_multiplication(12,10)