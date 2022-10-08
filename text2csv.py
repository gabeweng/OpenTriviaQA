import os
import pandas as pd
import numpy as np
def txt_to_csv(path,file): 
 
  questions=[]
  key=[]
  dist1=[]
  dist2=[]
  dist3=[]
  dist4=[]
  with open(path+file, errors='ignore',mode="r") as file1:
      files = file1.readlines()
      i=0
      for i in range(len(files)):
        if files[i][0]=='\n':
          try:
            if files[i+1][3]=='#':
              continue          
            questions.append((files[i+1][3:len(files)-1]).strip())
            key.append(files[i+2][2:len(files[i+2])-1])
            if (files[i+3]!="\n"):
              dist1.append(files[i+3][2:len(files[i+3])-1])
            else:
              dist1.append(np.nan)
              dist2.append(np.nan)
              dist3.append(np.nan)
              dist4.append(np.nan)
              continue
            if (files[i+4]!="\n"):
              dist2.append(files[i+4][2:len(files[i+4])-1])
            else:
              dist2.append(np.nan)
              dist3.append(np.nan)
              dist4.append(np.nan)
              continue
            if (files[i+5]!="\n"):
              dist3.append(files[i+5][2:len(files[i+5])-1])
            else:
              dist3.append(np.nan)
              dist4.append(np.nan)
              continue
            if (files[i+6]!="\n"):
              dist4.append(files[i+6][2:len(files[i+6])-1])
            else:
              dist4.append(np.nan)
          except:
            pass
  bank={}
  bank["Category"]=file
  bank["Questions"]=questions
  bank["Correct"]=key
  bank["A"]=dist1
  bank["B"]=dist2
  bank["C"]=dist3
  bank["D"]=dist4
  df=pd.DataFrame(bank)
  return df

def parse_files(sourcePath='categories/',destination='/'):

  li = []
  for file in os.listdir(sourcePath):
    print("Parsing file: ",file)
    data=txt_to_csv(sourcePath,file)
    li.append(data)
  return pd.concat(li, axis=0, ignore_index=True)

data = parse_files()
data.to_csv("trivia.csv",index=False)
print("Done!")