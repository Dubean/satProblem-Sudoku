# satProblem-Sudoku
A satProblem about Sudoku.

编译：
将input文件夹与satProblem.py放在同一目录下，并在同一目录下创建output文件夹
在python编译器（如PyCharm）中打开satProblem.py，点击运行即可
程序导入了pysat包（from pysat.solvers import Glucose3）
未安装的话则需要预先在环境中安装pysat包（pip install python-sat)

运行：
程序开始运行会自动读取input文件夹中的文件并进行计算
若用户想手动加入数据，则需按照一下格式，第一行输入数独阶数n，接下来输入初始数值（0代表空）如：
2
2 4 0 0
0 3 0 2
0 0 2 0
0 2 1 4

程序会算出结果，若可满足则在output文件夹中新建put文件，把填好的数独写入文件中，如：
2 4 3 1
1 3 4 2
4 1 2 3
3 2 1 4

并且在与satProblem.py同目录下生成result.txt文件记录结果和运行时间，程序运行结束。
