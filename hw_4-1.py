from pathlib import Path

path=Path('data.txt')                 # створення шляху до файла
def total_salary(path):               # 
    with open(path, 'r') as fh:       # відкриття файлу для читання
        fh=fh.readlines()             # читання по рядкам
        outlist=[]                    # 
    for line in fh:                   # розбиваєм рядки за ","
        line=line.split(",")          # та додаєм у новий список 
        outlist.append(int(line[1]))  # зарплати працівників у числах
    total=sum(outlist)                # обчислення суми та середньої зарплати
    averrage=total/len(outlist)       #
    return total,averrage

try:
    total,averrage=total_salary(path)
    print(f'total:{total}, averrage:{averrage}')   
except Exception as e:
    print(e)
    

