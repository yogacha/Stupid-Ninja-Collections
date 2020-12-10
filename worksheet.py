# %%
"""
make an dictionary of pandas.DataFrame,
mapping pandas.DataFrame method to every DataFrame in dict

"""
import pandas as pd


Function = type(lambda:0)


class _Loc(object):

    def __init__(self, father, is_iloc=False):
        self.father = father
        self.is_iloc = is_iloc

    def __getitem__(self, slicing):
        if self.is_iloc:
            return WorkSheet({
                name: df.iloc.__getitem__(slicing)
                 for name, df in self.father.items()
            })
        else:
            return WorkSheet({
                name: df.loc.__getitem__(slicing)
                 for name, df in self.father.items()
            })


def method_mapping(method):

    def mapping(self, *args, **kwargs):
        return WorkSheet({
            name: method(df_or_srs, *args, **kwargs)
                for name, df_or_srs in self.items()
        })

    return mapping



class WorkSheet(dict):

    """
    Collection of pandas.DataFrame or pnadas.Series
    """
    
    for method_name in dir(pd.DataFrame):
        method = getattr(pd.DataFrame, method_name)

        if ( isinstance( method, property ) 
             or method_name.startswith('_') 
             or method_name in dir(dict) ):
            pass

        elif isinstance(method, Function):
            locals()[method_name] = method_mapping(method)

    @property
    def loc(self):
        return _Loc(self, is_iloc=False)

    @property
    def iloc(self):
        return _Loc(self, is_iloc=True)