import requests
import os

def download_file(url, file_name):
    try:
        response = requests.get(url, stream=True)  # Stream for larger files
        response.raise_for_status()  # Raise an error for bad responses

        # Check if the file already exists
        if os.path.exists(file_name):
            overwrite = input(f"'{file_name}' already exists. Overwrite? (y/n): ")
            if overwrite.lower() != 'y':
                print("Download canceled.")
                return
        
        # Open a local file in binary write mode and save the content
        with open(file_name, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):  # Write in chunks
                file.write(chunk)
        print(f"File '{file_name}' downloaded successfully.")
    
    except requests.exceptions.RequestException as e:
        print(f"Failed to download file: {e}")

# Example usage
if __name__ == "__main__":  # Corrected line
    url = 'https://img.freepik.com/premium-psd/color-wing-png-isolated-transparent-background_1034016-9965.jpg'
    file_name = 'manish.jpg'  # Added file extension for clarity
    download_file(url, file_name)
