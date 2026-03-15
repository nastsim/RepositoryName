import ifcopenshell
import numpy as np

model = ifcopenshell.open('../../КР_rotated.ifc')


def get_internal_site_rot_angle(model: ifcopenshell.file):
    # Угол поворота
    ifc_rot = 0
    geomcont = model.by_type('IfcGeometricRepresentationContext')
    single_geom_cont = geomcont[0]

    if single_geom_cont.TrueNorth is not None:
        x = single_geom_cont.TrueNorth.DirectionRatios[0]
        y = single_geom_cont.TrueNorth.DirectionRatios[1]
        tan = x / y
        arctan = np.arctan(tan)
        ifc_rot = np.rad2deg(arctan)

    return ifc_rot

print(get_internal_site_rot_angle(model))
