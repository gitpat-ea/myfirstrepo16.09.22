def task1():
    # TODO: первое задание
    a = input()
    a = float(a)
    print(a ** 2)

def task2():
    # TODO: второе задание
    st = input()
    count = 0
    for i in st:
        if ord(i) in range(65,91):
            count+=1
    print(count)

def task3():
    # TODO: третье задание
    st = input()
    words = st.split()
    count = 0
    for word in words:
        a = []
        for i in word:
            a.append(i)
        if len(a) >= 2 and a[0] == 'a' and a[1] == 'b' and a[-1] == 'a' and a[-2] == 'b':
            count += 1
    print(count)

def task4(generator):
    # TODO: четвертое задание
    return filter(lambda x: x % 3 != 0, generator)

def task5(list_of_smth):
    # TODO:
    print(list_of_smth[5:-3:5])
def task6(list1, list2, list3, list4):
    # TODO: пятое задание
    s1 = set(list1)
    s2 = set(list2)
    s3 = set(list3)
    s4 = set(list4)
    sp1 = s1.union(s2)
    sp2 = s3.union(s4)
    spisok = sp1 & sp2
    print(spisok)
def task7():
    # TODO: ...
    import numpy as np

    np.random.seed(9)
    a = np.array([np.random.randint(50, size = 49)])
    a = a.reshape(7,7)
    b = np.delete(a, 6, axis=0)
    b = np.delete(b, 6, axis=1)
    print(np.linalg.det(b))
    return a

def task8(f, min_x, max_x, N, min_y, max_y):
    # TODO: ...
    import nump as np
    from matplotlib import pyplot as plt

    x1 = np.linspace(min_x, max_x, N)
    y1 = np.array(f(i) for i in x1)
    x = np.array([i for i in x1 if f(i) >= min_y and f(i) <= max_y])
    y = np.array([f(i) for i in x])
    plt.plot(x, y, "b--")
    plt.grid()
    plt.set_xscale('log')
    plt.savefig('function.pdf')
    plt.show()

def task9(data, x_array, y_array):
    # TODO: ...


def task10(list_of_smth, n):
    # TODO: ...
    a = []
    def srgeom(lis):
        l = len(lis)
        pr = 1
        for i in lis:
            pr = pr*i
        return pr**(1/l)
    for i in range(len(list_of_smth)):
        if i <= len(list_of_smth) - n:
            chis = []
            for j in range(n):
            chis.append(list_of_smth[i+j])
            a.append(srgeom(chis))
        else:
            chis = []
            for j in range(len(list_of_smth) - i):
                chis.append(list_of_smth[j])
                a.append(srgeom(chis))
    print(a)
def task11(filename="infile.csv"):
    # TODO: ...

def task12(filename="video-games.csv"):
    # TODO: ...
    import pandas as pd
    df = pd.read_csv('video-games1.csv')
    dick = {}
    dick['n_games'] = df.shape[0]
    year = df.groupby('year').agg({'title': 'count'})
    dick['by_years'] = year
    ea = df.groupby('publisher').agg({'price': 'mean'})
    onlyea = ea.loc[['EA']]
    dick['mean_price'] = onlyea
    return dick