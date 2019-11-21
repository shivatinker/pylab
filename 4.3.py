import pandas as pd

data1 = pd.read_table('students1.txt', sep='\s+')
data2 = pd.read_table('students2.txt', sep='\s+')
data3 = pd.read_table('students3.txt', sep='\s+')
eng = pd.DataFrame(data1, columns=['English1', 'English2'])
eng['English3'] = data2.English3
prbz = pd.DataFrame(data1, columns=['Programming2'])
prbz['BZhD'] = data3.BZhD
print(eng)
print('\n')
print(prbz)
print('\n')
print(eng.corr())
print('\n')
print(prbz.corr())
