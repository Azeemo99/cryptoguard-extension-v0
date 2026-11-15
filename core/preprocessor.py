import re
import unicodedata

class Preprocessor:
    def __init__(self, max_length:int=2048):
        self.max_length = max_length
        self.invisible_chars_pattern = re.compile(r"[\u200B-\u200D\u2060\uFEFF\u00AD]")

    def clean_text(self, text:str) -> str:
        text = self.invisible_chars_pattern.sub("", text)
        text = unicodedata.normalize("NFKC", text)
        text = re.sub(r"\n\s*\n", "\n", text)

        return text[:self.max_length]