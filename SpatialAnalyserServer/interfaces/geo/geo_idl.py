# Python stubs generated by omniidl from geo.idl

import omniORB, _omnipy
from omniORB import CORBA, PortableServer
_0_CORBA = CORBA

_omnipy.checkVersion(3,0, __file__)


#
# Start of module "Geo"
#
__name__ = "Geo"
_0_Geo = omniORB.openModule("Geo", r"geo.idl")
_0_Geo__POA = omniORB.openModule("Geo__POA", r"geo.idl")


# typedef ... latitude
class latitude:
    _NP_RepositoryId = "IDL:Geo/latitude:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Geo.latitude = latitude
_0_Geo._d_latitude  = omniORB.tcInternal.tv_float
_0_Geo._ad_latitude = (omniORB.tcInternal.tv_alias, latitude._NP_RepositoryId, "latitude", omniORB.tcInternal.tv_float)
_0_Geo._tc_latitude = omniORB.tcInternal.createTypeCode(_0_Geo._ad_latitude)
omniORB.registerType(latitude._NP_RepositoryId, _0_Geo._ad_latitude, _0_Geo._tc_latitude)
del latitude

# typedef ... longitude
class longitude:
    _NP_RepositoryId = "IDL:Geo/longitude:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Geo.longitude = longitude
_0_Geo._d_longitude  = omniORB.tcInternal.tv_float
_0_Geo._ad_longitude = (omniORB.tcInternal.tv_alias, longitude._NP_RepositoryId, "longitude", omniORB.tcInternal.tv_float)
_0_Geo._tc_longitude = omniORB.tcInternal.createTypeCode(_0_Geo._ad_longitude)
omniORB.registerType(longitude._NP_RepositoryId, _0_Geo._ad_longitude, _0_Geo._tc_longitude)
del longitude

# typedef ... distance
class distance:
    _NP_RepositoryId = "IDL:Geo/distance:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Geo.distance = distance
_0_Geo._d_distance  = omniORB.tcInternal.tv_float
_0_Geo._ad_distance = (omniORB.tcInternal.tv_alias, distance._NP_RepositoryId, "distance", omniORB.tcInternal.tv_float)
_0_Geo._tc_distance = omniORB.tcInternal.createTypeCode(_0_Geo._ad_distance)
omniORB.registerType(distance._NP_RepositoryId, _0_Geo._ad_distance, _0_Geo._tc_distance)
del distance

# typedef ... bearing
class bearing:
    _NP_RepositoryId = "IDL:Geo/bearing:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Geo.bearing = bearing
_0_Geo._d_bearing  = omniORB.tcInternal.tv_float
_0_Geo._ad_bearing = (omniORB.tcInternal.tv_alias, bearing._NP_RepositoryId, "bearing", omniORB.tcInternal.tv_float)
_0_Geo._tc_bearing = omniORB.tcInternal.createTypeCode(_0_Geo._ad_bearing)
omniORB.registerType(bearing._NP_RepositoryId, _0_Geo._ad_bearing, _0_Geo._tc_bearing)
del bearing

# struct Point
_0_Geo.Point = omniORB.newEmptyClass()
class Point (omniORB.StructBase):
    _NP_RepositoryId = "IDL:Geo/Point:1.0"

    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

_0_Geo.Point = Point
_0_Geo._d_Point  = (omniORB.tcInternal.tv_struct, Point, Point._NP_RepositoryId, "Point", "lat", omniORB.typeMapping["IDL:Geo/latitude:1.0"], "lon", omniORB.typeMapping["IDL:Geo/longitude:1.0"])
_0_Geo._tc_Point = omniORB.tcInternal.createTypeCode(_0_Geo._d_Point)
omniORB.registerType(Point._NP_RepositoryId, _0_Geo._d_Point, _0_Geo._tc_Point)
del Point

# exception LatitudeRangeException
_0_Geo.LatitudeRangeException = omniORB.newEmptyClass()
class LatitudeRangeException (CORBA.UserException):
    _NP_RepositoryId = "IDL:Geo/LatitudeRangeException:1.0"

    def __init__(self, reason):
        CORBA.UserException.__init__(self, reason)
        self.reason = reason

_0_Geo.LatitudeRangeException = LatitudeRangeException
_0_Geo._d_LatitudeRangeException  = (omniORB.tcInternal.tv_except, LatitudeRangeException, LatitudeRangeException._NP_RepositoryId, "LatitudeRangeException", "reason", (omniORB.tcInternal.tv_string,0))
_0_Geo._tc_LatitudeRangeException = omniORB.tcInternal.createTypeCode(_0_Geo._d_LatitudeRangeException)
omniORB.registerType(LatitudeRangeException._NP_RepositoryId, _0_Geo._d_LatitudeRangeException, _0_Geo._tc_LatitudeRangeException)
del LatitudeRangeException

