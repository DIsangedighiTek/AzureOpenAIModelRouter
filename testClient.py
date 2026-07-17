import os
from openai import AzureOpenAI

endpoint = "https://all-open-ai-models.openai.azure.com/"
model_name = "model-router"
deployment = "open-ai-model-router-sandbox"

subscription_key = "`<your api-key>`"
api_version = "2024-12-01-preview"

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=subscription_key,
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "What is model routing in Azure OpenAI and how does it work?",
        }
    ],
    max_tokens=8192,
    temperature=0.7,
    top_p=0.95,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    model=deployment
)

print("Model chosen by the router: ", response.model)
print(response.choices[0].message.content)
