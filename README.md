# Robot Framework based test suite

## Before you start
First you need to install required packages with next command:
```
python -m pip install -r requirements.txt
```

After that be sure you have `chromedriver.exe` in your PATH directory.

## Test execution
To execute test scripts go to your tests directory and type in terminal:
```
robot --outputdir ../results --pythonpath ../resources <test_name>.robot
```