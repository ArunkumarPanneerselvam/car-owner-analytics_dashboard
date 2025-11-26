# Car Owner Analytics Dashboard

An interactive data visualization dashboard built with Python Dash and Plotly that explores relationships between car owners' demographic characteristics and their vehicle preferences. This project demonstrates data generation, interactive filtering, and advanced visualization techniques for demographic and automotive data analysis.

## 📊 Project Overview

This dashboard provides an interactive interface to analyze correlations between owner demographics (age, gender, income, occupation) and vehicle characteristics (make, model, fuel type, body style, engine size). The project includes both a synthetic data generator and multiple dashboard implementations with varying levels of complexity.

## ✨ Features

### Data Analytics
- **300 synthetic car owner records** with 18 attributes
- **Owner demographics**: Gender, ethnicity, age, income, occupation, hair color
- **Vehicle specifications**: Make, model, age, engine size, body style, fuel type
- **Behavioral data**: Driving style, modification status, mileage, service history

### Interactive Dashboard
- **Multi-filter system**: Filter by gender, ethnicity, occupation, car make, fuel type, body style
- **Range sliders**: Age and income range selection
- **Dynamic visualizations**: Scatter plots, Sankey diagrams, animated timelines
- **Real-time updates**: Dashboard responds instantly to filter changes
- **Summary statistics**: Live record count and filter status display

### Visualizations
- **Scatter Plot**: Age vs Engine Size with gender-based color coding
- **Sankey Diagram**: Ownership flow from gender to body style preferences
- **Animated Timeline**: Car ownership history by vehicle age
- **Multi-dimensional analysis**: Size, color, and shape encoding for rich insights

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/car-owner-dashboard.git
cd car-owner-dashboard
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

### Dependencies

```
pandas>=1.3.0
numpy>=1.21.0
plotly>=5.3.0
dash>=2.0.0
```

## 📖 Usage

### Generate Sample Dataset

First, generate the synthetic car owner dataset:

```bash
python generate_dataset.py
```

This creates `car_owner_data.csv` with 300 records containing comprehensive owner and vehicle data.

### Run the Dashboard

Execute the main dashboard application:

```bash
python car_owner_dashboard.py
```

Then open your browser and navigate to:
```
http://127.0.0.1:8050/
```

### Alternative Dashboard Versions

The project includes multiple implementations:

**Enhanced Version** (with advanced visualizations):
```bash
python car_own_dash2.py
```

## 📁 Project Structure

```
car-owner-dashboard/
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
├── CONTRIBUTING.md
├── generate_dataset.py           # Data generation script
├── car_owner_dashboard.py        # Main dashboard application
├── car_own_dash2.py              # Enhanced dashboard version
├── car_owner_data.csv            # Generated dataset (after running script)
├── data/
│   └── sample_data.csv           # Backup sample data
├── docs/
│   └── screenshots/              # Dashboard screenshots
└── examples/
    └── usage_examples.md         # Usage examples and tutorials
```

## 🎯 Dashboard Features

### Filter Options

**Demographic Filters:**
- Gender (Male, Female, Other)
- Ethnicity (White, Black, Asian, Hispanic, Mixed, Other)
- Occupation (Engineer, Doctor, Artist, Teacher, Developer, Manager, Lawyer, Student, Unemployed)
- Age range slider (18-70 years)
- Income range slider ($15,000-$200,000)

**Vehicle Filters:**
- Car Make (Toyota, Honda, Ford, BMW, Audi, Skoda, Hyundai)
- Fuel Type (Petrol, Diesel, Electric, Hybrid)
- Body Style (Sedan, Hatchback, SUV, Coupe, Convertible, Wagon)
- Driving Style (Calm, Moderate, Aggressive)
- Modification Status (Yes/No)

### Visualization Types

**Scatter Plot Analysis:**
- X-axis: Owner Age or Car Age
- Y-axis: Car Cost or Engine Size
- Color: Gender or Fuel Type
- Size: Engine Size or Car Cost
- Hover: Detailed owner and vehicle information

**Sankey Diagram:**
- Flow visualization from demographics to vehicle preferences
- Node connections showing ownership patterns
- Interactive filtering for specific flows

**Animated Timeline:**
- Time-based visualization of ownership patterns
- Animation by car age
- Color-coded by manufacturer

## 🔧 Data Generation Details

### Data Schema

