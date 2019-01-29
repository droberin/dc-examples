# Docker compose using env file

See `.env`'s file content in this folder. It is loaded automatically by docker-compose but not mapped to containers

* Vars defined in shell's environment on docker-compose execution will be inherit if requested from compose file
* Vars defined in `.env` file will only be mapped if relation is required

* Example: `MY_TEST_VAR` is defined in `.env` file but it will be only used because it is mapped in docker-compose.yaml to be known as `TEST_VAR` inside container
* Another example: `MY_SECOND_TEST` is defined in `.env` but not mapped on compose file.
* Third example: `MOST_IMPORTANT_KEY` is defined in `.env` and is requested by compose.

## see what would it happen instead of doing it first...

Back to `config` command.
```bash
docker-compose config
``` 

Output example:
```
networks: {}
services:
  api:
    entrypoint: sleep 1000
    environment:
      LANG: es_ES.UTF-8
      MOST_IMPORTANT_KEY: happiness
      NODE_ENV: production
      TEST_VAR: 0.0.1
    image: alpine
version: '3.0'
volumes: {}
```

## Test what happens if a key is mapped but not defined.
Try adding a variable called `FORCE`, no mapping, just adding it.
meaning adding an extra line in compose file like:
```
  - FORCE
```

* Is `config` command exiting with errors?

## Run the project
```
docker-compose up -d
```

## Check results
```
docker-compose exec api env
```

## Clean-up, a little
```
docker-compose down
```

# EOF ;)
