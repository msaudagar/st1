import json

with open("thermo-props-coeffs.json", "r") as read_file:
    props_coeffs_dicts = json.load(read_file)


    
# print(props_coeffs_dicts[0])  

# ===== code for converting a dictionary to object ==========
# A dictionary's properties can not be accessed by dot(.) notation, we need ["prop"] notation which is tedious. An object properties can be accessed with dot(.), that is why we may need to change a dictionary to an object.
# declaring a Template class where __init__ takes input_dict 
# Template (passed as object_hook to json.dump) specifies the shape of resulting object
class Template:
      
    # constructor
    def __init__(self, input_dict):
        self.__dict__.update(input_dict)
   
def dict2obj(input_dict):
      
    # using json.loads method and passing json.dumps
    # method and custom object hook as arguments
    return json.loads(json.dumps(input_dict), object_hook=Template)
# ============================================================
coeffs = []
for i, comp in enumerate(props_coeffs_dicts):
    coeffs.append(dict2obj(props_coeffs_dicts[i]))


# A dictionary's properties can not be accessed by dot(.) notation, we need ["prop"] notation which is tedious. An object properties can be accessed with dot(.), that is why we needed to change props_coeffs_dicts to an object

h2o = dict2obj(props_coeffs_dicts[0])
# print(h2o.tfk)

from enum import IntEnum
class Comp(IntEnum):
    H2 = 0
    CH4 = 1
    C2H6 = 2
    C3H8 = 3
    C2H4 = 4
    C3H6 = 5
    C2H2 = 6
    C4H6 = 7
    C4H8 = 8
    C6H6 = 9
   
# print(Comp.H2+Comp.C2H4)

def cp(comp_num, tempk):
# Fourth order polynomial in T in K   "The Properties of Gases and Liquids" Fifth Edition
# Cp in J/(mol-K), T in K
    RGAS = 8.3143             # (J/(mol-K) or (m3-Pa)/(mol-K); RGas=8.3143E-5 in (m3-bar)/
    a0 = coeffs[comp_num].a0
    a1 = coeffs[comp_num].a1
    a2 = coeffs[comp_num].a2
    a3 = coeffs[comp_num].a3
    a4 = coeffs[comp_num].a4
    t = tempk/1000
    # cp1 = (a0 + a1*1.0E-3*tempk +  a2*1.0E-5*tempk**2 + a3*1.0E-8*tempk**3 + a4*1.0E-11*tempk**4)*RGAS
    cp1 = (a0 + a1*t +  a2*10*t**2 + a3*10*t**3 + a4*10*t**4)*RGAS
    return cp1

# print(cp(2, 800))
    
# print(repr(Comp.H2))

# list1 = [5,7,9]   
# print(list1[Comp.H2O])

       