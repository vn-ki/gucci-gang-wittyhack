from data import read_data
import glob
import time


files = glob.glob('../new/*')

for i in files:
    filename = i.split('/')[-1]
    df = read_data(i)
    df.to_csv('../csv/'+filename, sep='|')
    del df
    time.sleep(10)
