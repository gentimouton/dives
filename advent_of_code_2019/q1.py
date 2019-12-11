"""
Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.

For example:

    For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
    For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
    For a mass of 1969, the fuel required is 654.
    For a mass of 100756, the fuel required is 33583.

The Fuel Counter-Upper needs to know the total fuel requirement. To find it, individually calculate the fuel needed for the mass of each module (your puzzle input), then add together all the fuel values.

What is the sum of the fuel requirements for all of the modules on your spacecraft?
"""


def compute_fuel_req(mass):
    return (mass // 3) - 2
    
    
def test_compute_fuel_req(f):
    assert f(12) == 2
    assert f(14) == 2
    assert f(1969) == 654
    assert f(100756) == 33583


test_compute_fuel_req(compute_fuel_req)
    
    
def compute_fuel_requirement(filepath, mass_to_fuel_converter):
    with open(filepath, 'r') as file: 
        res = sum(
            [mass_to_fuel_converter(int(line)) for line in file.readlines()]
            )
        return res


""" 
Fuel itself requires fuel just like a module - take its mass, divide by three, 
round down, and subtract 2. However, that fuel also requires fuel, and that 
fuel requires fuel, and so on.
So, for each module mass, calculate its fuel and add it to the total.
Then, treat the fuel amount you just calculated as the input mass and 
repeat the process, continuing until a fuel requirement is zero or negative. 
For example:
At first, a module of mass 1969 requires 654 fuel. 
Then, this fuel requires 216 more fuel (654 / 3 - 2). 
216 then requires 70 more fuel, which requires 21 fuel, 
which requires 5 fuel, which requires no further fuel. So, 
the total fuel required for a module of mass 1969 is 654 + 216 + 70 + 21 + 5 = 966.
"""


def compute_fuel_req2(mass):
    module_fuel = compute_fuel_req(mass)
    extra_mass = module_fuel
    while extra_mass > 0:
        extra_fuel = max(compute_fuel_req(extra_mass), 0)
        module_fuel += extra_fuel
        extra_mass = extra_fuel
    return module_fuel


def test_compute_module_fuel_req2(f):
    assert f(14) == 2
    assert f(1969) == 966
    assert f(100756) == 50346


test_compute_module_fuel_req2(compute_fuel_req2)


if __name__ == '__main__':
    print('q1a', compute_fuel_requirement('q1_input.txt', compute_fuel_req))
    print('q1b', compute_fuel_requirement('q1_input.txt', compute_fuel_req2))
