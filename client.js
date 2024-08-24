const net = require('net');
const readline = require('readline');

function sendRequest(client, method, params, id) {
  return new Promise((resolve) => {
    const request = {
      method,
      params,
      id,
    };

    client.write(JSON.stringify(request));

    client.once('data', (data) => {
      const response = JSON.parse(data.toString());

      if (response.error) {
        console.error('Server error:', response.error);
      } else {
        console.log('Server response:', response);
      }

      resolve();
    });
  });
}

async function main() {
  const client = new net.Socket();

  client.connect(65432, 'localhost', async () => {
    console.log('Connected to server');

    const rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout,
    });

    while (true) {
      try {
        const functionName = await new Promise((resolve) => {
          rl.question('Enter function name (or "quit" to exit): ', resolve);
        });

        if (functionName === 'quit') {
          break;
        }

        const params = await new Promise((resolve) => {
          rl.question('Enter parameters (comma-separated): ', (input) => {
            try {
              resolve(input.split(',').map((param) => JSON.parse(param.trim())));
            } catch (error) {
              console.error('Invalid JSON input. Please try again.');
              console.error('SyntaxError:', error);
              resolve(null);
            }
          });
        });

        if (params !== null) {
          await sendRequest(client, functionName, params, 1);
        }
      } catch (error) {
        console.error('Error:', error);
      }
    }

    rl.close();
    client.end();
  });

  client.on('close', () => {
    console.log('Disconnected from server');
  });

  client.on('error', (error) => {
    console.error('Socket error:', error);
    client.destroy();
  });
}

main();