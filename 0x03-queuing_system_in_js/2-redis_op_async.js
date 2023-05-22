// redis client connects to a Redis server running on the default port
// it logs a message to the console to indicate the connection status

import redis from 'redis';
import { promisify } from 'util';

const redisClient = redis.createClient();

redisClient.on('connect', () => {
  console.log('Redis client connected to the server');
});

redisClient.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error.message}`);
});

// promisify the get and set methods
const getAsync = promisify(redisClient.get).bind(redisClient);
const setAsync = promisify(redisClient.set).bind(redisClient);

/* setNewSchool:
* it accepts two arguments schoolName, and value
* it should set in Redis the value for the key schoolName
* it should display a confirmation message using redis.print
*/
async function setNewSchool(schoolName, value) {
  try {
    await setAsync(schoolName, value);
    redis.print('Reply: OK');
  } catch (error) {
    console.error(error);
  }
}

/* displaySchoolValue:
* it accepts one argument schoolName
* it should log to the console the value for the key passed as argument
*/
async function displaySchoolValue(schoolName) {
  try {
    const value = await getAsync(schoolName);
    redis.print(value);
  } catch (error) {
    console.error(error);
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
