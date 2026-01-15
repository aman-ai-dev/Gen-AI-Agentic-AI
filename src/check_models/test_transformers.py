from transformers import pipeline

classifier = pipeline("sentiment-analysis")

result = classifier("Bhai transformers sahi me powerful hai")
print(result)
