# Template Replication Guide
Follow these steps to set up a new project using this template:


1. Install pipx globally (If not already installed):
    ```bash
    python -m pip install --user pipx
    pipx ensurepath
    ```

2. Install poetry globally (if it not already installed):
    ```bash    
    pipx install poetry
    pipx install cookiecutter
    ```

3. Make new project directory
    ```bash
    mkdir <dir_name>
    ```

4. Copy this template:
    ```bash
    cookiecutter https://github.com/AndyHenry93/cookiecutter_poetry_project
    ```

5. Initialize Poetry:
    ```bash
    poetry init
    ```

6. Add Dependencies
    ```bash
    poetry add <dependency_name> # runtime dependencies
    poetry add --dev pre-commit sphinx python-dotenv # dev dependencies
    ```

6. Install Dependencies
    ```bash
    poetry install
    ```

7. Essential setup for first use 
    -   Install Git 
        - sudo apt install git 
        - Configure Git 
            - git config --global user.name <name>
            - git config --global user.email <email>
            - git config --global core.editor "nano"
    -   Install precommit
        - precommit install
        
> **Note:** You may also want to install development dependencies such as `pre-commit` 
> for code formatting and hooks, and `Sphinx` for documentation.
 