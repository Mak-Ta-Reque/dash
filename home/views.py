from django.shortcuts import render
from plotly.offline import plot
import plotly.graph_objects as go
import dash_core_components as dcc


# Create your views here.
def home(request):
    def scatter():
        x1 = [1, 2, 3, 4]
        y1 = [30, 35, 25, 45]
        trace = go.Scatter(
            x=x1,
            y=y1
        )

        layout = dict(

            title='Simple Graph',
            xaxis=dict(range=[min(x1), max(x1)]),
            yaxis=dict(range=[min(y1), max(y1)])
        )

        fig = go.Figure(data=[trace], layout=layout)
        fig.update_layout(
            autosize=True,
            width=500,
            height=500,
            margin=dict(
                l=50,
                r=50,
                b=10,
                t=10,
                pad=4
            ),
            paper_bgcolor="LightSteelBlue",
        )
        plot_div = plot(fig, output_type='div', include_plotlyjs=False)
        return plot_div

    context = {
        'plot1': scatter()
    }

    return render(request, 'home/welcome.html', context)
