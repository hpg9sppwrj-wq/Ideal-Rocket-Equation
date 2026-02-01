import math

#Rocket Parameters
gravity = 9.81 #m/s^2
initial_mass = int(input("Initial Mass (kg): "))
final_mass = int(input("Final Mass (kg): "))
specific_impulse = int(input("Specific Impulse (s): "))

#Exhaust Velocity
exhaust_velocity = specific_impulse * gravity
print(f"Exhaust velocity is {exhaust_velocity} m/s")

#Mass Ratio
mass_ratio = initial_mass / final_mass
ln_mass_ratio = math.log(mass_ratio)

print('')

#Change in Velocity
delta_velocity = exhaust_velocity * ln_mass_ratio
print(f"Change in velocity is {delta_velocity} m/s")
