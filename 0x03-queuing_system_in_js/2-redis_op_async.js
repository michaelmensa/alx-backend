import { createClient, print } from 'redis';

import { promisify } from 'util';

const client = createClient({
  url: 'redis://127.0.0.1:6380'
}).on('error', (err) => {
  console.log('Redis client not connected to the server:', err)
}).on('connect', async () => {
  console.log('Redis client connected to the server')
  await main();
});

const getAsync = promisify(client.get).bind(client);

// add setNewSchool that sets in Redis the value for key schoolName
function setNewSchool(schoolName, value) {
  client.SET(schoolName, value, print);
}

// add displaySchoolValue that logs to console the value for the key passed
// modified function using promisify
async function displaySchoolValue(schoolName) {
  const value = await getAsync(schoolName);
  console.log(`${value}`);
}
// tests
async function main() {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
}
