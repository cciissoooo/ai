from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI()

# Define a simple user message to test the API
prompt = "Describe a sunset over the ocean"

# Get response with specific parameters
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.7,  # Controls response creativity
    max_tokens=100,   # Limits response length
    presence_penalty=0.6,  # Encourages new topics
    frequency_penalty=0.3  # Reduces repetition
)

# Process the response
reply = response.choices[0].message.content.strip()
print("Assistant:", reply)
