import json
import socket

def floor(x):
    return int(x)

def nroot(n, x):
    return x ** (1 / n)

def reverse(s):
    return s[::-1]

def validAnagram(str1, str2):
    return sorted(str1) == sorted(str2)

def sort(strArr):
    return sorted(strArr)

function_map = {
    'floor': floor,
    'nroot': nroot,
    'reverse': reverse,
    'validAnagram': validAnagram,
    'sort': sort
}

def handle_request(data):
    try:
        request = json.loads(data)
        method = request['method']
        params = request['params']
        id = request['id']

        if method not in function_map:
            response = {
                'error': f'Method "{method}" not found',
                'id': id
            }
        else:
            try:
                result = function_map[method](*params)
                response = {
                    'result': result,
                    'result_type': type(result).__name__,
                    'id': id
                }
            except Exception as e:
                response = {
                    'error': str(e),
                    'id': id
                }
    except json.JSONDecodeError:
        response = {
            'error': 'Invalid JSON format',
            'id': None
        }
    except KeyError:
        response = {
            'error': 'Missing required fields in JSON',
            'id': None
        }

    return json.dumps(response)

def handle_client(connection):
    while True:
        data = connection.recv(4096).decode('utf-8')
        if not data:
            break
        response = handle_request(data)
        connection.send(response.encode('utf-8'))
    connection.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 65432))
    server_socket.listen(1)
    print('Server is listening on port 65432')
    while True:
        connection, _ = server_socket.accept()
        handle_client(connection)

if __name__ == '__main__':
    main()