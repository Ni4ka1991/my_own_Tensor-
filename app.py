#!/usr/bin/env python3
import torch
from os import system


l = list( i for i in range(10))
two_dimensional_list = list( [l] * 3 )

#print( f"My list = {two_dimensional_list}" ) 
d = ( 1, 2, 3 )
#print( type(d))


class Tensor:
    
    def __init__( self, data ):
        
        if type( data ) == list:
            self.data = data
        else:
            self.data = tuple()
            print("Oops!  That was no valid data.  Try again...")
    
    def view( self, x, y ):
        pass

    def shape( self ):
        x = len( self.data )
        print( f" len of list = {x}" )
        output = isinstance(self.data, type(list) )
        print( f"isinstance output >>> {output}" )
        y = len( self.data[0] )
        return x, y

    def __str__( self ):
        try:
            return f"Tensor >>> {self.data}"
        except ValueError:
            print( "Empty value!" )
#a = Tensor( l )
b = Tensor( two_dimensional_list )
#print( a.__str__() )
system( "clear" )
print( f"sape of tensor B = {b.shape()}" )
#print( f"\nsape of tensor A = {a.shape()}" )
