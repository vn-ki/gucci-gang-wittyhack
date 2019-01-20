from data import read_data
import analyzers
from google.cloud import firestore


df = read_data('data.json')

req = analyzers.read_per_catergory.analyze(df)

top_categories = list(analyzers.read_per_catergory.analyze(df).groupby('category').groups.keys())[:10]
category_times = analyzers.catergory_time.analyze(df)
read_percentage = analyzers.read_percentage.analyze(df)
__import__('pdb').set_trace()

# upload top_categories to firestore
print("updating categories")
db = firestore.Client()
for cat in top_categories:
    db_ref = db.document("topCategories/{}".format(cat))
    db_ref.set({})

#upload category_times to firestore
print("updating categories_times")
for category, time in dict(category_times).items():
    db_ref = db.document("categoryTimes/{}".format(category))
    db_ref.set(
        {
            'popularTimestamp': int(time[0][0].astype("datetime64[s]").astype('int')),
            'hits': int( time[1][0] )
        }
    )

#upload user scroll data to firestore
print("updating read_percentage")
for category, scroll_data in dict(read_percentage).items():
    db_ref = db.document("readPercentages/{}".format(category))
    db_ref.set(
        {
            'readPercentage': scroll_data['read_percentage'][0],
            'totalBlocks': scroll_data['total_blocks'][0],
            'currentBlock': scroll_data['current_block'][0]
        }
    )
