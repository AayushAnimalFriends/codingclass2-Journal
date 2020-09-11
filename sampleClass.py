from dataclasses import dataclass


@dataclass
class Point:
    cmd: str
    value: int


p = Point("f", 2)
q = Point("b", 20)

a = [p,q]

print(a)
print(a[0])
print(a[1].value)

if (a[0].cmd == "f"):
    print ("Sharky Loves Papa", a[0].value, "times")
