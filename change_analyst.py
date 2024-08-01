import json
from datetime import datetime
from openai import OpenAI
client = OpenAI()

with open('Sample_Input_IN.json', 'r') as file:
    file_content = file.read()

content = f"""
    You are an analyst of organizational and technological Change. Your job is to respond with a complete summary of Change impacts on the team to give specific targeted understanding of advantages, challenges, and risks.
    Begin by creating a New Team API which implements Change
    Identify the properties of the Impacted Team API that will need to change to accomplish the Change.
    Do not give a response unless you have created your own Team API implementing the Change.
    Response must be in valid JSON format.

    <Impacted Team API>
    {file_content}
    </Impacted Team API>
    
    <Response Format>
        New Team API: The New Team API
        Change Complexity Score: specify low, medium, or high complexity to implement the Change. Base the score on the number and type of differences between the Impacted Team API and the New Team API
        Challenges: compared to the current state, identify the reasons the Change is complex, expensive, or untenable. Includes specific risks identified by the Change that uniquely impact this team and how. Be as specific and complete as possible.
        Advantages: compared to the current state, identify the reasons why the Change is beneficial and positive, including how they align with the Impacted Team API's mission, values, and project goals. Be as specific and complete as possible.
        Change Impact Areas: compare the Impacted Team API to the New Team API. respond with the specific JSON keys that are affected by the Change and a summary of the change.
    </Response Format>
""".replace('\n', '').replace('    ', '')
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    response_format={ "type": "json_object" },
    messages=[
        {"role": "system", "content": content },
        # {"role": "user", "content": "You do not want to build with React Native anymore, the technology is a dead-end. Switch to using native iOS and Android technologies like ObjC and Java."}
        # {"role": "user", "content": "You are getting a new member on the team. They are a junior developer and will require a lot of assistance getting started in the codebase so they deliver features."}
        # {"role": "user", "content": "You will use Slack for your internal team communication."}
        # {"role": "user", "content": "Stop sharing content with others."}
        {"role": "user", "content": "No longer value being transparent in everything you do."}
    ]
)

# Analysis areas
# - Ethics and values
# - Project scope
# - 

content = json.dumps(json.loads(completion.choices[0].message.content), indent=2)
print(content)


base_string = "Sample_Analyst"
current_date = datetime.now()
formatted_datetime = current_date.strftime("%Y%m%d_%H%M%S")
filename = f"{base_string}_{formatted_datetime}.json"
with open(filename, 'w') as f:
    print(content, file=f)