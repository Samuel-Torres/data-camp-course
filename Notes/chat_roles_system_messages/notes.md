We've learned single turn tasks up to this point which includes:

1. Text Generation
2. Text Transformation
3. Classification (Sentiment Analysis)

Chat Completion allows multi-turn tasks like:

We've been using the User Role so far. But there are also System & Assistant roles. 

System role: controls the behavior of the assistant. 
User: Instructs Assistant. 
Assistant: Response to user instructions.

Example:

System Role: The assistant is a polite and professional customer service assistant. 

User: Inserts request to the assistant. 

Assistant: Responds to the user in the way the system instructs. 

Role is defined here:  

messages=[{"role": "system"
"content": "You are a Python programming tutor who speaks concisely."},
{"role": "user",
"content": "What is the difference between mutable and immutable objects?"}]

System Messages is where you can add gaurdrails and prevent misuse of the ai. 

System vs Assistant vs User: (Where is the best place to provide examples?)

System message: Ideal for specifying a specific output format needed & specific information needed.
System message is most ideal for gaurdrails. 

Assistant: Most ideal for "user"/"assistant" pair example message examples to show the ai how to continue
the conversation. 

User: Best for single turn tasks for providing context required. 
example: If you need the ai to create a new job advert then you need to provide an existing advert example.