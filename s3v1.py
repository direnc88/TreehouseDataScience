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
    "from s2v5 import *\n",
    "\n",
    "def create_bool_field_from_search_term(data_sample, search_term):\n",
    "    new_array = []\n",
    "    new_array.append(data_sample[0].append(search_term))\n",
    "    \n",
    "    for row in data_sample[1:]:\n",
    "        new_bool_field = False\n",
    "        if search_term in row[7]:\n",
    "            new_bool_field = True\n",
    "        \n",
    "        row.append(new_bool_field)\n",
    "        new_array.append(row)\n",
    "    \n",
    "    \n",
    "    \n",
    "    return new_array\n",
    "\n",
    "def filter_col_by_bool(data_sample, col):\n",
    "    matches_search_terms = []\n",
    "    \n",
    "    for item in data_sample[1:]:\n",
    "        if item[col]:\n",
    "            matches_search_term.append(item)\n",
    "    return matches_search_term\n",
    "    \n",
    "my_new_csv = creat_bool_field_from_search_term(data_from_csv, \"cashmere\")\n",
    "number_of_cashmere_ties = number_of_records(filter_col_by_bool(my_new_csv, 11))\n",
    "print(\"Lenght: \", number_of_cashmere_ties)\n",
    "#we should have 56 ties that were made with cashmere in our data set\n",
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
