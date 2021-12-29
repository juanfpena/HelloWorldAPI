# HelloWorldAPI

This program is made to be used in either a Mac or Linux based distro computer.

```
python -m pip install -r ./dependencies/requirements.txt
```

## Usage

This general usage is made to be used with the clientcode UI.

This repository contains the same backend developed under two different API frameworks. You can use any of them, as the frontend was tweaked to communicate with any of them. Make sure both ports 5000 and 8000 are free in your machine, or else this will raise issues.

### FastAPI

Run the following command located inside the fastapi/ folder.

```
python3 main.py
```

Then go to clientcode and read further instructions.

### Flask

Run the following command located inside the flask/ folder.

```
python3 app.py
```

Then go to clientcode and read further instructions.
