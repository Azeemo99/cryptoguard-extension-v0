from pathlib import Path

MODEL_REPO = 'Azeemo99/cryptoguard-models'
MODEL_REVISION = 'f8369a7979e15bdcb48ecd169288364d3fbc6bf1'
MODEL_SUBFOLDER = 'distilbert_blockchain'

BASE_DIR = Path(__file__).resolve().parent.parent
token_path = BASE_DIR / "hf_token.txt"
token = token_path.read_text().strip() if token_path.exists() else None