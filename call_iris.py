import uuid
import pandas as pd
from afp_request import call_iris
from extract_event import parse_event_list

# Call Iris API
print("Calling Iris")
res = call_iris()

# Extract event data
print(f"Extracting data from {len(res)} events")
events = parse_event_list(res)

# Convert list to dataframe
df = pd.DataFrame(events)

## Save CSV:
print("Saving CSV")
# Generate a random hash using uuid
hash = str(uuid.uuid4())[:5]  # Take the first 5 chars
# Combine hash, name and filepath
csv_name = f"candidate-events-{hash}.csv"
filepath = 'data/'
df.to_csv(filepath+csv_name, index=False)
print(f"Saved: {csv_name}")