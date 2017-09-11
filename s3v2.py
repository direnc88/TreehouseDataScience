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
    "import s3v1 import *\n",
    "\n",
    "def filter_col_by_string(data_sample, field, filter_condition):\n",
    "    filtered_row = []\n",
    "    \n",
    "    col = int(data_sample[0].index(field))\n",
    "    filtered_rows.append(data_sample[0])\n",
    "    \n",
    "    for item in data_sample[1:]:\n",
    "        if item[col] == filter_condition:\n",
    "            filtered_rows.append\n",
    "    \n",
    "    return filtered_rows\n",
    "\n",
    "\n",
    "gucci_ties = filter_col_by_string(data_from_csv, \"brandName\", \"Gucci\")\n",
    "#print(\"found {} Gucci Ties\".format(number_of_records(gucci_ties)))\n",
    "\n",
    "silk_ties = filter_col_by_string(data_from_csv, \"material\", \"_silk\")\n",
    "#finds the number of silk ties\n",
    "#print(\"Found {} silk ties\".format(num_of_records(silk_ties)))\n",
    "\n",
    "wool_ties = filter_col_by_string(data_from_csv, \"material\", \"_wool\")\n",
    "#finds the number of wool ties\n",
    "#print(\"Found {} wool ties\".format(num_of_records(wool_ties)))\n",
    "\n",
    "cotton_ties = filter_col_by_string(data_from_csv, \"material\", \"_cotton\")\n",
    "#finds the number of silk ties\n",
    "#print(\"Found {} cotton ties\".format(num_of_records(cotton_ties)))\n",
    "\n",
    "\n",
    "def filter_col_by_float(data_sample, field, direction, filter_condition):\n",
    "    filtered_rows = []\n",
    "    \n",
    "    col = int(data_sample[0].index(field))\n",
    "    cond = float(filter_condition)\n",
    "    \n",
    "    for row in data_sample[1:]:\n",
    "        element = float(row[col])\n",
    "        \n",
    "        if direction == \"<\"\n",
    "            if element < cond:\n",
    "                filtered_rows.append(row)\n",
    "        elif direction == \"<=\"\n",
    "            if element <= cond:\n",
    "                filtered_rows.append(row)\n",
    "        elif direction == \">\"\n",
    "            if element > cond:\n",
    "                filtered_rows.append(row)\n",
    "        elif direction == \">=\"\n",
    "            if element >= cond:\n",
    "                filtered_rows.append(row)\n",
    "        elif direction == \"==\"\n",
    "            if element == cond:\n",
    "                filtered_rows.append(row)\n",
    "        else:\n",
    "            pass\n",
    "        return filtered_rows\n",
    "    \n",
    "under_20_bucks = filter_col_by_float(data_from_csv, \"priceLabel\", \"<=\", 20)\n",
    "print(\"Found {} ties < $20\".format(number_of_records(under_20_bucks)))\n",
    "\n",
    "\n",
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
