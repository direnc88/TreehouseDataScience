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
    "from s4v3 import *\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "#mainly used as an example, bar charts would be much better for this type of data/analysis\n",
    "\n",
    "def create_line_chart(data_sample, title, exported_figure_filename):\n",
    "    fig = plt.figure()\n",
    "    ax = fig.add_subplot(1, 1, 1)\n",
    "    \n",
    "    prices = (sorted(map(float, data_sample)))\n",
    "    \n",
    "    x_axis_ticks = list(range(len(data_sample))\n",
    "    ax.plot(x_axis_ticks, prices, linewidth=2)\n",
    "    ax.set_title(title)\n",
    "    ax.set_xlim([0, len(data_sample)])\n",
    "    ax.set_xlabel('Tie Price ($)')\n",
    "    ax.set_ylabel('Number of Ties')\n",
    "                        \n",
    "    fig.savefig(exported_figure_filename)\n",
    "                        \n",
    "create_line_chart([x[2] for x in gucci_ties[1:]], \"Distribution of Prices for Gucci Ties\", \"_charts/s5-line-gucci.png\")"
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
