import scipy.constants as sc

def cuboid_volume(a,b,c) :
    return a*b*c

def triangle_area(a,b,c) :
    s=0.5*(a+b+c)
    return (s*(s-a)*(s-b)*(s-c))**0.5

def fall_time(start_height) :
    return ((2*start_height)/sc.constants.g)**0.5




