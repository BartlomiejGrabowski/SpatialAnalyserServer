# Python stubs generated by omniidl from geodetic_computation.idl

import omniORB, _omnipy
from omniORB import CORBA, PortableServer
_0_CORBA = CORBA

_omnipy.checkVersion(3,0, __file__)


#
# Start of module "Projection"
#
__name__ = "Projection"
_0_Projection = omniORB.openModule("Projection", r"geodetic_computation.idl")
_0_Projection__POA = omniORB.openModule("Projection__POA", r"geodetic_computation.idl")


# typedef ... latitude
class latitude:
    _NP_RepositoryId = "IDL:Projection/latitude:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Projection.latitude = latitude
_0_Projection._d_latitude  = omniORB.tcInternal.tv_float
_0_Projection._ad_latitude = (omniORB.tcInternal.tv_alias, latitude._NP_RepositoryId, "latitude", omniORB.tcInternal.tv_float)
_0_Projection._tc_latitude = omniORB.tcInternal.createTypeCode(_0_Projection._ad_latitude)
omniORB.registerType(latitude._NP_RepositoryId, _0_Projection._ad_latitude, _0_Projection._tc_latitude)
del latitude

# typedef ... longitude
class longitude:
    _NP_RepositoryId = "IDL:Projection/longitude:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Projection.longitude = longitude
_0_Projection._d_longitude  = omniORB.tcInternal.tv_float
_0_Projection._ad_longitude = (omniORB.tcInternal.tv_alias, longitude._NP_RepositoryId, "longitude", omniORB.tcInternal.tv_float)
_0_Projection._tc_longitude = omniORB.tcInternal.createTypeCode(_0_Projection._ad_longitude)
omniORB.registerType(longitude._NP_RepositoryId, _0_Projection._ad_longitude, _0_Projection._tc_longitude)
del longitude

# typedef ... azimuth
class azimuth:
    _NP_RepositoryId = "IDL:Projection/azimuth:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Projection.azimuth = azimuth
_0_Projection._d_azimuth  = omniORB.tcInternal.tv_float
_0_Projection._ad_azimuth = (omniORB.tcInternal.tv_alias, azimuth._NP_RepositoryId, "azimuth", omniORB.tcInternal.tv_float)
_0_Projection._tc_azimuth = omniORB.tcInternal.createTypeCode(_0_Projection._ad_azimuth)
omniORB.registerType(azimuth._NP_RepositoryId, _0_Projection._ad_azimuth, _0_Projection._tc_azimuth)
del azimuth

# typedef ... distance
class distance:
    _NP_RepositoryId = "IDL:Projection/distance:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Projection.distance = distance
_0_Projection._d_distance  = omniORB.tcInternal.tv_float
_0_Projection._ad_distance = (omniORB.tcInternal.tv_alias, distance._NP_RepositoryId, "distance", omniORB.tcInternal.tv_float)
_0_Projection._tc_distance = omniORB.tcInternal.createTypeCode(_0_Projection._ad_distance)
omniORB.registerType(distance._NP_RepositoryId, _0_Projection._ad_distance, _0_Projection._tc_distance)
del distance

# typedef ... number_of_points
class number_of_points:
    _NP_RepositoryId = "IDL:Projection/number_of_points:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Projection.number_of_points = number_of_points
_0_Projection._d_number_of_points  = omniORB.tcInternal.tv_short
_0_Projection._ad_number_of_points = (omniORB.tcInternal.tv_alias, number_of_points._NP_RepositoryId, "number_of_points", omniORB.tcInternal.tv_short)
_0_Projection._tc_number_of_points = omniORB.tcInternal.createTypeCode(_0_Projection._ad_number_of_points)
omniORB.registerType(number_of_points._NP_RepositoryId, _0_Projection._ad_number_of_points, _0_Projection._tc_number_of_points)
del number_of_points

# typedef ... projection_name
class projection_name:
    _NP_RepositoryId = "IDL:Projection/projection_name:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Projection.projection_name = projection_name
