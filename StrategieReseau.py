
from Terrain import Terrain, Case

class StrategieReseau:
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[tuple[int, int]]]:
        return -1, {}, []

class StrategieReseauManuelle(StrategieReseau):
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[tuple[int, int]]]:
        # TODO
        return -1, {}, []

class StrategieReseauAuto(StrategieReseau):


    def move_forward(self, budget : int,  current_cell : tuple[int, int], known_cells : list[tuple[int, int]], t : Terrain) -> tuple[list[tuple[int,int]], list[tuple[tuple[int,int],tuple[int,int]]], int]:
        """
        Parameters
        ----------
        budget : int
            the remaning budget to move to an other cell

        current_cell : tuple[int, int]
            the starting position
        
        known_cells : list[tuple[int, int]]
            the list of the cases already reached with a cheaper cost
        
        t : Terrain
            the layout of the area

        Returns
        -------
        the result is divided in 3 values : 
            a list of the differents cells that compose an occurence of the cheapest path
            a list of the differents arcs between the cells
            an integer that represents the cost of those paths
        """
        pass

    def cheapest_paths(self, reference_cell : tuple[int, int], t : Terrain) -> tuple[list[tuple[int,int]], list[tuple[tuple[int,int],tuple[int,int]]], int]:
        """
        Parameters
        ----------
        reference_cell : tuple[int, int]
            the starting position
        
        t : Terrain
            the layout of the area

        Returns
        -------
        the result is divided in 3 values : 
            a list of the differents cells that compose an occurence of the cheapest path to reach the base or an other customer 
            a list of the differents arcs between the cells
            an integer that represents the cost of those paths
        """
        pass

    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[tuple[int, int]]]:
        # TODO
        return -1, {}, []

