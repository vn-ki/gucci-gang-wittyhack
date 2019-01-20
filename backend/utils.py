def delete_collection(db, coll_ref, batch_size, counter):
    batch = db.batch()
    init_counter=counter
    docs = coll_ref.limit(500).get()
    deleted = 0

    for doc in docs:
        batch.delete(doc.reference)
        deleted = deleted + 1

    if deleted >= batch_size:
        new_counter= init_counter + deleted
        batch.commit()
        print("potentially deleted: " + str(new_counter))
        return delete_collection(coll_ref, batch_size, new_counter)
    batch.commit()
