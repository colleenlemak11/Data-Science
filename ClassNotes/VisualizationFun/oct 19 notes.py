# Oct 19 Notes

# EDA: exporatory data analysis
# getting familiar with data
# visualizing data, mining data (looking for groups, patters, etc.)

# goal of data visualization
# 1. clearly and accurately represent data
# 2. be creative, with the goal of increasing readability and understanding
# 3. label the units, and points of interest

# some jargon
# chart: a 2D visualization
# plot: a chart with data points (ex: scatter plot)
# a graph: a chart for a math function (ex: sine)

# we will use the matplotlib library for charting with python
# 3 ways to use matplotlib
# 1. using the pyplot module (what data scientists typically use)

# * there is always a "current" figure *

# 2. using the OOP interface
# 3. a mix of the first two

import matplotlib.pyplot as plt
import numpy as np

# let's start with a simple line chart
# 1. line chart (Check)
def line_chart_example(x, y, y2, filename):
    # x and y could be 1D lists, 1D numpy arrays, pandas series, etc.
    plt.plot(x, y)

    # 1D lists, 1D numpy arrays, pandas series, etc
    plt.plot(x, y, label="X Squared")

    # "beautify" the plot
    plt.plot(x, y2, color="red", lw=5, label="X Cubed")
    plt.legend()
    plt.grid()
    plt.title("Our First 222 Chart")
    plt.xlabel("X units")
    plt.ylabel("Y units")

    # now we need to "show" the plot
    # 3 main ways
    # 1. plt.show() = opens a window
    # plt.show()
    # 2. plt.savefig (filename) = saves to a file (ex: png, jpg, etc)
    plt.savefig(filename)
    # 3. inline with jupyter notebook


# 2. scatter plot
def scatter_chart_example(x, y, filename):
    plt.figure() # create a new "current" figure
    plt.scatter(x, y, color="green", marker="x", s=500)
    plt.savefig(filename)


# 3. bar chart
def bar_chart_example(x, y, filename):
    plt.figure() # create a new "current" figure
    plt.bar(x, y, facecolor="green", edgecolor="black")
    plt.savefig(filename)


# 4. pie chart
def pie_chart_example(x, y, filename):
    plt.figure() # create a new "current" figure
    plt.pie(y, labels=x, autopct="%1.1f%%") # auto percent puts labes in pie chart
    plt.savefig(filename)


# 5. histogram
def histogram_chart_example(data, filename):
    plt.figure() # create a new "current" figure
    plt.hist(data, bins=30, edgecolor="black")
    plt.savefig(filename)


# 6. box plots (later)


def main():
    # we need some data
    x = list(range(6)) # [0, 1, 2, 3, 4, 5]
    y = [] # will be squares of x
    y2 = []
    for val in x:
        y.append(val ** 2)
        y2.append(val ** 3)
    print(x)
    print(y)

    line_chart_example(x, y, y2, "line_example.png")
    scatter_chart_example(x, y, "scatter_example.png")
    bar_chart_example(x, y, "bar_example.png")
    pie_chart_example(x, y, "pie_example.png")

    # we need more interesting data for our histogram...
    # let's randomly sample 1000 points from a normal distribution
    # with mean 100 and stdev 20
    np.random.seed(0) # for reproducibility
    mean = 100
    stdev = 20
    num_samples = 1000
    random_data = np.random.normal(mean, stdev, num_samples)
    histogram_chart_example(random_data, "histogram_example.png")

main()
