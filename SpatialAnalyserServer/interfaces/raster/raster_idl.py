# Python stubs generated by omniidl from raster.idl

import omniORB, _omnipy
from omniORB import CORBA, PortableServer
_0_CORBA = CORBA

_omnipy.checkVersion(3,0, __file__)


#
# Start of module "Raster"
#
__name__ = "Raster"
_0_Raster = omniORB.openModule("Raster", r"raster.idl")
_0_Raster__POA = omniORB.openModule("Raster__POA", r"raster.idl")


# exception FileException
_0_Raster.FileException = omniORB.newEmptyClass()
class FileException (CORBA.UserException):
    _NP_RepositoryId = "IDL:Raster/FileException:1.0"

    def __init__(self, reason):
        CORBA.UserException.__init__(self, reason)
        self.reason = reason

_0_Raster.FileException = FileException
_0_Raster._d_FileException  = (omniORB.tcInternal.tv_except, FileException, FileException._NP_RepositoryId, "FileException", "reason", (omniORB.tcInternal.tv_string,0))
_0_Raster._tc_FileException = omniORB.tcInternal.createTypeCode(_0_Raster._d_FileException)
omniORB.registerType(FileException._NP_RepositoryId, _0_Raster._d_FileException, _0_Raster._tc_FileException)
del FileException

# exception InternalException
_0_Raster.InternalException = omniORB.newEmptyClass()
class InternalException (CORBA.UserException):
    _NP_RepositoryId = "IDL:Raster/InternalException:1.0"

    def __init__(self, reason):
        CORBA.UserException.__init__(self, reason)
        self.reason = reason

_0_Raster.InternalException = InternalException
_0_Raster._d_InternalException  = (omniORB.tcInternal.tv_except, InternalException, InternalException._NP_RepositoryId, "InternalException", "reason", (omniORB.tcInternal.tv_string,0))
_0_Raster._tc_InternalException = omniORB.tcInternal.createTypeCode(_0_Raster._d_InternalException)
omniORB.registerType(InternalException._NP_RepositoryId, _0_Raster._d_InternalException, _0_Raster._tc_InternalException)
del InternalException

# interface Processing
_0_Raster._d_Processing = (omniORB.tcInternal.tv_objref, "IDL:Raster/Processing:1.0", "Processing")
omniORB.typeMapping["IDL:Raster/Processing:1.0"] = _0_Raster._d_Processing
_0_Raster.Processing = omniORB.newEmptyClass()
class Processing :
    _NP_RepositoryId = _0_Raster._d_Processing[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_Raster.Processing = Processing
_0_Raster._tc_Processing = omniORB.tcInternal.createTypeCode(_0_Raster._d_Processing)
omniORB.registerType(Processing._NP_RepositoryId, _0_Raster._d_Processing, _0_Raster._tc_Processing)

# Processing operations and attributes
Processing._d_image_filter = (((omniORB.tcInternal.tv_string,0), (omniORB.tcInternal.tv_string,0)), ((omniORB.tcInternal.tv_string,0), ), {_0_Raster.InternalException._NP_RepositoryId: _0_Raster._d_InternalException, _0_Raster.FileException._NP_RepositoryId: _0_Raster._d_FileException})
Processing._d_convert_image = (((omniORB.tcInternal.tv_string,0), (omniORB.tcInternal.tv_string,0)), ((omniORB.tcInternal.tv_string,0), ), {_0_Raster.InternalException._NP_RepositoryId: _0_Raster._d_InternalException, _0_Raster.FileException._NP_RepositoryId: _0_Raster._d_FileException})

# Processing object reference
class _objref_Processing (CORBA.Object):
    _NP_RepositoryId = Processing._NP_RepositoryId

    def __init__(self):
        CORBA.Object.__init__(self)

    def image_filter(self, *args):
        return _omnipy.invoke(self, "image_filter", _0_Raster.Processing._d_image_filter, args)

    def convert_image(self, *args):
        return _omnipy.invoke(self, "convert_image", _0_Raster.Processing._d_convert_image, args)

    __methods__ = ["image_filter", "convert_image"] + CORBA.Object.__methods__

omniORB.registerObjref(Processing._NP_RepositoryId, _objref_Processing)
_0_Raster._objref_Processing = _objref_Processing
del Processing, _objref_Processing

# Processing skeleton
__name__ = "Raster__POA"
class Processing (PortableServer.Servant):
    _NP_RepositoryId = _0_Raster.Processing._NP_RepositoryId


    _omni_op_d = {"image_filter": _0_Raster.Processing._d_image_filter, "convert_image": _0_Raster.Processing._d_convert_image}

Processing._omni_skeleton = Processing
_0_Raster__POA.Processing = Processing
omniORB.registerSkeleton(Processing._NP_RepositoryId, Processing)
del Processing
__name__ = "Raster"

#
# End of module "Raster"
#
__name__ = "raster_idl"

_exported_modules = ( "Raster", )

# The end.
