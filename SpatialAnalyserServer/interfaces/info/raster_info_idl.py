# Python stubs generated by omniidl from raster_info.idl

import omniORB, _omnipy
from omniORB import CORBA, PortableServer
_0_CORBA = CORBA

_omnipy.checkVersion(3,0, __file__)


#
# Start of module "Info"
#
__name__ = "Info"
_0_Info = omniORB.openModule("Info", r"raster_info.idl")
_0_Info__POA = omniORB.openModule("Info__POA", r"raster_info.idl")


# typedef ... driver_name
class driver_name:
    _NP_RepositoryId = "IDL:Info/driver_name:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Info.driver_name = driver_name
_0_Info._d_driver_name  = (omniORB.tcInternal.tv_string,1024)
_0_Info._ad_driver_name = (omniORB.tcInternal.tv_alias, driver_name._NP_RepositoryId, "driver_name", (omniORB.tcInternal.tv_string,1024))
_0_Info._tc_driver_name = omniORB.tcInternal.createTypeCode(_0_Info._ad_driver_name)
omniORB.registerType(driver_name._NP_RepositoryId, _0_Info._ad_driver_name, _0_Info._tc_driver_name)
del driver_name

# typedef ... raster_x_size
class raster_x_size:
    _NP_RepositoryId = "IDL:Info/raster_x_size:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Info.raster_x_size = raster_x_size
_0_Info._d_raster_x_size  = omniORB.tcInternal.tv_short
_0_Info._ad_raster_x_size = (omniORB.tcInternal.tv_alias, raster_x_size._NP_RepositoryId, "raster_x_size", omniORB.tcInternal.tv_short)
_0_Info._tc_raster_x_size = omniORB.tcInternal.createTypeCode(_0_Info._ad_raster_x_size)
omniORB.registerType(raster_x_size._NP_RepositoryId, _0_Info._ad_raster_x_size, _0_Info._tc_raster_x_size)
del raster_x_size

# typedef ... raster_y_size
class raster_y_size:
    _NP_RepositoryId = "IDL:Info/raster_y_size:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Info.raster_y_size = raster_y_size
_0_Info._d_raster_y_size  = omniORB.tcInternal.tv_short
_0_Info._ad_raster_y_size = (omniORB.tcInternal.tv_alias, raster_y_size._NP_RepositoryId, "raster_y_size", omniORB.tcInternal.tv_short)
_0_Info._tc_raster_y_size = omniORB.tcInternal.createTypeCode(_0_Info._ad_raster_y_size)
omniORB.registerType(raster_y_size._NP_RepositoryId, _0_Info._ad_raster_y_size, _0_Info._tc_raster_y_size)
del raster_y_size

# typedef ... raster_bands
class raster_bands:
    _NP_RepositoryId = "IDL:Info/raster_bands:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Info.raster_bands = raster_bands
_0_Info._d_raster_bands  = omniORB.tcInternal.tv_short
_0_Info._ad_raster_bands = (omniORB.tcInternal.tv_alias, raster_bands._NP_RepositoryId, "raster_bands", omniORB.tcInternal.tv_short)
_0_Info._tc_raster_bands = omniORB.tcInternal.createTypeCode(_0_Info._ad_raster_bands)
omniORB.registerType(raster_bands._NP_RepositoryId, _0_Info._ad_raster_bands, _0_Info._tc_raster_bands)
del raster_bands

# typedef ... associated_file
class associated_file:
    _NP_RepositoryId = "IDL:Info/associated_file:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Info.associated_file = associated_file
_0_Info._d_associated_file  = (omniORB.tcInternal.tv_string,1024)
_0_Info._ad_associated_file = (omniORB.tcInternal.tv_alias, associated_file._NP_RepositoryId, "associated_file", (omniORB.tcInternal.tv_string,1024))
_0_Info._tc_associated_file = omniORB.tcInternal.createTypeCode(_0_Info._ad_associated_file)
omniORB.registerType(associated_file._NP_RepositoryId, _0_Info._ad_associated_file, _0_Info._tc_associated_file)
del associated_file

# typedef ... coordinate_system
class coordinate_system:
    _NP_RepositoryId = "IDL:Info/coordinate_system:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Info.coordinate_system = coordinate_system
_0_Info._d_coordinate_system  = (omniORB.tcInternal.tv_string,1024)
_0_Info._ad_coordinate_system = (omniORB.tcInternal.tv_alias, coordinate_system._NP_RepositoryId, "coordinate_system", (omniORB.tcInternal.tv_string,1024))
_0_Info._tc_coordinate_system = omniORB.tcInternal.createTypeCode(_0_Info._ad_coordinate_system)
omniORB.registerType(coordinate_system._NP_RepositoryId, _0_Info._ad_coordinate_system, _0_Info._tc_coordinate_system)
del coordinate_system

# typedef ... gcp_info
class gcp_info:
    _NP_RepositoryId = "IDL:Info/gcp_info:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Info.gcp_info = gcp_info
