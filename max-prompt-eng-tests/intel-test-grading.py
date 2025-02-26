##
## Create three responses for AI PC SDK req analysis. Pretend explaining to 
## different audiences, 2nd grader, high school student, tech professional.
## Now use a model to critique each response and provide a score.
AUTHOR1 = "2nd grader"
AUTHOR2 = "high school student"
AUTHOR3 = "tech professional"

from _pipeline import create_payload, model_req

#### (1) Adjust the inbounding  Prompt, simulating inbounding requests from users or other systems
MESSAGE = "Conduct a requirement analysis for an Intel AI PC SDK. Pretend you are explaining it to a "

#### (2) Adjust the Prompt Engineering Technique to be applied, simulating Workflow Templates
PROMPT1 = MESSAGE + AUTHOR1 + "." 
PROMPT2 = MESSAGE + AUTHOR2 + "." 
PROMPT3 = MESSAGE + AUTHOR3 + "." 

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
                         prompt=PROMPT3, 
                         temperature=1.0, 
                         num_ctx=5000, 
                         num_predict=5000)

### YOU DONT NEED TO CONFIGURE ANYTHING ELSE FROM THIS POINT
# Send out to the model
time, response3 = model_req(payload=payload)
print(AUTHOR3, ": ", response3)
if time: print(f'Time taken: {time}s')


PROFMESSAGE = "You are a professor at leading AI software university. Your students were given an assignment to: Conduct a requirement analysis for an Intel AI PC SDK. You receive the following report and are to provide a score between 1 and 100 with 1 being a low score and 100 being perfect. Report: " 

#### (2) Adjust the Prompt Engineering Technique to be applied, simulating Workflow Templates
PROMPTA1 = PROFMESSAGE + response1 
PROMPTA2 = PROFMESSAGE + response2 
PROMPTA3 = PROFMESSAGE + response3 

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

