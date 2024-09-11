import pandas as pd
import json

# Load the CSV file
csv_file_path = 'cleaned_data.csv'  # Update this to the path of your CSV file
df = pd.read_csv(csv_file_path)

# Initialize the JSON structure
intents = []

# Iterate over each unique disease in the CSV
for disease in df['Disease'].unique():
    disease_data = df[df['Disease'] == disease]
    
    for topic in disease_data['Topic'].unique():
        topic_data = disease_data[disease_data['Topic'] == topic]
        
        # Generate the tag based on disease and topic
        tag = f"{disease.lower().replace(' ', '_')}_{topic.lower().replace(' ', '_')}"
        
        # Patterns and responses for each topic
        patterns = topic_data['Topic'].tolist()
        responses = topic_data['Information'].tolist()

        # Append the intent to the list
        intent = {
            "tag": tag,
            "patterns": patterns,
            "responses": responses
        }
        intents.append(intent)

# Save to JSON file
json_data = {"intents": intents}

with open('output_file.json', 'w') as json_file:
    json.dump(json_data, json_file, indent=4)
