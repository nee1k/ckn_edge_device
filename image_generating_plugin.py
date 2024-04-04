import requests
from PIL import Image
from io import BytesIO


def download_image(image_url, save_path):
    """
    Download an image from the internet and save it to a local file.

    Parameters:
    - image_url (str): The URL of the image to download.
    - save_path (str): The local path where the image should be saved.
    """
    try:
        # Send a GET request to the image URL
        response = requests.get(image_url)
        response.raise_for_status()  # Raise an error if the request failed

        # Open the image from the response's binary content
        image = Image.open(BytesIO(response.content))

        # Save the image to the specified path
        image.save(save_path)
        print(f"Image successfully downloaded and saved to {save_path}")
    except requests.RequestException as e:
        print(f"Failed to download the image: {e}")
    except IOError as e:
        print(f"Failed to save the image: {e}")


# if __name__ == '__main__':
#     image_url = "https://cdn.britannica.com/71/234471-050-093F4211/shiba-inu-dog-in-the-snow.jpg"
#     save_path = "/app/logs/animal_image.jpg"
#
#     download_image(image_url, save_path)
