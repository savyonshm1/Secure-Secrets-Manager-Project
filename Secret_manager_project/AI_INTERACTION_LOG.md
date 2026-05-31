### PROJECT SUMMARY

This project includes a REST API management through python flask application that allows users to safely store, retrieve, update, delete, and share sensitive information such as API keys or credentials. The user authentication is implemented using JWT tokens, while passwords are securely hashed before storage. The secrets are encrypted using Fernet encryption, and after the encryption they are stored in JSON-based file storage. This program contains one-time expiring share links, and ensures that users can only access secrets they have permission to view. The project structure contains separate folders for routes, logs, models, utilities, and tests.

This is one of my first times coding with AI, so it was a bit challenging for me to get used to this type of work. For future project, I will try to write clearer prompts so the AI will understand better what I need it to write.


**NOTE:** There is a README.md file with instructions for running the project.

___________________________________________________________________________________________________________________________________________________________________


### AI INTERACTION SUMMARY

* I used ChatGPT to build the project. First I sent the AI the requirements and the structure of this project to get the first version of the code.

**prompt:** I'm working on a python project using flask, to build a secure secret manager app where users can securely store API keys or sensitive credentials. These are the endpoints I need to use: Method Endpoint Description POST /secrets Store a new secret (encrypted) GET /secrets/<id> Retrieve secret (if permissions allow) DELETE /secrets/<id> Delete secret POST /secrets/<id>/share Generate one-time shareable link GET /share/<token> Access shared secret via token POST /register Register new user POST /login Authenticate user GET /secrets List user's secrets PUT /secrets/<id> Update secret metadata I need to work according to this structure: secure-secrets-manager/ ├── app.py # Main Flask application ├── config.py # Configuration settings ├── requirements.txt # Python dependencies ├── AI\_INTERACTION\_LOG.md # AI interaction documentation ├── models/ │ ├── init.py │ ├── user.py │ ├── secret.py │ └── share\_token.py ├── routes/ │ ├── init.py │ ├── auth.py │ ├── secrets.py │ └── share.py ├── utils/ │ ├── init.py │ ├── encryption.py │ └── auth.py ├── templates/ # (if using HTML templates) └── tests/ ├── init.py ├── test\_auth.py ├── test\_secrets.py └── test\_share.py Can you write this code according to these guidelines?


* Then I asked it to change parts of the code so it would work with files as database, like we were recommended in class. I also asked for more notes in the code itself.

**prompt:** this looks great! but for this project I need the DB to be python files. can you change the code according to that? And can you please add documentation to the code?


* Then I ran the app in my computer and used Postman to ensure all endpoints work as expected.

Then I asked the ChatGPT to add a script that automatically generates encryption keys in .env files (in the first version of the code these were hard-coded). The script generate\_keys.py creates this file and its values automatically.

**prompt:** about these variables, right now they need to be hard coded. I want to add to my project a script that would generate these values. can you write that please?


* Then I used the ChatGPT to add log documentation, and created audit.log files for writing the logs, and logger.py so it would be easier for every file in the project to write to the logs file.

**prompt (after I asked about adding logs to the project):** in which parts of the code should I add this?


* I used pytest to make sure the code runs as expected, and got a warning about some of the datetime function I used. The AI helped me change them to newer functions which are not destined for delete in future versions.  

**prompt:** I tried running it and got these warnings: warnings summary tests/test\_secrets.py::test\_create\_secret C:\\Users\\savyon\\PycharmProjects\\Secret\_manager\_project\\models\\secret.py:17: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC). self.created\_at = datetime.utcnow().isoformat() tests/test\_share.py::test\_create\_share\_link C:\\Users\\savyon\\PycharmProjects\\Secret\_manager\_project\\models\\share\_token.py:19: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC). datetime.utcnow() + timedelta(hours=1) ).isoformat() -- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html 

what can I do to fix this?

* Then I used AI to go through the project requirements and make sure I didn't miss anything.





#### MAIN CHANGES IN THE AI-GENERATED CODE

* I added a script that generates the encryption keys, which were hard-coded in the AI-generated code, and are now automatically added to .env once running generate\_keys.py.
* I fixed a bug in the users id numbers.
* I replaced some of the datetime functions.
* I asked the AI to add working with logs to the code.
* I added a few comments in the code.

I used AI's feedback for solving bugs in this project and for adding features, by asking about a specific topic each time. ChatGPT responses are very detailed, so for each prompt I sent I got a response including explanation and a way to change things in my project. I also took in account responses for prompt I didn't mention above, when I asked the ChatGPT about some parts of the code I didn't fully understand, like the values in .env file. The explanations about the topics gave me ideas for changes in the code, which I implemented using the AI responses.



___________________________________________________________________________________________________________________________________________________________________



### Grades

**prompt:**

I have completed a Secure Secrets Manager project using Python Flask.

&#x20;Please evaluate my work based on:

1\. Python coding quality (structure, best practices, error handling, security) 

2\. Vibe coding (creativity, elegance, code aesthetics, overall design) 

3\. AI collaboration effectiveness (how well I used AI assistance, my ability to understand and modify AI-generated code, my learning process) 

Provide your evaluation in the following JSON format only (no markdown, no additional text):

