import matplotlib.pyplot as plt
import matplotlib as mpl

print("matplotlib version:", mpl.__version__)
print("available styles:", plt.style.available)
try:
    plt.style.use('fivethirtyeight')
    print("fivethirtyeight available: YES")
except Exception as e:
    print("fivethirtyeight available: NO ->", type(e).__name__, e)

import os
print('mpl.__file__:', getattr(mpl, '__file__', 'n/a'))
print('mpl.get_configdir():', mpl.get_configdir())
print('mpl.get_data_path():', mpl.get_data_path())
style_dir = os.path.join(mpl.get_data_path(), 'stylelib')
print('stylelib exists:', os.path.isdir(style_dir))
if os.path.isdir(style_dir):
    print('stylelib contents sample:', os.listdir(style_dir)[:50])
