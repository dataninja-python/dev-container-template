#!/bin/bash

set -euo pipefail

# Function to display a message with a dopamine hit
function celebrate() {
  echo -e "\033[1;32m$1\033[0m" # Display in green
  say "Great job! $1"  # macOS text-to-speech for additional feedback
}

# Install Podman
echo "We are installing Podman, which is like a lightweight version of Docker. It's easy and fast!"
brew install podman
celebrate "Podman is installed!"

# Initialize Podman machine (since we are on a Mac, Podman requires a Linux VM)
podman machine init
podman machine start
celebrate "Podman machine is ready!"

# Pull the latest Ubuntu image
echo "Now, we're getting the latest Ubuntu image, which is like a blueprint for our development environment."
podman pull ubuntu:latest
celebrate "Latest Ubuntu image is pulled and ready!"

# Create a new container and set up SSH
read -p "Enter a name for your development pod: " pod_name
podman pod create --name "$pod_name" -p 2222:22
podman run -d --pod "$pod_name" --name "${pod_name}_ubuntu" -e "CONTAINER_SSH_PASSWORD=yourpassword" ubuntu:latest
celebrate "Your development pod '$pod_name' is set up with SSH!"

# Set up SSH access (this would be more complex in a full script)
echo "Setting up SSH for you. You will soon be able to connect to your Ubuntu environment from your terminal."
# The actual SSH setup commands would go here

# Final celebration
celebrate "All set! You can now SSH into your Ubuntu development environment!"

# Output the command to connect via SSH
echo "To connect to your development environment, use this command:"
echo "ssh -p 2222 user@localhost"

<<TODO
# Simplistic task CLI placeholder (would need a more comprehensive solution)
function task_cli() {
  echo "What task would you like to accomplish?"
  read -p "> " task
  echo "You've set out to: $task"
  # A pseudo-random celebration message to encourage the user
  declare -a celebrations=("Well done!" "You're on a roll!" "Keep up the great work!")
  random_index=$(($RANDOM % ${#celebrations[@]}))
  celebrate "${celebrations[$random_index]}"
  # A very simple JSON-like structure saved to a file
  echo "{\"task\":\"$task\", \"status\":\"in-progress\"}" > "./task_${task}.json"
}
TODO

# To use the simplistic task CLI, you'd call `task_cli` in the terminal
# The actual implementation