_0_Info._d_gcp_info  = (omniORB.tcInternal.tv_string,1024)
_0_Info._ad_gcp_info = (omniORB.tcInternal.tv_alias, gcp_info._NP_RepositoryId, "gcp_info", (omniORB.tcInternal.tv_string,1024))
_0_Info._tc_gcp_info = omniORB.tcInternal.createTypeCode(_0_Info._ad_gcp_info)
omniORB.registerType(gcp_info._NP_RepositoryId, _0_Info._ad_gcp_info, _0_Info._tc_gcp_info)
del gcp_info

# typedef ... metadata_item
class metadata_item:
    _NP_RepositoryId = "IDL:Info/metadata_item:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Info.metadata_item = metadata_item
_0_Info._d_metadata_item  = (omniORB.tcInternal.tv_string,1024)
_0_Info._ad_metadata_item = (omniORB.tcInternal.tv_alias, metadata_item._NP_RepositoryId, "metadata_item", (omniORB.tcInternal.tv_string,1024))
_0_Info._tc_metadata_item = omniORB.tcInternal.createTypeCode(_0_Info._ad_metadata_item)
omniORB.registerType(metadata_item._NP_RepositoryId, _0_Info._ad_metadata_item, _0_Info._tc_metadata_item)
del metadata_item

# typedef ... dataset
class dataset:
    _NP_RepositoryId = "IDL:Info/dataset:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Info.dataset = dataset
_0_Info._d_dataset  = (omniORB.tcInternal.tv_string,1024)
_0_Info._ad_dataset = (omniORB.tcInternal.tv_alias, dataset._NP_RepositoryId, "dataset", (omniORB.tcInternal.tv_string,1024))
_0_Info._tc_dataset = omniORB.tcInternal.createTypeCode(_0_Info._ad_dataset)
omniORB.registerType(dataset._NP_RepositoryId, _0_Info._ad_dataset, _0_Info._tc_dataset)
del dataset

# typedef ... origin
class origin:
    _NP_RepositoryId = "IDL:Info/origin:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Info.origin = origin
_0_Info._d_origin  = omniORB.tcInternal.tv_float
_0_Info._ad_origin = (omniORB.tcInternal.tv_alias, origin._NP_RepositoryId, "origin", omniORB.tcInternal.tv_float)
_0_Info._tc_origin = omniORB.tcInternal.createTypeCode(_0_Info._ad_origin)
omniORB.registerType(origin._NP_RepositoryId, _0_Info._ad_origin, _0_Info._tc_origin)
del origin

# typedef ... pixel_size
class pixel_size:
    _NP_RepositoryId = "IDL:Info/pixel_size:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Info.pixel_size = pixel_size
_0_Info._d_pixel_size  = omniORB.tcInternal.tv_float
_0_Info._ad_pixel_size = (omniORB.tcInternal.tv_alias, pixel_size._NP_RepositoryId, "pixel_size", omniORB.tcInternal.tv_float)
_0_Info._tc_pixel_size = omniORB.tcInternal.createTypeCode(_0_Info._ad_pixel_size)
omniORB.registerType(pixel_size._NP_RepositoryId, _0_Info._ad_pixel_size, _0_Info._tc_pixel_size)
del pixel_size

# typedef ... origins
class origins:
    _NP_RepositoryId = "IDL:Info/origins:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Info.origins = origins
