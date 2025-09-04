from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()

model=ChatOpenAI(model_name="gpt-3.5-turbo",temperature=0)

class Review(TypedDict):
    key_themes: Annotated[list[str],"list of key themes discussed in the review in a list"]
    sentiment: Annotated[Literal["pos","neg"],"return sentiment of the review either positive ,negative or neutral"]
    summary: Annotated[str,"a detailed summary of the review"]
    pros: Annotated[Optional[list[str]],"write down all the pros mentioned in the review in a list"]
    cons: Annotated[Optional[list[str]],"write down all the cons mentioned in the review in a list"]
    name: Annotated[Optional[str],"name of the reviewer if mentioned in the review"]

structured_model=model.with_structured_output(Review)


result=structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Reviewed by suman on August 15, 2025
""")

print(result)