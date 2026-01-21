{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f4433206-3ade-45bb-bd68-bdb9d7685099",
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "\n",
    "def plot_company_count(df):\n",
    "    ax = sns.countplot(x='company', data=df, hue='company')\n",
    "    ax.legend(title='Company', bbox_to_anchor=(1.05, 1), loc='upper left')\n",
    "    plt.tight_layout()\n",
    "    plt.show()\n",
    "\n",
    "def plot_topping_count(df):\n",
    "    counts = df['topping'].value_counts()\n",
    "    sns.barplot(x=counts.index, y=counts.values)\n",
    "    plt.xticks(rotation=90)\n",
    "    plt.show()\n",
    "\n",
    "def plot_size_price(df):\n",
    "    counts = df.groupby('size')['price'].mean().sort_values()\n",
    "    plt.bar(counts.index, counts.values)\n",
    "    plt.show()\n",
    "\n",
    "def plot_boxplots(df):\n",
    "    sns.boxplot(x='diameter', data=df)\n",
    "    plt.show()\n",
    "\n",
    "    sns.boxplot(x='price', data=df)\n",
    "    plt.show()"
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
