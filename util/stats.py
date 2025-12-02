import datetime

import matplotlib.pyplot as plt
import mplcyberpunk
import numpy as np
from aocd.models import User, default_user
from matplotlib.ticker import FuncFormatter, MultipleLocator


def format_func(x, pos):
    hours = int(x // 3600)
    minutes = int((x % 3600) // 60)
    seconds = int(x % 60)

    return "{:d}:{:02d}:{:02d}".format(hours, minutes, seconds)


formatter = FuncFormatter(format_func)


def get_stats(year):
    user = default_user()
    stats = user.get_stats(2023)
    for k in stats.keys():
        print(k)
    stats = {k.split("/")[1]: v for k, v in stats.items()}
    return stats


def time_fmt(t):
    seconds = t.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return "{:02}:{:02}:{:02}".format(hours, minutes, seconds % 60)


def stats_table(stats):
    header = """      -------Part 1--------   -------Part 2--------
Day       Time  Rank  Score       Time  Rank  Score"""
    print(header)
    for day, v in reversed(stats.items()):
        t1 = v["a"]["time"]
        r1 = v["a"]["rank"]
        s1 = v["a"]["score"]
        t2 = v["b"]["time"]
        r2 = v["b"]["rank"]
        s2 = v["b"]["score"]
        formatted = f" {int(day):2}   {time_fmt(t1)}  {r1:4}  {s1:5}   {time_fmt(t2)}  {r2:4}  {s2:5}"
        print(formatted)


def colorize(text, color):
    return "${\color{" + color + "} \\textsf{" + text + "}}$"


def md_stats_table(stats):
    header = (
        "      "
        + colorize("-------Part 1--------", "Gold")
        + "   "
        + colorize("-------Part 2--------", "Gold")
        + "Day       "
        + colorize("Time  Rank  Score", "Gold")
        + "       "
        + colorize("Time  Rank  Score", "Gold")
    )
    print(header)
    for day, v in reversed(stats.items()):
        t1 = v["a"]["time"]
        r1 = v["a"]["rank"]
        s1 = v["a"]["score"]
        t2 = v["b"]["time"]
        r2 = v["b"]["rank"]
        s2 = v["b"]["score"]
        formatted = f" {int(day):2}   {time_fmt(t1)}  {r1:4}  {s1:5}   {time_fmt(t2)}  {r2:4}  {s2:5}"
        print(formatted)


def plot_times(stats):
    dates = [int(k) for k in stats.keys()]
    times_a = np.array([s["a"]["time"].seconds for s in stats.values()])
    times_b = np.array([s["b"]["time"].seconds for s in stats.values()])
    # dates = [i for i in range(9)]
    # times_a = np.random.randint(0, 1000, 9)
    # times_b = np.random.randint(0, 1000, 9) + times_a
    width = 0.5
    plt.style.use("cyberpunk")
    f = plt.figure()
    ax = f.add_subplot(1, 1, 1)
    bars_b = ax.bar(
        dates, times_b - times_a, width, color="C2", label="Gold", bottom=times_a
    )
    bars_a = ax.bar(dates, times_a, width, color="C0", label="Silver", bottom=0)
    ax.yaxis.set_major_formatter(formatter)
    # this locates y-ticks at the hours
    ax.yaxis.set_major_locator(MultipleLocator(base=10 * 60))
    # this ensures each bar has a 'date' label
    ax.xaxis.set_major_locator(MultipleLocator(base=1))
    ax.legend(loc="upper left")
    ax.bar_label(bars_b, fmt=formatter)
    mplcyberpunk.add_bar_gradient(bars_a)
    mplcyberpunk.add_bar_gradient(bars_b)
    mplcyberpunk.add_glow_effects(ax)
    plt.show()


if __name__ == "__main__":
    stats = get_stats(2023)
    plot_times(stats)
    md_stats_table(stats)
