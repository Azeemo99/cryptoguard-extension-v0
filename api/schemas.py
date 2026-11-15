from pydantic import BaseModel, Field

class PredictRequest(BaseModel):
    text:str = Field(
        min_length=1,
        max_length=2048,
        description="Text for classifying",
        example="Get free ETH at ETH.com!"
    )

class PredictResponse(BaseModel):
    is_phishing:bool = Field(description="True if given input is phishing")
    risk_level:str = Field(description="Describes how risky it is to act on message")
    confidence_score:float = Field(description="Exact score for how likely the message is phishing")


