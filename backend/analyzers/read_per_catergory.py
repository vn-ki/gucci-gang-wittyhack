def analyze(df):
    return df.groupby('category').mean()
