import pandas as pd

# データの読み込みと欠損値の指定
# 欠損値 : "n/a", "NaN", "--" 
missing_values = ["n/a", "NaN", "--"]
df = pd.read_csv('weather_data.csv', na_values=missing_values)

# データの最初の数行を表示して、どのようなデータが含まれているか確認する
print("データの概要:")
print(df.head())

# 各列に欠損値が含まれているかどうかをチェックする
print("各列の欠損値の数:")
print(df.isnull().sum())

# 不正なデータの処理
# (1) Temperature 列の異常値をチェックし、-50°C 以下または 50°C 以上の値を欠損値として扱う
df.loc[(df['Temperature (°C)'] < -50) | (df['Temperature (°C)'] > 50), 'Temperature (°C)'] = None

# Humidity 列の欠損値を平均値で置き換える
mean_humidity = df['Humidity (%)'].mean()
df['Humidity (%)'] = df['Humidity (%)'].fillna(mean_humidity)

# 欠損値の処理
# Rainfall 列の欠損値を 0mm で置き換える（雨が降らなかったことを意味する）
df['Rainfall (mm)'] = df['Rainfall (mm)'].fillna(0)

# Temperature 列の欠損値を平均気温で置き換える
mean_temp = df['Temperature (°C)'].mean()
df['Temperature (°C)'] = df['Temperature (°C)'].fillna(mean_temp)

# 最終データの確認
print("処理後のデータ:")
print(df.to_string())

# 処理後のデータを新しいCSVファイルに保存する
df.to_csv('cleaned_data.csv', index=False)
