
# https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/firestore/cloud-client/snippets.py
from google.cloud import firestore

def add_data_types(request):
    db = firestore.Client()
    # [START add_data_types]
    # [START firestore_data_set_from_map_nested]
    name = request.args.get('name') # https://www.youtube.com/watch?v=SHrR2fFVDO4
    data = {
        'name': name
    }

    db.collection('httptests').add(data)
    # [END firestore_data_set_from_map_nested]
    # [END add_data_types]
    #return 'Name: ' + details[0] + ' and Pref: ' + details[1] + ' added to firestore!'
    return 'Name: ' + name + ' added to Firestore!'
