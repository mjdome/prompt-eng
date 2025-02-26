##
## Use zero shot, knowledge generate , and prompt for a prompt
## to create requirements and then grade each of them.
AUTHOR1 = "Zero shot"
AUTHOR2 = "Knowledge Generate"
AUTHOR3 = "Prompt for Prompt"

from _pipeline import create_payload, model_req

#### (1) Adjust the inbounding  Prompt, simulating inbounding requests from users or other systems
MESSAGE = "Conduct a requirement analysis for an Intel AI PC SDK"

MESSAGE2 = "You are a software strategist at Intel. You are tasked with Problem Identification and Solution Ideation that led to the desire to create an Intel AI PC SDK. Provide a 100 word summary of the Problem Identification and Solution Ideation and then conduct a requirement analysis for an Intel AI PC SDK"

MESSAGE3 = "Provide a prompt that can be used to prompt for a good requirement analysis for an Intel AI PC SDK"


#### (2) Adjust the Prompt Engineering Technique to be applied, simulating Workflow Templates
PROMPT1 = MESSAGE  
PROMPT2 = MESSAGE2  
PROMPT3a = MESSAGE3 

#### (3) Configure the Model request, simulating Workflow Orchestration
# Documentation: https://github.com/ollama/ollama/blob/main/docs/api.md
payload = create_payload(target="ollama",
                         model="llama3.2:latest", 
                         prompt=PROMPT1, 
                         temperature=1.0, 
                         num_ctx=5000, 
                         num_predict=5000)

### YOU DONT NEED TO CONFIGURE ANYTHING ELSE FROM THIS POINT
# Send out to the model
time, response1 = model_req(payload=payload)
print(AUTHOR1, ": ", response1)
if time: print(f'Time taken: {time}s')


#### (3) Configure the Model request, simulating Workflow Orchestration
# Documentation: https://github.com/ollama/ollama/blob/main/docs/api.md
payload = create_payload(target="ollama",
                         model="llama3.2:latest", 
                         prompt=PROMPT2, 
                         temperature=1.0, 
                         num_ctx=5000, 
                         num_predict=5000)

### YOU DONT NEED TO CONFIGURE ANYTHING ELSE FROM THIS POINT
# Send out to the model
time, response2 = model_req(payload=payload)
print(AUTHOR2, ": ", response2)
if time: print(f'Time taken: {time}s')

#### (3) Configure the Model request, simulating Workflow Orchestration
# Documentation: https://github.com/ollama/ollama/blob/main/docs/api.md
payload = create_payload(target="ollama",
                         model="llama3.2:latest", 
                         prompt=PROMPT3a, 
                         temperature=1.0, 
                         num_ctx=5000, 
                         num_predict=5000)

### YOU DONT NEED TO CONFIGURE ANYTHING ELSE FROM THIS POINT
# Send out to the model
time, response3a = model_req(payload=payload)
print(AUTHOR3, ": ", response3a)
if time: print(f'Time taken: {time}s')

PROMPT3b = response3a

#### (3) Configure the Model request, simulating Workflow Orchestration
# Documentation: https://github.com/ollama/ollama/blob/main/docs/api.md
payload = create_payload(target="ollama",
                         model="llama3.2:latest",
                         prompt=PROMPT3b,
                         temperature=1.0,
                         num_ctx=5000,
                         num_predict=5000)

### YOU DONT NEED TO CONFIGURE ANYTHING ELSE FROM THIS POINT
# Send out to the model
time, response3b = model_req(payload=payload)
print(response3b)
if time: print(f'Time taken: {time}s')


PROFMESSAGE = "You are a professor at leading AI software university. Your students were given an assignment to: Conduct a requirement analysis for an Intel AI PC SDK. You receive the following report and are to provide a score between 1 and 100 with 1 being a low score and 100 being perfect. Report: " 

#### (2) Adjust the Prompt Engineering Technique to be applied, simulating Workflow Templates
PROMPTA1 = PROFMESSAGE + response1 
PROMPTA2 = PROFMESSAGE + response2 
PROMPTA3 = PROFMESSAGE + response3b 

#### (3) Configure the Model request, simulating Workflow Orchestration
# Documentation: https://github.com/ollama/ollama/blob/main/docs/api.md
payload = create_payload(target="ollama",
                         model="llama3.2:latest", 
                         prompt=PROMPTA1, 
                         temperature=1.0, 
                         num_ctx=5000, 
                         num_predict=5000)

### YOU DONT NEED TO CONFIGURE ANYTHING ELSE FROM THIS POINT
# Send out to the model
time, profresponse1 = model_req(payload=payload)
print(AUTHOR1 + "score: ", profresponse1)
if time: print(f'Time taken: {time}s')

#### (3) Configure the Model request, simulating Workflow Orchestration
# Documentation: https://github.com/ollama/ollama/blob/main/docs/api.md
payload = create_payload(target="ollama",
                         model="llama3.2:latest", 
                         prompt=PROMPTA2, 
                         temperature=1.0, 
                         num_ctx=5000, 
                         num_predict=5000)

### YOU DONT NEED TO CONFIGURE ANYTHING ELSE FROM THIS POINT
# Send out to the model
time, profresponse2 = model_req(payload=payload)
print(AUTHOR2 + "score: ", profresponse2)
if time: print(f'Time taken: {time}s')

#### (3) Configure the Model request, simulating Workflow Orchestration
# Documentation: https://github.com/ollama/ollama/blob/main/docs/api.md
payload = create_payload(target="ollama",
                         model="llama3.2:latest", 
                         prompt=PROMPTA3, 
                         temperature=1.0, 
                         num_ctx=5000, 
                         num_predict=5000)

### YOU DONT NEED TO CONFIGURE ANYTHING ELSE FROM THIS POINT
# Send out to the model
time, profresponse3 = model_req(payload=payload)
print(AUTHOR3 + "score: ", profresponse3)
if time: print(f'Time taken: {time}s')