_0_Projection._d_projection_name  = (omniORB.tcInternal.tv_string,1024)
_0_Projection._ad_projection_name = (omniORB.tcInternal.tv_alias, projection_name._NP_RepositoryId, "projection_name", (omniORB.tcInternal.tv_string,1024))
_0_Projection._tc_projection_name = omniORB.tcInternal.createTypeCode(_0_Projection._ad_projection_name)
omniORB.registerType(projection_name._NP_RepositoryId, _0_Projection._ad_projection_name, _0_Projection._tc_projection_name)
del projection_name

# typedef ... projection_desc
class projection_desc:
    _NP_RepositoryId = "IDL:Projection/projection_desc:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Projection.projection_desc = projection_desc
_0_Projection._d_projection_desc  = (omniORB.tcInternal.tv_string,1024)
_0_Projection._ad_projection_desc = (omniORB.tcInternal.tv_alias, projection_desc._NP_RepositoryId, "projection_desc", (omniORB.tcInternal.tv_string,1024))
_0_Projection._tc_projection_desc = omniORB.tcInternal.createTypeCode(_0_Projection._ad_projection_desc)
omniORB.registerType(projection_desc._NP_RepositoryId, _0_Projection._ad_projection_desc, _0_Projection._tc_projection_desc)
del projection_desc

# typedef ... ellipsoid_name
class ellipsoid_name:
    _NP_RepositoryId = "IDL:Projection/ellipsoid_name:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Projection.ellipsoid_name = ellipsoid_name
_0_Projection._d_ellipsoid_name  = (omniORB.tcInternal.tv_string,1024)
_0_Projection._ad_ellipsoid_name = (omniORB.tcInternal.tv_alias, ellipsoid_name._NP_RepositoryId, "ellipsoid_name", (omniORB.tcInternal.tv_string,1024))
_0_Projection._tc_ellipsoid_name = omniORB.tcInternal.createTypeCode(_0_Projection._ad_ellipsoid_name)
omniORB.registerType(ellipsoid_name._NP_RepositoryId, _0_Projection._ad_ellipsoid_name, _0_Projection._tc_ellipsoid_name)
del ellipsoid_name

# typedef ... ellipsoid_desc
class ellipsoid_desc:
    _NP_RepositoryId = "IDL:Projection/ellipsoid_desc:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Projection.ellipsoid_desc = ellipsoid_desc
_0_Projection._d_ellipsoid_desc  = (omniORB.tcInternal.tv_string,1024)
_0_Projection._ad_ellipsoid_desc = (omniORB.tcInternal.tv_alias, ellipsoid_desc._NP_RepositoryId, "ellipsoid_desc", (omniORB.tcInternal.tv_string,1024))
_0_Projection._tc_ellipsoid_desc = omniORB.tcInternal.createTypeCode(_0_Projection._ad_ellipsoid_desc)
omniORB.registerType(ellipsoid_desc._NP_RepositoryId, _0_Projection._ad_ellipsoid_desc, _0_Projection._tc_ellipsoid_desc)
del ellipsoid_desc

# typedef ... input_projection
class input_projection:
    _NP_RepositoryId = "IDL:Projection/input_projection:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Projection.input_projection = input_projection
_0_Projection._d_input_projection  = (omniORB.tcInternal.tv_string,1024)
_0_Projection._ad_input_projection = (omniORB.tcInternal.tv_alias, input_projection._NP_RepositoryId, "input_projection", (omniORB.tcInternal.tv_string,1024))
_0_Projection._tc_input_projection = omniORB.tcInternal.createTypeCode(_0_Projection._ad_input_projection)
omniORB.registerType(input_projection._NP_RepositoryId, _0_Projection._ad_input_projection, _0_Projection._tc_input_projection)
del input_projection

# typedef ... output_projection
class output_projection:
    _NP_RepositoryId = "IDL:Projection/output_projection:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Projection.output_projection = output_projection
_0_Projection._d_output_projection  = (omniORB.tcInternal.tv_string,1024)
_0_Projection._ad_output_projection = (omniORB.tcInternal.tv_alias, output_projection._NP_RepositoryId, "output_projection", (omniORB.tcInternal.tv_string,1024))
_0_Projection._tc_output_projection = omniORB.tcInternal.createTypeCode(_0_Projection._ad_output_projection)
omniORB.registerType(output_projection._NP_RepositoryId, _0_Projection._ad_output_projection, _0_Projection._tc_output_projection)
del output_projection

