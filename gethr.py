import pandas as pd
import numpy as np
month = ['01','02','03','04','05','06','07','08','09','10','11','12']
#month = ['01','02']
gethead = pd.read_table('201701_cwb_hr.txt',skiprows=74,delim_whitespace=True)
head = list(gethead)[1:]
print(head)

df = pd.DataFrame([])
for mm in month:
    fn='2017%s_cwb_hr.txt'%mm
    data = pd.read_table(fn,skiprows=75,names=head,delim_whitespace=True)
    taipei = data.query('stno==466920')['TX01']
    hrfake = data.query('stno==466920')['yyyymmddhh']
    hrfake = hrfake.astype(str)
    hr = hrfake.str.slice(start=8)
    hr = hr.astype(int)
    fn = pd.concat([hr,taipei],axis=1)
    df = pd.concat([df,fn])
df.to_csv('taipei.csv',index=False)
