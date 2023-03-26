## GitHub API endpoint
api_url = 'https://api.github.com/repos/<username>/<repository>/readme'

## GitHub credentials
auth = ('<username>', '<personal_access_token>')

## Markdown content
markdown = """
## My Awesome Project

Welcome to my awesome project! This project is awesome because it does awesome things.

## Installation

To install this project, run the following command:

pip install my_awesome_project

## Usage

To use this project, simply import it in your Python code:

```python
import my_awesome_project

my_awesome_project.do_awesome_things()

## Contributing
If you'd like to contribute to this project, please fork the repository and submit a pull request. Thanks for your help!
"""

## Create payload for API request
payload = {
'message': 'Automatically generated README.md file',
'content': b64encode(markdown.encode()).decode()
}

## Create API request headers
headers = {
'Content-Type': 'application/json',
'Authorization': f'token {auth[1]}'
}

## Make API request to create README.md file
response = requests.put(api_url, data=json.dumps(payload), headers=headers)

## Check if API request was successful
if response.status_code == 201:
print('README.md file created successfully')
else:
print(f'Error creating README.md file: {response.json()["message"]}')
