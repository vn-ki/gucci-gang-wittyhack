def analyze(df):
    return df.groupby('category').mean().groupby('category').apply(dict)
