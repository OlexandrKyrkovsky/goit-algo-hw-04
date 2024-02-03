from pathlib import Path

path=Path('data_2.txt')

def get_cats_info(path):
    with open(path,'r') as fh:
        fh=fh.readlines()
        outlist=[]
        for line in fh:
            line=line.split(',')
            outlist.append({'id':line[0],'name':line[1],'age':line[2]})
    return outlist
       
print(*get_cats_info(path),sep='\n')