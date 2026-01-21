{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "062d296c-1713-4ba6-b770-1e91b5764ff3",
   "metadata": {},
   "outputs": [],
   "source": [
    "import math\n",
    "import pandas as pd\n",
    "from sklearn.model_selection import train_test_split, cross_val_score\n",
    "from sklearn.pipeline import Pipeline\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "from sklearn.linear_model import LinearRegression\n",
    "from sklearn.ensemble import RandomForestRegressor\n",
    "from sklearn.metrics import mean_squared_error, r2_score\n",
    "\n",
    "from data_cleaning import load_data, clean_data\n",
    "\n",
    "def remove_outliers(df):\n",
    "    cols = ['price', 'diameter']\n",
    "    Q1 = df[cols].quantile(0.25)\n",
    "    Q3 = df[cols].quantile(0.75)\n",
    "    IQR = Q3 - Q1\n",
    "    lower = Q1 - 1.5 * IQR\n",
    "    upper = Q3 + 1.5 * IQR\n",
    "    df[cols] = df[cols].clip(lower=lower, upper=upper, axis=1)\n",
    "    return df\n",
    "\n",
    "def train_model(path):\n",
    "    df = load_data(path)\n",
    "    df = clean_data(df)\n",
    "    df = remove_outliers(df)\n",
    "\n",
    "    X = df.drop(columns='price')\n",
    "    y = df['price']\n",
    "\n",
    "    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
    "\n",
    "    lr_pipeline = Pipeline([\n",
    "        ('scaler', StandardScaler()),\n",
    "        ('model', LinearRegression())\n",
    "    ])\n",
    "\n",
    "    lr_pipeline.fit(X_train, y_train)\n",
    "    y_pred_lr = lr_pipeline.predict(X_test)\n",
    "\n",
    "    print(\"Linear Regression R2:\", r2_score(y_test, y_pred_lr))\n",
    "    print(\"Linear Regression MSE:\", mean_squared_error(y_test, y_pred_lr))\n",
    "\n",
    "    rf_model = RandomForestRegressor(n_estimators=300, random_state=42, n_jobs=-1)\n",
    "    rf_model.fit(X_train, y_train)\n",
    "    y_pred_rf = rf_model.predict(X_test)\n",
    "\n",
    "    print(\"Random Forest MSE:\", mean_squared_error(y_test, y_pred_rf))\n",
    "    print(\"Random Forest R2:\", r2_score(y_test, y_pred_rf))\n",
    "\n",
    "    scores = cross_val_score(rf_model, X_train, y_train, cv=5, scoring='r2')\n",
    "    print(\"CV scores:\", scores)\n",
    "    print(\"CV mean:\", scores.mean())"
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
