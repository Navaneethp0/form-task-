from flask import Flask,render_template,request
app = Flask(__name__)
app=Flask(__name__)
        
@app.route('/')
def ab():
    return render_template('form.html')

@app.route('/NA',methods=['POST'])
def nv():
    fname = request.form['fname']
    email = request.form['email']
    return render_template('for.html',fname=fname,email=email)
    
if __name__ == '__main__':
    app.run(debug=True)
