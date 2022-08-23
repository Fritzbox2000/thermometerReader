import plotly
import pandas as pd
import time

def makePage():
    df = pd.read_csv("./data.csv")

    data = [plotly.graph_objs.Scatter(x = df['time'], y = df['heat'],)]

    layout = plotly.graph_objs.Layout(xaxis=dict(title='Time',),yaxis=dict(title='Temp',))
    fig = plotly.graph_objs.Figure(data=data, layout=layout)

    plotly.offline.plot(fig, filename='/var/www/html/index.html', config={'displayModeBar':False})

if __name__ == "__main__":
    while True:
        makePage()
        time.sleep(60 * 15)
