import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Oval
from bokeh.palettes import Spectral8

from graph import *

graph_data = Graph()
graph_data.debug_create_test_data()
print(graph_data.vertexes)

N = len(graph_data.vertexes)
node_indices = list(range(N))

color_list = []
for vertex in graph_data.vertexes:
    color_list.append(vertex.color)

# debug_pallete = Spectral8
# debug_pallete.append('#ff0000')
# debug_pallete.append('#0000ff')

# plot = figure(title='Graph Layout Demonstration', x_range=(-1.1, 1.1), y_range=(-1.1, 1.1),
#               tools='', toolbar_location=None)
plot = figure(title='Graph Layout Demonstration', x_range=(0, 500), y_range=(0, 500),
              tools='', toolbar_location=None)

graph = GraphRenderer()

graph.node_renderer.data_source.add(node_indices, 'index')
# graph.node_renderer.data_source.add(Spectral8, 'color')
# graph.node_renderer.data_source.add(debug_pallete, 'color')
graph.node_renderer.data_source.add(color_list, 'color')
graph.node_renderer.glyph = Oval(height=0.1, width=0.2, fill_color='color')

# This is drawing the edges from start to end

start_indexes = []
end_indexes = []

for start_index, vertex in enumerate(graph_data.vertexes):
    for e in vertex.edges:
        start_indexes.append(start_index)
        end_indexes.append(graph_data.vertexes.index(e.destination))

graph.edge_renderer.data_source.data = dict(
    start=start_indexes,  # a list of vertex indexes to start from
    end=end_indexes)  # a list of vertex indexes to end at

# start of layout code
# circ = [i*2*math.pi/8 for i in node_indices] ## writes them in a circle around 8
# writes it based on node count, or N
# circ = [i*2*math.pi/N for i in node_indices]
# x = [math.cos(i) for i in circ]
# y = [math.sin(i) for i in circ]

# sets position of vertexes

x = [v.pos['x'] for v in graph_data.vertexes]
y = [v.pos['y'] for v in graph_data.vertexes]

graph_layout = dict(zip(node_indices, zip(x, y)))
graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

plot.renderers.append(graph)

output_file('graph.html')
show(plot)
