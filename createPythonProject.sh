#!/bin/bash

# Define the structure of directories and files
DIRS=(
    "app"
    "tests"
    "scripts"
    "docs"
    "data"
)

FILES=(
    "app/__init__.py"
    "app/cli.py"
    "app/image_management.py"
    "app/container_setup.py"
    "app/security.py"
    "tests/__init__.py"
    "tests/test_image_management.py"
    "tests/test_container_setup.py"
    "tests/test_security.py"
    ".gitignore"
    "requirements.txt"
    "setup.py"
    "LICENSE"
    "README.md"
)

PYTHON_TEMPLATE='"""\nModule Docstring\n"""\n\ndef main():\n    """Main entry point of the application."""\n    pass\n\n\nif __name__ == "__main__":\n    main()\n'

# Function to create a directory if it doesn't exist
create_dir() {
    if [ ! -d "$1" ]; then
        mkdir "$1"
        echo "Created directory: $1"
    else
        echo "Directory already exists: $1"
    fi
}

# Function to create a file with basic Python template if it doesn't exist
create_file() {
    if [ ! -f "$1" ]; then
        if [[ "$1" == *.py ]]; then
            echo -e "$PYTHON_TEMPLATE" > "$1"
        else
            touch "$1"
        fi
        echo "Created file: $1"
    else
        echo "File already exists: $1"
    fi
}

# Create the directories
for dir in "${DIRS[@]}"; do
    create_dir "$dir"
done

# Create the files
for file in "${FILES[@]}"; do
    create_file "$file"
done

# Create the .gitignore content
echo '__pycache__/' > .gitignore
echo '*.pyc' >> .gitignore
echo '*.pyo' >> .gitignore
echo '*.env' >> .gitignore

# Create an example requirements.txt content
echo 'flask' > requirements.txt
echo 'requests' >> requirements.txt

# Create an example setup.py content
cat <<EOT > setup.py
from setuptools import setup, find_packages

setup(
    name='YourAppName',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # Add your project's dependencies here
        'flask',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'yourappname=app.cli:main',
        ],
    },
)
EOT

echo "Project structure setup complete."

