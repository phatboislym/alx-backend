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
