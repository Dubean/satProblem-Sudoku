import os
import time
from pysat.solvers import Glucose3


# （x, y, z)表示在第x行第y列填入z，其编码为((x-1)*n2+y)+(n2*n2*(z-1))
def f(x, y, z):
    return ((x-1)*n2+y)+(n2*n2*(z-1))


# 将编码转换为位置
def f2(x, n):
    a = int((x + n - 1) / n)
    b = int(x - (a - 1) * n)
    return a, b


if __name__ == '__main__':
    # 初始化数据
    in_path = os.getcwd() + '\\input'
    out_path = os.getcwd() + '\\output'
    for txt in os.listdir(in_path):
        # 读取数据
        with open(in_path + '\\' + txt, 'r') as fr:
            n = int(fr.readline())                   # 阶数
            n2 = n * n
            S = []                                  # 数独初始位置
            for i in range(n2):
                S.append(fr.readline().replace('\n', '').split(' '))

        g = Glucose3()
        # 每个格子需填入1~n^2的其中一个
        for x in range(1, n2 + 1):
            for y in range(1, n2 + 1):
                g.add_clause([f(x, y, z) for z in range(1, n2 + 1)])
        # 每个格子不重复
        for x in range(1, n2 + 1):
            for y in range(1, n2 + 1):
                for z in range(1, n2):
                    g.add_clause([-1 * f(x, y, z) for i in range(z + 1, n2 + 1)]
                                 + [-1 * f(x, y, i) for i in range(z + 1, n2 + 1)])
        # 每行需填入每个数一次
        for x in range(1, n2 + 1):
            for z in range(1, n2 + 1):
                g.add_clause([f(x, y, z) for y in range(1, n2 + 1)])
        # 每行的每个数不重复
        for x in range(1, n2 + 1):
            for z in range(1, n2 + 1):
                for y in range(1, n2):
                    for i in range(y + 1, n2 + 1):
                        g.add_clause([-1 * f(x, y, z), -1 * f(x, i, z)])
        # 每列需填入每个数一次
        for y in range(1, n2 + 1):
            for z in range(1, n2 + 1):
                g.add_clause([f(x, y, z) for x in range(1, n2 + 1)])
        # 每列的每个数不重复
        for y in range(1, n2 + 1):
            for z in range(1, n2 + 1):
                for x in range(1, n2):
                    for i in range(x + 1, n2 + 1):
                        g.add_clause([-1 * f(x, y, z), -1 * f(i, y, z)])
        # 每个格子需填入每个数一次
        for i in range(n):
            for j in range(n):
                for z in range(1, n2 + 1):
                    g.add_clause([f(i*n+x, j*n+y, z) for x in range(1, n + 1) for y in range(1, n + 1)])
        # 每个格子的每个数不重复
        for i in range(n):
            for j in range(n):
                for z in range(1, n2 + 1):
                    for x in range(1, n2 + 1):
                        for y in range(x + 1, n2 + 1):
                            x1, y1 = f2(x, n)
                            x2, y2 = f2(y, n)
                            g.add_clause([-1 * f(x1, y1, z), -1 * f(x2, y2, z)])
        # 在(x, y)中已填有z
        for x in range(n2):
            for y in range(n2):
                if S[x][y] != '0':
                    g.add_clause([f(x + 1, y + 1, int(S[x][y]))])

        # 判断结果并记录时间
        start = time.time()
        result = g.solve()
        end = time.time()

        # 记录结果
        with open(out_path + '\\' + txt.replace('in', 'out'), 'w') as fw:
            with open(os.getcwd() + '\\result.txt', 'a+') as fw2:
                if result:
                    # 将结果转化为序列
                    for item in g.get_model():
                        if item > 0:
                            x, y = f2(item % (n2 * n2), n2)
                            z = int((item + (n2 * n2) - 1) / (n2 * n2))
                            S[x - 1][y - 1] = z
                    # 写入结果
                    for item in S:
                        print(*item, sep=' ', end='\n', file=fw)
                else:
                    print(result, file=fw)
                print(txt.replace('.txt', ''), n, 'x', n, file=fw2)
                print('result = ' + str(result), file=fw2)
                print('time = ' + str(end - start), file=fw2)
                print('-' * 15, file=fw2)
