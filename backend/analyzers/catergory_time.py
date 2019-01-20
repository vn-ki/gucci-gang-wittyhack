from scipy import stats

__all__ = [
    'analyze',
]


def analyze(df):
    timemodegp = df.groupby('category').time.agg(stats.mode)
    timemodegp = timemodegp[timemodegp.apply(lambda x: x.count[0] > 3)]
    return timemodegp
