##
## 1. Create a prompt for a prompt for a requirements analysis of 
## an Intel AI PC SDK.
## 2. Use another model request to score the analysis and provide improvement feedback.
## 3. Prompt the model to take the current analysis and improve it
## based upon the feedback.
## 4. Continue repeating steps 2 and 3 until the score plateaus or goes down.
 
from _pipeline import create_payload, model_req

#### (1) Adjust the inbounding  Prompt, simulating inbounding requests from users or other systems
MESSAGE = "Provide a prompt that can be used to prompt for a good requirement analysis for an Intel AI PC SDK"

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

PROMPT2 = response

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
print(response2)
if time: print(f'Time taken: {time}s')


MESSAGE4 = "You are a professor at leading AI software university. Your students were given an assignment to: Conduct a requirement analysis for an Intel AI PC SDK. You receive the following report and are to provide a score between 1 and 100 with 1 being a low score and 100 being perfect. Also, provide feedback on good sections and improvement ideas. Report: " 

#### (2) Adjust the Prompt Engineering Technique to be applied, simulating Workflow Templates
PROMPT4 = MESSAGE4 + response2

#### (3) Configure the Model request, simulating Workflow Orchestration
# Documentation: https://github.com/ollama/ollama/blob/main/docs/api.md
payload = create_payload(target="ollama",
                         model="llama3.2:latest", 
                         prompt=PROMPT4, 
                         temperature=1.0, 
                         num_ctx=5000, 
                         num_predict=5000)

### YOU DONT NEED TO CONFIGURE ANYTHING ELSE FROM THIS POINT
# Send out to the model
time, response4 = model_req(payload=payload)
print("Score 1 : ", response4)
if time: print(f'Time taken: {time}s')


MESSAGE5 = "You were asked to Conduct a requirement analysis for an Intel AI PC SDK. You received feedback on good sections and improvement areas. Take your original analysis delimited by *ANALYSIS* and the feedback delimited by *FEEDBACK* and create a better requirement analysis." + " *ANALYSIS* " + response2 + " *ANALYSIS* " + " *FEEDBACK* " + response4 + " *FEEDBACK* "

#### (2) Adjust the Prompt Engineering Technique to be applied, simulating Workflow Templates
PROMPT5 = MESSAGE5

#### (3) Configure the Model request, simulating Workflow Orchestration
# Documentation: https://github.com/ollama/ollama/blob/main/docs/api.md
payload = create_payload(target="ollama",
                         model="llama3.2:latest", 
                         prompt=PROMPT5, 
                         temperature=1.0, 
                         num_ctx=5000, 
                         num_predict=5000)

### YOU DONT NEED TO CONFIGURE ANYTHING ELSE FROM THIS POINT
# Send out to the model
time, response5 = model_req(payload=payload)
print("Improve it : ", response5)
if time: print(f'Time taken: {time}s')

MESSAGE6 = "You are a professor at leading AI software university. Your students were given an assignment to: Conduct a requirement analysis for an Intel AI PC SDK. You receive the following report and are to provide a score between 1 and 100 with 1 being a low score and 100 being perfect. Report: " + response5

#### (2) Adjust the Prompt Engineering Technique to be applied, simulating Workflow Templates
PROMPT6 = MESSAGE6

#### (3) Configure the Model request, simulating Workflow Orchestration
# Documentation: https://github.com/ollama/ollama/blob/main/docs/api.md
payload = create_payload(target="ollama",
                         model="llama3.2:latest", 
                         prompt=PROMPT6, 
                         temperature=1.0, 
                         num_ctx=5000, 
                         num_predict=5000)

### YOU DONT NEED TO CONFIGURE ANYTHING ELSE FROM THIS POINT
# Send out to the model
time, response6 = model_req(payload=payload)
print("Improve 2 : ", response6)
if time: print(f'Time taken: {time}s')

MESSAGE7 = "You were asked to Conduct a requirement analysis for an Intel AI PC SDK. You received feedback on good sections and improvement areas. Take your original analysis delimited by *ANALYSIS* and the feedback delimited by *FEEDBACK* and create a better requirement analysis." + " *ANALYSIS* " + response5 + " *ANALYSIS* " + " *FEEDBACK* " + response6 + " *FEEDBACK* "

#### (2) Adjust the Prompt Engineering Technique to be applied, simulating Workflow Templates
PROMPT7 = MESSAGE7

#### (3) Configure the Model request, simulating Workflow Orchestration
# Documentation: https://github.com/ollama/ollama/blob/main/docs/api.md
payload = create_payload(target="ollama",
                         model="llama3.2:latest", 
                         prompt=PROMPT7, 
                         temperature=1.0, 
                         num_ctx=5000, 
                         num_predict=5000)

### YOU DONT NEED TO CONFIGURE ANYTHING ELSE FROM THIS POINT
# Send out to the model
time, response7 = model_req(payload=payload)
print("Improve it : ", response7)
if time: print(f'Time taken: {time}s')

MESSAGE8 = "You are a professor at leading AI software university. Your students were given an assignment to: Conduct a requirement analysis for an Intel AI PC SDK. You receive the following report and are to provide a score between 1 and 100 with 1 being a low score and 100 being perfect. Also, provide feedback on good sections and improvement ideas. Report: " 

#### (2) Adjust the Prompt Engineering Technique to be applied, simulating Workflow Templates
PROMPT8 = MESSAGE8 + response7

#### (3) Configure the Model request, simulating Workflow Orchestration
# Documentation: https://github.com/ollama/ollama/blob/main/docs/api.md
payload = create_payload(target="ollama",
                         model="llama3.2:latest", 
                         prompt=PROMPT8, 
                         temperature=1.0, 
                         num_ctx=5000, 
                         num_predict=5000)

### YOU DONT NEED TO CONFIGURE ANYTHING ELSE FROM THIS POINT
# Send out to the model
time, response9 = model_req(payload=payload)
print("Score 3: ", response9)
if time: print(f'Time taken: {time}s')
