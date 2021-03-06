{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "c59cda66",
   "metadata": {},
   "outputs": [],
   "source": [
    "import math  # Import Math library\n",
    " \n",
    "def polysum(n,s):\n",
    "    '''  Function takes 2 arguments, 'n' and 's', where  'n' number of sides and side has length 's'.\n",
    "    This function summarizes the area and square of the perimeter of the regular polygon, and returns the sum, \n",
    "    rounded to 4 decimal places.\n",
    "    '''\n",
    "    return round(((0.25*n*s**2)/(math.tan(math.pi/n)) +(n*s)**2),4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b0ebc992",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "45e9bdae",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "8542442.876758019"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "polysum(97, 29)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "71406056",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3.141592653589793"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "math.pi"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "52c20084",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1.0"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "math.tanh(45)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b99d4b4d",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.8.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
