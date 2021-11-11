def create_corona_message(data):
    message = ''
    country = data.get('country') or 'world'
    message += f'Covid data - {country}\n\n'

    cases = data.get('cases')
    deaths = data.get('deaths')
    recovered = data.get('recovered')
    
    message += (f'Cases: {cases}\n' + \
        f'Deaths: {deaths}\n' + \
        f'Recovered: {recovered}')

    return message