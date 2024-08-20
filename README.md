# simple_cea_analysis
A Python script for performing a simple cost-effectiveness analysis (CEA) on healthcare interventions

# Cost-Effectiveness Analysis (CEA) Script

This Python script performs a simple deterministic cost-effectiveness analysis (CEA) to compare two healthcare interventions. The analysis includes the calculation of total costs, health outcomes in Quality-Adjusted Life Years (QALYs), and the Incremental Cost-Effectiveness Ratio (ICER).

## How to Use

1. **Key Variables:**
   - `cost_intervention_A`: Base cost for the more expensive intervention.
   - `cost_intervention_B`: Base cost for the standard intervention.
   - `qaly_intervention_A`: QALYs associated with intervention A.
   - `qaly_intervention_B`: QALYs associated with intervention B.
   - `discount_rate`: Discount rate for future costs and QALYs (set according to guidelines, e.g., NICE).
   - `wtp`: Willingness to Pay threshold, typically set at £20,000 per QALY.

2. **Functions:**
   - `total_cost`: Calculates the total cost of an intervention.
   - `discount_value`: Discounts future costs and QALYs to present value.
   - `calculate_cost_per_qaly`: Calculates the cost-effectiveness in terms of cost per QALY.
   - `calculate_icer`: Computes the ICER, which shows the cost per additional QALY gained by using one intervention over the other.

3. **Running the Script:**
   - The script calculates the total and discounted costs, cost per QALY, and ICER for the two interventions.
   - It also generates a Cost-Effectiveness (CE) plane plot to visually compare the cost-effectiveness of the interventions.

4. **Outputs:**
   - The results are printed in the console.
   - A CE plane plot is saved as `CE_plane.png` in the specified directory.
