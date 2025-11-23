import csv
import pickle

def load_table(all_path=['Group.csv', 'Group2.csv']):
    tab = []
    n=0
    for path in all_path:
        if '.csv' in path:
            with open(path, encoding='utf-8-sig') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=';')
                for row in spamreader:
                    for i in range(len(row)):
                        if row[i] == '':
                            row[i]='None'
                    tab.append(row)
                    if n != 0:
                        tab.pop(-1)
                        if row != tab[0]:
                            print('\nНесоответствие столбцов\n')
                            break
                        n=0
                n+=1

        elif '.pickle' in path:
            with open(path, 'rb') as f:
                if n != 0:
                    temp = pickle.load(f)
                    temp.pop(0)
                else:
                    temp = pickle.load(f)
                tab.append(temp)
                tab=tab[0]

    return tab


def concat(table1, table2):
    load_table([table1, table2])


def split(row_number):
    tab = load_table()
    tab1 = tab[:row_number]
    tab2 = tab[row_number:]

    with open('result1.csv', 'w', encoding='utf-8-sig') as res:
        for i in tab1:
            a = csv.writer(res, delimiter=';')
            a.writerow(i)
    with open('result2.csv', 'w', encoding='utf-8-sig') as res:
        for i in tab2:
            a = csv.writer(res, delimiter=';')
            a.writerow(i)



def print_table():
    for i in load_table():
        for j in i:
            print(j, end=' ')
        print('\n', end='')


def save_table(tab=load_table()):
    with open('result.csv', 'w', encoding='utf-8-sig') as res:
        for i in tab:
            a = csv.writer(res, delimiter=';')
            a.writerow(i)
    with open('result.pickle', 'wb') as f:
        pickle.dump(tab, f)
    with open('result.txt', 'w') as f:
        for i in tab:
            try:
                s = ' '.join(i) + '\n'
                f.write(s)
            except:
                continue


def get_values(column=0):
    tab = load_table()

    if column in tab[0]:
        index = tab[0].index(column)
        res = list()
        for j in tab:
            res.append(j[index])
        print(res[0], res[1:], sep='\n')

    elif str(column).isdigit() and column < len(tab[0]):
        res = list()
        for j in tab:
            res.append(j[column])
        print(res[0], res[1:], sep='\n')

    else:
        print('Такого столбца не существует')


def get_value(column=0):
    tab = load_table()

    if column in tab[0]:
        index = tab[0].index(column)
        res = tab[1][index]
        print(column, res, sep='\n')

    elif str(column).isdigit() and column < len(tab[0]):
        print(tab[0][column], tab[1][column], sep='\n')

    else:
        print('Такого столбца не существует')


def set_values(values, column=0):
    tab = load_table()

    if column in tab[0]:
        index = tab[0].index(column)
        for j in range(1, len(tab)):
            try:
                tab[j][index] = values[j-1]
            except:
                print('Не совпало количество значений. Записал что есть')
                break
        save_table(tab)

    elif str(column).isdigit() and column < len(tab[0]):
        for j in range(1, len(tab)):
            try:
                tab[j][column] = values[j-1]
            except:
                print('Не совпало количество значений. Записал что есть')
                break
        save_table(tab)
    
    else:
        print('Такого столбца не существует')


def set_value(values, column=0):
    tab = load_table()

    if column in tab[0]:
        index = tab[0].index(column)
        tab[1][index] = values
        save_table(tab)

    elif str(column).isdigit() and column < len(tab[0]):
        tab[1][column] = values
        save_table(tab)

    else:
        print('Такого столбца не существует')


def get_rows_by_number(start, stop=0):
    tab = load_table()
    if start <= stop and len(tab)+1>start>0:
        for i in tab[start-1:stop]:
            print(i)
    elif stop==0 and len(tab)+1>start>0:
        print(tab[start-1])
    else:
        print('Неправильный диапазон')


def get_rows_by_index(*values):
    tab = load_table()
    for j in values:
        for i in tab:
            if i[0]==j:
                print(i)


def get_column_types(by_number=True):
    tab = load_table()
    integer = list()
    string = list()
    booler = list()
    floater = list()
    for i in tab[1]:
        if i=='True' or i=='False':
            booler.append(tab[1].index(i))
        else:
            try:
                flag = int(i)
                integer.append(tab[1].index(i))
            except:
                try:
                    flag = float(i)
                    floater.append(tab[1].index(i))
                except:
                    string.append(tab[1].index(i))
            
    if by_number==True:
        common_dict = dict()
        for i in string:
            common_dict[tab[0][i]] = 'str'
        for i in integer:
            common_dict[tab[0][i]] = 'int'
        for i in floater:
            common_dict[tab[0][i]] = 'float'
        for i in booler:
            common_dict[tab[0][i]] = 'bool'

    elif by_number==False:
        common_dict = dict()
        for i in string:
            common_dict[i] = 'str'
        for i in integer:
            common_dict[i] = 'int'
        for i in floater:
            common_dict[i] = 'float'
        for i in booler:
            common_dict[i] = 'bool'

    print(common_dict)
    

