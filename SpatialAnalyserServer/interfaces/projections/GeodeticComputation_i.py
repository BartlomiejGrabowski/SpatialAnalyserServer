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
        self.logger = Logger("SHPDraw Basic", "../../../src/server/main/server.log")
        
    '''
    Returns longitudes, latitudes and back azimuths of terminus points given 
    longitudes (lons) and latitudes (lats) of initial points, plus forward azimuths (az) and distances (dist).
    '''
    def get_fwd_transformation(self, lons, lats, az, dist):
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
    
    '''
    Returns forward and back azimuths, plus distances between initial points (specified by lons1, lats1) 
    and terminus points (specified by lons2, lats2).
    '''
    def get_inv_transformation(self, lons1, lats1, lons2, lats2):
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
    
    '''
    Given a single initial point and terminus point (specified by python floats lon1,lat1 and lon2,lat2), 
    returns a list of longitude/latitude pairs describing npts equally spaced intermediate points along 
    the geodesic between the initial and terminus points.
    '''
    def get_intermediate_points(self, lons1, lats1, lons2, lats2, npts):
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