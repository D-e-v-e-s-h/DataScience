import asyncio
from autogen_agentchat.agents import CodeExecutorAgent
# from autogen_agentchat.agents import assistant_agent
from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor
from autogen_agentchat.messages import TextMessage
from autogen_core import CancellationToken

async def main():
    docker = DockerCommandLineCodeExecutor(
        work_dir="/tmp",
        timeout=120
    )

    code_executor_agent = CodeExecutorAgent(
        name="CodeExecutorAgent",
        code_executor=docker
    )

    task=TextMessage(
        content= '''here is some code
``python
print('hello world')
````
    ''',
        source="user",
    )

    await docker.start()

    try:
        result = await code_executor_agent.on_messages(
            messages=[task],
            cancellation_token=CancellationToken()
        )
        print("Result is:", result)
    except Exception as e:
        print("Error occurred:", e)
    finally:
        await docker.stop()

if __name__ == "__main__":
    asyncio.run(main())