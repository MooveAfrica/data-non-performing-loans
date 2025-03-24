class Trace:
    """
    A generic plotly trace wrapper class to handle different trace types.
    """
    def __init__(self, **kwargs):
        self._plot_params = {}
        self._trace = None
        if 'legendgrouptitle' in kwargs:
            title = kwargs['legendgrouptitle']
            kwargs['legendgrouptitle'] = dict(
                text=f'<b>{title}</b>',
                font=dict(
                    family='Arial Black, sans-serif',
                    size=16,
                    color='#2a3f5f'
                )
            )
        for key, value in kwargs.items():
            if key in self._valid_props:
                self._plot_params[key] = value

    @property
    def trace(self):
        return self._trace
    @trace.setter
    def trace(self, value):
        self._trace = value