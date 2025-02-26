![GenI-Banner](https://github.com/genilab-fau/genial-fau.github.io/blob/8f1a2d3523f879e1082918c7bba19553cb6e7212/images/geni-lab-banner.png?raw=true)

# Automating the Grading of Prompt Output

This project explores the feasibility of employing Gen AI to critique prompt engineering techniques and improve prompt results for use in the domain of Software Requirements Analysis.

<!-- WHEN APPLICABLE, REMOVE THE COMMENT MARK AND COMPLETE
This is a response to the Assignment part of the COURSE.
-->

* Authors: [Max Domeika](https://github.com/mjdome/prompt-eng)
* Academic Supervisor: [Dr. Fernando Koch](http://www.fernandokoch.me)

The code to run the experiments are located in the directory, max-prompt-eng-tests. The output data of the experiments are located in the directory, max-prompt-eng-tests/data3.
  
# Research Question 

This research seeks to answer two questions. The first question is: Can Gen AI with confidence be relied upon to judge the quality of various prompt engineering techniques? The second question then asks: Can Gen AI be relied upon to improve the results of the prompt engineering techniques even further? We employ the research techniques on the task of generating a Software Requirements Analysis for a real world software development kit. Software Requirements Analysis is one step of the Software Development Lifecycle. 

## Arguments

#### What is already known about this topic

One of the primary goals of prompt engineering is to create a query of a Gen AI system that results in the highest quality answer. Multiple techniques have been devised to engineer prompts including the following which are summarized as: 
* Zero shot  - direct ask of the question with minimal extra context. [Wei et al. (2022)](https://arxiv.org/pdf/2109.01652)
* Knowledge prompting - provide context in terms of similar information, logic flow, and then ask the question [Liu et al. (2022)](https://arxiv.org/pdf/2110.08387)
* Prompt for a prompt (Meta Prompting) -  ask Gen AI to create an effective prompt which is then employed to ask the desired question [Reynolds and McDonell (2021)](https://arxiv.org/html/2406.06608v1#bib.bib233)

The [Prompt Engineering Guide](https://www.promptingguide.ai) provides a much more comprehensive summary of different prompting techniques. 

Feedback loop is a known method of refining a prompt's output by employing another Gen AI to play the role of evaluator and provide feedback used to improve the output. A recent paper by [Shumailov et al.(2023)](https://arxiv.org/pdf/2305.17493v2) discusses challenges of using a Gen AI evaluator to recursively train a model. 

#### What this research is exploring

<!-- Free-format; use the topics that are applicable to your exploration  -->

One key challenge in employing a feedback loop is having confidence that the Gen AI evaluator is actually competent and able to provide useful feedback. Colloquially, how do we know that a Gen AI evaluator is any good?

We will explore this challenge by verifying the effectiveness of a Gen AI evaluator on rating three prompt engineering techniques and their results on a hypothethical real world problem. We are constraining the feedback loop to the inferencing side of the model and therefore are avoiding the challenges (and potential benefits) of retraining a model.  

Our process employs having the Gen AI evaluator rate the output of three prompts that are the same except for the addition of differing output guidance of the form "Pretend you are explaining it to a SUBJECT", where SUBJECT is of different academic capabilities. 

The differing output is then rated by the Gen AI evaluator and checked to see if the ratings are inline with the expected output, e.g. the known academic capabilities. 

Once we have confidence in the ability of the Gen AI evaluator, the three prompt engineering techniques previously mentioned are evaluated to determine which scores the highest on creating the software analysis requirements. 

The research then explores the ability to feed the evaluation back into the Gen AI to improve the requirements analysis. A feedback loop is thus created: 
1. Prompt Gen AI to create analysis requirements
2. Prompt Gen AI to evaluate analysis requirements
3. Prompt Gen AI to employ the results of step 1 and 2 to further improve the analysis requirements

After every analysis requirements creation step, we employ the Gen AI evaluator to rate the output. The desired output would be a higher evaluation score than the previously generated analysis requirements.

#### Implications for practice

<!-- Free-format; use the topics that are applicable to your exploration  -->

The desired contribution of this research is initial confidence of employing Gen AI as an evaluator of prompting techniques in the task of generating software requirements analysis.  As a result, it will be easier to automate the process of prompt evaluation. As an additional benefit, the automation can also improve the results of the prompting technique.

# Research Method

The research is targeted at helping the process of employing Gen AI to create software requirements analysis. The specific software we are hypothetically developing is for an Intel AI PC SDK. We chose this specific software due to the author's expertise in the area; the author can gauge the quality of the output.

The research process is summarized by the following steps:
1. Create a set of test prompt output of known differential quality.
2. Employ a Gen AI evaluator to grade the set of test prompts from step 1. Determine if the ratings align with the known differential quality.
3. Create a set of test prompts for the task of software requirements analysis. Execute each test prompt and save the output.
4. Employ the Gen AI evaluator to grade the output of the test prompts from step 3. Answer research question 1. 
5. Create a new prompt combining the output of the highest rated test prompt and the Gen AI evaluator feedback from the previous step. Execute the new prompt.
6. Employ the Gen AI evaluator to grade the output from step 5. Answer research question 2.

The research is not exploring different parameters of Gen AI usage such as particular models, temperature settings, context settings, and num predictions. Instead, we empirically selected the following models/paramters and held them constant throughout the study:
* Model = llama 3.2 
* temperature = 1.0
* num_ctx = 5000
* num_predict = 5000

Each use of Gen AI on a specific prompt was executed 3 times recording the average score and highest score.

The following sections provide details on each of the research process steps.

### 1. Generate a set of test prompts

A set of test prompts are generated of the form:
*Conduct a requirements analysis for an Intel AI PC SDK. Pretend you are explaining it to a SUBJECT*
where *SUBJECT* is one of *2nd grader*, *high school student*, or *tech professional*. The expectation of the prompt output is to have a known ordering of the quality of the output from lower (2nd grader), to middle (high school student) to highest (tech professional). 

### 2. Grade the set of test prompts 

Gen AI was asked to grade the set of test prompts generated in step 1. The prompt employed is: *You are a professor at leading AI software university. Your students were given an assignment to: Conduct a requirement analysis for an Intel AI PC SDK. You receive the following report and are to provide a score between 1 and 100 with 1 being a low score and 100 being perfect. Report:*
Each prompt output from step 1 is appended to this new prompt and Gen AI executes each and provides a score. 
This step seeks to provide confidence in employing Gen AI as an evaluator because the relative scores of the three prompts from step 1 are known.

### 3. Create and execute a set of test prompts for software analysis requirements
In step 3, a set of prompts for the use cases is created and executed. The three prompt engineering techniques and the specific prompt using each technique are as follows:
* Zero shot - *Conduct a requirement analysis for an Intel AI PC SDK*
* Knowledge prompting - *You are a software strategist at Intel. You are tasked with Problem Identification and Solution Ideation that led to the desire to create an Intel AI PC SDK. Provide a 100 word summary of the Problem Identification and Solution Ideation and then conduct a requirement analysis for an Intel AI PC SDK*
* Prompt for a Prompt - *Provide a prompt that can be used to prompt for a good requirement analysis for an Intel AI PC SDK*

The prompt for a prompt technique required a second Gen AI execution for the generated prompt.

### 4. Grade the test prompts for software analysis requirements
The Gen AI prompt from step 2 is employed on the Gen AI output from step 3. We are rating the quality of output from each of the prompt engineering techniques. The results from step 4 provides an answer for Research question 1.

### 5. Create a new prompt 
The output of step 4 includes a rating as well as feedback on how to improve the output of the prompt. A new prompt is created of the form:
*You were asked to Conduct a requirement analysis for an Intel AI PC SDK. You received feedback on good sections and improvement areas. Take your original analysis delimited by *ANALYSIS* and the feedback delimited by *FEEDBACK* and create a better requirement analysis.*

The output of the highest rated prompting technique is appended and delimited by ANALYSIS. The grading feedback from step 4 is appended and delimited by FEEDBACK.

### 6. Grade 
The Gen AI evalatuor and prompt from step 2 is employed on the output of step 5. The desired outcome is for the score of the output to be higher than the score of output from step 4. This provides an answer for Research question 2.

<!-- WHEN APPLICABLE AND AVAILABLE -->

# Results

The following table lists the ratings of the prompt output from step 2. The prompts were executed 3 times and averaged. Highest score of each prompt technique is also listed.

| Subject | Average Score | Highest Score |
| --- | --- | --- |
| 2nd grader | 32.3 | 40 |
| High Schooler | 80.6 | 92 |
| Tech professional | 86.3 | 92 |

The results give confidence that a Gen AI evaluator can accurately score the quality of a prompt output. One of the scores from the high schooler prompt output was 92 which was equivalent to the highest score from the tech professional prompt output. This suggests that multiple executions should be employed and averaged as opposed to relying on a single execution.

The following table lists the ratings of the prompt output from step 4. The prompts were executed 3 times and averaged. Highest score is also listed.

| Prompt | Average Score | Highest Score |
| --- | --- | --- |
| Zero Shot | 87.3 | 92 |
| Knowledge | 88.6 | 92 |
| Prompt for Prompt | 94.0 | 95 |

The results indicate the most capable prompt technique for the use case is the Prompt for a Prompt technique with a score average of 94.0. The 2nd best prompt technique out of the 3 under study is the knowledge prompt. The zero shot prompt technique resulted in the lowest score. Research question 1 is answered by these results; there is evidence that a Gen AI evaluator can be employed to provide qualitative feedback on prompt output and because of the results from step 2, we have some confidence that the ratings are accurate.

The following table lists the ratings of the prompt output from the prompt for prompt technique and the rating after using the Gen AI evaluator feedback. The Improve 1 prompt is the first request to improve the prompt output using the Gen AI Evaluator feedback. The feedback process was repeated again and Improve 2 results reflect it.

| Prompt | Average Score | Highest Score |
| --- | --- | ---|
| Prompt for Prompt | 89.6 | 92 |
| Improve 1 | 92.0 | 92 |
| Improve 2 | 91.6 | 95 |

The results indicate that the feedback loop can improve the quality of the prompt output. The average score increased from 89.6 to 92.0 with the feedback loop Improve 1. The average score dropped to 91.6 by applying the second feedback loop Improve 2. The highest score out of the three runs was 95 for the Improve 2 iterations. These results suggest limitations on repeatedly apply a Gen AI evaluator to improve output, however more study is necessary.

# Further research

Future research could explore employing the Gen AI Evaluator on the result of the initial prompt in a Prompt for a Prompt technique.

Future research should include iterating the feedback loop to improe prompt output and observe the long term trajectory of the score. Does the score eventually reach an asymptote? Do the results eventually degrade?

Finally, a future research could explore integrating a Retrieval Augmented Generation (RAG) with context on the particular use case. For the specific use case under study relevant information from the Intel website on AI PC and Intel's software products could supplement the input context. 

# Make Your Case

Based upon the grading criteria, I would argue this work merits a grade of Exceptional. The research includes an analysis of behavior, performance, and effectivness of three different prompt engineering techniques. The Level-1 automation pertains to the ability to evaluate the quality of prompt engineering output using Gen AI. Te even better portion is the use of the Gen AI evaluator to improve the quality of the prompt output even further. Lastly, a draft of the research report is included. This work could be further refined to target submissino at NEURIPS 2025 (http://www.wikicfp.com/cfp/servlet/event.showcfp?eventid=182647&copyownerid=163282), due date May 1.
