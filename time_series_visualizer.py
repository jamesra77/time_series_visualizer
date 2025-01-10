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
    df_yearly = df_bar.resample("ME").mean().rename(columns={"value": "Average Page Views"})
    df_yearly.reset_index(inplace=True)
    df_yearly["month"] = df_yearly["date"].dt.strftime("%B")
    df_yearly["Years"] = df_yearly["date"].dt.strftime("%Y")

    month_order = [
        "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
    ]
    df_yearly["month"] = pd.Categorical(df_yearly["month"], categories=month_order, ordered=True)

    # Draw bar plot
    fig = sns.catplot(
        data=df_yearly,
        x="Years",
        y="Average Page Views",
        hue="month",
        kind="bar",
        palette="deep"
    )




    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    month_order = [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ]

    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['Year'] = [d.year for d in df_box.date]
    df_box['Month'] = [d.strftime('%b') for d in df_box.date]
    df_box.rename(columns={"value": "Page Views"}, inplace=True)
    df_box["Year"] = pd.Categorical(df_box["Year"])
    df_box["Month"] = pd.Categorical(df_box["Month"], categories=month_order, ordered=True)


    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(14,6))

    flierprops = {
        "marker": "o",
        "markerfacecolor": "None",
        "markersize": 1,
    }

    sns.boxplot(data=df_box, x="Year", y="Page Views", ax=ax1, flierprops=flierprops, palette="deep", hue="Year", legend=False)
    sns.boxplot(data=df_box, x="Month", y="Page Views", ax=ax2, flierprops=flierprops, palette="deep", hue="Month", legend=False)

    ax1.set_title("Year-wise Box Plot (Trend)")
    ax2.set_title("Month-wise Box Plot (Seasonality)")




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
