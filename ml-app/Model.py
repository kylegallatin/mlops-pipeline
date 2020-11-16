import pickle 
import sklearn

class Model(object):

    def __init__(self):
        print("Initialising")
        with open('model.pkl', "rb") as f:
            self.model = pickle.load(f)

    def predict(self,X,features_names):
        print("Predict called")
        return self.model.predict(X)

    def metrics(self):
        return [
            {"type": "COUNTER", "key": "mycounter", "value": 1}, # a counter which will increase by the given value
            {"type": "GAUGE", "key": "mygauge", "value": 100},   # a gauge which will be set to given value
            {"type": "TIMER", "key": "mytimer", "value": 20.2},  # a timer which will add sum and count metrics - assumed millisecs
        ]