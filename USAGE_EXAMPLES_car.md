Usage Examples
Basic Usage
1. Generate Fresh Dataset
bash
python generate_dataset.py
This creates car_owner_data.csv with 300 synthetic records.

2. Launch Dashboard
bash
python car_owner_dashboard.py
Navigate to http://127.0.0.1:8050/

3. Apply Filters
Select gender: Male, Female

Set age range: 25-45

Choose car make: BMW, Audi

Select income range: $50,000-$150,000

The visualization updates in real-time!

Advanced Examples
Custom Data Generation
Generate 500 records with specific parameters:

python
# In generate_dataset.py, modify:
df = generate_data(500)  # Instead of 300
Filtering Specific Demographics
Find all young professionals with luxury cars:

Age range: 25-35

Income: $80,000-$200,000

Occupation: Engineer, Developer, Doctor

Car Make: BMW, Audi

Analyzing Fuel Type Trends
Compare electric vs traditional fuel preferences:

Select Fuel Type: Electric

Observe age distribution

Clear filters, select Fuel Type: Petrol

Compare patterns

Finding Modified Car Owners
Select "Modified Car": Yes

Observe driving style distribution

Check car make preferences

Analyze age and income correlations

Visualization Techniques
Scatter Plot Insights
Age vs Engine Size:

Larger bubbles = higher engine size

Color = gender

Hover for detailed information

Car Age vs Cost:

Shows depreciation patterns

Identify outliers (well-maintained older cars)

Compare across manufacturers

Sankey Diagram Analysis
View ownership flow:

Left side: Demographics (gender, ethnicity)

Right side: Vehicle preferences (body style)

Line thickness: number of owners

Animated Timeline
Watch ownership patterns evolve:

Press play to animate through car ages

Observe how ownership changes over vehicle lifetime

Identify popular models at different ages

Data Export
Export Filtered Data
Add this to your dashboard callback:

python
# In car_owner_dashboard.py
dff.to_csv('filtered_results.csv', index=False)
Generate Reports
Create summary statistics:

python
summary = dff.groupby('CarMake')['CarCost'].agg(['mean', 'median', 'count'])
print(summary)
Troubleshooting
Issue: Dashboard Not Loading
Solution:

bash
# Check if port is in use
lsof -i :8050

# Use different port
app.run(debug=True, port=8051)
