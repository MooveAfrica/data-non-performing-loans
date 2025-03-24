import plotly.graph_objects as go
import importlib
from .trace import Trace
import src.plotly_wrapper.trace_config as tc
importlib.reload(tc)

class Bar(Trace):
    """
    A class to represent a bar plot in a plotly plot.
    """
    _valid_props = {
        "alignmentgroup",
        "base",
        "basesrc",
        "cliponaxis",
        "constraintext",
        "customdata",
        "customdatasrc",
        "dx",
        "dy",
        "error_x",
        "error_y",
        "hoverinfo",
        "hoverinfosrc",
        "hoverlabel",
        "hovertemplate",
        "hovertemplatesrc",
        "hovertext",
        "hovertextsrc",
        "ids",
        "idssrc",
        "insidetextanchor",
        "insidetextfont",
        "legend",
        "legendgroup",
        "legendgrouptitle",
        "legendrank",
        "legendwidth",
        "marker",
        "meta",
        "metasrc",
        "name",
        "offset",
        "offsetgroup",
        "offsetsrc",
        "opacity",
        "orientation",
        "outsidetextfont",
        "selected",
        "selectedpoints",
        "showlegend",
        "stream",
        "text",
        "textangle",
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
        "width",
        "widthsrc",
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
    def __init__(self, df, x_col=None, y_col=None, **kwargs):
        self.kwargs= kwargs
        self.kwargs['x'] = df[x_col]
        self.kwargs['y'] = df[y_col]
        # self.kwargs['marker'] = self.kwargs.get('marker', tc.get_trace_config(plot_type='bar'))
        # print(self.kwargs['marker'])
        super().__init__(**kwargs)
        self._trace = go.Bar(self._plot_params)
