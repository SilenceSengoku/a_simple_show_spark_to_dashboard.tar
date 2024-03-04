# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd


app = Dash(__name__)

df = pd.read_csv(r'data_for_dashboard_Bubble_Chart.csv')

#print (df)
fig = px.scatter(df, x="revenue", y="vote_count",
                 size="budget", color="original_language", hover_name="title",
                 log_x=True, size_max=60)

app.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True, port=8001)
    # 注意外部点开需要本地开发防火墙端口8001
