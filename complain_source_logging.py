import requests
import json
import time
import os

# Set your OpenRouter API endpoint and key
api_url = "https://openrouter.ai/api/v1/chat/completions"  # Replace with actual endpoint

# Function to send a prompt to OpenRouter API
def get_openrouter_response(prompt):
    headers = {
        'Authorization': f'Bearer {os.env('API_KEY')}',
        'Content-Type': 'application/json'
    }
    
    data = {
        "model": "openai/gpt-4o",  # Specify the model you want to use
        "prompt": prompt,
        "max_tokens": 1000,  # Adjust response length
        "temperature": 0.7,  # Creativity level (adjust as needed)
    }

    try:
        # Send request to OpenRouter API
        response = requests.post(api_url, headers=headers, data=json.dumps(data))
        
        # Check if the response is successful
        if response.status_code == 200:
            result = response.json()
            return result['choices'][0]['text'].strip()
        else:
            return f"Error: {response.status_code} - {response.text}"

    except Exception as e:
        return f"An error occurred: {e}"


def check_n_call(location):
    second_prompt = open(r"combined_prompt.txt", "r")
    added_prompt = f"\nAnd my region is {location} ,also make sure to verify if these websites or apps are up and running and include twitter handles etc"
    final_prompt=second_prompt.read()+added_prompt
    fin_response = get_openrouter_response(final_prompt)
    return fin_response

