import sqlite3
import datetime
day = datetime.datetime.now() + datetime.timedelta(days=1)


# c.execute(f"CREATE TABLE groups (filial text, guruh text, hafta_kunlari text, fan text)")

def detected_teacher_and_fan(txt):        # guruh qo'shish uchun
    con = sqlite3.connect(f'teacher.db')
    c = con.cursor()  
    c.execute(f'SELECT*FROM teachers WHERE id = "{txt}" ')
    t = c.fetchone()
    con.commit()
    con.close()
    return t


def create_group(filial, guruh, hafta_kunlari, id):        # guruh qo'shish uchun
    con = sqlite3.connect('group.db')
    c = con.cursor()
    txt = (f"{filial}",f"{guruh}", f"{hafta_kunlari}", f"{detected_teacher_and_fan(id)[0]}", f"{detected_teacher_and_fan(id)[2]}")
    c.execute(" INSERT INTO groups VALUES(?, ?, ?, ?, ?)", txt)
    # c.execute(f"CREATE TABLE groups (filial text, guruh text, hafta_kunlari text, fan text, uqituvchi text)")
    # c.execute(" DROP TABLE groups")
    con.commit()
    con.close()

# create_group("Sarmijon", '3-4-a',"Shanba/8:30/Yakshanba/8:30", "Matematika", "G'aniyev Qodirjon")

# c.execute(f"CREATE TABLE students (filial text, guruh text, s_fio text, t_fio text, tel text, school_no text, fanlar text, id text)")
# create_student(arr[0], arr[1], arr[3], arr[4], arr[5], arr[6], arr[2], )
def info_group_fan(txt):
    txet = ""
    con = sqlite3.connect(f'group.db')
    c = con.cursor()
    c.execute(f'SELECT*FROM groups WHERE guruh = "{txt}"')
    t = c.fetchone()
    con.commit()
    con.close()
    return t[3]

def create_student(filial, guruh, s_fio, t_fio, tel, school_no, id):        # talaba qo'shish uchun
    con = sqlite3.connect('student.db')
    c = con.cursor()
    txt = (f"{filial}", f"{guruh}", f"{s_fio}", f"{t_fio}", f"{tel}", f"{school_no}", f"{info_group_fan(guruh)}", f"{id}")
    c.execute(" INSERT INTO students VALUES(?, ?, ?, ?, ?, ?, ?, ?)", txt)
    

    con.commit()
    con.close()
# create_student("Sarmijon", "3-4-a","G'aniyev Xurshid", "G'aniyeva Muhabbat", "914413060", "3", "Matematika/Ingliz tili", "747245771")


def info_group_students(txt):
    txet = True
    con = sqlite3.connect(f'group.db')
    c = con.cursor()
    c.execute(f'SELECT*FROM groups WHERE guruh = "{txt}"')
    t = c.fetchone()
    if t is not None:
        txet = False
    con.commit()
    con.close()
    return txet



# c.execute(f"CREATE TABLE teachers (ism text, tel text, fan text, id text)")
def create_teacher(ism, tel, fan, id):
    con = sqlite3.connect('teacher.db')
    c = con.cursor()

    txt = (f"{ism}",f"{tel}", f"{fan}", f"{id}")
    c.execute(" INSERT INTO teachers VALUES(?, ?, ?, ?)", txt)
    con.commit()
    con.close()
# create_teacher("G'aniyev Qodirjon", "916457170", "Matematika", '747245771')

def detected_group(txt):        # guruh qo'shish uchun
    con = sqlite3.connect(f'group.db')
    c = con.cursor()  
    i = False
    c.execute(f'SELECT*FROM groups WHERE guruh = "{txt}" ')
    t = c.fetchone()
    if t is None:
        i = True
    con.commit()
    con.close()
    return i

def permisson_group(group, id):
    boo = False
    con = sqlite3.connect(f'group.db')
    c = con.cursor()
    c.execute(f'SELECT*FROM groups WHERE guruh = "{group}"')
    t = c.fetchone()
    # print(t)
    if t[3] == detected_teacher_and_fan(id)[0]:
        boo = True
    con.commit()
    con.close()
    return boo
# print(permisson_group("5-4-b","1245032358"))


def info_group_student(txt):
    txet = f""
    con = sqlite3.connect(f'student.db')
    c = con.cursor()
    c.execute(f'SELECT*FROM students WHERE guruh = "{txt}"')
    t = c.fetchall()
    if len(t)!= 0:
        step = 1
        for i in t:
            txet += f"\n{step}. {i[2]}"
            step += 1
    con.commit()
    con.close()
    return txet
# print(info_group_student("3-4-a"))

