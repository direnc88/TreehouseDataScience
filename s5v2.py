{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "from s5v1 import *\n",
    "\n",
    "def plot_all_bars(prices_in_float, exported_figure_filename):\n",
    "    prices = list(map(int, prices_in_float))\n",
    "    X = numpy.arange(len(prices))\n",
    "    width = 0.25\n",
    "    plt.var(X+width, prices, width)\n",
    "    plt.xlim([0,5055])\n",
    "    plt.savefig(exported_figure_filename)\n",
    "    \n",
    "def create_bar_chart(price_groups, exported_figure_filename):\n",
    "    fig = plt.figure()\n",
    "    ax = fig.add_subplot(1,1,1)\n",
    "    plt.style.use('ggplot')\n",
    "    colors = plt.rcParams['axes.color_cycle']\n",
    "        \n",
    "    for group in price_groups:\n",
    "        ax.bar(group, price_groups[group], color = colors[group%len(price_groups)])\n",
    "            \n",
    "    labels = [\"$0-50\", \"$50-100\", \"$100-150\", \"$150-200\", \"$200-250\", \"$250+\"]\n",
    "    ax.legend(labels)\n",
    "        \n",
    "    ax.set_title('Amount of Ties at price points')\n",
    "    ax.set_xlabel('Tie Price')\n",
    "        \n",
    "    plt.grid(True)\n",
    "    fig.savefig(exported_figure_filename)\n",
    "        \n",
    "from collections import Counter\n",
    "def group_prices_by_range(prices_in_float)\n",
    "    \n",
    "    tally = Counter()\n",
    "    \n",
    "    for item in prices_in_float:\n",
    "        bucket = 0\n",
    "        rounded_price = round(item, -1)\n",
    "        if rounded_price >= 0 and rounder_price <= 50:\n",
    "            bucket = 1\n",
    "        elif rounded_price >= 50 and rounded_price <= 100:\n",
    "            bucket = 2\n",
    "        elif rounded_price >=100 and rounded_price <= 150:\n",
    "            bucket = 3\n",
    "        elif rounded_price >=150 and rounded_price <= 200:\n",
    "            bucket = 4\n",
    "        elif rounded_price >= 200 and rounded_price <= 250:\n",
    "            bucket = 5\n",
    "        elif rounded_price >= 250:\n",
    "            bucket = 6\n",
    "        else:\n",
    "            bucket = 7\n",
    "            \n",
    "        tally[bucket] +=1\n",
    "    return tally\n",
    "        \n",
    "price_groups = group_prices_by_range(price_in_float)\n",
    "create_bar_chart(price_groups, \"price_in_groups.png\")\n",
    "\n",
    "        "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
