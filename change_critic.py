import json
from datetime import datetime
from openai import OpenAI
client = OpenAI()

with open('Sample_Input.json', 'r') as file:
    file_content = file.read()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    response_format={ "type": "json_object" },
    messages=[
        {"role": "system", "content": f"""
            You are a critic of organizational and technological Change. Your job is to respond with a complete summary of Change impacts on the team to give specific targeted understanding of advantages, challenges, and risks.
            The Current Team API is in <Impacted Team API>
            If the user provides a proposed Change, identify the properties of the TeamAPI that will need to change to pivot to accomplish the new objective or outcome.
            Response must be in valid JSON format.
        
            <Impacted Team API>
            {file_content}
            </Impacted Team API>
            
            <Response Format>
                Impact Summary Score: the score from 0 to 10 that indicates the overall difficulty and risk of implementing the Change on the Impacted Team API.
                Challenges: the reasons the Change is complex, expensive, or untenable. Includes specific risks identified by the Change that uniquely impact this team and how. Be as specific and complete as possible.
                Advantages: the reason why the Change is beneficial and positive, including how they align with the Impacted Team API's mission, values, and project goals. Be as specific and complete as possible.
                Change Impact Areas: the list of Impacted Team API keys that are affected by the Change. Affects include expanded scope, resource changes, specification changes, artifact changes, implementation changes, execution changes, and other forms of technological and organizational change. Responses include a description of the impact.
            </Response Format>
        """},
        {"role": "user", "content": "You do not want to build with React Native anymore, the technology is a dead-end. Switch to using native iOS and Android technologies like ObjC and Java."}
        # {"role": "user", "content": "You are getting a new member on the team. They are a junior developer and will require a lot of assistance getting started in the codebase so they deliver features."}
    ]
)

content = json.dumps(json.loads(completion.choices[0].message.content), indent=2)
print(content)


# base_string = "Sample_Output"
# current_date = datetime.now()
# formatted_datetime = current_date.strftime("%Y%m%d_%H%M%S")
# filename = f"{base_string}_{formatted_datetime}.json"
# with open(filename, 'w') as f:
#     print(content, file=f)