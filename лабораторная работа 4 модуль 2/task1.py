import ifcopenshell
import ifcopenshell.util.element

model = ifcopenshell.open('../../Sample model.ifc')

elements = model.by_type('IfcElement')

requirements = [
    {'property_set': 'Идентификация',
     'property_name': 'Com.Code'},
    {'property_set': 'Идентификация',
     'property_name': 'Огнестойкость'},
    {'property_set': 'Материалы и отделка',
     'property_name': 'Материал несущих конструкций'},
]

success = 0
count = 0

for element in elements:

    dct_ = {
        'type': element.is_a(),
        'GlobalId': element.GlobalId,
        'failed_checks': []
    }

    psets = ifcopenshell.util.element.get_psets(element)

    for requirement in requirements:
        p_set = requirement['property_set']
        p_name = requirement['property_name']

        prop = psets.get(p_set, {}).get(p_name)

        if prop is None:
            dct_['failed_checks'].append(p_name)
        else:
            success += 1

        count += 1

    # ВАЖНО: использовать print
    print(dct_)

print('Успешных проверок: ', success)
print('Всего проверок: ', count)
print('Качество модели: ', (success / count) * 100, '%')