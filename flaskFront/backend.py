import requests
import os
 
def generate_animal_pictures():
    """
    Function to generate 100 animal pictures.
 
    This function uses the Unsplash API to fetch random animal pictures.
    It saves the pictures in a local directory named 'animal_pictures'.
 
    Returns:
    - None
 
    Raises:
    - requests.exceptions.RequestException:
        If there is an error while making the API request.
    """
 
    # Create a directory to store the animal pictures if it doesn't exist
    if not os.path.exists('animal_pictures'):
        os.makedirs('animal_pictures')
 
    # Fetch 100 random animal pictures from the Unsplash API
    for i in range(100):
        try:
            response = requests.get('https://source.unsplash.com/random/500x500', stream=True)
            response.raise_for_status()
 
            # Save the picture to the local directory
            with open(f'animal_pictures/animal_{i+1}.jpg', 'wb') as file:
                for chunk in response.iter_content(chunk_size=1024):
                    file.write(chunk)
 
            print(f"Animal picture {i+1} saved successfully.")
 
        except requests.exceptions.RequestException as e:
            print(f"Error while fetching animal picture {i+1}: {e}")
 
# Call the function to generate the animal pictures
generate_animal_pictures()
