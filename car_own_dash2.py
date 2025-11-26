# car_owner_dashboard.py

import pandas as pd
import numpy as np
import dash
from dash import html, dcc, Input, Output
import plotly.express as px
import plotly.graph_objects as go

# Load sample data (sample 100 rows for performance during development)
data_path = r"D:\MInfoTech_Waikato\Assignements\COMPX532\Assignment_3\car_owner_data.csv"
df_full = pd.read_csv(data_path)
df = df_full.sample(100, random_state=42)  # Change 100 to desired size later

# Initialize app
app = dash.Dash(__name__)
app.title = 'Car-Owner Relationship Explorer'

# Layout
app.layout = html.Div([
    html.H1("Car-Owner Relationship Explorer", style={'textAlign': 'center'}),
    html.H2(id='dynamic-title', style={'textAlign': 'center', 'marginBottom': '20px'}),

    html.Div([
        html.Div([
            html.Label('Select Car Make:'),
            dcc.Dropdown(options=[{'label': m, 'value': m} for m in sorted(df['make'].unique())],
                         id='make-dropdown', multi=True),

            html.Label('Select Gender:'),
            dcc.Dropdown(options=[{'label': g, 'value': g} for g in sorted(df['gender'].unique())],
                         id='gender-dropdown', multi=True),

            html.Label('Select Age Range:'),
            dcc.RangeSlider(id='age-slider',
                            min=18, max=80, step=1,
                            marks={i: str(i) for i in range(20, 81, 10)},
                            value=[20, 50]),

            html.Label('Select Income Range ($):'),
            dcc.RangeSlider(id='income-slider',
                            min=10000, max=200000, step=5000,
                            marks={i: str(i//1000)+'K' for i in range(20000, 200001, 20000)},
                            value=[30000, 100000]),

            html.Label('Select Fuel Type:'),
            dcc.Dropdown(options=[{'label': f, 'value': f} for f in sorted(df['fuel_type'].unique())],
                         id='fuel-dropdown', multi=True),

            html.Label('Select Body Style:'),
            dcc.Dropdown(options=[{'label': b, 'value': b} for b in sorted(df['body_style'].unique())],
                         id='style-dropdown', multi=True),

            html.Label('Change Visualization:'),
            dcc.Dropdown(id='viz-dropdown',
                         options=[
                             {'label': 'Scatter Plot (Age vs Engine Size)', 'value': 'scatter'},
                             {'label': 'Sankey Diagram (Ownership Flow)', 'value': 'sankey'},
                             {'label': 'Animated Timeline (Ownership by Car Age)', 'value': 'timeline'}
                         ],
                         value='scatter')
        ], style={'width': '30%', 'display': 'inline-block', 'verticalAlign': 'top', 'padding': '10px'}),

        html.Div([
            dcc.Graph(id='main-graph')
        ], style={'width': '68%', 'display': 'inline-block', 'padding': '10px'})
    ])
])

# Update dynamic title
@app.callback(
    Output('dynamic-title', 'children'),
    Input('make-dropdown', 'value'),
    Input('gender-dropdown', 'value'),
    Input('age-slider', 'value'),
    Input('income-slider', 'value'),
    Input('fuel-dropdown', 'value'),
    Input('style-dropdown', 'value')
)
def update_title(make, gender, age_range, income_range, fuel, body_style):
    parts = []
    if gender: parts.append(f"{' & '.join(gender)}")
    if age_range: parts.append(f"ages {age_range[0]}–{age_range[1]}")
    if income_range: parts.append(f"income ${income_range[0]}–${income_range[1]}")
    if make: parts.append(f"driving {' & '.join(make)}")
    if fuel: parts.append(f"using {' & '.join(fuel)}")
    if body_style: parts.append(f"({', '.join(body_style)})")
    return "Filtered View: " + ", ".join(parts) if parts else "Exploring Car-Owner Relationships"

# Update visualization
@app.callback(
    Output('main-graph', 'figure'),
    Input('make-dropdown', 'value'),
    Input('gender-dropdown', 'value'),
    Input('age-slider', 'value'),
    Input('income-slider', 'value'),
    Input('fuel-dropdown', 'value'),
    Input('style-dropdown', 'value'),
    Input('viz-dropdown', 'value')
)
def update_graph(make, gender, age_range, income_range, fuel, body_style, viz_type):
    dff = df[
        (df['age'].between(age_range[0], age_range[1])) &
        (df['income'].between(income_range[0], income_range[1]))
    ]
    if make:
        dff = dff[dff['make'].isin(make)]
    if gender:
        dff = dff[dff['gender'].isin(gender)]
    if fuel:
        dff = dff[dff['fuel_type'].isin(fuel)]
    if body_style:
        dff = dff[dff['body_style'].isin(body_style)]

    if viz_type == 'scatter':
        fig = px.scatter(
            dff, x='age', y='engine_size', color='gender', size='cost',
            hover_data=['make', 'model', 'body_style', 'income'],
            title='Owner Age vs Engine Size by Gender'
        )

    elif viz_type == 'sankey':
        labels = list(pd.unique(dff['gender'].tolist() + dff['body_style'].tolist()))
        label_map = {label: i for i, label in enumerate(labels)}

        fig = go.Figure(data=[go.Sankey(
            node=dict(label=labels),
            link=dict(
                source=[label_map[g] for g in dff['gender']],
                target=[label_map[b] for b in dff['body_style']],
                value=[1]*len(dff)
            )
        )])
        fig.update_layout(title='Gender to Body Style Ownership Flow')

    elif viz_type == 'timeline':
        fig = px.scatter(
            dff, x='car_age', y='number_of_owners', animation_frame='car_age',
            size='cost', color='make', hover_data=['model', 'fuel_type'],
            title='Ownership History by Car Age'
        )
    else:
        fig = px.scatter(dff, x='age', y='cost')

    return fig

if __name__ == '__main__':
    app.run(debug=True)
