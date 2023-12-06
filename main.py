import os
import random
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def download_random_image(save_path='./images'):
     # Create a directory to save images if there is none
     if not os.path.exists(save_path):
         os.makedirs(save_path)

     # URL of the image source (you can replace it with another resource)
     base_url = 'https://example.com'
    
     # Send a request to a page with images
     response = requests.get(base_url)
     if response.status_code == 200:
         # Use BeautifulSoup to parse HTML
         soup = BeautifulSoup(response.text, 'html.parser')
        
         # Find all tags with images
         img_tags = soup.find_all('img')
        
         # Select a random image
         random_image = random.choice(img_tags)
        
         # Get the image URL
         image_url = urljoin(base_url, random_image['src'])
        
         # Send a request for an image
         image_response = requests.get(image_url)
         if image_response.status_code == 200:
             # Create a path to save the image
             image_name = os.path.join(save_path, 'random_image.jpg')
            
             # Save the image
             with open(image_name, 'wb') as f:
                 f.write(image_response.content)
            
             print(f'Image saved: {image_name}')
         else:
             print(f'Error loading image. Status code: {image_response.status_code}')
     else:
         print(f'Error when requesting page. Status code: {response.status_code}')

if __name__ == "__main__":
     download_random_image()
