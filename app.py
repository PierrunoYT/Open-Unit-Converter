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
            'mg': 0.001, 'g': 1, 'kg': 1000, 't': 1000000,
            'oz': 28.34952, 'lb': 453.59237, 'st': 6350.29318,
            'ton_us': 907184.74, 'ton_uk': 1016046.9088
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
        def celsius_to_kelvin(c):
            return c + 273.15

        def kelvin_to_celsius(k):
            return k - 273.15

        temp_conversions = {
            'celsius': lambda x: x,
            'fahrenheit': lambda x: (x - 32) * 5/9,
            'kelvin': kelvin_to_celsius,
            'rankine': lambda x: (x - 491.67) * 5/9,
            'reaumur': lambda x: x * 5/4,
            'romer': lambda x: (x - 7.5) * 40/21,
            'delisle': lambda x: (100 - x) * 2/3,
            'newton': lambda x: x * 100/33,
        }

        inverse_temp_conversions = {
            'celsius': lambda x: x,
            'fahrenheit': lambda x: x * 9/5 + 32,
            'kelvin': celsius_to_kelvin,
            'rankine': lambda x: x * 9/5 + 491.67,
            'reaumur': lambda x: x * 4/5,
            'romer': lambda x: x * 21/40 + 7.5,
            'delisle': lambda x: 100 - x * 3/2,
            'newton': lambda x: x * 33/100,
        }

        if from_unit in temp_conversions and to_unit in inverse_temp_conversions:
            celsius = temp_conversions[from_unit](value)
            result = inverse_temp_conversions[to_unit](celsius)
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
