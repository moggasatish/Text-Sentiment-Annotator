Text Sentiment Annotation using Python(step by step process)
Step 1: Import Library
Import the Pandas library to handle and store text data in table format.
Python
import pandas as pd
Step 2: Create Text Dataset
Create a list of sample text sentences that need sentiment labeling.
Python
texts = [...]
Step 3: Convert into DataFrame
Convert the text list into a DataFrame with one column named text.
Python
df = pd.DataFrame({'text': texts})
Step 4: Annotate Sentiment Labels
Run a loop to display each sentence and manually enter a sentiment label:
Positive
Negative
Neutral
The labels are stored in a list.
Step 5: Add Labels to Dataset
Create a new column called sentiment and store all annotated labels in it.
Python
df['sentiment'] = labels
Step 6: Save as CSV File
Save the final annotated dataset into a CSV file for future use in NLP or machine learning projects.
Python
df.to_csv("annotated_sentiments.csv", index=False)
Output:
Bash
annotated_sentiments.csv
