import { createClient, print } from 'redis';

const client = createClient({
  url: 'redis://127.0.0.1:6380'
}).on('error', (err) => {
  console.log('Redis client not connected to the server:', err)
}).on('connect', () => {
  console.log('Redis client connected to the server')
});

// add setNewSchool that sets in Redis the value for key schoolName
function setNewSchool(schoolName, value) {
  client.SET(schoolName, value, print);
}

// add displaySchoolValue that logs to console the value for the key passed
function displaySchoolValue(schoolName) {
  client.GET(schoolName, (err, reply) => {
    console.log(reply);
  });
}

// tests
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
