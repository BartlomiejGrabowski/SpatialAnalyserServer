'''
Created on Jul 3, 2012

@author: bartek
'''
import sys
import Projection
import Projection__POA

import pyproj as pyproj

sys.path.append("../../src/logger")
from Logger import Logger

class GeodeticComputation_i(Projection__POA.Geodetic):
    '''
    Implementation Geodetic interface
    '''
    
    def __init__(self):
        #Create logger handler.
        self.logger = Logger("Projection Geodetic", "../../../src/server/main/server.log")
        
    def get_fwd_transformation(self, lons, lats, az, dist):
        '''
        Returns longitudes, latitudes and back azimuths of terminus points given 
        longitudes (lons) and latitudes (lats) of initial points, plus forward azimuths (az) and distances (dist).
        '''
        self.logger.log.info("get_fwd_transformation method invocation.")
        
        try:
            geod = pyproj.Geod(ellps='WGS84')
            end_lons, end_lats, back_az = geod.fwd(lons, lats, az, dist)            
            fwd_transform = Projection.Fwd_transformation(end_lons, end_lats, back_az)
        except ValueError as ex:
            self.logger.error("%s exception occurred during creating forward trasformation" % (ex))
            raise Projection.ArgumentsNotInOrder("Error occurred during creating forward trasformation")
            sys.exit(1)
        return fwd_transform
    
    def get_inv_transformation(self, lons1, lats1, lons2, lats2):
        '''
        Returns forward and back azimuths, plus distances between initial points (specified by lons1, lats1) 
        and terminus points (specified by lons2, lats2).
        '''
        self.logger.log.info("get_inv_transformation method invocation.")
        
        try:
            geod = pyproj.Geod(ellps='WGS84')
            azimuth, back_azimuth, distance = geod.inv(lons1, lats1, lons2, lats2)            
            inv_transform = Projection.Inv_transformation(azimuth, back_azimuth, distance)
        except ValueError as ex:
            self.logger.error("%s exception occurred during creating forward trasformation" % (ex))
            raise Projection.ArgumentsNotInOrder("Error occurred during creating forward trasformation")
            sys.exit(1)
        return inv_transform
    

    def get_intermediate_points(self, lons1, lats1, lons2, lats2, npts):
        '''
        Given a single initial point and terminus point (specified by python floats lon1,lat1 and lon2,lat2), 
        returns a list of longitude/latitude pairs describing npts equally spaced intermediate points along 
        the geodesic between the initial and terminus points.
        '''
        self.logger.log.info("get_inv_transformation method invocation.")
        
        npts_list = list()
        npts_out_list = list()
        
        try:
            geod = pyproj.Geod(ellps='WGS84')
            npts_list = geod.npts(lons1, lats1, lons2, lats2, npts)
            for point in npts_list:
                intermediate_point = list()
                intermediate_point = Projection.Npt(point[0], point[1])
                npts_out_list.append(intermediate_point)
                
        except ValueError as ex:
            self.logger.error("%s exception occurred during creating forward trasformation" % (ex))
            raise Projection.ArgumentsNotInOrder("Error occurred during creating forward trasformation")
            sys.exit(1)
        return npts_out_list
    

    def get_projection_list(self):
        '''Function get_projection_list returns a list of available projection. 
        The function takes no input parameters.
        '''
        self.logger.log.info("get_projection_list method invocation")
        
        projection_list = pyproj.pj_list
        projection = {}
        out_projection_list = list()
        
        #For each projection in projection list (from pj_list)
        for item in projection_list.keys():
            #Fill fields.
            projection['name'] = item
            projection['description'] = projection_list[item]
            #Append projection idl object to output projection list.
            out_projection_list.append(Projection.Proj(projection['name'], projection['description']))
        
        return out_projection_list
    

    def get_ellipsoid_list(self):
        '''Function get_projection_list returns a list of available ellipsoide. 
        The function takes no input parameters.
        '''
        self.logger.log.info("get_ellipsoid_list method invocation")
        
        ellipsoid_list = pyproj.pj_ellps
        ellipsoid = {}
        out_ellipsoid_list = list()
        
        #For each ellipsoid in projection list (from pj_ellps)
        for item in ellipsoid_list.keys():
            #Fill fields.
            ellipsoid['name'] = item
            ellipsoid['info'] = ellipsoid_list[item]
            #Append ellipsoid idl object to output ellipsoid list.
            out_ellipsoid_list.append(Projection.Ellipsoid(ellipsoid['name'],ellipsoid['info']['description']))
        
        return out_ellipsoid_list
    
    def transform_coordinate_systems(self, in_projection, out_projection, x1, y1, z1=0):
        ''' Function transform_coordinate_systems - Transforms points between two coordinate systems defined 
        by the Proj instances p1 (input_projection) and p2 (output_projection).
        The points x1,y1,z1 in the coordinate system defined by p1 are transformed to x2,y2,z2 in the coordinate system defined by p
        def transform_coordinate_systems(self, in_projection, out_projection, x1, y1, z1=0):
        '''
        self.logger.log.info("transform_coordinate_systems method invocation")
        
        try:
            #Create two different coordinate systems.
            self.input_proj = pyproj.Proj(init=in_projection)
            self.output_proj = pyproj.Proj(init=out_projection)
            x2, y2, z2 = pyproj.transform(self.input_proj, self.output_proj, x1, y1, z1)
            self.output_coordinates = Projection.Coordinates(x2, y2, z2)
            return self.output_coordinates
        except ValueError as ex:
            self.logger.error("%s exception occurred during transform coordinate between two different systems" % (ex))
            raise Projection.ArgumentsNotInOrder("Error occurred during transform coordinate between two different systems")
            sys.exit(1)
            