from specialization import Coordinate
from view import TileState

class Bord(object):
    def __init__( self, size ):
        self.resize( size )
        self.ships = {}

    def resize( self, size ): #Coordinate assumed
        empty_row = []
        if not len( size ): #0-D 
            return
        #1-D+
        for i in range( 0, size.pop() ):
            empty_row.append( TileState['Empty'] ) 
        if not len( size ): #1-D
            self.tiles = empty_row
            return
        #2-D+
        filler = empty_row
        for dimension in size:
            this_dimension = []
            for i in range( 0, dimension ):
                this_dimension.append( list( filler ) )
            filler = this_dimension
        self.tiles = filler

    def state( self, coordinate ):
        result = self.tiles
        for dimension in coordinate:
            result = result[dimension]
        if not isinstance( result, TileState ):
            raise IndexError( "Fewer dimensions in coordinate than board" )
            #type matches error raised if there are too many dimensions
        return result

    def position_ship( self, ship, position, direction ):
        proposed_position = map( lambda coordinate: position + coordinate, ship.occupied_space )

    def fire( self, position ):
        state = self.state( position )
        if state == TileState['Hit'] or state == TileState['Miss']:
            return ('repeat')
        #else state is Empty
        for ship_name in self.ships:
            ship = self.ships[ship_name]
            if position in ship:
                return ('Hit', ship_name, ship.sunk())
        return ('Miss')

