# Flask implementation of API challenge

## Usage

Open up cli and run

```
python main.py
```

### Calculator

Open up cli and run

arg1 = first number
arg2 = second number
arg3 = operation to be made, select value from dict: 

{'summation': 'sum', 
'subtraction': 'sub', 
'multiplication': 'mul'
'division': 'div'}

```
curl --location --request PUT 'http://127.0.0.1:5000/services/calculator?a={arg1}&b={arg2}&operation={arg3}'
```

### Date-fmt

Open up cli and run

arg1 = date to modify
arg2 = days to add to date 1

```
curl --location --request PUT 'http://127.0.0.1:5000/services/calculator?date={arg1}&days={arg2}'
```
