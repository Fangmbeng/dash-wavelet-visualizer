import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pywt
from plotly.subplots import make_subplots

# Generate random data
data = np.random.randn(512)

# Create app
app = dash.Dash()

# Create layout
app.layout = html.Div([
    dcc.Graph(
        id='wavelet-graph',
        figure={
            'data': [
                {'x': np.arange(len(data)), 'y': data, 'name': 'Data'}
            ],
            'layout': {
                'title': 'Haar Wavelet Decomposition of Random Data',
                'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                'paper_bgcolor': 'rgba(0, 0, 0, 0)',
                'xaxis': {'showgrid': False, 'visible': False},
                'yaxis': {'showgrid': False, 'visible': False},
                'bargap': 0.2,
                'bargroupgap': 0.1
            }
        }
    )
])

# Create callback to update graph based on slider value
@app.callback(
    dash.dependencies.Output('wavelet-graph', 'figure'),
    [dash.dependencies.Input('wavelet-slider', 'value')]
)
def update_graph(level):
    # Apply Haar wavelet
    coeffs = pywt.wavedec(data, 'haar', level=level)

    # Create figure
    figure = make_subplots(rows=level+1, cols=1, shared_xaxes=True, vertical_spacing=0.05)

    # Add data and reconstructions to figure
    figure.add_trace(
        {'x': np.arange(len(data)), 'y': data, 'name': 'Data'},
        row=1, col=1
    )
    for i, coeff in enumerate(coeffs):
        approximation = pywt.waverec(coeff, 'haar')
        figure.add_trace(
            {'x': np.arange(len(approximation)), 'y': approximation, 'name': f'Level {i} Approximation'},
            row=i+2, col=1
        )

    # Set layout
    figure.update_layout(
        title='Haar Wavelet Decomposition of Random Data',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
        xaxis={'showgrid': False, 'visible': False},
        yaxis={'showgrid': False, 'visible': False},
        bargap=0.2,
        bargroupgap=0.1,
        height=800
    )

    return figure

# Create slider
app.layout.children.append(
    dcc.Slider(
        id='wavelet-slider',
        min=1,
        max=4,
        value=3,
        marks={str(i): str(i) for i in range(1, 5)},
        step=None
    )
)

# Run app
if __name__ == '__main__':
    app.run_server(debug=True)
