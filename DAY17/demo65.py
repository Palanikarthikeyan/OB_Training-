def calc1(a,b):
    return a+b

calc1(10,20)


def calc2(a: int,b: int) ->float:
    return a+b

calc2(10,20)

from typing import List,Tuple,Dict
ecity: List[str] = ["bglore","pune","hyderabad","chennai"]
#
# Vs
Ecity = ["bglore","pune","hyderabad","chennai",56] # OK

T=("Raj",101,20000.0)

Emp_T: Tuple[str,int,float] = ("Raj",101,20000.44) 

d: Dict[str,int] = {"K":101}


class box:
    def __init__(self,a: int,b: str) ->None:
        self.a = a
        self.b = b
