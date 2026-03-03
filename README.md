

-Very first Install python in the system:
https://www.python.org/downloads/
-Check “Add Python to PATH”

-Check pip version, if not isntalled then follow chatgpt steps.

Things discussed in the video:
-Install UV (To install variaous dependencies for this project) instead of pip:

link for UV: and fllow the isntructions from the link:

https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqblpPSEs4dmV5U3FMR0gzYWFXbllBamhyMkJiQXxBQ3Jtc0tsLU9zX2MtNng3SkU1WEMwSUVTS1dBMEY3ei1LdjVSd085WlVMX2RnLVlid2tPMmdrSzNCUURDYUJlSjlDZk5JUlltUFk0ZkR2NWJVaGt6REJWUzFsajd5WFoxNmlucC1mNktEczJRYlZKT05wNVIySQ&q=https%3A%2F%2Fdocs.astral.sh%2Fuv%2Fgetting-started%2Finstallation%2F%23standalone-installer&v=XZdY15sHUa8
 
 This will initialize a new UV project inside of this particular directory 



How to run the program:

1. Create one Virtual Environment
2. Activate environment
3. Install all dependencies langchain_core.messages,langchain_ollama,langgraph.prebuilt
4. pip install langchain langgraph langchain-ollama
5. python A_OpenAIAgent.py command to run project



steps 

1. python -m venv .venv
2. .\.venv\Scripts\Activate
3. python -m pip install langchain langgraph langchain-ollama



starting step :
How to run the code and get the response:
---------------------------------->>>>>
PS G:\1.textToOpenAI> & g:\1.textToOpenAI\COPY1\.venv\Scripts\Activate.ps1
(.venv) PS G:\1.textToOpenAI> & g:\1.textToOpenAI\COPY1\.venv\Scripts\Activate.ps1
(.venv) PS G:\1.textToOpenAI> & G:\1.textToOpenAI\COPY1\.venv\Scripts\python.exe g:/1.textToOpenAI/COPY1/A_OpenAIAgent.py
G:\1.textToOpenAI\COPY1\.venv\Lib\site-packages\langchain_core\_api\deprecation.py:25: UserWarning: Core Pydantic V1 functionality isn't compatible with Python 3.14 or greater.
  from pydantic.v1.fields import FieldInfo as FieldInfoV1
g:\1.textToOpenAI\COPY1\A_OpenAIAgent.py:13: LangGraphDeprecatedSinceV10: create_react_agent has been moved to `langchain.agents`. Please update your import to `from langchain.agents import create_agent`. Deprecated in LangGraph V1.0 to be removed in V2.0.
  agent_executor = create_react_agent(model, tools)
🤏 Llama3.2 Ollama Assistant Ready
Type 'quit' to exit

You: hi

Assistant: How can I help you today?

----------------------------------------->>>>>