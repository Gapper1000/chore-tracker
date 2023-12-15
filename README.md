# chore-tracker
Chore Tracker Freestyle Project OPAN-244

## Setup

Create and activate a virtual environment:

```sh
conda create -n freestyle-project-env python=3.10

conda activate freestyle-project-env
```

Create a ".env" file and paste in the following contents:

```sh
# this is the ".env" file...

SECRET_KEY = "example_secret_key"

```



Install Packages:
```sh
pip install -r requirements.txt
```

## Usage

Run the example script:

```sh
python app/login.py

python app/choreFileReader.py
```

File setup for choreFileReader.py:



## Testing

Run tests:

```sh
pytest
```

## Web APP

Run the web app (then view in the browser at http://localhost:5000/):

```sh
FLASK_APP=web_app flask run
```