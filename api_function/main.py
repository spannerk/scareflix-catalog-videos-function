import functions_framework
from google.cloud import firestore_v1

def get_metadata(doc, collection_ref):
    metadata_id = doc.to_dict().get('tmdb_metadata_id')
    if metadata_id:
        metadata_ref = collection_ref.document(metadata_id)
        metadata = metadata_ref.get()
        if metadata.exists:
            return metadata.to_dict()
    return None


@functions_framework.http
def get_videos(request):
    db = firestore_v1.Client(project='scareflix', database='scareflix-db')
    col_ref = db.collection("videos")
    return [{'id':doc.id, 'data': doc.to_dict(), 'metadata': get_metadata(doc, db.collection("tmdb_metadata"))} for doc in col_ref.get()]
