import requests

class DownloadPDF:
    def __init__(self,url,filepath):
        self.url = url
        self.filepath = filepath
        self.download_pdf()

    def download_pdf(self):
        response = requests.get(self.url)
        print(response.status_code)
        if response.status_code == 200:
                if response.headers['content-type'] == 'application/pdf':
                    # Open the file in binary write mode ('wb') and write the content
                    with open(self.filepath, 'wb') as f:
                        f.write(response.content)
                    print("Successfully downloaded file.")
                else:
                    print("No pdf found.")
        else:
            print(f"Failed to download file. Status code: {response.status_code}")