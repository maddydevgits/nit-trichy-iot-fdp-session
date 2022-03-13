import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from flask import Flask,request,render_template

data=pd.read_csv('iot.csv')
#print(data)

# col0 - index, col1- temp, col2 - hum, col3- outcome
# Input  - col1, col2
# Output - col3

X=data.iloc[:,[1,2]].values
#print(X)

Y=data.iloc[:,-1].values
print(Y)

classifier=KNeighborsClassifier()
classifier.fit(X,Y)

print(classifier.predict([[22.0,58.0]]))

from sklearn.model_selection import train_test_split

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3)
Y_pred=classifier.predict(X_test)

from sklearn.metrics import accuracy_score
print(accuracy_score(Y_pred,Y_test)*100)


app=Flask(__name__)

@app.route('/')
def homePage():
    return(render_template('index.html'))

@app.route('/predict',methods=['POST','GET'])
def predictData():
    humidity=float(request.form['humidity'])
    temperature=float(request.form['temperature'])
    print(humidity,temperature)
    outcome=classifier.predict([[temperature,humidity]])
    outcome=outcome[0]
    result="The class this data {0}, {1} is {2}".format(temperature,humidity,outcome)
    return (render_template('index.html',result=result))

if __name__=="__main__":
    app.run()
