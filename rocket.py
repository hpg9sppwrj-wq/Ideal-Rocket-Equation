import math

gravity = 9.81 #m/s^2

def get_rocket_parameters():
    initial_mass = float(input("Initial Mass (kg): "))
    final_mass = float(input("Final Mass (kg): "))

    return initial_mass, final_mass

def get_simulation_parameters(gravity):
    specific_impulse = float(input("Specific Impulse (s): "))
    exhaust_velocity = specific_impulse * gravity
    print(f"Exhaust velocity is {exhaust_velocity} m/s")

    return exhaust_velocity

def calculate_delta_velocity(initial_mass, final_mass, exhaust_velocity):
    mass_ratio = initial_mass / final_mass
    ln_mass_ratio = math.log(mass_ratio)

    print('')

    delta_velocity = exhaust_velocity * ln_mass_ratio
    print(f"Maximum theoretical speed is {delta_velocity} m/s")

    return delta_velocity

def calculate_fuel_fraction(exhaust_velocity):
    delta_velocity = float(input("Maximum Theoretical Speed (m/s): "))

    print('')

    mass_ratio = math.exp(-1 * (delta_velocity / exhaust_velocity))
    fuel_fraction = (1 - mass_ratio) * 100
    print(f"Fuel fraction is {fuel_fraction}%")

    return fuel_fraction

def calculate_specific_impulse(initial_mass, final_mass):
    delta_velocity = float(input("Maximum Theoretical Speed (m/s): "))
    mass_ratio = initial_mass / final_mass
    ln_mass_ratio = math.log(mass_ratio)

    exhaust_velocity = delta_velocity / ln_mass_ratio

    print('')

    specific_impulse = exhaust_velocity / gravity
    print(f"Required engine efficiency is {specific_impulse} s")

    return specific_impulse

def calculate_thrust(exhaust_velocity, intitial_mass, final_mass):
    thrust = exhaust_velocity * (intitial_mass - final_mass)

    print('')

    print(f"Thrust is {thrust} N")

    return thrust

def calculate_burn_time(exhaust_velocity, initial_mass, final_mass, thrust):
    mass_flow_rate = thrust / exhaust_velocity

    burn_time = (initial_mass - final_mass) / mass_flow_rate
    print(f"Burn time is {burn_time} s")

    return burn_time

response = input("Rocket Parameters or Change in Velocity [X/Y]: ")

if response == "X":
    response_1 = input("Fuel Fraction, Specific Impulse, or Burn Time [A/B/C]: ")
    if response_1 == "A":
        exhaust_velocity = get_simulation_parameters(gravity)
        calculate_fuel_fraction(exhaust_velocity)
    elif response_1 == "B":
        initial_mass, final_mass = get_rocket_parameters()
        calculate_specific_impulse(initial_mass, final_mass)
    elif response_1 == "C":
        initial_mass, final_mass = get_rocket_parameters()
        exhaust_velocity = get_simulation_parameters(gravity)
        thrust = calculate_thrust(exhaust_velocity, initial_mass, final_mass)
        calculate_burn_time(exhaust_velocity, initial_mass, final_mass, thrust)
        
elif response == "Y":
    initial_mass, final_mass = get_rocket_parameters()
    exhaust_velocity = get_simulation_parameters(gravity)
    calculate_delta_velocity(initial_mass, final_mass, exhaust_velocity)
