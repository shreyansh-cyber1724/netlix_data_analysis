import pandas as pd
#for laoding data of netflix
df = pd.read_csv("netflix_titles.csv")
#for getting netflix data rows and coloumn
print(df.shape)
#for getting netflix's coloumn data type and info

print(df.info()) #for data type and non null for missing value

print(df.isnull().sum()) # for getting count of null value in coloumn
#now we got to find percentage missing value with this 
print(df.isnull().sum() / df.shape[0] * 100)

mising = df.isnull().sum()
mising = mising[mising > 0] #with boolean masking to get only missing data count
print(mising)

#filling missing data
df["director"].fillna("Unknown" , inplace=True) 
df["cast"].fillna("Unknown", inplace = True)
df["country"].fillna("Unknown", inplace = True)
df["rating"].fillna("Unknown", inplace=True)

#droping row with 
df.dropna(subset =["date_added"] , inplace=True)
df.dropna(subset=["duration"],)



#for getting netflix data's important inspection
#print(df.describe())
