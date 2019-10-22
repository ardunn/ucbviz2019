"""
Functions for generating bulk (multiple) graphs for prototyping etc.
"""
import dash_html_components as html

from ucbviz2019.graphs import get_generic_line_graph_html, get_generic_heatmap_html


def generate_bulk_graphs_html(data, graph_function):
    graphs = []
    for ds_name, ds in data.items():
        info = ds["info"]
        df = ds["df"]

        if ds_name != "pdst_cpi":
            lg = graph_function(df)
            lg_label = html.Div(ds_name, className="is-size-4")
            lg_info = html.Div(info, className="is-size-7")
            lg_container = html.Div([lg_label, lg_info, lg], className="container")
            graphs.append(lg_container)
    return html.Div(graphs, className="section")


def select_bulk_graphs_html(graph_selector):
    graph_selector_map = {
        "lines": get_generic_line_graph_html,
        "heatmaps": get_generic_heatmap_html
    }
    return graph_selector_map[graph_selector]