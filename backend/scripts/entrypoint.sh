#!/bin/sh

echo "Waiting for MongoDB..."

while ! nc -z $DB_HOST $DB_PORT; do
    sleep 0.1
done

echo "MongoDB started."

exec "$@"
