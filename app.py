import streamlit as st
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from streamlit_ace import st_ace
import re

st.title('CP Homework Solver')
st.write('This is a simple web app that solves CP homework problems.')

# API Key input
api_key = st.sidebar.text_input("Enter API Key", type="password")

model_name = st.sidebar.selectbox("Select Open Source model", ["Deepseek-r1-distill-llama-70b"])
st.sidebar.write("Programming Language")
language = st.sidebar.selectbox("Select Programming Language", ["C", "python", "java", "c++"], index=0)

def generator(Cprompt, problem_statement): 
    prompt=ChatPromptTemplate.from_messages([
        ("system", Cprompt),
        MessagesPlaceholder(variable_name="messages")
    ])
      
    chain=prompt|model

    respone = chain.invoke({"messages":[HumanMessage(content=problem_statement)]})
    return response.content


def code(problem_statement):
    Cprompt = f"You are a student who solves Coding problems in {language} language. You have to solve a problem with two modules brute force and optimized approach approach in single programme. with proper modules and main function.you have to give just code no explantion, no comments is needed. and alaways start the coding part with ```c\n and end with \n```"
    solution = generator(Cprompt, problem_statement)

    cleaned_content = re.search(r'```c\n(.*?)\n```', solution, re.DOTALL).group(1) 

    with open("code.c", "w") as file:
        file.write(cleaned_content)
    
    st.code(cleaned_content, language=language)
    return cleaned_content

def complexity(cleaned_content):
    ComPrompt = f"You are a code analyzer who analyzes Coding problems codes in {language} language. You have to analyze the code and provide the time complexity of need modules by using some maths , text like for this part of loop N and overall n2 something like that."
    solution = generator(ComPrompt, cleaned_content)

    cleaned_content = re.sub(r'<think>.*?</think>', '', solution, flags=re.DOTALL)

    with open("complexity.txt", "w") as file:
        file.write(cleaned_content)

def testcases(code) :
    Tprompt = f"You are a code analyzer who analyzes Coding problems codes in {language} language and gives appropriate test cases to run programme and check it's proper functionality. You have to analyze the code and provide test cases in .md format tables having colums of sample inputs and other column of sample output."
    solution = generator(Tprompt, code)

    cleaned_content = re.sub(r'<think>.*?</think>', '', solution, flags=re.DOTALL)

    with open("testcase.md", "w") as file:
        file.write(cleaned_content)

if api_key:
    model = ChatGroq(model=model_name, groq_api_key=api_key)

    # Options
    st.sidebar.write("select your needs : ")
    option = st.sidebar.radio("Select your needs:", ["Generate Code", "Analyze Complexity", "Generate Test Cases"])

    # Problem input
    problem_statement = st.text_area("Enter your CP problem here:")

    if st.button("Solve"):
        if problem_statement:
            prompt = f"Problem:\n{problem_statement}\n\n"

            if option == "Generate Code":
                cleaned_code = code(problem_statement)
                complexity(cleaned_code)
                testcases(cleaned_code)

            elif option == "Analyze Complexity":
                cleaned_code = st.text_area("Enter your code here:")
                complexity(cleaned_code)
                cleaned_code = code(problem_statement)
                prompt += "Analyze the time and space complexity.\n"
            if testcases:
                prompt += "Provide sample test cases.\n"

            # Get response from model
            response = model.invoke(prompt)
            
            # Display output
            st.write("### Solution:")
            st.write(response)
        else:
            st.warning("Please enter a problem statement.")
else:
    st.warning("Enter a valid API Key to use the service.")
