## Install Dependencies

1. Install [Docker Desktop](https://docs.docker.com/desktop/install/mac-install/)
2. Install [VS Code](https://code.visualstudio.com/download)
3. Verify [Python](https://www.python.org/downloads/) installation: `python --version`. Should be Python 3.9.x or above. I am using Python 3.11.x for the workshop today

> Replace `python` with `python3` depending on how Python 3 is configured on your machine

4. Verify [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) is installed: `git --version`. [Github Desktop](https://desktop.github.com/) is a handy UI tool if you have trouble setting up `git` on the terminal
5. Clone the Github repo: [github.com/allentv/pycon2023-docker-desktop](https://github.com/allentv/pycon2023-docker-desktop)
6. Setup a new virtual environment: `python -m venv .venv` in the cloned folder
7. Activate virtual environment with `source ./.venv/bin/activate`. Your terminal prompt should be updated with `(.venv)` at the beginning
8. Install python packages: `pip install -r requirements.txt`

> Replace `pip` with `pip3` depending on how Python 3 is configured on your machine


<br>

## Windows Users

Use `powershell` for running all commands. Some of the above steps should be replaced by the below to work on `powershell`

1. Install [Docker Desktop](https://docs.docker.com/desktop/install/windows-install/)
7. Activate virtual environment with `.\.venv\bin\activate`. Your terminal prompt should be updated with `(.venv)` at the beginning
