1. Function Definitions:

    calculate_corrected_temperature(T_target, T_actual): Takes the target temperature (T_target) and actual temperature (T_actual) as input and calculates the corrected temperature (T_corr) using a specific formula.
    calculate_flow_temperature(T_desired, h_c, T_outside): Takes the desired temperature (T_desired), heat transfer coefficient (h_c), and outside temperature (T_outside) as input and calculates the flow temperature (T_flow) using a specific formula.

2. Load Compensation Adjustment:

    Takes user input for the target temperature (T_target) and actual temperature (T_actual).
    Calls the calculate_corrected_temperature function to calculate the corrected temperature (corrected_temp) based on the provided formula.

3. Heating Curve Calculation with Load Compensation:

    Uses the corrected temperature (corrected_temp) as the new desired temperature.
    Takes user input for the heat transfer coefficient (h_c) and outside temperature (T_outside).
    Calls the calculate_flow_temperature function to calculate the flow temperature (flow_temp) based on the provided formula.

4. Output:

    Prints the calculated flow temperature (flow_temp).
