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
    "from s2v3 import *\n",
    "\n",
    "def find_average(data_sample, header = False):\n",
    "    if header: \n",
    "        data_sample = data_sample[1:]\n",
    "    total = calculate_sum(data_sample)\n",
    "    size = number_of_records(data_sample)\n",
    "    average = total / size\n",
    "    return average\n",
    "\n",
    "average_price = find_average(data_from_csv, True)\n",
    "#print(\"Average = \", average_price)\n",
    "#print('{:03.2f}'.format(average_price))\n",
    "\n",
    "#use the built in type function to double check the types of variables. \n",
    "\n",
    "print(average_prince, int(average_price))\n",
    "print(type(int(average_price)))\n",
    "print(type(data_from_csv))\n",
    "print(type(my_csv))\n",
    "\n",
    "\n",
    "#dividing data in half. calculating midpoint value\n",
    "\n",
    "midpoint = round(numer_of_ties / 2) \n",
    "message = \"Average of {} half = ${:3.2f}\"\n",
    "print =(message.format(\"1st\", find_average(data_from_csv[:midpoint], True)))\n",
    "print =(message.format(\"2nd\", find_average(data_from_csv[midpoint:], False)))\n",
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
