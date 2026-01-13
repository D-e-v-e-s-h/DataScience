from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor
from config.constant import WORK_DIR, TIMEOUT

def get_docker_executor():
    '''function to get the docker command line code executor.
    This executor will run the code in a docker container
    '''
    docker_executor = DockerCommandLineCodeExecutor(
        work_dir=WORK_DIR,
        timeout=TIMEOUT
    )
    return docker_executor