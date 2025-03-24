import plotly.graph_objects as go
import importlib
from .trace import Trace
import src.plotly_wrapper.trace_config as tc
importlib.reload(tc)

class Box(Trace):
    _valid_props = {
        "alignmentgroup",
        "boxmean",
        "boxpoints",
        "customdata",
        "customdatasrc",
        "dx",
        "dy",
        "fillcolor",
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
        "jitter",
        "legend",
        "legendgroup",
        "legendgrouptitle",
        "legendrank",
        "legendwidth",
        "line",
        "lowerfence",
        "lowerfencesrc",
        "marker",
        "mean",
        "meansrc",
        "median",
        "mediansrc",
        "meta",
        "metasrc",
        "name",
        "notched",
        "notchspan",
        "notchspansrc",
        "notchwidth",
        "offsetgroup",
        "opacity",
        "orientation",
        "pointpos",
        "q1",
        "q1src",
        "q3",
        "q3src",
        "quartilemethod",
        "sd",
        "sdmultiple",
        "sdsrc",
        "selected",
        "selectedpoints",
        "showlegend",
        "showwhiskers",
        "sizemode",
        "stream",
        "text",
        "textsrc",
        "type",
        "uid",
        "uirevision",
        "unselected",
        "upperfence",
        "upperfencesrc",
        "visible",
        "whiskerwidth",
        "width",
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
    def __init__(self, df, x_col, y_col, **kwargs):
        self.kwargs = kwargs
        self.kwargs['plot_type'] = 'box'
        self.kwargs['x'] = df[x_col]
        self.kwargs['y'] = df[y_col]
        trace_config = tc.get_trace_config(plot_type='box')
        self.kwargs['marker'] = self.kwargs.get('marker', trace_config['marker'])
        
        super().__init__(**kwargs)
        
        # Create the Box trace and set it in the parent class
        self._trace = go.Box(self._plot_params)
        
        
        