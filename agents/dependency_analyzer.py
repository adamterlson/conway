import json
from openai import OpenAI
import requests

client = OpenAI()

def fetch_github_contents(owner, repo, path='', token=None) -> str:
    print('FETCHING', owner, repo, path)
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    
    if token:
        headers["Authorization"] = f"Bearer {token}"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return str(response.json())  # Return the response content as JSON
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

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

def callToolForMessage(res_msg):
    tool_call = res_msg.tool_calls[0]
    if not tool_call:
        return

    tool_call_id = tool_call.id
    tool_function_name = tool_call.function.name
    tool_function_args = tool_call.function.arguments

    if tool_function_name == "fetch_github_contents":
        result = fetch_github_contents(**json.loads(tool_function_args))
  
    return {
        "role":"tool", 
        "tool_call_id":tool_call_id, 
        "name": tool_function_name, 
        "content":result
    }

def checkRepoForDependency(repoPath, dependencyName):
    messages = []
    messages.append({"role": "system", "content": """
        You are an engineer whose job is to analyze code repository dependencies. Use the supplied tools to assist the user.
        A public github repository web URL format is https://github.com/{owner}/{repo}
    """})
    messages.append({"role": "user", "content": f"What are the files in the root folder of this repository? Repository URL:{repoPath}"})

    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=messages,
        tools=tools
    )
    response_message = response.choices[0].message 
    messages.append(response_message) #tool call
    responseMessage = callToolForMessage(response_message)
    messages.append(responseMessage) #tool response


    messages.append({
        "role":"user", 
        "content":"Get the contents of the file that contains a list of project dependencies."
    })

    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=messages,
        tools=tools
    )
    response_message = response.choices[0].message 
    messages.append(response_message) #tool call
    responseMessage = callToolForMessage(response_message)
    messages.append(responseMessage) #tool response


    # print("--------MESSAGES--------_")
    # for index, message in enumerate(messages):
    #     print(index)
    #     print(message)

    messages.append({
        "role":"user", 
        "content":f"Does the file list {dependencyName} as a dependency?"
    })

    model_response_final_call = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=tools
    )
    result = model_response_final_call.choices[0].message.content
    print(result)
    return result