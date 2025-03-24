import plotly.graph_objects as go
import importlib
import src.plotly_wrapper.trace_config as tc
importlib.reload(tc)
from .trace import Trace

class Scatter(Trace):
    _valid_props = {
        "alignmentgroup",
        "cliponaxis",
        "connectgaps",
        "customdata",
        "customdatasrc",
        "dx",
        "dy",
        "error_x",
        "error_y",
        "fill",
        "fillcolor",
        "fillgradient",
        "fillpattern",
        "groupnorm",
        "hoverinfo",
        "hoverinfosrc",
        "hoverlabel",
        "hoveron",
        "hovertemplate",
        "hovertemplatesrc",
        "hovertext",
        "hovertextsrc",
        "ids",
        "idssrc",
        "legend",
        "legendgroup",
        "legendgrouptitle",
        "legendrank",
        "legendwidth",
        "line",
        "marker",
        "meta",
        "metasrc",
        "mode",
        "name",
        "offsetgroup",
        "opacity",
        "orientation",
        "selected",
        "selectedpoints",
        "showlegend",
        "stackgaps",
        "stackgroup",
        "stream",
        "text",
        "textfont",
        "textposition",
        "textpositionsrc",
        "textsrc",
        "texttemplate",
        "texttemplatesrc",
        "type",
        "uid",
        "uirevision",
        "unselected",
        "visible",
        "x",
        "x0",
        "xaxis",
        "xcalendar",
        "xhoverformat",
        "xperiod",
        "xperiod0",
        "xperiodalignment",
        "xsrc",
        "y",
        "y0",
        "yaxis",
        "ycalendar",
        "yhoverformat",
        "yperiod",
        "yperiod0",
        "yperiodalignment",
        "ysrc",
        "zorder",
    }
    _valid_modes = ['markers', 'lines', 'markers+lines']    
    def __init__(self, df, x_col=None, y_col=None, mode='lines', **kwargs):
        
        if mode not in self._valid_modes:
            raise ValueError(f"Invalid mode: {mode}. Valid modes are: {self._valid_modes}")
        
        self.kwargs= kwargs
        
        trace_config = tc.get_trace_config(plot_type='scatter', mode=mode)
        
        self.kwargs['mode'] = mode
        self.kwargs['x'] = df[x_col]
        self.kwargs['y'] = df[y_col]
        
        if mode == 'markers':
            self.kwargs['marker'] = trace_config['marker']
        elif mode == 'lines':
            self.kwargs['line'] = trace_config['line']
        elif mode == 'markers+lines':
            self.kwargs['marker'] = trace_config['marker']
            self.kwargs['line'] = trace_config['line']
        
        super().__init__(**kwargs)
        
        self._trace = go.Scatter(self._plot_params)
        