import pandas as pd

# Step 1: Sample text data
texts = [
    "I love this product!",
    "This is terrible.",
    "It's okay, not great.",
    "Absolutely fantastic experience.",
    "I wouldn't recommend it."
]

# Step 2: Create a DataFrame
df = pd.DataFrame({'text': texts})

# Step 3: Manual annotation
print("Label each text as Positive, Negative, or Neutral:\n")
labels = []
for i, row in df.iterrows():
    print(f"{i+1}. {row['text']}")
    label = input("Sentiment (Positive/Negative/Neutral): ").strip().capitalize()
    labels.append(label)

# Step 4: Save annotated data
df['sentiment'] = labels
df.to_csv("annotated_sentiments.csv", index=False)

print("\n✅ Annotation complete. Saved to 'annotated_sentiments.csv'")
