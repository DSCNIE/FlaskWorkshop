from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/form', methods=['POST', 'GET'])
def port():
    if request.method == 'POST':
        data = request.form
        print(data)
        return render_template(
            'Port.html', 
            name=data['Name'], 
            about=data['About'], 
            insta=data['Insta'], 
            linkedIn=data['Link'], 
            twitter=data['Twitter'], 
            gender=data['gender'], 
            github=data['Github']
        )

if __name__ == "__main__":
    app.run(debug = True)