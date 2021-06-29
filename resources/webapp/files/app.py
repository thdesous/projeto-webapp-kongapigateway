from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello():  
    return render_template('hellopage.html')

@app.route('/about')
def about():
    #return 'The about page'
    return render_template('aboutpage.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')