| Field | Type | Description | Range/Options |
|-------|------|-------------|---------------|
| OwnerID | String | Unique identifier | O001-O300 |
| Gender | Categorical | Owner gender | Male, Female, Other |
| Ethnicity | Categorical | Owner ethnicity | 6 categories |
| Age | Integer | Owner age | 18-70 years |
| Income | Integer | Annual income | $15,000-$200,000 |
| Occupation | Categorical | Job category | 9 occupations |
| HairColor | Categorical | Hair color | 7 colors |
| CarMake | Categorical | Vehicle manufacturer | 7 brands |
| CarModel | Categorical | Specific model | 28 models |
| CarAge | Integer | Vehicle age | 0-20 years |
| EngineSize | Float | Engine displacement | 1.0-4.0L |
| BodyStyle | Categorical | Vehicle type | 6 styles |
| CarCost | Integer | Vehicle value | $5,000-$50,000 |
| FuelType | Categorical | Fuel category | 4 types |
| DrivingStyle | Categorical | Behavior pattern | 3 styles |
| IsModified | Boolean | Modification status | Yes/No |
| MileagePerYear | Integer | Annual mileage | 5,000-30,000 km |
| ServiceHistory | Integer | Service visits | 0-6 visits |

### Customizing Data Generation

Modify `generate_dataset.py` to adjust:

```python
# Change number of records
df = generate_data(500)  # Generate 500 records

# Modify value ranges
age = np.random.randint(21, 65)  # Different age range
income = np.random.randint(20000, 300000)  # Different income range

# Add new car makes
car_makes_models = {
    "Tesla": ["Model 3", "Model S", "Model X"],
    # ... add more
}
```

## 💡 Use Cases

- **Market Research**: Understand demographic preferences for vehicle types
- **Sales Analytics**: Identify target demographics for specific car models
- **Educational**: Learn data visualization and dashboard development
- **Portfolio Project**: Demonstrate full-stack data science capabilities
- **Synthetic Data Testing**: Generate realistic datasets for testing purposes

## 🎨 Customization Guide

### Change Dashboard Theme

```python
app = dash.Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
```

### Modify Visualization Colors

```python
fig = px.scatter(
    dff, 
    color_discrete_sequence=['#FF6B6B', '#4ECDC4', '#45B7D1']
)
```

### Add New Filters

```python
html.Label("New Filter"),
dcc.Dropdown(
    id="new-filter-dropdown",
    options=[{"label": i, "value": i} for i in df["NewColumn"].unique()],
    multi=True
)
```

### Adjust Layout Proportions

```python
# Change filter panel width
style={"width": "30%", ...}  # Increase from 25% to 30%

# Change graph area width
style={"width": "65%", ...}  # Decrease from 70% to 65%
```

## 📊 Sample Insights

The dashboard can reveal insights such as:

- **Age-Income Correlation**: Older owners tend to have higher incomes and prefer luxury brands
- **Gender Preferences**: Different body style preferences across gender categories
- **Fuel Type Trends**: Younger owners show higher preference for electric vehicles
- **Modification Patterns**: Aggressive drivers are more likely to modify vehicles
- **Occupation Influence**: Engineers and developers prefer specific fuel types and body styles

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add: detailed description'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## 📝 Future Enhancements

- [ ] Add machine learning predictions for car preferences
- [ ] Integrate real automotive API data
- [ ] Export filtered data to CSV/Excel
- [ ] Add statistical correlation analysis
- [ ] Implement user authentication for saved filters
- [ ] Create PDF report generation
- [ ] Add comparative analysis between demographic groups
- [ ] Implement database backend for larger datasets
- [ ] Mobile-responsive design improvements
- [ ] Add more visualization types (3D plots, geographic maps)

## 🐛 Troubleshooting

### Dashboard doesn't start
- Check Python version (3.8+ required)
- Verify all dependencies installed: `pip list`
- Check port 8050 is not in use

### Data generation fails
- Ensure numpy and pandas are installed
- Check write permissions in current directory

### Visualizations not updating
- Clear browser cache
- Check browser console for JavaScript errors
- Verify callback functions are properly defined

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your Profile](https://linkedin.com/in/yourprofile)
- Email: your.email@example.com

## 🙏 Acknowledgments

- Plotly Dash documentation and community
- Pandas and NumPy development teams
- Synthetic data generation techniques from data science community
- Inspiration from automotive market research dashboards

## 📧 Contact

For questions, suggestions, or collaboration opportunities:
- Open an issue on GitHub
- Email: your.email@example.com
- Twitter: [@yourhandle](https://twitter.com/yourhandle)

## 📈 Project Stats

- **Dataset Size**: 300 records
- **Attributes**: 18 fields per record
- **Filter Options**: 10+ interactive filters
- **Visualization Types**: 3 different chart types
- **Car Manufacturers**: 7 brands with 28+ models
- **Code Quality**: PEP 8 compliant

---

**⭐ If you find this project helpful, please give it a star!**

**🔗 Related Projects:**
- [Weather Dashboard](https://github.com/yourusername/weather-dashboard)
- [Sales Analytics Dashboard](https://github.com/yourusername/sales-dashboard)
