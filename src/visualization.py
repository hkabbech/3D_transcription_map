"""
.. module:: visualisation
   :synopsis: This module implements the 3D visualization part
"""

# Third-party modules
import os
import plotly
import plotly.graph_objs as go
# import plotly.plotly as py
# plotly.tools.set_credentials_file(username='kabhel', api_key='wqu9rTwIlkzLusElqKrg')

def visualize_4d_genome(coordinates, transcription_map, colors_map='Reds'):
    """
    Plot a 3D visualization of the genes colored by their transcription map.

    Args:
        coordinates (Pandas Dataframe): X, Y, Z Coordinates of the genes
        transcription_map (list): Transcription map for the studied genes
        colors_map (str): Chosen colors of the color bar. Default: Reds
    """
    trace = go.Scatter3d(
        x=coordinates['X'],
        y=coordinates['Y'],
        z=coordinates['Z'],
        mode='markers',
        marker=dict(
            size=4,
            color=transcription_map,
            colorscale=colors_map,
            opacity=0.8,
            showscale=True
        ),
        text="gene: " + coordinates.index + "<br>chr: " + coordinates[' chr']
    )

    layout = go.Layout(
        title="<b>3d Transcription Map</b>",
        margin=dict(
            l=65,
            r=50,
            b=65,
            t=90
        )
    )
    fig = go.Figure(data=[trace], layout=layout)
    # py.iplot(fig, filename='3d transcription map')
    os.makedirs('result', exist_ok=True)
    plotly.offline.plot(fig, filename='result/3d_transcription_map.html')
