#importing module
from numericcalculation import calculate_addition
#-------------------------------------------------
a = 5
b = 10
print("Sum of",a,"and",b,"is:",calculate_addition(a,b))
m = 50
n = 40
print("Difference of",m,"and",n,"is:",calculate_difference(a,b))


#--------------------------------------------------
"""
Output:
Sum of 5 and 10 is:15
--------------------------------------------
Traceback (most recent call last):
   File "C:\ANP-D7096_IPEC_python-5th_sem\Class_work\Day10_Module_8th_july\example3.py",line9,in <module>
      print("Difference of",m,"and",n,"is:",calculate_difference(a,b))
                               ^^^^^^^^^^^^^^^^^^^^^^^^^^
NameError: name 'calculate_difference' is not defined"""