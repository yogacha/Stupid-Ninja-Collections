# %%
"""
Book:
    A dictionary of pandas.DataFrame,
    mapping pandas.DataFrame method to every DataFrame in dict

"""
import pandas as pd


Function = type(lambda: 0)


class _Loc(object):
    """
    For pandas-like slicing: loc[...], iloc[...]
    """

    def __init__(self, caller, is_iloc=False):
        self.caller = caller
        self.is_iloc = is_iloc

    def __getitem__(self, slicing):
        if self.is_iloc:
            return Book({
                name: df.iloc.__getitem__(slicing) 
                for name, df in self.caller.items()
            })
        else:
            return Book({
                name: df.loc.__getitem__(slicing) 
                for name, df in self.caller.items()
            })


def method_mapping(method):
    def method_mapper(self, *args, **kwargs):
        return Book({
            name: method(df_or_srs, *args, **kwargs)
            for name, df_or_srs in self.items()
        })

    return method_mapper


class Book(dict):

    """
    Collection of pandas.DataFrame or pnadas.Series
    """

    for method_name in dir(pd.DataFrame):
        method = getattr(pd.DataFrame, method_name)

        if ( isinstance(method, property)
             or method_name.startswith("_")
             or method_name in dir(dict)
            ):
            pass

        elif isinstance(method, Function):
            locals()[method_name] = method_mapping(method)

    @property
    def loc(self):
        return _Loc(self, is_iloc=False)

    @property
    def iloc(self):
        return _Loc(self, is_iloc=True)

    @property
    def T(self):
        return Book({
            name: df.T for name, df in self.items()
        })
