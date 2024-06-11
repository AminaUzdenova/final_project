from flask import Flask, request

app = Flask(__name__);
@app.route('/predict_price', methods = ['GET'])
def predict():
    args = request.args
    floor = args.get ('floor', default = -1, type=int)
    open_plan = args.get ('open_plan', default = -1, type=int)
    rooms = args.get ('rooms', default = -1, type=int)
    area = args.get ('area', default = -1, type=int)
    renovation = args.get ('renovation', default = -1, type=int)
    
    response = "floor:{}, open plan:{}, rooms:{}, area:{}, renovation:{}".format(floor, open_plan, rooms, area, renovation)

    return response

if __name__=='__main__':
    app.run(debug = True, port = 7778, host = '0.0.0.0')