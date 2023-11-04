# app/cli.py
"""Command Line Interface for the application."""

import argparse
from image_management import ImageManager
from container_setup import ContainerSetup
from security import SecurityManager

def search_and_select_image():
    """Search images and let the user select one to pull."""
    search_term = input("Enter search term for images: ")
    manager = ImageManager()
    images = manager.search_images(search_term)
    
    if not images:
        print("No images found.")
        return None
    
    for i, image in enumerate(images, start=1):
        print(f"{i}. {image}")

    selection = input("Select an image to use (number): ")
    try:
        selected_image = images[int(selection) - 1]
    except (IndexError, ValueError):
        print("Invalid selection.")
        return None
    
    return selected_image

def pull_image(args):
    """Pull an image from a registry."""
    if args.search:
        image_name = search_and_select_image()
        if image_name is None:
            return  # Early exit if no image is selected or found
    else:
        image_name = args.image
    
    manager = ImageManager()
    manager.pull_image(image_name)
    print(f"Image {image_name} pulled successfully.")

def create_container(args):
    """Create a new container from an image."""
    if args.search:
        image_name = search_and_select_image()
        if image_name is None:
            return  # Early exit if no image is selected or found
    else:
        image_name = args.image
    
    setup = ContainerSetup()
    setup.create_container(image_name)
    print(f"Container created from image {image_name}.")

def setup_ssh(args):
    """Setup SSH for a container."""
    security = SecurityManager()
    security.setup_ssh(args.container_id)
    print(f"SSH setup for container {args.container_id}.")

def main():
    parser = argparse.ArgumentParser(description="Application CLI")
    subparsers = parser.add_subparsers(help="sub-command help")

    # Subcommand to pull an image
    parser_pull = subparsers.add_parser('pull', help='Pull an image')
    parser_pull.add_argument('image', nargs='?', help='Image name to pull', default=None)
    parser_pull.add_argument('--search', action='store_true', help='Search for an image to pull')
    parser_pull.set_defaults(func=pull_image)

    # Subcommand to create a container
    parser_create = subparsers.add_parser('create', help='Create a container')
    parser_create.add_argument('image', nargs='?', help='Image name to create container from', default=None)
    parser_create.add_argument('--search', action='store_true', help='Search for an image to create a container from')
    parser_create.set_defaults(func=create_container)

    # Subcommand to setup SSH
    parser_ssh = subparsers.add_parser('ssh', help='Setup SSH on a container')
    parser_ssh.add_argument('container_id', help='Container ID for SSH setup')
    parser_ssh.set_defaults(func=setup_ssh)

    # Parse the arguments
    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
