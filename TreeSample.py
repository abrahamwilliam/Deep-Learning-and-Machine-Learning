from sklearn import tree

x=[[23,24,224],[23,215,246],[29,242,242],[232,242,214],
  [23,24,24],[23,25,26],[29,242,242],[232,242,214],
  [23,241,241],[231,215,216],[291,242,242],[232,242,214]]

y=['male','female','male','female','male','female','male','female','male','female','male','female']

clf=tree.DecisionTreeClassifier()

clf=clf.fit(x,y)

prediction=clf.predict([[100,213,333]])

print(prediction)