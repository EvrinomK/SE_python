PH_value = float(input('Введите PH: '))

def get_material(PH_value):
    PH_map = {
        1.1:'Яблочный сок',
        2.6:'Мыло', 
        2.8:'Шампунь'}

    result = PH_map.get(PH_value)
    if result == None:
        return 'Не найден'
    else:
        return result
   
print(f'Материал: {get_material(PH_value)}')