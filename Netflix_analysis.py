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
df["director"] = df["director"].fillna("Unknown") 
df["cast"] = df["cast"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")
df["rating"] = df["rating"].fillna("Unknown")

#droping row with 
df = df.dropna(subset =["date_added"])
df = df.dropna(subset=["duration"])

#groupby




#for getting netflix data's important inspection
#print(df.describe())
