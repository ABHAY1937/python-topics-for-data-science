from sklearn.neighbors import KNeighborsClassifier
#sklearn ==>package name
#.neighbors ==> module
#KNeihborsClassifier ==> function name
knn=KNeighborsClassifier(n_neighbors=3) #k=3
x1=[7,7,3,1]
y1=[7,4,4,4]
target=["bad","bad","good","good"]

#[(7,7),(7,4),(3,4),(1,4)]
#zip function (used for connecting two lists)

features=list(zip(x1,y1))
print(features)

#ml model creation using K Nearest Neighour =====>
#objname.fit(features,target)

knn.fit(features,target) #-=====>model
print(knn.predict([[3,7]]))
