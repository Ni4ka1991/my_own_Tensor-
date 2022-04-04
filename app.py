#!/usr/bin/env python3
import torch

#print( "Hello" )

a = torch.Tensor( 2,3 )
a2 = torch.Tensor( 3,2 )
b = torch.Tensor( [ 1, 2, 3 ] )
c = torch.Tensor( [-1] )
print( f"Tensor a( 2,3 ) >>>\n {a}" )
print( f"Tensor a2( 3,2 ) >>>\n {a2}" )
print( f"size of tensor a : {len(a)}" )
print( f"size of tensor a2: {len(a2)}" )
print( f"Shape of tensor a : {a.shape}" )
print( f"Shape of tensor a2: {a2.shape}" )
print( f"Tensor b([1]) >>>\n {b}" )
print( f"size of tensor b : {len(b)}" )
print( f"Shape of tensor b : {b.shape}" )
print( f"Tensor c([-1]) >>>\n {c}" )
x = torch.Tensor( [i for i in range( 10 )] ).type(torch.int16)
print( f"x.Tensor = {x}" )


class Tensor:
    
    def __init__( self, data ):
        
        if type( data == list ):
            self.data = data
        
        else:
            print( "Type error" )
    
    def view( self, x, y ):
        pass

    def shape( self ):
        pass

    def __str__():
        pass
