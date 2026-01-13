import streamlit as st
from team.dsa_team import get_dsa_team_and_docker
from config.docker_utils import start_docker_container, stop_docker_container
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult
import asyncio




st.title("AlgoGenie - DSA Problem Solver")
st.write("Welcome to Algogenie! Here you can ask for answer of various DSA problem.")

task = st.text_input("Enter your DSA problem statement:")

async def run(team,docker,task):
    try:
        await start_docker_container(docker)
        async for message in team.run_stream(task=task):
            if isinstance(message, TextMessage):
                print(msg:= f"{message.source}: {message.content}")
                yield msg
            elif isinstance(message, TaskResult):
                print(msg:=f"Stop Reason: {message.stop_reason}")
                yield msg
        print("Task Completed.")
    except Exception as e:
        print(f"Error: {e}")
        yield f"Error: {e}"
    finally:
        await stop_docker_container(docker)

    print("Task completed.")

if st.button("RUN"):
    st.write("Running the task...")  

    team, docker = get_dsa_team_and_docker()


    async def collect_messages():
        async for msg in run(team,docker,task):
            if isinstance(msg, str):
                st.markdown(msg)
            elif isinstance(msg, TaskResult):
                st.markdown(f"Stop Reason: {msg.stop_reason}")

    asyncio.run(collect_messages())