def analyze(df):
    return df.groupby(['referral_domain', 'country_name']).country_name.agg(len)
