
def build_pts_description(d):
    return f'''
ПТС: {d['pts']}
Авто: {d['auto']}
Пробег: {d['mileage']} км
Цена: {d['price']}
Владельцев: {d['owners']}

Двигатель: {d['engine']}
Турбо: {d['turbo']}
Гидравлика: {d['hydro']}
Чип: {d['chip']}
Тормоза: {d['brakes']}
Нитро: {d['nitro']}
Трансмиссия: {d['trans']}
Шины: {d['tires']}
Подвеска: {d['susp']}
'''.strip()
