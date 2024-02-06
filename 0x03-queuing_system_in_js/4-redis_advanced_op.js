import { createClient, print } from 'redis';

const client = createClient({
  url: 'redis://127.0.0.1:6380'
});

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err);
});

client.on('connect', () => {
  console.log('Redis client connected to the server')
  main();
});

function main() {
  const obj = {
    'Portland': 50,
    'Seattle': 80,
    'New York': 20,
    'Bogota': 20,
    'Cali': 40,
    'Paris': 2,
  };

  for (const [field, value] of Object.entries(obj)) {
    client.hset('HolbertonSchools', field, value, print);
  }

  client.hgetall('HolbertonSchools', (err, reply) => {
    console.log(reply);
  });
}
