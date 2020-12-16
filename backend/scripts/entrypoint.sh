#!/usr/bin/env bash

set -o errexit
set -o pipefail
cmd="$@"

function postgres_ready(){
python << END
import sys
import psycopg2
import environ

try:
    base = environ.Path(__file__) - 2
    env = environ.Env()
    env_file = '.env'
    if not env.str('ENV_PATH', '.env') == '.env':
        env_file = env.str('ENV_PATH', '.env') + env_file
    env.read_env(env_file=base(env_file))
    dbname = env.str('POSTGRES_DB')
    user = env.str('POSTGRES_USER')
    password = env.str('POSTGRES_PASSWORD')
    host = env.str('POSTGRES_HOST')
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=5432)
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}

until postgres_ready; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - continuing..."
exec $cmd
