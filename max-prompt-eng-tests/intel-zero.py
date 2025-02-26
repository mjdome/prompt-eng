##
## ZERO SHOT PROMPTING
##

from _pipeline import create_payload, model_req

#### (1) Adjust the inbounding  Prompt, simulating inbounding requests from users or other systems
MESSAGE = "Conduct a requirement analysis for an Intel AI PC SDK"

#### (2) Adjust the Prompt Engineering Technique to be applied, simulating Workflow Templates
PROMPT = MESSAGE 

#### (3) Configure the Model request, simulating Workflow Orchestration
# Documentation: https://github.com/ollama/ollama/blob/main/docs/api.md
payload = create_payload(target="ollama",
                         model="llama3.2:latest", 
                         prompt=PROMPT, 
                         temperature=1.0, 
                         num_ctx=5000, 
                         num_predict=5000)

### YOU DONT NEED TO CONFIGURE ANYTHING ELSE FROM THIS POINT
# Send out to the model
time, response = model_req(payload=payload)
print(response)
if time: print(f'Time taken: {time}s')
