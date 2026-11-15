import os
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from core.config import MODEL_REPO, MODEL_SUBFOLDER, MODEL_REVISION

def main():
    print(f"Downloading model {MODEL_SUBFOLDER} from {MODEL_REPO}, revision {MODEL_REVISION[:7]}...")
    token = os.environ.get("HF_TOKEN")
    AutoTokenizer.from_pretrained(
        MODEL_REPO,
        subfolder=MODEL_SUBFOLDER,
        revision=MODEL_REVISION,
        token=token
    )

    AutoModelForSequenceClassification.from_pretrained(
        MODEL_REPO,
        subfolder=MODEL_SUBFOLDER,
        revision=MODEL_REVISION,
        token=token
    )

    print("Download complete!")

if __name__ == "__main__":
    main()