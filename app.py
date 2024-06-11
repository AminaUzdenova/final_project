from flask import Flask, request
import joblib
import numpy

MODEL_PATH ='mlmodel/model.pkl'
Scaler_X_PATH ='mlmodel/scaler_x.pkl'
Scaler_Y_PATH ='mlmodel/scaler_y.pkl'

app = Flask(__name__)
model = joblib.load(MODEL_PATH)
sc_X = joblib.load(Scaler_X_PATH)
sc_Y = joblib.load(Scaler_Y_PATH)

@app.route('/predict_price', methods = ['GET'])
def predict():
    args = request.args
    floor = args.get ('floor', default = -1, type=int)
    open_plan = args.get ('open_plan', default = -1, type=int)
    rooms = args.get ('rooms', default = -1, type=int)
    area = args.get ('area', default = -1, type=int)
    renovation = args.get ('renovation', default = -1, type=int)
    
    response = "floor:{}, open plan:{}, rooms:{}, area:{}, renovation:{}".format(floor, open_plan, rooms, area, renovation)
    x = numpy.array([floor, open_plan, rooms, area, renovation]).reshape(1,-1)
    x =  sc_X.transform(x)


    result = model.predict(x)
    result = sc_Y.inverse_transform(result.reshape(1,-1))

    return str(result[0][0])

if __name__=='__main__':
    app.run(debug = True, port = 7778, host = '0.0.0.0')