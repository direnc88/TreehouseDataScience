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
    "from s2v2 import\n",
    "\n",
    "def calculate_sum(data_sample):\n",
    "    total=0\n",
    "    for row in data_sample[1:]:\n",
    "        price = float(row[2])\n",
    "        total += price\n",
    "    return total\n",
    "\n",
    "#this next line does the same thing, but more succinct. \n",
    "def calculate_sum_succint(data_sample):\n",
    "    prices = [float(row[2]) for row in data_sample[1:]]\n",
    "    return prices\n",
    "\n",
    "def calculate_sum_concise(data_sample):\n",
    "    prices = list(map(lambda x: float(x[2]), data_sample[1:]))\n",
    "    return sum(prices)\n",
    "\n",
    "#print(calculate_sum_concise(data_from_csv)) \n",
    "#print(calculate_sum(data_from_csv))\n",
    "#print(calculate_sum_succint(data_from_csv))\n",
    "\n",
    "def calc_numpy_sum(price):\n",
    "    prices_in_float = [float(line) for line in price]\n",
    "    total = numpy.sum(prices_in_float)\n",
    "    return total\n",
    "\n",
    "price = mu_csv['priceLabel']\n",
    "my_sum = calc_numpy_sum(price)\n",
    "print(\"The sum (numpy):\", my_sum)\n",
    "\n"
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
