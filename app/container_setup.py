# app/container_setup.py
"""Module for setting up and managing containers using Podman."""

import subprocess
import json

class ContainerSetup:
    def __init__(self):
        # Initializes Podman configuration if needed
        pass

    def create_container(self, image_name, container_name=None):
        """
        Create a new container from an image using Podman.
        
        :param image_name: The name of the image to create container from.
        :param container_name: Optional custom name for the container.
        :return: ID of the created container.
        """
        # Generate a unique container name if not provided
        if container_name is None:
            container_name = f"container_{image_name.replace(':', '_')}"

        # Run Podman command to create a container
        try:
            result = subprocess.run(
                ["podman", "container", "create", "--name", container_name, image_name],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=True,
                text=True
            )
            container_id = result.stdout.strip()
            print(f"Container '{container_name}' with ID {container_id} created successfully.")
            return container_id
        except subprocess.CalledProcessError as e:
            print(f"Failed to create container: {e.stderr}")
            return None

    def list_containers(self):
        """
        List all containers using Podman.
        
        :return: A list of containers.
        """
        try:
            result = subprocess.run(
                ["podman", "container", "ls", "--format", "json"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=True,
                text=True
            )
            containers = json.loads(result.stdout)
            return containers
        except subprocess.CalledProcessError as e:
            print(f"Failed to list containers: {e.stderr}")
            return []

# Example usage:
if __name__ == "__main__":
    setup = ContainerSetup()
    new_container_id = setup.create_container("ubuntu:latest")
    if new_container_id:
        print(f"New Container ID: {new_container_id}")
        containers = setup.list_containers()
        for container in containers:
            print(f"Container ID: {container['Id']}, Name: {container['Names'][0]}, Image: {container['Image']}")


