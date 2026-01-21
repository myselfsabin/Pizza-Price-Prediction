{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0a25f776-8332-4b7d-8afc-67a491061d8c",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "def load_data(path):\n",
    "    df = pd.read_csv(path)\n",
    "    return df\n",
    "\n",
    "def clean_data(df):\n",
    "    df = df.drop_duplicates()\n",
    "    df = df.rename(columns={'price_rupiah':'price'})\n",
    "\n",
    "    df['price'] = pd.to_numeric(df['price'].str.replace(r'[^\\d.]', '', regex=True))\n",
    "    df['diameter'] = df['diameter'].str.replace(r'[^\\d.]', '', regex=True)\n",
    "    df['diameter'] = df['diameter'].astype(float)\n",
    "\n",
    "    # Convert yes/no to 0/1\n",
    "    bin_c = ['extra_sauce', 'extra_cheese', 'extra_mushrooms']\n",
    "    for col in bin_c:\n",
    "        df[col] = df[col].map({'yes': 1, 'no': 0})\n",
    "\n",
    "    # One hot encoding\n",
    "    cats_of_columns = ['company', 'topping', 'variant', 'size']\n",
    "    df = pd.get_dummies(df, columns=cats_of_columns, drop_first=True)\n",
    "\n",
    "    return df"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.14.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
