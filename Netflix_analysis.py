import pandas as pd
import matplotlib.pyplot as plt

#for laoding data of netflix
df = pd.read_csv("netflix_titles.csv")


#for getting netflix data rows and coloumn


print(df.info()) #for data type and non null for missing value

print(df.isnull().sum()) # for getting count of null value in coloumn
# #now to get percentage missing value with this 
# print(df.isnull().sum() / df.shape[0] * 100)

#filling missing data
df["director"] = df["director"].fillna("Unknown") 
df["cast"] = df["cast"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")
df["rating"] = df["rating"].fillna("Unknown")

#droping row with missing data
df = df.dropna(subset =["date_added"])

# #reset indexing
df = df.reset_index(drop=True)

#for date time analysis

df["date_added"]=df["date_added"].str.strip() #for treating whitespace after or before
df["date_added"]= pd.to_datetime(df["date_added"]) #changing data to date time data type


print(df.info())

df["year_added"] = df['date_added'].dt.year #to fetch year in date_added coloumn

g6 = df.groupby("year_added").size().sort_index()
print(g6)

#from the g6 we get to know that 2019 have highest number of movie and series
#and growth till 2019 but then decrease 2020

g1 = df.groupby(["year_added", "type"]).size().unstack()
print(g1) #this shows more detieled yearly data

g2 = df["year_added"].value_counts().idxmax()
print(g2)


# ploting graph 


table = df.groupby(["year_added", "type"])["show_id"].count().unstack(fill_value=0).sort_index()
table.plot(figsize=(10,6), marker='o', grid=True)
plt.title("Netflix Content Added per Year")
plt.xlabel("Year Added")
plt.ylabel("Number of Titles")


#plt.show()#for ploting the graph

#for bar chart ploting
type_cont = df["type"].value_counts()
plt.figure()
plt.bar(type_cont.index,type_cont.values)
plt.xlabel("type")
plt.ylabel("count")
plt.title("movies vs tv shows on netflix")
plt.show()


Summury = df.groupby("type").agg({
    "release_year":["min","max","mean"],
    "show_id" :"count"
})
print(Summury)