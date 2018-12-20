# LogicalNetwork
Logic circuits trained and implemented in the style of feed-forward neural networks

## Concept
The Logical Network is comprised of an *n* number of layers, an *n* of logic gates in that layer, each gate having *2* inputs.

##

    ------Previous-Layer------
    -o--o------o--o------o--o-
    
     |  |      |  |      |  |
     
    -i--i------i--i------i--i-
    -Gate-    -Gate-    -Gate-
    ---o---------o---------o--
    
       |         |         |
       
    ---i---------i---------i--
    --------Next-Layer--------

##

*o* represents any output

*i* represents any input

The LogicalNetwork class in framework.py will generate these randomly, with connections being randomly assigned to the previous layer. What the diagram doesn't show is that multiple connections can be made to a single output or input of one gate.

The gate can be any one of `and, or, xor, nand, nor, xnor` logic gates.
