from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        value = float(request.form['value'])
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']
        
        # Length conversions
        if from_unit == 'meters' and to_unit == 'feet':
            result = value * 3.28084
        elif from_unit == 'feet' and to_unit == 'meters':
            result = value / 3.28084
        elif from_unit == 'kilometers' and to_unit == 'miles':
            result = value * 0.621371
        elif from_unit == 'miles' and to_unit == 'kilometers':
            result = value / 0.621371
        elif from_unit == 'meters' and to_unit == 'yards':
            result = value * 1.09361
        elif from_unit == 'yards' and to_unit == 'meters':
            result = value / 1.09361
        elif from_unit == 'meters' and to_unit == 'inches':
            result = value * 39.3701
        elif from_unit == 'inches' and to_unit == 'meters':
            result = value / 39.3701
        # Temperature conversions
        elif from_unit == 'celsius' and to_unit == 'fahrenheit':
            result = (value * 9/5) + 32
        elif from_unit == 'fahrenheit' and to_unit == 'celsius':
            result = (value - 32) * 5/9
        elif from_unit == 'celsius' and to_unit == 'kelvin':
            result = value + 273.15
        elif from_unit == 'kelvin' and to_unit == 'celsius':
            result = value - 273.15
        elif from_unit == 'fahrenheit' and to_unit == 'kelvin':
            result = (value - 32) * 5/9 + 273.15
        elif from_unit == 'kelvin' and to_unit == 'fahrenheit':
            result = (value - 273.15) * 9/5 + 32
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
