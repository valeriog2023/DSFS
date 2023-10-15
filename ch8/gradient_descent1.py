from typing import Callable
import sys
sys.path.append("/home/vale6811/Desktop/oreilly/DSFS/ch4/")
import vector
from matplotlib import pyplot as plt


def sum_of_squares(v: vector.Vector) -> float:
    """Givena vector v returns the  sum of squares of the elements in the Vector using the vector dot product"""
    return vector.dot(v,v)

print("Basic assert on sum of squares")
assert sum_of_squares([2,2]) == 8
assert sum_of_squares([2,2,0,2]) == 12
print("Basic assert done")

def difference_quotient(f: Callable[[float], float], x:float, h:float) -> float:
    """
    This method takes as input a:
      f: a function that has as input a float and returns a float
      x: a float that is used as the input of function x
      h: a float that is used as a step

    The method returns (f(x+h) - (fx)) / h
    Note: for h->0 this is the definition of derivative
    """
    return (f(x+h) - f(x)) / h


def square(x: float) -> float:
    """Square function used to test the difference_quotient function"""
    return x * x


def square_derivative(x: float) -> float:
    """Derivative of the square function (used for testing)"""
    return 2 * x


def partial_difference_quotient(f: Callable[[vector.Vector], float],  # function that has multiple input floats and returns a float
                                v: vector.Vector,                     # starting point of the function f
                                i: int,                        # selects the coordinate for which we run the derivative
                                h: float                       # step
                                ) -> float:
    """
    Returns the partial difference quotient of f at the point v for the coordinate i
    it uses h as a step
    """
    v_h = [v_j + ( 0 if j != i else h) for j,v_j in enumerate(v)]
    return (f(v_h) - f(v)) / h


def estimate_gradient(f: Callable[[vector.Vector], float],
                      v: vector.Vector,               # starting point of the function f
                      h: float = 0.0001,              # step  (default is 0.0001)
                     ) -> vector.Vector:              # returns a vector
    """
    Returns the vector of partial derivates of the function f at the point v
    it uses h as a step (default is 0.0001)
    """
    return [ partial_difference_quotient(f,v,i,h) for i in range(len(v)) ]






if __name__ == "__main__":
    xs =range(-10,11)
    actuals = [square_derivative(x) for x in xs]
    estimates = [difference_quotient(square, x, h=0.001) for x in xs ]

    # plot to show that the result is basically the same
    plt.title("Actual Derivates of x^2 vs approximation")
    plt.plot(xs,actuals,'rx', label='Actual')   # red x dot
    plt.plot(xs,estimates, 'b+', label='Estimate')
    plt.legend(loc='best')
    plt.show()