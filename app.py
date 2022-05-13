from flask import Flask , render_template,request
from markupsafe import escape





app = Flask(__name__) #instance of flask  #__name__ = __main__


@app.route("/")
def hello_world():
    return "Hello, Hi EveryBody Welcome to Flask Learning!"


@app.route("/test")
def test():
    a="Hey test2 this is the testing for render htmls"
    return render_template('home.html', data=a)


@app.route("/calci")
def calci():
    return render_template('calculator.html')

@app.route('/calculator',methods=['POST',"GET"])
def calculator():

    if request.method=='POST':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        sym = request.form['symbol']
        if(sym=='+'):
            sum_res = num1+num2;
        elif(sym=='-'):
            sum_res = num1-num2;
        elif(sym=='*'):
            sum_res = num1*num2
        elif(sym=='/'):
            sum_res = num1/num2;
        elif(sym=='//'):
            sum_res = num1//num2;
        else:
            sum_res = "invalid symbol"
        res=f'YOUR RESULT IS \n {num1} {sym} {num2} = {sum_res}'
        return render_template('result.html',result=res)



@app.route('/deepa')
def Deepa():
    return "Hey Deepa this is your page!"

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/ak')
def ak():
    return 'Hello, Hey AK'

@app.route("/<name>")
def hey(name):
    return f"Hello, {escape(name)}!"


@app.route("/<name>/<name1>")
def hey1(name,name1):
    return f"Hello, {escape(name)}!  {escape(name1)}"


if __name__=="__main__":
    app.run(debug=True, use_reloader=False)
#    app.run(debug=False)