_0_Info._d_origins  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:Info/origin:1.0"], 0)
_0_Info._ad_origins = (omniORB.tcInternal.tv_alias, origins._NP_RepositoryId, "origins", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:Info/origin:1.0"], 0))
_0_Info._tc_origins = omniORB.tcInternal.createTypeCode(_0_Info._ad_origins)
omniORB.registerType(origins._NP_RepositoryId, _0_Info._ad_origins, _0_Info._tc_origins)
del origins

# typedef ... metadata_list
class metadata_list:
    _NP_RepositoryId = "IDL:Info/metadata_list:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Info.metadata_list = metadata_list
_0_Info._d_metadata_list  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:Info/metadata_item:1.0"], 0)
_0_Info._ad_metadata_list = (omniORB.tcInternal.tv_alias, metadata_list._NP_RepositoryId, "metadata_list", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:Info/metadata_item:1.0"], 0))
_0_Info._tc_metadata_list = omniORB.tcInternal.createTypeCode(_0_Info._ad_metadata_list)
omniORB.registerType(metadata_list._NP_RepositoryId, _0_Info._ad_metadata_list, _0_Info._tc_metadata_list)
del metadata_list

# struct Pixel_X_Y_size
_0_Info.Pixel_X_Y_size = omniORB.newEmptyClass()
class Pixel_X_Y_size (omniORB.StructBase):
    _NP_RepositoryId = "IDL:Info/Pixel_X_Y_size:1.0"

    def __init__(self, x_size, y_size):
        self.x_size = x_size
        self.y_size = y_size

_0_Info.Pixel_X_Y_size = Pixel_X_Y_size
_0_Info._d_Pixel_X_Y_size  = (omniORB.tcInternal.tv_struct, Pixel_X_Y_size, Pixel_X_Y_size._NP_RepositoryId, "Pixel_X_Y_size", "x_size", omniORB.typeMapping["IDL:Info/pixel_size:1.0"], "y_size", omniORB.typeMapping["IDL:Info/pixel_size:1.0"])
_0_Info._tc_Pixel_X_Y_size = omniORB.tcInternal.createTypeCode(_0_Info._d_Pixel_X_Y_size)
omniORB.registerType(Pixel_X_Y_size._NP_RepositoryId, _0_Info._d_Pixel_X_Y_size, _0_Info._tc_Pixel_X_Y_size)
del Pixel_X_Y_size

# struct GCP
_0_Info.GCP = omniORB.newEmptyClass()
class GCP (omniORB.StructBase):
    _NP_RepositoryId = "IDL:Info/GCP:1.0"

    def __init__(self, ID, GCP_pixel, GCP_line, GCP_x, GCP_y, GCP_z, GCP_information):
        self.ID = ID
        self.GCP_pixel = GCP_pixel
        self.GCP_line = GCP_line
        self.GCP_x = GCP_x
        self.GCP_y = GCP_y
        self.GCP_z = GCP_z
        self.GCP_information = GCP_information

_0_Info.GCP = GCP
_0_Info._d_GCP  = (omniORB.tcInternal.tv_struct, GCP, GCP._NP_RepositoryId, "GCP", "ID", omniORB.tcInternal.tv_short, "GCP_pixel", omniORB.tcInternal.tv_float, "GCP_line", omniORB.tcInternal.tv_float, "GCP_x", omniORB.tcInternal.tv_float, "GCP_y", omniORB.tcInternal.tv_float, "GCP_z", omniORB.tcInternal.tv_float, "GCP_information", omniORB.typeMapping["IDL:Info/gcp_info:1.0"])
_0_Info._tc_GCP = omniORB.tcInternal.createTypeCode(_0_Info._d_GCP)
omniORB.registerType(GCP._NP_RepositoryId, _0_Info._d_GCP, _0_Info._tc_GCP)
del GCP

# exception DatasetOpenFailed
_0_Info.DatasetOpenFailed = omniORB.newEmptyClass()
class DatasetOpenFailed (CORBA.UserException):
    _NP_RepositoryId = "IDL:Info/DatasetOpenFailed:1.0"

    def __init__(self, reason):
        CORBA.UserException.__init__(self, reason)
        self.reason = reason

_0_Info.DatasetOpenFailed = DatasetOpenFailed
_0_Info._d_DatasetOpenFailed  = (omniORB.tcInternal.tv_except, DatasetOpenFailed, DatasetOpenFailed._NP_RepositoryId, "DatasetOpenFailed", "reason", (omniORB.tcInternal.tv_string,0))
_0_Info._tc_DatasetOpenFailed = omniORB.tcInternal.createTypeCode(_0_Info._d_DatasetOpenFailed)
omniORB.registerType(DatasetOpenFailed._NP_RepositoryId, _0_Info._d_DatasetOpenFailed, _0_Info._tc_DatasetOpenFailed)
del DatasetOpenFailed

# interface Raster
_0_Info._d_Raster = (omniORB.tcInternal.tv_objref, "IDL:Info/Raster:1.0", "Raster")
omniORB.typeMapping["IDL:Info/Raster:1.0"] = _0_Info._d_Raster
_0_Info.Raster = omniORB.newEmptyClass()
class Raster :
    _NP_RepositoryId = _0_Info._d_Raster[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_Info.Raster = Raster
_0_Info._tc_Raster = omniORB.tcInternal.createTypeCode(_0_Info._d_Raster)
omniORB.registerType(Raster._NP_RepositoryId, _0_Info._d_Raster, _0_Info._tc_Raster)

# Raster operations and attributes
Raster._d_get_pixel_size = ((omniORB.typeMapping["IDL:Info/dataset:1.0"], ), (omniORB.typeMapping["IDL:Info/Pixel_X_Y_size:1.0"], ), {_0_Info.DatasetOpenFailed._NP_RepositoryId: _0_Info._d_DatasetOpenFailed})

# Raster object reference
class _objref_Raster (CORBA.Object):
    _NP_RepositoryId = Raster._NP_RepositoryId

    def __init__(self):
        CORBA.Object.__init__(self)

    def get_pixel_size(self, *args):
        return _omnipy.invoke(self, "get_pixel_size", _0_Info.Raster._d_get_pixel_size, args)

    __methods__ = ["get_pixel_size"] + CORBA.Object.__methods__

omniORB.registerObjref(Raster._NP_RepositoryId, _objref_Raster)
_0_Info._objref_Raster = _objref_Raster
del Raster, _objref_Raster

# Raster skeleton
__name__ = "Info__POA"
class Raster (PortableServer.Servant):
    _NP_RepositoryId = _0_Info.Raster._NP_RepositoryId


    _omni_op_d = {"get_pixel_size": _0_Info.Raster._d_get_pixel_size}

Raster._omni_skeleton = Raster
_0_Info__POA.Raster = Raster
omniORB.registerSkeleton(Raster._NP_RepositoryId, Raster)
del Raster
__name__ = "Info"

#
# End of module "Info"
#
__name__ = "raster_info_idl"

_exported_modules = ( "Info", )

# The end.
