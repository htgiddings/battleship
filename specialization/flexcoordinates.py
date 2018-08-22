 #!/usr/bin/env python
"""

Logic concerning a coordinate system that is extensible to as many dimensions
as one could possibly desire, aka. the practical limits on built-in lists of
integers.

This construct is likely impractical for several reasons.  First, this
construct is optimal pretty much only when the number of dimensions in the
coordinate system will change over the course of the program’s execution, which
is highly unlikely in any practical application. Second, because humans cannot
see in more than 3 dimensions, your needs are likely better covered by another
package such as coordinate, numpy, or the coordinate type of whatever graphics
library is being used, but this was fun to make anyway.

"""

import operator

__author__ = "htgiddings"
__copyright__ = "(c) 2018"

#No checks are performed to make sure the operands contain the same number of
# dimensions.  For most functions an error will be thrown if there are fewer
# objects in the passed-in list than there are in the current list, but not if
# the passed-in one has more.
class Coordinate(list):
    
    def __map( self, other, funct ):
        collector = Coordinate()
        for i in len( self ):
            collector.append( funct( self[i], other[i] ) )
        return collector

    #Arithmetic

    def __add__( self, other ):
        return self.__map( other, operator.add )

    def __mul__( self, other ):
        return self.__map( other, operator.mul )

    def scale( self, scalar ):
        return Coordinate( map( lambda x: x * scalar, self ) ) 

    def __sub__( self, other ):
        return self + other.scale( -1 )

    #This operator is included solely to respect a possible decision to use
    #floating point units.  Note that this is not appropriate for most uses of 
    # the coordinate system and floordiv (//) should be used instead.
    def __truediv__( self, other ):
        return self.__map( other, operator.truediv )

    def __floordiv__( self, other ):
        return self.__map( other, operator.floordiv )

    #Equality
