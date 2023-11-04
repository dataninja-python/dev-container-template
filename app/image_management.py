# app/image_management.py
"""Module for managing container images using Podman."""

import subprocess
import json

class ImageManagement:
    def search_images(self, search_term):
        """
        Search for container images in registry using Podman.
        
        :param search_term: The search keyword for images.
        :return: List of found images.
        """
        try:
            result = subprocess.run(
                ["podman", "search", search_term, "--format", "json"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=True,
                text=True
            )
            images = json.loads(result.stdout)
            return images
        except subprocess.CalledProcessError as e:
            print(f"Failed to search images: {e.stderr}")
            return []

    def pull_image(self, image_name):
        """
        Pull container image using Podman.
        
        :param image_name: The name of the image to pull.
        """
        try:
            print(f"Pulling image {image_name}...")
            subprocess.run(
                ["podman", "pull", image_name],
                check=True,
                text=True
            )
            print(f"Image {image_name} pulled successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to pull image: {e.stderr}")

    def list_images(self):
        """
        List all local container images using Podman.
        
        :return: List of local images.
        """
        try:
            result = subprocess.run(
                ["podman", "images", "--format", "json"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=True,
                text=True
            )
            images = json.loads(result.stdout)
            return images
        except subprocess.CalledProcessError as e:
            print(f"Failed to list images: {e.stderr}")
            return []

# Example usage:
if __name__ == "__main__":
    manager = ImageManagement()
    search_results = manager.search_images("ubuntu")
    for image in search_results:
        print(f"{image['Name']}: {image['Description']}")

    if search_results:
        manager.pull_image(search_results[0]['Name'])

    local_images = manager.list_images()
    for image in local_images:
        print(f"{image['Repository']}: {image['Tag']}")

