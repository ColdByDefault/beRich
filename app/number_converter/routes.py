from flask import render_template, request, flash
from . import number_converter

@number_converter.route('/convert', methods=['GET', 'POST'])
def convert():
    if request.method == 'POST':
        number = request.form.get('number')
        base = request.form.get('base')

        if not number or not base:
            flash('Please provide both number and base.', 'error')
            return render_template('number_converter/convert.html')

        try:
            base = int(base)
            if base == 10:
                decimal = int(number)
            elif base == 2:
                decimal = int(number, 2)
            elif base == 16:
                decimal = int(number, 16)
            else:
                flash('Unsupported base. Use 2, 10, or 16.', 'error')
                return render_template('number_converter/convert.html')

            binary = bin(decimal)[2:]
            hexadecimal = hex(decimal)[2:]
            return render_template('number_converter/convert.html', decimal=decimal, binary=binary, hexadecimal=hexadecimal)
        except ValueError:
            flash('Invalid number for the given base.', 'error')

    return render_template('number_converter/convert.html')