# struct Fwd_transformation
_0_Projection.Fwd_transformation = omniORB.newEmptyClass()
class Fwd_transformation (omniORB.StructBase):
    _NP_RepositoryId = "IDL:Projection/Fwd_transformation:1.0"

    def __init__(self, end_latitude, end_longitude, back_azimuth):
        self.end_latitude = end_latitude
        self.end_longitude = end_longitude
        self.back_azimuth = back_azimuth

_0_Projection.Fwd_transformation = Fwd_transformation
_0_Projection._d_Fwd_transformation  = (omniORB.tcInternal.tv_struct, Fwd_transformation, Fwd_transformation._NP_RepositoryId, "Fwd_transformation", "end_latitude", omniORB.typeMapping["IDL:Projection/latitude:1.0"], "end_longitude", omniORB.typeMapping["IDL:Projection/longitude:1.0"], "back_azimuth", omniORB.typeMapping["IDL:Projection/azimuth:1.0"])
_0_Projection._tc_Fwd_transformation = omniORB.tcInternal.createTypeCode(_0_Projection._d_Fwd_transformation)
omniORB.registerType(Fwd_transformation._NP_RepositoryId, _0_Projection._d_Fwd_transformation, _0_Projection._tc_Fwd_transformation)
del Fwd_transformation

# struct Inv_transformation
_0_Projection.Inv_transformation = omniORB.newEmptyClass()
class Inv_transformation (omniORB.StructBase):
    _NP_RepositoryId = "IDL:Projection/Inv_transformation:1.0"

    def __init__(self, trans_azimuth, back_azimuth, dist):
        self.trans_azimuth = trans_azimuth
        self.back_azimuth = back_azimuth
        self.dist = dist

_0_Projection.Inv_transformation = Inv_transformation
_0_Projection._d_Inv_transformation  = (omniORB.tcInternal.tv_struct, Inv_transformation, Inv_transformation._NP_RepositoryId, "Inv_transformation", "trans_azimuth", omniORB.typeMapping["IDL:Projection/azimuth:1.0"], "back_azimuth", omniORB.typeMapping["IDL:Projection/azimuth:1.0"], "dist", omniORB.typeMapping["IDL:Projection/distance:1.0"])
_0_Projection._tc_Inv_transformation = omniORB.tcInternal.createTypeCode(_0_Projection._d_Inv_transformation)
omniORB.registerType(Inv_transformation._NP_RepositoryId, _0_Projection._d_Inv_transformation, _0_Projection._tc_Inv_transformation)
del Inv_transformation

# struct Npt
_0_Projection.Npt = omniORB.newEmptyClass()
class Npt (omniORB.StructBase):
    _NP_RepositoryId = "IDL:Projection/Npt:1.0"

    def __init__(self, end_longitude, end_latitude):
        self.end_longitude = end_longitude
        self.end_latitude = end_latitude

_0_Projection.Npt = Npt
_0_Projection._d_Npt  = (omniORB.tcInternal.tv_struct, Npt, Npt._NP_RepositoryId, "Npt", "end_longitude", omniORB.typeMapping["IDL:Projection/longitude:1.0"], "end_latitude", omniORB.typeMapping["IDL:Projection/latitude:1.0"])
_0_Projection._tc_Npt = omniORB.tcInternal.createTypeCode(_0_Projection._d_Npt)
omniORB.registerType(Npt._NP_RepositoryId, _0_Projection._d_Npt, _0_Projection._tc_Npt)
del Npt

# struct Proj
_0_Projection.Proj = omniORB.newEmptyClass()
class Proj (omniORB.StructBase):
    _NP_RepositoryId = "IDL:Projection/Proj:1.0"

    def __init__(self, proj_name, proj_desc):
        self.proj_name = proj_name
        self.proj_desc = proj_desc