# exception LongitudeRangeException
_0_Geo.LongitudeRangeException = omniORB.newEmptyClass()
class LongitudeRangeException (CORBA.UserException):
    _NP_RepositoryId = "IDL:Geo/LongitudeRangeException:1.0"

    def __init__(self, reason):
        CORBA.UserException.__init__(self, reason)
        self.reason = reason

_0_Geo.LongitudeRangeException = LongitudeRangeException
_0_Geo._d_LongitudeRangeException  = (omniORB.tcInternal.tv_except, LongitudeRangeException, LongitudeRangeException._NP_RepositoryId, "LongitudeRangeException", "reason", (omniORB.tcInternal.tv_string,0))
_0_Geo._tc_LongitudeRangeException = omniORB.tcInternal.createTypeCode(_0_Geo._d_LongitudeRangeException)
omniORB.registerType(LongitudeRangeException._NP_RepositoryId, _0_Geo._d_LongitudeRangeException, _0_Geo._tc_LongitudeRangeException)
del LongitudeRangeException

# exception InternalException
_0_Geo.InternalException = omniORB.newEmptyClass()
class InternalException (CORBA.UserException):
    _NP_RepositoryId = "IDL:Geo/InternalException:1.0"

    def __init__(self, reason):
        CORBA.UserException.__init__(self, reason)
        self.reason = reason

_0_Geo.InternalException = InternalException
_0_Geo._d_InternalException  = (omniORB.tcInternal.tv_except, InternalException, InternalException._NP_RepositoryId, "InternalException", "reason", (omniORB.tcInternal.tv_string,0))
_0_Geo._tc_InternalException = omniORB.tcInternal.createTypeCode(_0_Geo._d_InternalException)
omniORB.registerType(InternalException._NP_RepositoryId, _0_Geo._d_InternalException, _0_Geo._tc_InternalException)
del InternalException

