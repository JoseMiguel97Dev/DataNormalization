import os
import pandas as pd
import openai as OpenAI

#AI client configuration
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))