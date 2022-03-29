#!/usr/bin/env python3
import torch

#print( "Hello" )

a = torch.Tensor( 2,3 )
a2 = torch.Tensor( 3,2 )
b = torch.Tensor( [1] )
c = torch.Tensor( [-1] )
print( f"Tensor a( 2,3 ) >>>\n {a}" )
print( f"Tensor a2( 3,2 ) >>>\n {a2}" )
print( f"size of tensor a : {len(a)}" )
print( f"size of tensor a2: {len(a2)}" )
print( f"Tensor b([1]) >>>\n {b}" )
print( f"Tensor c([-1]) >>>\n {c}" )



