"""
Health Economic Analysis: Simple Deterministic Cost-Effectiveness Analysis (CEA)

Script compares two different interventions, calculating the total cost, health outcomes (in QALYs), and the incremental cost-effectiveness ratio (ICER).

1. Calculate the total cost of each intervention, including costs associated with treatment, outpatient visits, and tests.
2. Compute the cost-effectiveness in terms of cost per QALY for each intervention.
3. Discount future costs and QALYs to their present values using a standard discount rate, reflecting the time value of money and societal preferences for current consumption.
4. Compute the Incremental Cost-Effectiveness Ratio (ICER) to determine the cost per additional QALY gained when one intervention is used instead of the other.
5. Print which intervention provides better value for money based on the cost per QALY ratio and the ICER.

Checked with:
    https://www.valueanalyticslabs.com/icer-calculator/
    https://awttc.nhs.wales/files/training-repository/factsheet-4-economic-evaluation-for-healthcare-resource-allocation/

"""
import pandas as pd

######################################################################################################################################################
# Define key financial and health-related variables for interventions
######################################################################################################################################################
cost_intervention_A = 46734  # Base cost in GBP for more expensive intervention
cost_intervention_B = 45447  # Base cost in GBP for standard intervention

qaly_intervention_A = 3.57  # Quality-Adjusted Life Years for A
qaly_intervention_B = 3.46  # Quality-Adjusted Life Years for B

# Hypothetical costs in GBP for additional health care utilisation
cost_per_outpatient_visit = 0
cost_per_test = 0

# Quantity of additional health care utilisation for each intervention
number_of_visits_A = 0
number_of_tests_A = 0
number_of_visits_B = 0
number_of_tests_B = 0 

# Parameters for discounting future costs and QALYs to their present values
discount_rate = 0.0  # Discount rate according to NICE guidelines is 3.5%
years = 0             # Time horizon for the analysis

# Willingness to pay threshold
wtp = 20000  # £20,000 per QALY

######################################################################################################################################################
# Function definitions
######################################################################################################################################################
# Calculate the total cost of an intervention by summing base costs, and costs from outpatient visits and tests.
def total_cost(base_cost, visits, visit_cost, tests, test_cost):
    return base_cost + (visits * visit_cost) + (tests * test_cost)

# Discounting function
def discount_value(value, rate, years):
    return value / ((1 + rate) ** years)

# Calculate the cost per QALY
def calculate_cost_per_qaly(cost, qaly):
    if qaly == 0:
        return float('inf')  # Avoid division by zero; assume infinite cost effectiveness
    return cost / qaly

# Calculate ICER based on QALYs
# An ICER shows the extra costs divided by the extra benefit when comparing two treatments or interventions. 
# It shows how much more you have to spend to gain an additional unit of health benefit (like one extra healthy year, QALY). 
# This makes it easier to decide if the extra cost is worth the extra benefit.
def calculate_icer(cost1, cost2, qaly1, qaly2):
    """Calculates the Incremental Cost-Effectiveness Ratio (ICER) between two interventions."""
    delta_cost = abs(cost1 - cost2)
    delta_qaly = qaly1 - qaly2
    if delta_qaly == 0:
        return float('inf')  # Prevent division by zero
    return delta_cost / delta_qaly

######################################################################################################################################################
# Apply functions to calculate costs and outcomes
#####################################################################################################################################################
total_cost_A = total_cost(cost_intervention_A, number_of_visits_A, cost_per_outpatient_visit, number_of_tests_A, cost_per_test)
total_cost_B = total_cost(cost_intervention_B, number_of_visits_B, cost_per_outpatient_visit, number_of_tests_B, cost_per_test)

discounted_cost_A = discount_value(total_cost_A, discount_rate, years)
discounted_cost_B = discount_value(total_cost_B, discount_rate, years)

cost_per_qaly_A = calculate_cost_per_qaly(discounted_cost_A, qaly_intervention_A)
cost_per_qaly_B = calculate_cost_per_qaly(discounted_cost_B, qaly_intervention_B)

# Calculate ICER
icer = calculate_icer(discounted_cost_A, discounted_cost_B, qaly_intervention_A, qaly_intervention_B)

######################################################################################################################################################
# Print results
#####################################################################################################################################################
print("Total and Discounted Cost for Intervention A: £{:.2f}, £{:.2f}".format(total_cost_A, discounted_cost_A))
print("Total and Discounted Cost for Intervention B: £{:.2f}, £{:.2f}".format(total_cost_B, discounted_cost_B))
print("Cost per QALY for Intervention A: £{:.2f}".format(cost_per_qaly_A))
print("Cost per QALY for Intervention B: £{:.2f}".format(cost_per_qaly_B))
print("ICER (Incremental Cost-Effectiveness Ratio): £{:.2f}".format(icer))

######################################################################################################################################################
# Plot results with CEA plane
#####################################################################################################################################################
import matplotlib.pyplot as plt

# Calculate differences
delta_cost = discounted_cost_A - discounted_cost_B
delta_qaly = qaly_intervention_A - qaly_intervention_B

# Create a scatter plot with expanded limits
plt.figure(figsize=(8, 6))
plt.rcParams['font.family'] = 'Calibri'
plt.scatter(delta_qaly, delta_cost, color='#3498db', label='Base case ICER', s=100, edgecolors='#2980b9', zorder=5)
plt.axhline(0, color='black', linestyle='-')  # Horizontal zero line
plt.axvline(0, color='black', linestyle='-')  # Vertical zero line

# Plot CEA line
x = [min(-2, delta_qaly * 1.2), max(2, delta_qaly * 1.2)]
y = [x * icer for x in x]
plt.plot(x, y, color='#1f77b4', linestyle='--', label='Cost/QALY')

# Expanding the axes limits
plt.xlim(-delta_qaly * 1.2, delta_qaly * 1.2)
plt.ylim(-delta_cost * 1.2, delta_cost * 1.2)

# Plot WTP threshold
x_values = [min(-5, delta_qaly * 1.2), max(5, delta_qaly * 1.2)]
y_values = [x * wtp for x in x_values]
plt.plot(x_values, y_values, color='#d62728', linestyle=':', label='WTP threshold')

# Formatting plot
plt.xticks(fontsize=14)  # You can change the fontsize to any desired size
plt.yticks(fontsize=14)  # You can change the fontsize to any desired size
plt.xlabel(r'$\Delta$ QALYs', fontsize=18, fontweight='bold')
plt.ylabel(r'$\Delta$ Cost (£)', fontsize=18, fontweight='bold')
plt.title('Cost-Effectiveness Plane', fontsize=18, fontweight='bold')
plt.legend()
# Remove the box around the plot
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['bottom'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.tick_params(axis='both', which='both', length=0)  # Removes the ticks
plt.legend( loc='upper left')
plt.grid(True, linestyle='--', alpha=0.2)
# Save the figure
save_folder = 'C:/Users/bc22/OneDrive - King\'s College London/KCL/Projects/HE_code/'
plt.savefig(save_folder + 'CE_plane.png', dpi=300, bbox_inches='tight')
plt.show()

######################################################################################################################################################
# Put results into dataframe
#####################################################################################################################################################
df = pd.DataFrame({'Costs': [discounted_cost_A,discounted_cost_B],
                  'QALYs': [qaly_intervention_A,qaly_intervention_B],
                  'Incremental costs':[delta_cost,0],
                  'Incremental QALY':[delta_qaly,0],
                  'ICER':[icer,0]},index=['Intervention A','Intervention B'])