// redis client connects to a Redis server running on the default port
// it logs a message to the console to indicate the connection status

import redis from 'redis';

const redisClient = redis.createClient();

redisClient.on('connect', () => {
  console.log('Redis client connected to the server');
});

redisClient.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error.message}`);
});

/** setNewSchool:
* it accepts two arguments schoolName, and value
* it should set in Redis the value for the key schoolName
* it should display a confirmation message using redis.print
*/
function setNewSchool(schoolName, value) {
  redisClient.set(schoolName, value, redis.print);
}

/** displaySchoolValue:
* it accepts one argument schoolName
* it should log to the console the value for the key passed as argument
*/
function displaySchoolValue(schoolName) {
  redisClient.get(schoolName, (error, response) => {
    if (error) {
      console.error(error);
    } else {
      redis.print(response);
    }
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
