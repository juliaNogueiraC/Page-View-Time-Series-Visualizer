import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

from time_series_visualizer import clean_data, draw_line_plot, draw_bar_plot, draw_box_plot

def main():
  clean_data()

  draw_line_plot()

  draw_bar_plot()

  draw_box_plot()



if __name__ == "__main__":
    main()
