# RPC (Remote Procedure Call)

This implements socket communication between a server and client, allowing the client to call functions on the server.

## Features

- The server provides multiple functions and executes them based on client requests.
- The client connects to the server and sends requests specifying the function name and parameters.
- The server processes the request and sends the result back to the client.
- The client receives the response from the server and displays the result.
- The client continues to operate even if invalid input is provided, prompting the user for re-entry.

## Usage

1. Start the server:

   ```bash
   python3 server.py
   ```

2. In a separate terminal, run the client:

   ```bash
   node client.js
   ```

3. Enter the function name and parameters in the client to send requests to the server.
4. The server's response will be displayed in the client.
5. If invalid input is provided, an error message will be displayed, prompting for re-entry.
6. Enter "quit" in the client to end the connection.
7. Press Ctrl+C in the server terminal to stop the server.

## Available Functions

The server provides the following functions:

- `floor(x)`: Returns the largest integer less than or equal to x.
- `nroot(n, x)`: Calculates the nth root of x.
- `reverse(s)`: Returns the reverse of string s.
- `validAnagram(str1, str2)`: Determines if two strings str1 and str2 are anagrams.
- `sort(strArr)`: Returns a sorted version of the string array strArr.

## Communication Protocol

The client and server communicate using JSON. The request and response formats are as follows:

### Request
```json
{
  "method": "functionName",
  "params": [param1, param2, ...],
  "id": requestID
}
```

### Response
```json
{
  "result": resultValue,
  "result_type": resultType,
  "id": requestID
}
```

## Error Handling

- The client displays error messages for invalid input and prompts the user for re-entry.
- The server sends error messages to the client if an error occurs during function execution.

