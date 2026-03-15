import ifcopenshell


def move_model(ifc_model: ifcopenshell.file,
               vector: tuple[float, float, float]):
    sites = ifc_model.by_type('IfcSite')
    site = sites[0]

    coordinates = site.ObjectPlacement.RelativePlacement.Location.Coordinates
    old_x, old_y, old_z = coordinates
    new_x, new_y, new_z = (old_x + vector[0],
                           old_y + vector[1],
                           old_z + vector[2])

    new_coordinates = (new_x, new_y, new_z)
    site.ObjectPlacement.RelativePlacement.Location.Coordinates = new_coordinates

    return ifc_model


# Координаты модели до перемещения
old_model = ifcopenshell.open('../../ОВК.ifc')
site = old_model.by_type('IfcSite')[0]
print(site.ObjectPlacement.RelativePlacement.Location.Coordinates)

# Перемещаем модель
new_model = move_model(old_model, (0., 0., 241554.))
new_model.write("../../movedModel.ifc")

# Координаты модели после перемещения
new_model = ifcopenshell.open("../../movedModel.ifc")
site = new_model.by_type('IfcSite')[0]
print(site.ObjectPlacement.RelativePlacement.Location.Coordinates)
