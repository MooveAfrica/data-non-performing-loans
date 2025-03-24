import plotly.graph_objects as go
from .trace import Trace
class Figure:
    def __init__(self, data: list[Trace], layout: dict, title: str=None):
        self.data = data
        self.title = title
        self.layout = layout if layout else self._default_layout()
        self._annotations = []
        
    def _default_layout(self):
        return go.Layout(
            title=dict(
                text=self.title,
                font=dict(
                    family="Arial Black, sans-serif",
                    size=18,
                    color="#2a3f5f"
                ),
                x=0.5, 
                y=0.95
            ),
            xaxis=dict(
                title=dict(
                    text='<b>X Axis</b>',
                    font=dict(
                        family="Arial Black, sans-serif",
                        size=16,
                        color="#2a3f5f"
                    )
                ), 
                tickfont=dict(
                    family="Arial Black, sans-serif",
                    size=14,
                    color="#2a3f5f"
                ),
                showgrid=True,
                gridwidth=1, 
                gridcolor="#E5ECF6", 
                zeroline=False,
                zerolinewidth=1,
                zerolinecolor="#2a3f5f",
                showline=True,
                linewidth=2,
                linecolor="#2a3f5f",
                tickangle=-45,
            ),
            yaxis=dict(
                title=dict(
                    text='<b>Y Axis</b>',
                    font=dict(
                        family="Arial Black, sans-serif",
                        size=16,    
                        color="#2a3f5f"
                    )
                ),
                tickfont=dict(
                    family="Arial Black, sans-serif",
                    size=14,
                    color="#2a3f5f"
                ),
                showgrid=True,
                gridwidth=1, 
                gridcolor="#E5ECF6", 
                zeroline=False, 
                zerolinewidth=1,
                zerolinecolor="#2a3f5f",
                showline=True,
                linewidth=2,
                linecolor="#2a3f5f",
            ),
            plot_bgcolor="white",
            paper_bgcolor="white",
            margin=dict(
                l=20,
                r=20,
                t=50,
                b=20
            ),
            showlegend=True,
            legend=dict( 
                bgcolor="white",
                bordercolor="#E5ECF6",
                font=dict(
                    family="Arial Black, sans-serif",
                    size=14,
                    color="#2a3f5f"
                )
            ),
            hovermode="closest",
            hoverlabel=dict(
                bgcolor="white",
                bordercolor="#E5ECF6",
                font=dict(
                    family="Arial, sans-serif",
                    size=14,
                    color="#2a3f5f"
                )
            ),
            font=dict(
                family="Arial, sans-serif",
                size=14,
                color="#2a3f5f"
            ),
            template="plotly_white",
            width=1200,
            height=800,
            transition=dict(
                duration=500,
                easing="cubic-in-out"
            ),
            modebar=dict(
                orientation="h",
                bgcolor="rgba(255, 255, 255, 0.8)",
                color="#2a3f5f"
            )
        )
        
    
    @property
    def show_legend(self):
        return self.layout['showlegend']
    
    @show_legend.setter
    def show_legend(self, show: bool):
        self.layout['showlegend'] = show
    
    def set_bar_mode(self, mode: str):
        self.layout['barmode'] = mode
    
    def set_axis_title(self, xaxis_title: str, yaxis_title: str):
        if xaxis_title is not None:
            self.layout['xaxis']['title']['text'] = xaxis_title
        if yaxis_title is not None:
            self.layout['yaxis']['title']['text'] = yaxis_title
    
    def save(self, filename: str, width: int=600, height: int=400, scale: int=6):
        fig = go.Figure(data= [t.trace for t in self.data], layout=self.layout)
        for a in self._annotations:
            fig.add_annotation(a)
        fig.write_image(
            "../reports/plots/" + filename, 
            format="jpeg",
            width=width, 
            height=height, 
            scale=scale,
            engine="kaleido"
        )
    
    
    def add_trace(self, trace: Trace):
        if isinstance(trace, list):
            for t in trace:
                if isinstance(t, Trace):
                    self.data.append(t)
                else:
                    raise ValueError("Trace must be a list of Trace objects")
        elif isinstance(trace, Trace):
            self.data.append(trace)
        else:
            raise ValueError("Trace must be a Trace object")
    
    def add_annotation(self, x: float, y: float, text: str, showarrow: bool=False):
        self._annotations.append(
            dict(
                x=x,
                y=y,
                text=text,
                showarrow=showarrow, 
                font=dict(size=12, color="Red", family="Arial")
            )
        )
    def show(self):
        fig = go.Figure(data=[t.trace for t in self.data], layout=self.layout)
        for a in self._annotations:
            fig.add_annotation(a)
        fig.show()
        
    def set_percentage_axis(self, axis: str = 'y') -> None:
        """Set the axis format to display percentage values with 1 decimal place."""
        if axis == 'x':
            self.layout['xaxis']['tickformat'] = '.1%'
        elif axis == 'y':
            self.layout['yaxis']['tickformat'] = '.1%'
        else:
            raise ValueError("Axis must be 'x' or 'y'")