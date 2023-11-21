import requests
import os
from flask import url_for
 
def generate_animal_pictures():
    image_urls = []
    image_dir = 'static/images'  # Define the directory path

    # Create a directory to store the animal pictures if it doesn't exist
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    # Fetch and save a certain number of random animal pictures
    for i in range(1):  # Reduced the number for demonstration purposes
        try:
            response = requests.get('https://source.unsplash.com/random/500x500', stream=True)
            response.raise_for_status()

            # Define the image path
            image_path = f'{image_dir}/animal_{i+1}.jpg'
            with open(image_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=1024):
                    file.write(chunk)
            
            # Generate the URL for the saved image
            image_urls.append(url_for('static', filename=f'images/animal_{i+1}.jpg'))

        except requests.exceptions.RequestException as e:
            print(f"Error while fetching animal picture {i+1}: {e}")

    return image_urls

