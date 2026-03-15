import os
from pprint import pprint

import ifcopenshell


def get_internal_site_coordinates(ifc_model: ifcopenshell.file):
    # TODO Реализуйте функцию определения координат IFC-модели

    return ifc_x, ifc_y, ifc_z


models = [ifcopenshell.open('../../КР.ifc'),
          ifcopenshell.open('../../ОВК.ifc'),
          ifcopenshell.open('../../ВК.ifc')]

for model in models:
    print(get_internal_site_coordinates(model))