def info_davomat_nb(txt, a):
    arr = []
    con = sqlite3.connect(f'student.db')
    c = con.cursor()
    c.execute(f'SELECT*FROM students WHERE guruh = "{txt}"')
    t = c.fetchall()
    for i in a:
        arr.append(t[i-1])
    con.commit()
    con.close()
    return arr
# print(info_davomat("3-4-c", [1]))

def info_davomat_b(txt, a):
    arr = []
    con = sqlite3.connect(f'student.db')
    c = con.cursor()
    c.execute(f'SELECT*FROM students WHERE guruh = "{txt}"')
    t = c.fetchall()
    l = 0
    for i in range(len(t)):
        if len(a)!=0:
            if l<len(a):
                if i == a[l]-1:
                    l+=1
                continue
        arr.append(t[i])
    con.commit()
    con.close()
    return arr
# print(info_davomat_b("H", [1]))

# c.execute("CREATE TABLE dars_jadvals (id text, guruh text, soat text)")

def date_info(id, guruh, soat):
    con = sqlite3.connect("dars_jadval.db")
    c = con.cursor()
    txt = (f"{id}",f"{guruh}", f"{soat}")
    c.execute(" INSERT INTO dars_jadvals VALUES(?, ?, ?)", txt)
    c = con.cursor()
    con.commit()
    con.close()

# date_info("Saturday", "3-4-a", "13:30")


def group_fan(txt):
    con = sqlite3.connect(f'group.db')
    c = con.cursor()
    c.execute(f'SELECT*FROM groups WHERE guruh = "{txt}"')
    t = c.fetchone()
    con.commit()
    con.close()
    return t



def student_group_delete(txt):
    con = sqlite3.connect(f'student.db')
    c = con.cursor()
    c.execute(f'DELETE FROM students WHERE guruh = "{txt}"')
    con.commit()
    con.close()

def dars_jadval_delete(txt):
    con = sqlite3.connect(f'dars_jadval.db')
    c = con.cursor()
    c.execute(f'DELETE FROM dars_jadvals WHERE guruh = "{txt}"')
    con.commit()
    con.close()

def delete_group(txt):
    con = sqlite3.connect(f'group.db')
    c = con.cursor()
    c.execute(f'DELETE FROM groups WHERE guruh = "{txt}"')
    dars_jadval_delete(txt)
    student_group_delete(txt)
    con.commit()
    con.close()
# delete_group("Asd")
    
# print(group_fan("3-4-c"))
def dars_jadval_info(txt):        # guruh qo'shish uchun
    con = sqlite3.connect(f'group.db')
    c = con.cursor()
    # c.execute("DROP TABLE groups")    
    r = ""
    c.execute(f'SELECT*FROM groups WHERE guruh = "{txt}" ')
    t = c.fetchone()
    r += f"\n\n<b>Filiali:</b>\n {t[0]}"
    r += "\n<b>Dars Jadvali:</b>"
    a = list(map(str, t[2].split("/")))
    for i in range(len(a)):
        if i%2==1:
            continue
        r += f"\n  {a[i]} - {a[i+1]}"
    r += f"\n\n<b>Fan:</b>\n {t[4]}"
    r += f"\n\n<b>O'qituvchi:</b>\n {t[3]}"
    con.commit()
    con.close()
    return r
# dars_jadval_info("A")

def week_day_group(txt):
    arr = []
    con = sqlite3.connect(f'dars_jadval.db')
    c = con.cursor()
    c.execute(f'SELECT*FROM dars_jadvals WHERE id = "{txt}"')
    t = c.fetchall()
    for i in t:
        arr.append(i[1])
    con.commit()
    con.close()
    return arr
# print(week_day_group("Monday"))

def group_user_id():
    txt = week_day_group(str(day.strftime("%A")))
    # txt = week_day_group(str("Monday"))
    arr = []
    con = sqlite3.connect(f'student.db')
    c = con.cursor()
    for i in txt:
        c.execute(f'SELECT*FROM students WHERE guruh = "{i}"')
        t = c.fetchall()
        for item in t:
            arr.append(item[7])
    con.commit()
    con.close()
    return arr
# print(group_user_id(week_day_group("Monday")))

def tek_parent_id(txt):
    b = False
    con = sqlite3.connect(f'student.db')
    c = con.cursor()
    c.execute(f'SELECT*FROM students WHERE id = "{txt}"')
    t = c.fetchall()
    if len(t)!=0:
        b = True
    con.commit()
    con.close()
    return b

def test(txt):        # guruh qo'shish uchun
    con = sqlite3.connect(f'{txt}.db')
    c = con.cursor()
    # c.execute("DROP TABLE groups")    

    c.execute(f'SELECT*FROM {txt}s ')
    t = c.fetchall()
    print(t)
    con.commit()
    con.close()


# test('dars_jadval')
# print(detected_group("3-4-b"))
# print(info_group_student('3-4-a'))
