import json
from openai import OpenAI
import requests

client = OpenAI()

def fetch_github_contents(owner, repo, path='', token=None) -> str:
    print('FETCHING', owner, repo, path)
    url = f"https://api.github.com/repos/{owner}/{repo}/contents"
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    
    if token:
        headers["Authorization"] = f"Bearer {token}"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return str(response)  # Return the response content as JSON
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"


# # Example usage
# owner = 'adamterlson'
# repo = 'cairn'
# # Call without token and path
# print(fetch_github_contents(owner, repo))
# # # Call with token but without path
# # token = '<YOUR-TOKEN>'
# # print(fetch_github_contents(owner, repo, token))
# # Call with token and path
# path = 'package.json'
# print(fetch_github_contents(owner, repo, None, path))


tools = [
    {
        "type": "function",
        "function": {
            "name": "fetch_github_contents",
            "description": "Gets the contents of a directory or file in a repository.",
            "parameters": {
                "type": "object",
                "properties": {
                    "owner": {
                        "type": "string",
                        "description": "The repository owner account."
                    },
                    "repo": {
                        "type": "string",
                        "description": "The name of the repository"
                    },
                    "path": {
                        "type": "string",
                        "description": "Include the path to get the contents of a single file"
                    }
                },
                "required": ["owner", "repo"],
                "additionalProperties": False
            }
        }
    }
]

messages = []
messages.append({"role": "system", "content": """
    You are a code repository dependency analyzer. Use the supplied tools to assist the user.
    A public github repository web URL format is https://github.com/{owner}/{repo}
"""})
messages.append({"role": "user", "content": "What file contains the dependencies for this repository? Return only the path of the file, e.g. 'package.json'. Repository URL: https://github.com/adamterlson/cairn"})

response = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=messages,
    tools=tools
)
response_message = response.choices[0].message 
messages.append(response_message)

tool_call = response_message.tool_calls[0]
if tool_call:
    tool_call_id = tool_call.id
    tool_function_name = tool_call.function.name
    tool_function_args = tool_call.function.arguments
    print('tools', tool_function_name)
    print('arguments', tool_function_args)
    if tool_function_name == "fetch_github_contents":
        result = fetch_github_contents(**json.loads(tool_function_args))
        messages.append({
            "role":"tool", 
            "tool_call_id":tool_call_id, 
            "name": tool_function_name, 
            "content":result
        })
        
        messages.append({
            "role":"user", 
            "content":"Get the contents of the dependencies file"
        })
        
        
        model_response_with_function_call = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            tools=tools
        )  # get a new response from the model where it can see the function response
        print(model_response_with_function_call.choices[0].message.content)
        print(model_response_with_function_call.choices[0].message.tool_calls)
else:
    print('No tool call')