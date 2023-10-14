import sys
sys.path.append("/home/vale6811/Desktop/oreilly/DSFS/ch4/")
import vector,matrices

def sum_of_squares(v: vector.Vector) -> float:
    """Givena vector v returns the  sum of squares of the elements in the Vector using the vector dot product"""
    return vector.dot(v,v)

print("Basic assert")
assert sum_of_squares([2,2]) == 8
assert sum_of_squares([2,2,0,2]) == 12
print("Basic assert done")