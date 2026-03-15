from pprint import pprint

import ifcopenshell

model = ifcopenshell.open('../../КР.ifc')

sites = model.by_type('IfcSite')
site = sites[0]

# Получим свойства строительной площадки
site_info = site.get_info()
print('site:')
pprint(site_info)
print()

# Одно из свойств - это ObjectPlacement, расположение объекта
# Теперь посмотрим, какими свойствами обладает сам объект ObjectPlacement
obj_plm = site_info['ObjectPlacement']
obj_plm_info = obj_plm.get_info()
print('ObjectPlacement:')
pprint(obj_plm_info)
print()

# RelativePlacement - это свойство расположения объекта площадки
# относительно другого объекта.
# В данном случае, относительно расположения осей IfcAxis2Placement3D
rlt_plm = obj_plm_info['RelativePlacement']
rlt_plm_info = rlt_plm.get_info()
print('RelativePlacement:')
pprint(rlt_plm_info)
print()

# И, наконец, свойство Location, которое содержит искомые координаты
# строительной площадки
location = rlt_plm_info['Location']
location_info = location.get_info()
print('Location:')
pprint(location_info)
print()

coordinates = location_info['Coordinates']

# Вспомним, что к свойствам можно обращаться напрямую,
# без применения метода get_info()
coordinates2 = site.ObjectPlacement.RelativePlacement.Location.Coordinates
print('coordinates2: ', coordinates2)
print()

ifc_x = round(coordinates[0])
ifc_y = round(coordinates[1])
ifc_z = round(coordinates[2])

print('X: ', ifc_x)
print('Y: ', ifc_y)
print('Z: ', ifc_z)