_0_Projection.Proj = Proj
_0_Projection._d_Proj  = (omniORB.tcInternal.tv_struct, Proj, Proj._NP_RepositoryId, "Proj", "proj_name", omniORB.typeMapping["IDL:Projection/projection_name:1.0"], "proj_desc", omniORB.typeMapping["IDL:Projection/projection_desc:1.0"])
_0_Projection._tc_Proj = omniORB.tcInternal.createTypeCode(_0_Projection._d_Proj)
omniORB.registerType(Proj._NP_RepositoryId, _0_Projection._d_Proj, _0_Projection._tc_Proj)
del Proj

# struct Ellipsoid
_0_Projection.Ellipsoid = omniORB.newEmptyClass()
class Ellipsoid (omniORB.StructBase):
    _NP_RepositoryId = "IDL:Projection/Ellipsoid:1.0"

    def __init__(self, ellps_name, ellps_desc):
        self.ellps_name = ellps_name
        self.ellps_desc = ellps_desc

_0_Projection.Ellipsoid = Ellipsoid
_0_Projection._d_Ellipsoid  = (omniORB.tcInternal.tv_struct, Ellipsoid, Ellipsoid._NP_RepositoryId, "Ellipsoid", "ellps_name", omniORB.typeMapping["IDL:Projection/ellipsoid_name:1.0"], "ellps_desc", omniORB.typeMapping["IDL:Projection/ellipsoid_desc:1.0"])
_0_Projection._tc_Ellipsoid = omniORB.tcInternal.createTypeCode(_0_Projection._d_Ellipsoid)
omniORB.registerType(Ellipsoid._NP_RepositoryId, _0_Projection._d_Ellipsoid, _0_Projection._tc_Ellipsoid)
del Ellipsoid

# struct Coordinates
_0_Projection.Coordinates = omniORB.newEmptyClass()
class Coordinates (omniORB.StructBase):
    _NP_RepositoryId = "IDL:Projection/Coordinates:1.0"

    def __init__(self, x2, y2, z2):
        self.x2 = x2
        self.y2 = y2
        self.z2 = z2

_0_Projection.Coordinates = Coordinates
_0_Projection._d_Coordinates  = (omniORB.tcInternal.tv_struct, Coordinates, Coordinates._NP_RepositoryId, "Coordinates", "x2", omniORB.tcInternal.tv_float, "y2", omniORB.tcInternal.tv_float, "z2", omniORB.tcInternal.tv_float)
_0_Projection._tc_Coordinates = omniORB.tcInternal.createTypeCode(_0_Projection._d_Coordinates)
omniORB.registerType(Coordinates._NP_RepositoryId, _0_Projection._d_Coordinates, _0_Projection._tc_Coordinates)
del Coordinates

# typedef ... Npts
class Npts:
    _NP_RepositoryId = "IDL:Projection/Npts:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Projection.Npts = Npts
