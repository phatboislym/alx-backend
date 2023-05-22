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

/* createHash:
* it accepts three arguments: key, field and value
* it should set in Redis the key, field and value
* it should display a confirmation message using redis.print
*/
function createHash(key, field, value) {
  redisClient.hset(key, field, value, redis.print);
}

/* displayHash:
* it accepts one argument key
* it should log to the console the hash for the key passed as argument
*/
function displayHash(key) {
  redisClient.hgetall(key, (error, result) => {
    if (error) {
      console.error(error);
    } else {
      console.log(result);
    }
  });
}

createHash('HolbertonSchools', 'Portland', '50');
createHash('HolbertonSchools', 'Seattle', '80');
createHash('HolbertonSchools', 'New York', '20');
createHash('HolbertonSchools', 'Bogota', '20');
createHash('HolbertonSchools', 'Cali', '40');
createHash('HolbertonSchools', 'Paris', '2');
displayHash('HolbertonSchools');
