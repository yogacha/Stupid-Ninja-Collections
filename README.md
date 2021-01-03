# Stupid-Ninja-Collections

Prototypes of random stupid ideas pop into my head. Usable but may not stable. 

See example code in `usage.ipynb`.


# Content

+ ## pandas extension

  + ### ***Book***, Dict[DataFrame or Series] 
      **To get rid of for loops and increase readablility when applying same opreation on different Dataframes.**

      A class mapping pandas-like operations to every pandas objects in the dictionary.
      
      It works as if it's a pandas object.

+ ## curry

  + ### ***keyword_first***, decorator
    **To get rid of over-nested function.**

    Partial application on kwargs. See [magic](usage.ipynb) use of it.

    Ex: *f(a, b, \*, x=1, y=2) → f(x=1, y=2)(a, b)*