# Random Image Downloader
RandomImageDownloader is a Python script that allows you to download random images from the Internet. Easy to use and can be configured to download images from various sources.

## Installation
Install dependencies:

```bash
pip install requests
pip install beautifulsoup4
```

## Run the script:

```bash
python random_image_downloader.py
```

## Usage
The script by default sends a request to a page with images (replace the `base_url` in the code with your source), selects a random image and saves it to the `./images` directory under the name random_image.jpg.

You can configure the save path and source of the images in the script code.

```python
def download_random_image(save_path='./images'):
     #...
     # Change base_url to your image source
     base_url = 'https://example.com'
     #...
     # Change image_name if you want to save the image under a different name
     image_name = os.path.join(save_path, 'random_image.jpg')
     #...
```
    
## Notes
Be sure you have permission to use and download images from the source you choose.
Examples and comments in the code can help you better understand and customize the script to suit your needs.
Remember to maintain the code and update it according to changes in the image source structure.
