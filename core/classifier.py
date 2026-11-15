from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
from core.config import MODEL_REPO, MODEL_REVISION, MODEL_SUBFOLDER, token

class Classifier:
    def __init__(self):
        print("Initialising DistilBERT Classifier...")
        self.tokeniser = AutoTokenizer.from_pretrained(
            MODEL_REPO,
            subfolder = MODEL_SUBFOLDER,
            revision = MODEL_REVISION,
            token = token
        )

        self.model = AutoModelForSequenceClassification.from_pretrained(
            MODEL_REPO,
            subfolder = MODEL_SUBFOLDER,
            revision = MODEL_REVISION,
            token = token
        )

        self.model.eval()

    def predict(self, text:str) -> dict:
        input = self.tokeniser(text, return_tensors='pt', truncation=True, max_length=1024)

        with torch.no_grad():
            output = self.model(**input)
            probabilities = torch.softmax(output.logits, dim=1)
            phishing_score = probabilities[0][1].item()

        return {
            "is_phishing":phishing_score>0.5,
            "risk_level": "HIGH" if phishing_score > 0.8 else "MEDIUM" if phishing_score>0.5 else "LOW",
            "confidence_score":round(phishing_score*100, 2)
        }