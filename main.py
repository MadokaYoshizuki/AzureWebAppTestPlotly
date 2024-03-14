from flask import Flask, render_template
from dash import Dash, html, dcc, Input, Output
from figures import line_chart, bar_chart, scatter_chart

# Initialize Flask server:
server = Flask(__name__, template_folder="templates")

# Define Routes:


@server.route("/")
def home():
    """
        Redirecting to home page.
    """
    return render_template("home.html")


s = scatter_chart()

# Dash Apps:
app1 = Dash(__name__, server=server, url_base_pathname="/sampleDashApp1/", assets_folder="assets")
app1.layout = html.Div([
    html.H1("Sample Dash App"),
    html.P("This is a simple Dash app running on a Flask server."),

    html.H2("散布図（吉月追加）"),
    dcc.Graph(id='scatter-chart'),
    s.slider,

    html.H2("Sample Line Chart"),
    dcc.Graph(figure=line_chart()),
    html.H2("Sample Bar Chart"),
    dcc.Graph(figure=bar_chart())
])


# Define callback to update scatter chart:
@app1.callback(
    Output('scatter-chart', 'figure'),
    Input(s.slider.id, 'value')
)
def update_scatter_chart(selected_year):
    return s.get_figure(selected_year)


# Run the App:
if __name__ == "__main__":
    server.run(host="0.0.0.0", port=5000, debug=True)  # Set debug to False during production
