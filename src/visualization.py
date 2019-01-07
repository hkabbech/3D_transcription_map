"""
.. module:: visualisation
   :synopsis: This module implements the 3D visualization part
"""

# Third-party modules
import os
import plotly
import plotly.graph_objs as go
#import plotly.plotly as py
#plotly.tools.set_credentials_file(username='kabhel', api_key='wqu9rTwIlkzLusElqKrg')

def visualize_4d_genome(coordinates, transcription_map, output_path, colors_map='Cividis'):
    """
    Plot a 3D interactive visualization of the genes colored by their transcription map.
    The interactive plot is saved in an html format.

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
            size=3,
            color=transcription_map,
            colorscale=colors_map,
            opacity=1,
            showscale=True,
        ),
        text='gene: ' + coordinates.index + '<br>chr: ' + coordinates[' chr'],
        hoverinfo='text'
    )

    layout = go.Layout(
        title="<b>3D Transcription Map</b>",
        margin=dict(
            l=65,
            r=50,
            b=65,
            t=90
        )
    )
    fig = go.Figure(data=[trace], layout=layout)
    # py.iplot(fig, filename='3D transcription map')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plotly.offline.plot(fig, filename=output_path)
