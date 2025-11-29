from numpy import random
import pandas as pd
import matplotlib.pyplot as plt

def amount(x: int) -> list:
    l=list()
    for _ in range(x):
        m = random.randint(0, 100)
        l.append(m)
    return l

def flines(file: str) -> int:
    with open(file, "r") as file:
        lines = file.readlines()
    file.close()
    return len(lines)

def fwriter(text: str, path: str):
    with open(path, 'w') as file:
        for item in text:
            file.write(f"{item}")

def ploter(dfile: str, x :str, y: str, title: str, chart='hist',img='fig1.png'):
    df = pd.read_excel(dfile)
    if chart =='line':
        plt.plot(df[x],df[y], marker='o', linestyle='-', color='b' )
        plt.xlabel(x)
        plt.ylabel(y)
    elif chart =='pie':
        plt.pie(df[y], labels=df[x], autopct="%1.1f%%", startangle=90)
    else:
        plt.hist(df[x], bins=10, color='skyblue', edgecolor='black')
        plt.xlabel(x)
        plt.ylabel(y)
        plt.title(title)
        plt.grid(True)
        plt.savefig(img)
        #plt.close()
        plt.show()