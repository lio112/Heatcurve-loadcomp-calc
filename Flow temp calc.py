def calculate_corrected_temperature(T_target, T_actual):
    T_corr = T_target + (T_target - T_actual)
    return T_corr

def calculate_flow_temperature(T_desired, heat_curve, T_outside):
    T_flow = 2.55 * (heat_curve * (T_desired - T_outside))**0.78 + T_desired
    return round(T_flow)  # Round to the nearest integer

# Load compensation adjustment
T_target = float(input("Enter the target room temperature: "))
T_actual = float(input("Enter the actual room temperature: "))
corrected_temp = calculate_corrected_temperature(T_target, T_actual)

# Calculate the heating curve with load compensation
T_desired = float(corrected_temp)
heat_curve = float(input("Enter the heat curve: "))
T_outside = float(input("Enter the outside temperature: "))

flow_temp = calculate_flow_temperature(T_desired, heat_curve, T_outside)
print(f"The calculated flow temperature is: {flow_temp}")
