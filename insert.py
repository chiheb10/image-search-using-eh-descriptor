import numpy as np
from pymongo import MongoClient
from sklearn.cluster import KMeans

#MongoDB
client=MongoClient('mongodb://localhost:27017/Photos')
db=client.Photos
collection=db.collection_En

path='eh_descriptors'
table=[]
#n=100
n=8 #on choisit 80000 images 
for k in range(1,n+1,1):
	with open(path+ '/'+'eh'+str(k)+'.txt','r') as f:
		lines = f.readlines()
	for i in lines:
		table.append(i.split())
print(len(table))
array_edge=np.array(table)
print(len(array_edge))

Kmeans=KMeans(n_clusters=20).fit(array_edge)
Clusters=Kmeans.predict(array_edge)
centroids = Kmeans.cluster_centers_
for i in centroids:
	print(i) 
for k in range(0,80000):
	cluster=str(Clusters[k])
	line_DB={"index":k,"edge_value":table[k],"cluster":cluster}
	collection.insert_one(line_DB)
	
