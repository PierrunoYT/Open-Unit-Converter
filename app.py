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
            'in': 0.0254, 'ft': 0.3048, 'yd': 0.9144, 'mi': 1609.344,
            'nmi': 1852, 'fathom': 1.8288,
            'μm': 1e-6, 'nm': 1e-9, 'Å': 1e-10,
            'ly': 9.461e15, 'pc': 3.086e16, 'AU': 1.496e11,
            'league': 4828.032, 'furlong': 201.168, 'rod': 5.0292, 'chain': 20.1168, 'link': 0.201168
        }
        
        weight_units = {
            'μg': 1e-6, 'mg': 0.001, 'g': 1, 'kg': 1000, 't': 1000000,
            'oz': 28.34952, 'lb': 453.59237, 'st': 6350.29318,
            'ton_us': 907184.74, 'ton_uk': 1016046.9088,
            'ct': 0.2, 'gr': 0.06479891, 'dr': 1.7718451953125,
            'amu': 1.66053906660e-24,
            'cwt_us': 45359.237, 'cwt_uk': 50802.34544,
            'quarter_us': 11339.80925, 'quarter_uk': 12700.58636,
            'slug': 14593.903,
            'scruple': 1.2959782,
            'drachm': 3.8879346
        }
        
        volume_units = {
            'mL': 0.001, 'cL': 0.01, 'dL': 0.1, 'L': 1, 'cm³': 0.001, 'm³': 1000,
            'fl_oz': 0.0295735, 'cup': 0.236588, 'pt': 0.473176, 'qt': 0.946353, 'gal': 3.78541,
            'in³': 0.0163871, 'ft³': 28.3168, 'yd³': 764.555,
            'tsp': 0.00492892, 'tbsp': 0.0147868,
            'μL': 1e-6, 'nL': 1e-9,
            'bbl': 158.987,
            'TEU': 33200,  # Approximate volume of a 20-foot shipping container
            'bushel': 35.2391, 'peck': 8.80977, 'gill': 0.118294, 'hogshead': 238.481,
            'shot': 0.0443603, 'fifth': 0.757082
        }
        
        if from_unit in length_units and to_unit in length_units:
            # Convert to meters first, then to the target unit
            meters = value * length_units[from_unit]
            result = meters / length_units[to_unit]
        elif from_unit in weight_units and to_unit in weight_units:
            # Convert to grams first, then to the target unit
            grams = value * weight_units[from_unit]
            result = grams / weight_units[to_unit]
        elif from_unit in volume_units and to_unit in volume_units:
            # Convert to liters first, then to the target unit
            liters = value * volume_units[from_unit]
            result = liters / volume_units[to_unit]
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
