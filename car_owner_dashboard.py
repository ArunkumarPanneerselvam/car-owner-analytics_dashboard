import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# Load dataset
df = pd.read_csv("car_owner_data.csv")

# Initialize Dash app
app = Dash(__name__)
app.title = "Car-Owner Relationship Visualizer"

# App layout
app.layout = html.Div(style={"padding": "30px", "fontFamily": "Arial"}, children=[
    html.H1("Car and Owner Relationship Visualizer", style={"textAlign": "center"}),

    html.Div([
        html.Div([
            html.Label("Gender"),
            dcc.Dropdown(
                id="gender-dropdown",
                options=[{"label": i, "value": i} for i in sorted(df["Gender"].unique())],
                multi=True
            ),
            html.Label("Ethnicity"),
            dcc.Dropdown(
                id="ethnicity-dropdown",
                options=[{"label": i, "value": i} for i in sorted(df["Ethnicity"].unique())],
                multi=True
            ),
            html.Label("Occupation"),
            dcc.Dropdown(
                id="occupation-dropdown",
                options=[{"label": i, "value": i} for i in sorted(df["Occupation"].unique())],
                multi=True
            ),
            html.Label("Car Make"),
            dcc.Dropdown(
                id="make-dropdown",
                options=[{"label": i, "value": i} for i in sorted(df["CarMake"].unique())],
                multi=True
            ),
            html.Label("Fuel Type"),
            dcc.Dropdown(
                id="fuel-type-dropdown",
                options=[{"label": i, "value": i} for i in sorted(df["FuelType"].unique())],
                multi=True
            ),
            html.Label("Driving Style"),
            dcc.Dropdown(
                id="driving-style-dropdown",
                options=[{"label": i, "value": i} for i in sorted(df["DrivingStyle"].unique())],
                multi=True
            ),
            html.Label("Modified Car?"),
            dcc.RadioItems(
                id="modified-radio",
                options=[
                    {"label": "Yes", "value": "Yes"},
                    {"label": "No", "value": "No"}
                ],
                value=None,
                inline=True
            ),
            html.Label("Age Range"),
            dcc.RangeSlider(
                id="age-slider",
                min=df["Age"].min(),
                max=df["Age"].max(),
                step=1,
                marks={int(i): str(int(i)) for i in range(20, 70, 10)},
                value=[20, 50]
            ),
            html.Label("Income Range"),
            dcc.RangeSlider(
                id="income-slider",
                min=df["Income"].min(),
                max=df["Income"].max(),
                step=5000,
                marks={i: f"${i//1000}k" for i in range(20000, 200001, 40000)},
                value=[30000, 120000]
            ),
        ], style={"width": "25%", "display": "inline-block", "verticalAlign": "top", "paddingRight": "30px"}),

        html.Div([
            dcc.Graph(id="scatter-plot"),
            html.Div(id="summary-text", style={"paddingTop": "10px", "fontSize": "16px"})
        ], style={"width": "70%", "display": "inline-block"})
    ])
])

# Callback for interactive filtering and plotting
@app.callback(
    Output("scatter-plot", "figure"),
    Output("summary-text", "children"),
    Input("gender-dropdown", "value"),
    Input("ethnicity-dropdown", "value"),
    Input("occupation-dropdown", "value"),
    Input("make-dropdown", "value"),
    Input("fuel-type-dropdown", "value"),
    Input("driving-style-dropdown", "value"),
    Input("modified-radio", "value"),
    Input("age-slider", "value"),
    Input("income-slider", "value"),
)
def update_graph(selected_gender, selected_ethnicity, selected_occupation,
                 selected_make, selected_fuel, selected_driving,
                 modified_status, age_range, income_range):

    dff = df.copy()

    if selected_gender:
        dff = dff[dff["Gender"].isin(selected_gender)]
    if selected_ethnicity:
        dff = dff[dff["Ethnicity"].isin(selected_ethnicity)]
    if selected_occupation:
        dff = dff[dff["Occupation"].isin(selected_occupation)]
    if selected_make:
        dff = dff[dff["CarMake"].isin(selected_make)]
    if selected_fuel:
        dff = dff[dff["FuelType"].isin(selected_fuel)]
    if selected_driving:
        dff = dff[dff["DrivingStyle"].isin(selected_driving)]
    if modified_status:
        dff = dff[dff["IsModified"] == modified_status]

    dff = dff[(dff["Age"] >= age_range[0]) & (dff["Age"] <= age_range[1])]
    dff = dff[(dff["Income"] >= income_range[0]) & (dff["Income"] <= income_range[1])]

    fig = px.scatter(
        dff,
        x="CarAge",
        y="CarCost",
        color="Gender",
        size="EngineSize",
        hover_data=["OwnerID", "Occupation", "FuelType", "DrivingStyle", "MileagePerYear", "ServiceHistory"],
        symbol="BodyStyle",
        title="Relationship Between Car Cost & Age by Owner Attributes",
        template="plotly_white"
    )
    fig.update_layout(
        legend_title="Gender",
        margin=dict(l=40, r=40, t=60, b=40),
        height=600
    )

    summary = f"Showing {len(dff)} records filtered from total {len(df)} owners."

    return fig, summary

# Run server
if __name__ == '__main__':
    app.run(debug=True)
