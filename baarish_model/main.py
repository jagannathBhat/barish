import pickle
from sklearn.linear_model import LogisticRegression
from firebase import firebase

firebase = firebase.FirebaseApplication('https://baarish-cf1d5.firebaseio.com', None)

humidity = firebase.get('/DHT11/Humidity', None)
rain = firebase.get('/DHT11/Rain', None)
temperature = firebase.get('/DHT11/Temperature', None)

humidity = float(list(humidity.values())[-1])
rain = float(list(rain.values())[-1])
temperature = float(list(temperature.values())[-1])

X = [[temperature, humidity]]

loaded_model = pickle.load(open('Model/model.sav', 'rb'))
y_pred = loaded_model.predict(X)
print(y_pred[0])

if y_pred == 1:
	result = firebase.post('/prediction', 'one')

else:
	result = firebase.post('/prediction', 'zero ')
