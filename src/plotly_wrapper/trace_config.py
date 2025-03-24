import numpy as np
from collections import OrderedDict
import colorsys
from ordered_set import OrderedSet


def _generate_distinct_colors(num_colors):
    """
    Generate a list of distinct colors.
    """
   
    colors = OrderedSet([
        ## T10 Colors           
        '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
        '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'
    ])
    
    golden_ration = (1 + np.sqrt(5)) / 2
    h=0
    
    
    for i in range(10, num_colors):
        h = (h + golden_ration) % 1
        s = 0.7 + 0.3 * (i%2) # alternate between 0.7 and 1
        l = 0.8 + 0.2 * (i%2) # alternate between 0.8 and 1
        
        rgb = colorsys.hls_to_rgb(h, l, s)
        
        hex_color = '#{:02x}{:02x}{:02x}'.format(
            int(rgb[0]*255), 
            int(rgb[1]*255), 
            int(rgb[2]*255)
        )
        colors.add(hex_color)
    
    return colors

COLORS_PALETTE = _generate_distinct_colors(100)


def get_trace_config(plot_type='scatter', mode=None):
    trace_config = {}
    # Get the first color from OrderedSet and remove it
    first_color = next(iter(COLORS_PALETTE))
    COLORS_PALETTE.remove(first_color)
    
    if plot_type == 'scatter':
        
        line_config = {
            'color': first_color,
            'width': 2
        }
        marker_config= {
            'size': 5,
            'color': first_color,
        }   
        if mode == 'markers':
            trace_config['marker'] = marker_config
        elif mode == 'lines':
            trace_config['line'] = line_config
        elif mode == 'markers+lines':
            trace_config['marker'] = marker_config
            trace_config['line'] = line_config
    elif plot_type == 'bar':
        trace_config['marker'] = {
            'color': first_color,
        }   
    elif plot_type == 'box':
        trace_config['marker'] = {      
            'color': first_color,
        }
    elif plot_type == 'pie':
        trace_config['marker'] = {
            'color': first_color,
        }
    return trace_config