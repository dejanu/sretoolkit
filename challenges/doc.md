1) You’re given a directory full of .log files. Your task is to write a Python script that:

Recursively scans a directory for .log files.
Parses each log file to count:
Total lines
Number of lines containing "ERROR"
Number of lines containing "WARNING"
Outputs a summary report to the terminal.
(Bonus) Accepts the directory path as a command-line argument.

2) Write a script to monitor a public API. Your task is to:

Make a GET request to a public API (e.g., https://api.coindesk.com/v1/bpi/currentprice.json)
Parse the JSON response
Extract and print:
Current Bitcoin price in USD
Time of last update
Handle errors (e.g., network issues, bad responses)

Make a GET request to https://api.open-meteo.com/v1/forecast?latitude=44.43&longitude=26.10&current_weather=true

Make a GET request to the Open-Meteo API
Parse the JSON response
Extract and print:
Temperature
Wind speed
Time of observation

Send a POST request with a JSON payload to https://httpbin.org/post

{
  "name": "Alice",
  "role": "SRE",
  "skills": ["Python", "Bash", "Monitoring"]
}

3) You're writing a script to simulate registering a new user to a service via an API. The API endpoint is: `https://httpbin.org/post`
Create a Python function that:
Accepts a username, email, and role:
```json
{
  "username": "alice",
  "email": "alice@example.com",
  "role": "SRE"
}
```
Sends a POST request with this data as a JSON payload
Print:
The status code
The echoed JSON response
Handle:
HTTP errors
Connection errors