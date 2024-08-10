from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        value = float(request.form['value'])
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']
        
        if from_unit == 'meters' and to_unit == 'feet':
            result = value * 3.28084
        elif from_unit == 'feet' and to_unit == 'meters':
            result = value / 3.28084
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
