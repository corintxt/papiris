def extract_event_data(data):
#     # First check validity
#     if data['locations'][0]['locationStatus'] == "NOT_USABLE"
    
    # Get ID
    event_id = data['sequenceId']
    event_hash = data['id']
    
    # Extract the event title (assuming it's in English) and ID
    event_title = data['title']['en']
    # Categorize candidate - str.find('target') returns -1 if not found
    if (event_title.find('Trump') != -1):
        candidate = 'TRUMP'
    elif (event_title.find('Biden') != -1):
        candidate = 'BIDEN'
    else:
        candidate = 'UNKNOWN'

    # Access location data
    location = data['locations'][0]
    
    # Extract the city, state, and country
    # We use {}.get() to check fo a key and return default value if not present
    city = location.get('label', {}).get('en', 'Unknown')
    state = location.get('parent', {}).get('label', {}).get('en', 'Unknown')
    status = location['locationStatus']

    # Extract the event date and time
    datestring = data['dateBegin'].split('T')
    event_date = datestring[0]
    
    # Get event time if it was included in dateBegin
    if len(datestring) > 1:
        event_time = datestring[1][:5]
    else:
        event_time = None

    # Extract the geographic coordinates
    latitude = location.get('latitude', None)
    longitude = location.get('longitude', None)

    # Format and return the extracted information
    details = dict()
    details['event_id'] = event_id
    details['candidate'] = candidate
    details['event_title'] = event_title
    details['city'] = city
    details['state'] = state
    details['date'] = event_date
    details['time'] = event_time
    details['lat'] = latitude
    details['lon'] = longitude
    details['status'] = status
    details['event_hash'] = event_hash


    return details

# Extract event data, append to list
def parse_event_list(api_response):
    events = list()
    for idx,r in enumerate(api_response):
        # print(idx)
        e = extract_event_data(r)
        events.append(e)
    return events