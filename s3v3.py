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
    "from s3v2 import * \n",
    "\n",
    "#we're going to be exploring grouping here\n",
    "\n",
    "gucci_ties = filter_col_by_string(data_from_csv, \"brandName\", \"Gucci\")\n",
    "jcrew_ties = filter_col_by_string(data_from_csv, \"brandName\", \"J.Crew\")\n",
    "\n",
    "max_gucci = find_max(gucci_ties[1:], 2)\n",
    "max_jcrew = find_max_min(jcrew_ties[1:], 2)\n",
    "\n",
    "message = \"Maximum {} tie price is  = ${:03.2f}\"\n",
    "print(message.format(\"Maximum\", \"Gucci\", max_gucci))\n",
    "print(message.format(\"Maximum\", \"J.Crew\", max_jcrew))\n",
    "\n",
    "avg_gucci = find_average(gucci_ties, True)\n",
    "print(message.format(\"Average\", \"Gucci\", avg_gucci))\n",
    "\n",
    "avg_jcrew = find_average(jcrew_ties, True)\n",
    "print(message.format(\"Average\", \"J.Crew\", avg_jcrew))\n",
    "\n",
    "\n",
    "striped_ties = filter_col_by_string(data_from_csv, \"print\", \"_striped\")\n",
    "print_ties = filter_col_by_string(data_from_csv, \"print\", \"_print\")\n",
    "paisley_ties = filter_col_by_string(data_from_csv, \"print\", \"_paisley\")\n",
    "solid_ties = filter_col_by_string(data_from_csv, \"print\", \"_solid\")\n",
    "\n",
    "message2 = \"{}\\t${:03.2f}\"\n",
    "print(\"Print\\tAverage\")\n",
    "print(message.format(\"striped\", find_average(striped_ties)))\n",
    "print(message.format(\"print\", find_average(print_ties)))\n",
    "print(message.format(\"paisley\", find_average(paisley_ties)))\n",
    "print(message.format(\"solid\", find_average(solid_ties)))\n",
    "\n",
    "\n",
    "\n",
    "\n",
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
