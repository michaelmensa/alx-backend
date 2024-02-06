import { createClient } from 'redis';

const client = createClient({
  url: 'redis://127.0.0.1:6380'
});

client.on('error', (err) => {
  console.log('Redis client not connected to the server', err)
});

client.on('connect', () => {
  console.log('Redis client connected to the server')
});

// client should subscribe to "holberton school" channel
client.subscribe('holberton school channel');

client.on('message', (channel, message) => {
  if (message === 'KILL_SERVER') {
    client.unsubscribe(channel);
    client.quit();
  }
  console.log(`${message}`);
});
