import datetime
import matplotlib.pyplot as plt
import pandas as pd
from math import ceil, sqrt
# Super simple timer
#  Timing implemented as class methods
#  to avoid having to instantiate
class Timer:

    @classmethod
    def start(cls):
        cls.start_time = datetime.datetime.now()

    @classmethod
    def end(cls):
        delta = datetime.datetime.now() - cls.start_time
        sec = delta.seconds
        ms  = delta.microseconds // 1000
        print(f'{sec}.{ms} seconds elapsed')


class FeaturePlot:
    '''
        Manages a figure containing plots of many unrelated variables
        To use: this is an iterable that will yield (col_name, data, axis)
        for each variable it contains
    '''
    def __init__(self, *data):
        self.data     = pd.concat(data, axis = 'columns')
        self.columns  = self.data.columns
        self.num_cols = len(self.columns)
        self._make_figure()

    def clone(self):
        return FeaturePlot(self.data)

    def _make_figure(self):
        '''
           Makes the main figure
        '''

        # Compute the size and get fig, axes
        s = ceil(sqrt(self.num_cols))
        fig, axes = plt.subplots(s, s, figsize = (4*s, 4*s));
        axes = axes.ravel()

        # Delete excess axes
        to_delete = axes[self.num_cols:]
        for ax in to_delete:
            ax.remove()

        # Retain references
        self.fig  = fig
        self.axes = dict(zip(self.columns, axes))

        # Add titles
        for col, ax in self.axes.items():
            ax.set_title(col)

        self.grid_size = s

    def overlay(self, label, sharex = False, sharey = False):
        '''
            Adds a new layer of axes on top of an existing figure

            - Is a generator in similar style to self.__iter__ below.
            - A reference to the newly created axes is not maintained
                 by the class - the axes are intended to be single use.
                 If you want to access the axes later, either use the
                 matplotlib figure object or retain a reference
        '''
        for index, col in enumerate(self.columns):
            base_ax = self.axes[col]
            ax = self.fig.add_subplot(self.grid_size, self.grid_size, index + 1,
                                      sharex = base_ax if sharex else None,
                                      sharey = base_ax if sharey else None,
                                      label  = label,
                                      facecolor = 'none')

            for a in [ax, base_ax]:
                if not sharex:
                    a.tick_params(bottom = False,
                                  top = False,
                                  labelbottom = False,
                                  labeltop    = False)
                if not sharey:
                    a.tick_params(left = False,
                                  right = False,
                                  labelleft = False,
                                  labelright = False)


            yield col, self.data[col].values, ax

    def __iter__(self):
        for col in self.columns:
            yield col, self.data[col].values, self.axes[col]

def plot(fn, *args, **kwargs):
    if 'figsize' in kwargs:
        fig, ax = plt.subplots(figsize = kwargs['figsize'])
        del kwargs['figsize']
    else:
        fig, ax = plt.subplots()
    kwargs['ax'] = ax
    fn(*args, **kwargs)
    return fig

def drop_by_rule(df, bool_series):
    index = df[bool_series].index
    df.drop(index = index, inplace = True)
