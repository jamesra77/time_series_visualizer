import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv",
                 parse_dates=True,
                 index_col="date")

# Clean data
outliers_mask = (df["value"] > df["value"].quantile(0.025)) & (df["value"] < df["value"].quantile(0.975))
df = df[outliers_mask]


def draw_line_plot():
    # Draw line plot
    fig, axes = plt.subplots(figsize=(21, 6))

    axes.plot(df, color="firebrick", linewidth=1.5)
    axes.set_xlabel("Date")
    axes.set_ylabel("Page Views")
    axes.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # ***probably use sns.catplot() instead***
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    # Draw bar plot
    fig, axes = None




    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
