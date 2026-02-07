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

def calculate_mass_ratio(exhaust_velocity):
    delta_velocity = float(input("Maximum Theoretical Speed (m/s): "))

    print('')

    mass_ratio = math.exp(delta_velocity / exhaust_velocity)
    print(f"Fuel fraction is {mass_ratio}%")

    return mass_ratio

response = input("Rocket Parameter or Change in Velocity [X/Y]: ")

if response == "X":
    exhaust_velocity = get_simulation_parameters(gravity)
    calculate_mass_ratio(exhaust_velocity)

elif response == "Y":
    initial_mass, final_mass = get_rocket_parameters()
    exhaust_velocity = get_simulation_parameters(gravity)
    calculate_delta_velocity(initial_mass, final_mass, exhaust_velocity)
