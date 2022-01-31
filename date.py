import datetime
import base
x = datetime.datetime.now() + datetime.timedelta(days=1)

def jadval(kun):
    x = ""
    x = kun.capitalize()
    if x == "Dushanba":
        x = "Monday"
    elif x == "Seshanba":
        x = "Tuesday"
    elif x == "Chorshanba":
        x = "Wednesday"
    elif x == "Payshanba":
        x = "Thursday"
    elif x == "Juma":
        x = "Friday"
    elif x == "Shanba":
        x = "Saturday"
    elif x == "Yakshanba":
        x = "Sunday"
    return x

# jadval("AsdS")

def jadval_tek(kun):
    x = ""
    i = False
    if len(kun)%2==0:  
        step = 0
        for t in kun:
            x = kun[step].capitalize()
            if (x == "Dushanba" or x == "Seshanba" or x == "Chorshanba" or x == "Payshanba" or x == "Juma" or x == "Shanba" or x == "Yakshanba"):
                i = True
                # print(x)
                if step+1 < len(kun)-1:
                    step+=2
            else:
                i = False
                break
    return i
# print(jadval_tek(["Dushanba", "1", "shaba", "2"]))


import base
def per_user(id):
    if base.users("teacher", id) is not None and base.users("student", id) is not None:
        return 2
    elif base.users("teacher", id) is not None:
        return 1
    elif base.users("student", id) is not None:
        return 0
    else:
        return 3
global step, arr
arr = ["09"]
step = 0
def asd():
   print(base.week_day_group(str(x.strftime("%A"))))
(asd())

