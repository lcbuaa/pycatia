#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-09 09:53:18.676780

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.hybrid_shape_interfaces.plane import Plane


class HybridShapePlaneMean(Plane):

    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.Plane
                |                             HybridShapePlaneMean
                | 
                | Represents the hybrid shape mean plane feature object.
                | Role: To access the data of the hybrid shape mean plane feature object. This
                | data includes:
                | 
                |     The list of points
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapePlaneMean
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_plane_mean = com_object

    def add_point(self, i_passing_point=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub AddPoint(Reference iPassingPoint)
                | 
                |     Adds a point to the mean plane.
                | 
                |     Parameters:
                | 
                |         iPassingPoint
                |             The point to add
                | 
                |             Sub-element(s) supported (see 
                | 
                |         Boundary object): Vertex.

        :param Reference i_passing_point:
        :return: None
        """
        return self.hybrid_shape_plane_mean.AddPoint(i_passing_point)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_point'
        # # vba_code = """
        # # Public Function add_point(hybrid_shape_plane_mean)
        # #     Dim iPassingPoint (2)
        # #     hybrid_shape_plane_mean.AddPoint iPassingPoint
        # #     add_point = iPassingPoint
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_point(self, i_rank=None, o_passing_point=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub GetPoint(long iRank,
                | Reference oPassingPoint)
                | 
                |     Retrieves the point at a given position.
                | 
                |     Parameters:
                | 
                |         iRank
                |             The rank of the point to retrieve 
                |         oPassingPoint
                |             The point retrieved at this rank

        :param int i_rank:
        :param Reference o_passing_point:
        :return: None
        """
        return self.hybrid_shape_plane_mean.GetPoint(i_rank, o_passing_point)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_point'
        # # vba_code = """
        # # Public Function get_point(hybrid_shape_plane_mean)
        # #     Dim iRank (2)
        # #     hybrid_shape_plane_mean.GetPoint iRank
        # #     get_point = iRank
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_pos(self, i_point=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetPos(Reference iPoint) As long
                | 
                |     Gets the position of an element in the list.
                | 
                |     Parameters:
                | 
                |         iPoint
                |             point 
                |         oPos
                |             position of point

        :param Reference i_point:
        :return: int
        """
        return int(self.hybrid_shape_plane_mean.GetPos(i_point))

    def get_size(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetSize() As long
                | 
                |     Gets the size of the list (number of points).
                | 
                |     Parameters:
                | 
                |         oSize
                |             position of point

        :return: int
        """
        return int(self.hybrid_shape_plane_mean.GetSize())

    def remove_all(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub RemoveAll()
                | 
                |     Removes all elements in the list of points.

        :return: None
        """
        return self.hybrid_shape_plane_mean.RemoveAll()

    def remove_element(self, i_rank=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub RemoveElement(long iRank)
                | 
                |     Removes a point in the list.
                | 
                |     Parameters:
                | 
                |         iRank
                |             The rank of the point to remove

        :param int i_rank:
        :return: None
        """
        return self.hybrid_shape_plane_mean.RemoveElement(i_rank)

    def replace_point_at_position(self, i_point=None, i_pos=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub ReplacePointAtPosition(Reference iPoint,
                | long iPos)
                | 
                |     Replaces a point in the list at the given position.
                | 
                |     Parameters:
                | 
                |         oPoint
                |             point 
                |         iPos
                |             position of point

        :param Reference i_point:
        :param int i_pos:
        :return: None
        """
        return self.hybrid_shape_plane_mean.ReplacePointAtPosition(i_point, i_pos)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'replace_point_at_position'
        # # vba_code = """
        # # Public Function replace_point_at_position(hybrid_shape_plane_mean)
        # #     Dim iPoint (2)
        # #     hybrid_shape_plane_mean.ReplacePointAtPosition iPoint
        # #     replace_point_at_position = iPoint
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'HybridShapePlaneMean(name="{ self.name }")'