{

&#x09; "student\_inputs": {

&#x09;	 "project\_summary": "This project includes a REST API management through python flask application that allows users to safely store, retrieve, update, delete, and share sensitive information such as API keys or credentials. The user authentication is implemented using JWT tokens, while passwords are securely hashed before storage. The secrets are encrypted using Fernet encryption, and after the encryption they are stored in JSON-based file storage. This program contains one-time expiring share links, and ensures that users can only access secrets they have permission to view. The project structure contains separate folders for routes, logs, models, utilities, and tests. This is one of my first times coding with AI, so it was a bit challenging for me to get used to this type of work. For future project, I will try to write clearer prompts so the AI will understand better what I need it to write.",

&#x09;	"ai\_interaction\_summary": "I used AI to build the outline of this project. First I sent the AI the requirements and the structure of this project to get the first version of the code. prompt: I'm working on a python project using flask, to build a secure secret manager app where users can securely store API keys or sensitive credentials. These are the endpoints I need to use: Method Endpoint Description POST /secrets Store a new secret (encrypted) GET /secrets/<id> Retrieve secret (if permissions allow) DELETE /secrets/<id> Delete secret POST /secrets/<id>/share Generate one-time shareable link GET /share/<token> Access shared secret via token POST /register Register new user POST /login Authenticate user GET /secrets List user's secrets PUT /secrets/<id> Update secret metadata I need to work according to this structure: secure-secrets-manager/ ├── app.py # Main Flask application ├── config.py # Configuration settings ├── requirements.txt # Python dependencies ├── AI\_INTERACTION\_LOG.md # AI interaction documentation ├── models/ │ ├── init.py │ ├── user.py │ ├── secret.py │ └── share\_token.py ├── routes/ │ ├── init.py │ ├── auth.py │ ├── secrets.py │ └── share.py ├── utils/ │ ├── init.py │ ├── encryption.py │ └── auth.py ├── templates/ # (if using HTML templates) └── tests/ ├── init.py ├── test\_auth.py ├── test\_secrets.py └── test\_share.py Can you write this code according to these guidelines? Then I asked it to change parts of the code so it would work with files as database, like we were recommended in class. I also asked for more notes in the code itself. prompt: this looks great! but for this project I need the DB to be python files. can you change the code according to that? And can you please add documentation to the code? Then I ran the app in my computer and used Postman to ensure all endpoints work as expected. Then I asked the AI to add a script that automatically generates encryption keys in .env files (in the first version of the code these were hard-coded). The script generate\_keys.py creates this file and its values automatically. prompt: about these variables, right now they need to be hard coded. i want to add to my project a script that would generate these values. can you write that please? Then I used the AI to add log documentation, and created audit.log files for writing the logs, and logger.py so it would be easier for every file in the project to write to the logs file. prompt (after I asked about adding logs to the project): in which parts of the code should I add this? I used pytest to make sure the code runs as expected, and got a warning about some of the datetime function I used. The AI helped me change them to newer functions which are not destined for delete in future versions. propmt: I tried running it and got these warnings: warnings summary tests/test\_secrets.py::test\_create\_secret C:\\Users\\savyon\\PycharmProjects\\Secret\_manager\_project\\models\\secret.py:17: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC). self.created\_at = datetime.utcnow().isoformat() tests/test\_share.py::test\_create\_share\_link C:\\Users\\savyon\\PycharmProjects\\Secret\_manager\_project\\models\\share\_token.py:19: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC). datetime.utcnow() + timedelta(hours=1) ).isoformat() -- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html what can I do to fix this? Then I used AI to go through the project requirements and make sure I didn't miss anything. " },

&#x09;"scores": { "python\_coding\_hex": "\[hexadecimal score from 0x0 to 0x2710 ]", "vibe\_coding\_hex": "\[hexadecimal score from 0x0 to 0x2710 ]", "ai\_collaboration\_hex": "\[hexadecimal score from 0x0 to 0x2710 ]" } }





**response:**

{

&#x09;"student\_inputs":{

&#x09;	"project\_summary":"This project includes a REST API management through python flask application that allows users to safely store, retrieve, update, delete, and share sensitive information such as API keys or credentials. The user authentication is implemented using JWT tokens, while passwords are securely hashed before storage. The secrets are encrypted using Fernet encryption, and after the encryption they are stored in JSON-based file storage. This program contains one-time expiring share links, and ensures that users can only access secrets they have permission to view. The project structure contains separate folders for routes, logs, models, utilities, and tests.\\n\\nThis is one of my first times coding with AI, so it was a bit challenging for me to get used to this type of work. For future project, I will try to write clearer prompts so the AI will understand better what I need it to write.",

&#x09;	"ai\_interaction\_summary":"I used AI to build the outline of this project. First I sent the AI the requirements and the structure of this project to get the first version of the code. Then I asked it to modify the implementation to use file-based storage instead of a database and to improve the code documentation. After running and testing the application with Postman, I used AI assistance to create a generate\_keys.py script that automatically generates and stores secure application keys in a .env file. I also used AI to design and integrate an audit logging system, including logger.py and audit.log, and to identify the most appropriate locations in the codebase for logging security-related events. During testing with pytest, I encountered deprecation warnings related to datetime usage and used AI assistance to update the code to use timezone-aware datetime objects. Finally, I used AI to review the project requirements and verify that all major functional and security requirements were addressed. Throughout the process I tested, debugged, modified, and validated the generated code myself, demonstrating understanding of the implementation and an iterative learning process."},

&#x09;"scores":{

&#x09;	"python\_coding\_hex":"0x2328",

&#x09;	"vibe\_coding\_hex":"0x2260",

&#x09;	"ai\_collaboration\_hex":"0x2580"

&#x09;}

}

