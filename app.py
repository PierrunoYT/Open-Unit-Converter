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
        length_units = {
            'mm': 0.001, 'cm': 0.01, 'm': 1, 'km': 1000,
            'in': 0.0254, 'ft': 0.3048, 'yd': 0.9144, 'mi': 1609.344
        }
        
        weight_units = {
            'mg': 0.001, 'g': 1, 'kg': 1000, 't': 1000000
        }
        
        if from_unit in length_units and to_unit in length_units:
            # Convert to meters first, then to the target unit
            meters = value * length_units[from_unit]
            result = meters / length_units[to_unit]
        elif from_unit in weight_units and to_unit in weight_units:
            # Convert to grams first, then to the target unit
            grams = value * weight_units[from_unit]
            result = grams / weight_units[to_unit]
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