# interface Basic
_0_Geo._d_Basic = (omniORB.tcInternal.tv_objref, "IDL:Geo/Basic:1.0", "Basic")
omniORB.typeMapping["IDL:Geo/Basic:1.0"] = _0_Geo._d_Basic
_0_Geo.Basic = omniORB.newEmptyClass()
class Basic :
    _NP_RepositoryId = _0_Geo._d_Basic[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_Geo.Basic = Basic
_0_Geo._tc_Basic = omniORB.tcInternal.createTypeCode(_0_Geo._d_Basic)
omniORB.registerType(Basic._NP_RepositoryId, _0_Geo._d_Basic, _0_Geo._tc_Basic)

# Basic operations and attributes
Basic._d_distance_haversine = ((omniORB.typeMapping["IDL:Geo/latitude:1.0"], omniORB.typeMapping["IDL:Geo/longitude:1.0"], omniORB.typeMapping["IDL:Geo/latitude:1.0"], omniORB.typeMapping["IDL:Geo/longitude:1.0"]), (omniORB.typeMapping["IDL:Geo/distance:1.0"], ), {_0_Geo.LatitudeRangeException._NP_RepositoryId: _0_Geo._d_LatitudeRangeException, _0_Geo.LongitudeRangeException._NP_RepositoryId: _0_Geo._d_LongitudeRangeException, _0_Geo.InternalException._NP_RepositoryId: _0_Geo._d_InternalException})
Basic._d_distance_sloc = ((omniORB.typeMapping["IDL:Geo/latitude:1.0"], omniORB.typeMapping["IDL:Geo/longitude:1.0"], omniORB.typeMapping["IDL:Geo/latitude:1.0"], omniORB.typeMapping["IDL:Geo/longitude:1.0"]), (omniORB.typeMapping["IDL:Geo/distance:1.0"], ), {_0_Geo.LatitudeRangeException._NP_RepositoryId: _0_Geo._d_LatitudeRangeException, _0_Geo.LongitudeRangeException._NP_RepositoryId: _0_Geo._d_LongitudeRangeException, _0_Geo.InternalException._NP_RepositoryId: _0_Geo._d_InternalException})
Basic._d_initial_bearing = ((omniORB.typeMapping["IDL:Geo/latitude:1.0"], omniORB.typeMapping["IDL:Geo/longitude:1.0"], omniORB.typeMapping["IDL:Geo/latitude:1.0"], omniORB.typeMapping["IDL:Geo/longitude:1.0"]), (omniORB.typeMapping["IDL:Geo/bearing:1.0"], ), {_0_Geo.LatitudeRangeException._NP_RepositoryId: _0_Geo._d_LatitudeRangeException, _0_Geo.LongitudeRangeException._NP_RepositoryId: _0_Geo._d_LongitudeRangeException, _0_Geo.InternalException._NP_RepositoryId: _0_Geo._d_InternalException})
Basic._d_final_bearing = ((omniORB.typeMapping["IDL:Geo/latitude:1.0"], omniORB.typeMapping["IDL:Geo/longitude:1.0"], omniORB.typeMapping["IDL:Geo/latitude:1.0"], omniORB.typeMapping["IDL:Geo/longitude:1.0"]), (omniORB.typeMapping["IDL:Geo/bearing:1.0"], ), {_0_Geo.LatitudeRangeException._NP_RepositoryId: _0_Geo._d_LatitudeRangeException, _0_Geo.LongitudeRangeException._NP_RepositoryId: _0_Geo._d_LongitudeRangeException, _0_Geo.InternalException._NP_RepositoryId: _0_Geo._d_InternalException})
Basic._d_midpoint = ((omniORB.typeMapping["IDL:Geo/latitude:1.0"], omniORB.typeMapping["IDL:Geo/longitude:1.0"], omniORB.typeMapping["IDL:Geo/latitude:1.0"], omniORB.typeMapping["IDL:Geo/longitude:1.0"]), (omniORB.typeMapping["IDL:Geo/Point:1.0"], ), {_0_Geo.LatitudeRangeException._NP_RepositoryId: _0_Geo._d_LatitudeRangeException, _0_Geo.LongitudeRangeException._NP_RepositoryId: _0_Geo._d_LongitudeRangeException, _0_Geo.InternalException._NP_RepositoryId: _0_Geo._d_InternalException})
Basic._d_intersection = ((omniORB.typeMapping["IDL:Geo/latitude:1.0"], omniORB.typeMapping["IDL:Geo/longitude:1.0"], omniORB.typeMapping["IDL:Geo/bearing:1.0"], omniORB.typeMapping["IDL:Geo/latitude:1.0"], omniORB.typeMapping["IDL:Geo/longitude:1.0"], omniORB.typeMapping["IDL:Geo/bearing:1.0"]), (omniORB.typeMapping["IDL:Geo/Point:1.0"], ), {_0_Geo.LatitudeRangeException._NP_RepositoryId: _0_Geo._d_LatitudeRangeException, _0_Geo.LongitudeRangeException._NP_RepositoryId: _0_Geo._d_LongitudeRangeException, _0_Geo.InternalException._NP_RepositoryId: _0_Geo._d_InternalException})
Basic._d_rhumb_distance = ((omniORB.typeMapping["IDL:Geo/latitude:1.0"], omniORB.typeMapping["IDL:Geo/longitude:1.0"], omniORB.typeMapping["IDL:Geo/latitude:1.0"], omniORB.typeMapping["IDL:Geo/longitude:1.0"]), (omniORB.typeMapping["IDL:Geo/distance:1.0"], ), {_0_Geo.LatitudeRangeException._NP_RepositoryId: _0_Geo._d_LatitudeRangeException, _0_Geo.LongitudeRangeException._NP_RepositoryId: _0_Geo._d_LongitudeRangeException, _0_Geo.InternalException._NP_RepositoryId: _0_Geo._d_InternalException})
Basic._d_rhumb_bearing = ((omniORB.typeMapping["IDL:Geo/latitude:1.0"], omniORB.typeMapping["IDL:Geo/longitude:1.0"], omniORB.typeMapping["IDL:Geo/latitude:1.0"], omniORB.typeMapping["IDL:Geo/longitude:1.0"]), (omniORB.typeMapping["IDL:Geo/bearing:1.0"], ), {_0_Geo.LatitudeRangeException._NP_RepositoryId: _0_Geo._d_LatitudeRangeException, _0_Geo.LongitudeRangeException._NP_RepositoryId: _0_Geo._d_LongitudeRangeException, _0_Geo.InternalException._NP_RepositoryId: _0_Geo._d_InternalException})
Basic._d_rhumb_destination_point = ((omniORB.typeMapping["IDL:Geo/latitude:1.0"], omniORB.typeMapping["IDL:Geo/longitude:1.0"], omniORB.typeMapping["IDL:Geo/latitude:1.0"], omniORB.typeMapping["IDL:Geo/longitude:1.0"]), (omniORB.typeMapping["IDL:Geo/Point:1.0"], ), {_0_Geo.LatitudeRangeException._NP_RepositoryId: _0_Geo._d_LatitudeRangeException, _0_Geo.LongitudeRangeException._NP_RepositoryId: _0_Geo._d_LongitudeRangeException, _0_Geo.InternalException._NP_RepositoryId: _0_Geo._d_InternalException})
Basic._d_rhumb_midpoint = ((omniORB.typeMapping["IDL:Geo/latitude:1.0"], omniORB.typeMapping["IDL:Geo/longitude:1.0"], omniORB.typeMapping["IDL:Geo/latitude:1.0"], omniORB.typeMapping["IDL:Geo/longitude:1.0"]), (omniORB.typeMapping["IDL:Geo/Point:1.0"], ), {_0_Geo.LatitudeRangeException._NP_RepositoryId: _0_Geo._d_LatitudeRangeException, _0_Geo.LongitudeRangeException._NP_RepositoryId: _0_Geo._d_LongitudeRangeException, _0_Geo.InternalException._NP_RepositoryId: _0_Geo._d_InternalException})
Basic._d_destination_point = ((omniORB.typeMapping["IDL:Geo/latitude:1.0"], omniORB.typeMapping["IDL:Geo/longitude:1.0"], omniORB.typeMapping["IDL:Geo/bearing:1.0"], omniORB.typeMapping["IDL:Geo/distance:1.0"]), (omniORB.typeMapping["IDL:Geo/Point:1.0"], ), {_0_Geo.LatitudeRangeException._NP_RepositoryId: _0_Geo._d_LatitudeRangeException, _0_Geo.LongitudeRangeException._NP_RepositoryId: _0_Geo._d_LongitudeRangeException, _0_Geo.InternalException._NP_RepositoryId: _0_Geo._d_InternalException})

# Basic object reference
class _objref_Basic (CORBA.Object):
    _NP_RepositoryId = Basic._NP_RepositoryId

    def __init__(self):
        CORBA.Object.__init__(self)

    def distance_haversine(self, *args):
        return _omnipy.invoke(self, "distance_haversine", _0_Geo.Basic._d_distance_haversine, args)

    def distance_sloc(self, *args):
        return _omnipy.invoke(self, "distance_sloc", _0_Geo.Basic._d_distance_sloc, args)

    def initial_bearing(self, *args):
        return _omnipy.invoke(self, "initial_bearing", _0_Geo.Basic._d_initial_bearing, args)

    def final_bearing(self, *args):
        return _omnipy.invoke(self, "final_bearing", _0_Geo.Basic._d_final_bearing, args)

    def midpoint(self, *args):
        return _omnipy.invoke(self, "midpoint", _0_Geo.Basic._d_midpoint, args)

    def intersection(self, *args):
        return _omnipy.invoke(self, "intersection", _0_Geo.Basic._d_intersection, args)

    def rhumb_distance(self, *args):
        return _omnipy.invoke(self, "rhumb_distance", _0_Geo.Basic._d_rhumb_distance, args)

    def rhumb_bearing(self, *args):
        return _omnipy.invoke(self, "rhumb_bearing", _0_Geo.Basic._d_rhumb_bearing, args)

    def rhumb_destination_point(self, *args):
        return _omnipy.invoke(self, "rhumb_destination_point", _0_Geo.Basic._d_rhumb_destination_point, args)

    def rhumb_midpoint(self, *args):
        return _omnipy.invoke(self, "rhumb_midpoint", _0_Geo.Basic._d_rhumb_midpoint, args)

    def destination_point(self, *args):
        return _omnipy.invoke(self, "destination_point", _0_Geo.Basic._d_destination_point, args)

    __methods__ = ["distance_haversine", "distance_sloc", "initial_bearing", "final_bearing", "midpoint", "intersection", "rhumb_distance", "rhumb_bearing", "rhumb_destination_point", "rhumb_midpoint", "destination_point"] + CORBA.Object.__methods__

omniORB.registerObjref(Basic._NP_RepositoryId, _objref_Basic)
_0_Geo._objref_Basic = _objref_Basic
del Basic, _objref_Basic

# Basic skeleton
__name__ = "Geo__POA"
class Basic (PortableServer.Servant):
    _NP_RepositoryId = _0_Geo.Basic._NP_RepositoryId


    _omni_op_d = {"distance_haversine": _0_Geo.Basic._d_distance_haversine, "distance_sloc": _0_Geo.Basic._d_distance_sloc, "initial_bearing": _0_Geo.Basic._d_initial_bearing, "final_bearing": _0_Geo.Basic._d_final_bearing, "midpoint": _0_Geo.Basic._d_midpoint, "intersection": _0_Geo.Basic._d_intersection, "rhumb_distance": _0_Geo.Basic._d_rhumb_distance, "rhumb_bearing": _0_Geo.Basic._d_rhumb_bearing, "rhumb_destination_point": _0_Geo.Basic._d_rhumb_destination_point, "rhumb_midpoint": _0_Geo.Basic._d_rhumb_midpoint, "destination_point": _0_Geo.Basic._d_destination_point}

Basic._omni_skeleton = Basic
_0_Geo__POA.Basic = Basic
omniORB.registerSkeleton(Basic._NP_RepositoryId, Basic)
del Basic
__name__ = "Geo"

#
# End of module "Geo"
#
__name__ = "geo_idl"

_exported_modules = ( "Geo", )

# The end.