def set_column_types(types_dict, by_number=True):
    tab = load_table()
    if by_number==True:
        n=0
        for i in tab[1]:
            if types_dict[n]=='int':
                try:
                    t=0
                    for i in tab:
                        if i != tab[0]:
                            tab[t][n] = int(tab[t][n])
                        t+=1
                except:
                    print(f'Неправильный тип для {n, types_dict[n]}')


            if types_dict[n]=='str':
                try:
                    t=0
                    for i in tab:
                        if i != tab[0]:
                            tab[t][n] = str(tab[t][n])
                        t+=1
                except:
                    print(f'Неправильный тип для {n, types_dict[n], n}')


            if types_dict[n]=='float':
                try:
                    t=0
                    for i in tab:
                        if i != tab[0]:
                            tab[t][n] = float(tab[t][n])
                        t+=1
                except:
                    print(f'Неправильный тип для {n, types_dict[n], n}')

            
            if types_dict[n]=='bool':
                try:
                    t=0
                    for i in tab:
                        if i != tab[0]:
                            tab[t][n] = bool(tab[t][n])
                        t+=1
                except:
                    print(f'Неправильный тип для {n, types_dict[n]}')
            n+=1
    for i in tab:
        print(i)


def add():
    res = 0
    tab = load_table()
    for i in tab:
        if i != tab[0]:
            for j in i:
                try:
                    res += int(j)
                except:
                    pass
    if res==0:
        print('Не удалось подсчитать сумму значений')
    else:
        print(f'Сумма значений - {res}')

def sub():
    res = 0
    tab = load_table()
    for i in tab:
        if i != tab[0]:
            for j in i:
                try:
                    res -= int(j)
                except:
                    pass
    if res==0:
        print('Не удалось подсчитать разницу значений')
    else:
        print(f'Разница значений - {res}')

def mul():
    res = 1
    tab = load_table()
    for i in tab:
        if i != tab[0]:
            for j in i:
                try:
                    res *= int(j)
                except:
                    pass
    if res==0:
        print('Не удалось подсчитать произведение значений')
    else:
        print(f'Произведение значений - {res}')

def div():
    res = 1
    tab = load_table()
    for i in tab:
        if i != tab[0]:
            for j in i:
                try:
                    res /= int(j)
                except:
                    pass
    if res==0:
        print('Не удалось подсчитать частное значений')
    else:
        print(f'Частное значений - {res}')

def eq(col1, col2):
    tab = load_table()
    res=[]
    for i in tab:
        if i != tab[0]:
            if i[col1]==i[col2]:
                res.append(True)
            else:
                res.append(False)
    print(res)

def gr(col1,col2):
    tab = load_table()
    res=[]
    for i in tab:
        if i != tab[0]:
            if i[col1]>i[col2]:
                res.append(True)
            else:
                res.append(False)
    print(res)

def ls(col1,col2):
    tab = load_table()
    res=[]
    for i in tab:
        if i != tab[0]:
            if i[col1]<i[col2]:
                res.append(True)
            else:
                res.append(False)
    print(res)

def ge(col1,col2):
    tab = load_table()
    res=[]
    for i in tab:
        if i != tab[0]:
            if i[col1]>=i[col2]:
                res.append(True)
            else:
                res.append(False)
    print(res)

def le(col1,col2):
    tab = load_table()
    res=[]
    for i in tab:
        if i != tab[0]:
            if i[col1]<=i[col2]:
                res.append(True)
            else:
                res.append(False)
    print(res)

def ne(col1, col2):
    tab = load_table()
    res=[]
    for i in tab:
        if i != tab[0]:
            if i[col1]!=i[col2]:
                res.append(True)
            else:
                res.append(False)
    print(res)


def filter_rows(bool_list):
    tab = load_table()
    n = 0
    for i in bool_list:
        if i==True:
            print(tab[n+1])
        n += 1


def merge_tables(table1, table2, by_number=True):
    tab1 = []
    tab2 = []
    with open(table1, encoding='utf-8-sig') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        for row in spamreader:
            tab1.append(row)
    
    with open(table2, encoding='utf-8-sig') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        for row in spamreader:
            tab2.append(row)
    
    table1 = dict()
    n=0
    for i in tab1[0]:
        val=[]
        for j in tab1:
            if j != tab1[0]:
                val.append(j[n])
        table1[i] = val
        n += 1
    
    table2 = dict()
    n=0
    for i in tab2[0]:
        val2=[]
        for j in tab2:
            if j != tab2[0]:
                val2.append(j[n])
        table2[i] = val2
        n += 1
    
    common = dict()
    for v in table1.keys():
        for v2 in table2.keys():
            if v==v2:
                common[v] = table1[v] + table2[v2]
    
    with open('result.csv', 'w', encoding='utf-8-sig') as res:
        first = []
        sec = []
        for i in common.keys():
            first.append(i)
            sec.append(common[i])
        a = csv.writer(res, delimiter=';')
        a.writerow(first)
        temp = []
        for i in range(len(sec[0])):
            temp1 = []
            for j in range(len(sec)):
                temp1.append(sec[j][i])
            temp.append(temp1)
        for i in temp:
            a.writerow(i)
    



# merge_tables('Group.csv', 'Group2.csv')
# filter_rows([False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True])

# eq(3, 4)
# gr(1, 2)
# ls(1,2)
# ge(1,2)
# le(1,2)
# ne(3,4)

# add()
# sub()
# mul()
# div()

# print(load_table())
# split(5)
# save_table()
# get_rows_by_number(3,14)
# get_rows_by_index('fsd', 52, 'ПМ25-3', 12, 'БИ25-6')
# get_column_types(True)
# set_column_types({0: 'str', 1: 'str', 2: 'str', 3: 'int', 4: 'float'})
# get_values(4)
# get_value(0)
# set_values([3,2,4,3,2], 2)
# set_value(3, 3)
# print_table()