_0_Projection._d_Npts  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:Projection/Npt:1.0"], 0)
_0_Projection._ad_Npts = (omniORB.tcInternal.tv_alias, Npts._NP_RepositoryId, "Npts", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:Projection/Npt:1.0"], 0))
_0_Projection._tc_Npts = omniORB.tcInternal.createTypeCode(_0_Projection._ad_Npts)
omniORB.registerType(Npts._NP_RepositoryId, _0_Projection._ad_Npts, _0_Projection._tc_Npts)
del Npts

# typedef ... Proj_list
class Proj_list:
    _NP_RepositoryId = "IDL:Projection/Proj_list:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Projection.Proj_list = Proj_list
_0_Projection._d_Proj_list  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:Projection/Proj:1.0"], 0)
_0_Projection._ad_Proj_list = (omniORB.tcInternal.tv_alias, Proj_list._NP_RepositoryId, "Proj_list", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:Projection/Proj:1.0"], 0))
_0_Projection._tc_Proj_list = omniORB.tcInternal.createTypeCode(_0_Projection._ad_Proj_list)
omniORB.registerType(Proj_list._NP_RepositoryId, _0_Projection._ad_Proj_list, _0_Projection._tc_Proj_list)
del Proj_list

# typedef ... Ellipsoid_list
class Ellipsoid_list:
    _NP_RepositoryId = "IDL:Projection/Ellipsoid_list:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Projection.Ellipsoid_list = Ellipsoid_list
_0_Projection._d_Ellipsoid_list  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:Projection/Ellipsoid:1.0"], 0)
_0_Projection._ad_Ellipsoid_list = (omniORB.tcInternal.tv_alias, Ellipsoid_list._NP_RepositoryId, "Ellipsoid_list", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:Projection/Ellipsoid:1.0"], 0))
_0_Projection._tc_Ellipsoid_list = omniORB.tcInternal.createTypeCode(_0_Projection._ad_Ellipsoid_list)
omniORB.registerType(Ellipsoid_list._NP_RepositoryId, _0_Projection._ad_Ellipsoid_list, _0_Projection._tc_Ellipsoid_list)
del Ellipsoid_list

# exception ArgumentsNotInOrder
_0_Projection.ArgumentsNotInOrder = omniORB.newEmptyClass()
class ArgumentsNotInOrder (CORBA.UserException):
    _NP_RepositoryId = "IDL:Projection/ArgumentsNotInOrder:1.0"

    def __init__(self, reason):
        CORBA.UserException.__init__(self, reason)
        self.reason = reason

_0_Projection.ArgumentsNotInOrder = ArgumentsNotInOrder
_0_Projection._d_ArgumentsNotInOrder  = (omniORB.tcInternal.tv_except, ArgumentsNotInOrder, ArgumentsNotInOrder._NP_RepositoryId, "ArgumentsNotInOrder", "reason", (omniORB.tcInternal.tv_string,0))
_0_Projection._tc_ArgumentsNotInOrder = omniORB.tcInternal.createTypeCode(_0_Projection._d_ArgumentsNotInOrder)
omniORB.registerType(ArgumentsNotInOrder._NP_RepositoryId, _0_Projection._d_ArgumentsNotInOrder, _0_Projection._tc_ArgumentsNotInOrder)
del ArgumentsNotInOrder

# interface Geodetic
_0_Projection._d_Geodetic = (omniORB.tcInternal.tv_objref, "IDL:Projection/Geodetic:1.0", "Geodetic")
omniORB.typeMapping["IDL:Projection/Geodetic:1.0"] = _0_Projection._d_Geodetic
_0_Projection.Geodetic = omniORB.newEmptyClass()
class Geodetic :
    _NP_RepositoryId = _0_Projection._d_Geodetic[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_Projection.Geodetic = Geodetic
_0_Projection._tc_Geodetic = omniORB.tcInternal.createTypeCode(_0_Projection._d_Geodetic)
omniORB.registerType(Geodetic._NP_RepositoryId, _0_Projection._d_Geodetic, _0_Projection._tc_Geodetic)

# Geodetic operations and attributes
Geodetic._d_get_fwd_transformation = ((omniORB.typeMapping["IDL:Projection/longitude:1.0"], omniORB.typeMapping["IDL:Projection/latitude:1.0"], omniORB.typeMapping["IDL:Projection/azimuth:1.0"], omniORB.typeMapping["IDL:Projection/distance:1.0"]), (omniORB.typeMapping["IDL:Projection/Fwd_transformation:1.0"], ), {_0_Projection.ArgumentsNotInOrder._NP_RepositoryId: _0_Projection._d_ArgumentsNotInOrder})
Geodetic._d_get_inv_transformation = ((omniORB.typeMapping["IDL:Projection/longitude:1.0"], omniORB.typeMapping["IDL:Projection/latitude:1.0"], omniORB.typeMapping["IDL:Projection/longitude:1.0"], omniORB.typeMapping["IDL:Projection/latitude:1.0"]), (omniORB.typeMapping["IDL:Projection/Inv_transformation:1.0"], ), {_0_Projection.ArgumentsNotInOrder._NP_RepositoryId: _0_Projection._d_ArgumentsNotInOrder})
Geodetic._d_get_intermediate_points = ((omniORB.typeMapping["IDL:Projection/longitude:1.0"], omniORB.typeMapping["IDL:Projection/latitude:1.0"], omniORB.typeMapping["IDL:Projection/longitude:1.0"], omniORB.typeMapping["IDL:Projection/latitude:1.0"], omniORB.typeMapping["IDL:Projection/number_of_points:1.0"]), (omniORB.typeMapping["IDL:Projection/Npts:1.0"], ), {_0_Projection.ArgumentsNotInOrder._NP_RepositoryId: _0_Projection._d_ArgumentsNotInOrder})
Geodetic._d_get_projection_list = ((), (omniORB.typeMapping["IDL:Projection/Proj_list:1.0"], ), None)
Geodetic._d_get_ellipsoid_list = ((), (omniORB.typeMapping["IDL:Projection/Ellipsoid_list:1.0"], ), None)
Geodetic._d_transform_coordinate_systems = ((omniORB.typeMapping["IDL:Projection/input_projection:1.0"], omniORB.typeMapping["IDL:Projection/output_projection:1.0"], omniORB.tcInternal.tv_float, omniORB.tcInternal.tv_float, omniORB.tcInternal.tv_float), (omniORB.typeMapping["IDL:Projection/Coordinates:1.0"], ), {_0_Projection.ArgumentsNotInOrder._NP_RepositoryId: _0_Projection._d_ArgumentsNotInOrder})

# Geodetic object reference
class _objref_Geodetic (CORBA.Object):
    _NP_RepositoryId = Geodetic._NP_RepositoryId

    def __init__(self):
        CORBA.Object.__init__(self)

    def get_fwd_transformation(self, *args):
        return _omnipy.invoke(self, "get_fwd_transformation", _0_Projection.Geodetic._d_get_fwd_transformation, args)

    def get_inv_transformation(self, *args):
        return _omnipy.invoke(self, "get_inv_transformation", _0_Projection.Geodetic._d_get_inv_transformation, args)

    def get_intermediate_points(self, *args):
        return _omnipy.invoke(self, "get_intermediate_points", _0_Projection.Geodetic._d_get_intermediate_points, args)

    def get_projection_list(self, *args):
        return _omnipy.invoke(self, "get_projection_list", _0_Projection.Geodetic._d_get_projection_list, args)

    def get_ellipsoid_list(self, *args):
        return _omnipy.invoke(self, "get_ellipsoid_list", _0_Projection.Geodetic._d_get_ellipsoid_list, args)

    def transform_coordinate_systems(self, *args):
        return _omnipy.invoke(self, "transform_coordinate_systems", _0_Projection.Geodetic._d_transform_coordinate_systems, args)

    __methods__ = ["get_fwd_transformation", "get_inv_transformation", "get_intermediate_points", "get_projection_list", "get_ellipsoid_list", "transform_coordinate_systems"] + CORBA.Object.__methods__

omniORB.registerObjref(Geodetic._NP_RepositoryId, _objref_Geodetic)
_0_Projection._objref_Geodetic = _objref_Geodetic
del Geodetic, _objref_Geodetic

# Geodetic skeleton
__name__ = "Projection__POA"
class Geodetic (PortableServer.Servant):
    _NP_RepositoryId = _0_Projection.Geodetic._NP_RepositoryId


    _omni_op_d = {"get_fwd_transformation": _0_Projection.Geodetic._d_get_fwd_transformation, "get_inv_transformation": _0_Projection.Geodetic._d_get_inv_transformation, "get_intermediate_points": _0_Projection.Geodetic._d_get_intermediate_points, "get_projection_list": _0_Projection.Geodetic._d_get_projection_list, "get_ellipsoid_list": _0_Projection.Geodetic._d_get_ellipsoid_list, "transform_coordinate_systems": _0_Projection.Geodetic._d_transform_coordinate_systems}

Geodetic._omni_skeleton = Geodetic
_0_Projection__POA.Geodetic = Geodetic
omniORB.registerSkeleton(Geodetic._NP_RepositoryId, Geodetic)
del Geodetic
__name__ = "Projection"

#
# End of module "Projection"
#
__name__ = "geodetic_computation_idl"

_exported_modules = ( "Projection", )

# The end.
