from pathlib import Path

path=Path('data.txt')
def total_salary(path):
    with open(path, 'r') as fh:
        fh=fh.readlines()
        outlist=[]
    for line in fh:
        line=line.split(",")    
        outlist.append(int(line[1]))
    total=sum(outlist)
    averrage=total/len(outlist)
    return total,averrage

total,averrage=total_salary(path)
print(f'total:{total}, averrage:{averrage}')   
    

