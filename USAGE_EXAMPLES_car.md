# Usage Examples

## Basic Usage

### 1. Generate Fresh Dataset

```bash
python generate_dataset.py
```

This creates `car_owner_data.csv` with 300 synthetic records.

### 2. Launch Dashboard

```bash
python car_owner_dashboard.py
```

Navigate to http://127.0.0.1:8050/

### 3. Apply Filters

- Select gender: Male, Female
- Set age range: 25-45
- Choose car make: BMW, Audi
- Select income range: $50,000-$150,000

The visualization updates in real-time!

## Advanced Examples

### Custom Data Generation

Generate 500 records with specific parameters:

```python
# In generate_dataset.py, modify:
df = generate_data(500)  # Instead of 300
```

### Filtering Specific Demographics

Find all young professionals with luxury cars:

1. Age range: 25-35
2. Income: $80,000-$200,000
3. Occupation: Engineer, Developer, Doctor
4. Car Make: BMW, Audi

### Analyzing Fuel Type Trends

Compare electric vs traditional fuel preferences:

1. Select Fuel Type: Electric
2. Observe age distribution
3. Clear filters, select Fuel Type: Petrol
4. Compare patterns

### Finding Modified Car Owners

1. Select "Modified Car": Yes
2. Observe driving style distribution
3. Check car make preferences
4. Analyze age and income correlations

## Visualization Techniques

### Scatter Plot Insights

**Age vs Engine Size:**
- Larger bubbles = higher engine size
- Color = gender
- Hover for detailed information

**Car Age vs Cost:**
- Shows depreciation patterns
- Identify outliers (well-maintained older cars)
- Compare across manufacturers

### Sankey Diagram Analysis

View ownership flow:
- Left side: Demographics (gender, ethnicity)
- Right side: Vehicle preferences (body style)
- Line thickness: number of owners

### Animated Timeline

Watch ownership patterns evolve:
- Press play to animate through car ages
- Observe how ownership changes over vehicle lifetime
- Identify popular models at different ages

## Data Export

### Export Filtered Data

Add this to your dashboard callback:

```python
# In car_owner_dashboard.py
dff.to_csv('filtered_results.csv', index=False)
```

### Generate Reports

Create summary statistics:

```python
summary = dff.groupby('CarMake')['CarCost'].agg(['mean', 'median', 'count'])
print(summary)
```

## Troubleshooting

### Issue: Dashboard Not Loading

**Solution:**
```bash
# Check if port is in use
lsof -i :8050

# Use different port
app.run(debug=True, port=8051)
```

### Issue: No Data Displayed

**Solution:**
- Verify `car_owner_data.csv` exists
- Check file path in `car_owner_dashboard.py`
- Ensure file has correct structure

### Issue: Slow Performance

**Solution:**
- Reduce dataset size
- Sample data: `df = df.sample(100)`
- Turn off debug mode: `app.run(debug=False)`

## Tips and Tricks

### 1. Quick Testing
Use sample data for faster testing:
```python
df = df_full.sample(50, random_state=42)
```

### 2. Multiple Dashboards
Run different versions simultaneously on different ports:
```bash
# Terminal 1
python car_owner_dashboard.py  # Port 8050

# Terminal 2
python car_own_dash2.py  # Port 8051
```

### 3. Save Filter Presets
Create common filter combinations as functions:

```python
def filter_luxury_segment(df):
    return df[
        (df['Income'] > 100000) & 
        (df['CarMake'].isin(['BMW', 'Audi']))
    ]
```

### 4. Custom Visualizations
Add new chart types:

```python
fig = px.box(dff, x='CarMake', y='CarCost', color='FuelType')
```

## Integration Examples

### With Jupyter Notebooks

```python
import pandas as pd
import plotly.express as px

df = pd.read_csv('car_owner_data.csv')
fig = px.scatter(df, x='Age', y='CarCost', color='Gender')
fig.show()
```

### With Flask API

```python
from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/api/data')
def get_data():
    df = pd.read_csv('car_owner_data.csv')
    return jsonify(df.to_dict('records'))
```

## Best Practices

1. **Start Simple**: Begin with basic filters, add complexity gradually
2. **Test Incrementally**: Test each new feature independently
3. **Document Changes**: Keep notes on customizations
4. **Version Control**: Commit changes frequently
5. **Backup Data**: Keep original CSV safe before modifications

## Next Steps

- Explore all filter combinations
- Try different visualization types
- Generate custom datasets
- Share insights with team
- Extend functionality with new features
