import plotly.express as px
import pandas as pd
import numpy as np
from dash import dcc


class scatter_chart:
    def __init__(self):
        self.df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')
        self.slider = dcc.Slider(
            min=self.df['year'].min(),
            max=self.df['year'].max(),
            step=None,
            value=self.df['year'].min(),
            marks={str(year): str(year) for year in self.df['year'].unique()},
            id='year-slider'
        )

    def get_figure(self, selected_year):
        filtered_df = self.df[self.df.year == selected_year]

        fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
                         size="pop", color="continent", hover_name="country",
                         log_x=True, size_max=55)

        fig.update_layout(transition_duration=500)

        return fig


def line_chart():
    """
        Sample Plotly Line Chart
    """
    df = pd.DataFrame({
        "X": np.linspace(0, 10, 100),
        "Y": np.sin(np.linspace(0, 10, 100))
    })

    fig = px.line(df, x="X", y="Y", title="Line Chart")

    return fig


def bar_chart():
    """
        Sample Plotly Bar Chart
    """

    df = pd.DataFrame({
        "Category": ["A", "B", "C", "D", "E"],
        "Values": np.random.randint(10, 100, size=5)
    })

    fig = px.bar(df, x="Category", y="Values", title="Bar Chart")

    return fig
