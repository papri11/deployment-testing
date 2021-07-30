# import a library
from re import DEBUG
from flask import Flask, render_template , request
import joblib

# instance of an app
app = Flask(__name__)

model = joblib.load('dib_79.pkl')

#@app.route('/')
#def welcome():
#    return 'welcome'
 

@app.route('/')
def home_page():
    return render_template('home.html')


@app.route('/blogs' , methods= ['POST'])
def contact():
    a = request.form.get('preg')
    b = request.form.get('plas')
    c = request.form.get('pres')
    d = request.form.get('skin')
    e = request.form.get('test')
    f = request.form.get('mass')
    g = request.form.get('pedi')
    h = request.form.get('age')


    pred = model.predict([[int(a),int(b),int(c),int(d),int(e),int(f),int(g),h]])

    if pred[0] == 1:
            output = 'diabatic'

    else:
        output = ' not diabatic'

    return render_template('blogs.html' , predicted_text = f'the person is {output}')

# run the app
if __name__ == '__main__':
    app.run(debug=True)

