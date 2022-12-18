import os
import openai

openai.api_key = "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"

prompt = "Write a tagline for an ice scream shop"

reponse = openai.Completion.create(
    engine = "text-davinci-002",
    prompt= prompt,
    temperature = 1
)

print(reponse)