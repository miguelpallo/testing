from flask import Flask, request, jsonify
import pandas as pd
import numpy as np

app = Flask(__name__)

# Lee el archivo CSV con las tasas de cambio
exchange_rates_df = pd.read_csv('exchange_rates.csv')
# Ruta para convertir moneda
# Ruta para convertir moneda
@app.route('/convert', methods=['POST'])
def convert_currency():
    data = request.get_json()
    source_currency = data.get('source_currency')
    target_currency = data.get('target_currency')
    amount = data.get('amount')
    date = data.get('date')  # Agregar fecha como parámetro

    if source_currency is None or target_currency is None or amount is None:
        return jsonify({'error': 'Debes proporcionar source_currency, target_currency, amount y date'}), 400

    # Intenta encontrar la tasa de cambio para la fecha proporcionada
    exchange_rate = exchange_rates_df[(exchange_rates_df['source_currency'] == source_currency) &
                                       (exchange_rates_df['target_currency'] == target_currency) &
                                       (exchange_rates_df['date'] == date)]

    if not exchange_rate.empty:
        rate = exchange_rate.iloc[0]['rate']
        converted_amount = amount * rate
    else:
        # Si no se encontró una tasa específica para la fecha, busca la tasa de cambio más cercana en el tiempo
        nearest_exchange_rate = exchange_rates_df[(exchange_rates_df['source_currency'] == source_currency) &
                                                   (exchange_rates_df['target_currency'] == target_currency)]

        if not nearest_exchange_rate.empty:
            # Calcula la diferencia en días y encuentra la fecha más cercana
            nearest_exchange_rate['date_diff'] = abs(pd.to_datetime(nearest_exchange_rate['date']) - pd.to_datetime(date))
            nearest_rate = nearest_exchange_rate.loc[nearest_exchange_rate['date_diff'].idxmin()]['rate']
            converted_amount = amount * nearest_rate
        else:
            return jsonify({'error': 'No se encontraron tasas de cambio para la conversión'}), 400
    #only 4 decimals
    converted_amount = round(converted_amount, 4)
    return jsonify({'converted_amount': converted_amount})


if __name__ == '__main__':
    app.run(debug=True)