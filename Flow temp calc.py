def calculate_corrected_temperature(T_target, T_actual):
    T_corr = T_target + (T_target - T_actual)
    return T_corr

def calculate_flow_temperature(T_desired, h_c, T_outside):
    T_flow = T_desired + (2.8 * h_c**0.8) * (T_desired - T_outside)**0.75
    return T_flow

# Load compensation adjustment
T_target = float(input("Enter the target room temperature: "))
T_actual = float(input("Enter the actual room temperature: "))
corrected_temp = calculate_corrected_temperature(T_target, T_actual)

# Calculate the heating curve with load compensation
T_desired = float(corrected_temp)
heat_coefficient = float(input("Enter the heat curve: "))
T_outside = float(input("Enter the outside temperature: "))

flow_temp = calculate_flow_temperature(T_desired, heat_coefficient, T_outside)
print(f"The calculated flow temperature is: {flow_temp}")

