# Building images from Docker Compose

This example shows the `build` capability of Docker-compose.

## Build it
```
docker-compose build
```
Open (cat) docker-compose.yaml.



## Start project and access web service
Up the project, just detached is alright.
```
docker-compose up -d
```

Now access port 5000

```bash
curl localhost:5000
```

Curl it a few times...


## Check ports on project services
```
docker-compose ps
```

Output should be similar to:
```
       Name                     Command               State           Ports          
------------------------------------------------------------------------------------
example002_redis_1   docker-entrypoint.sh redis ...   Up      6379/tcp               
example002_web_1     /bin/sh -c /usr/local/bin/ ...   Up      0.0.0.0:5000->5000/tcp 
```

* Is Redis exposed outside its network?


### Challenge: Scale web
Try scaling `web` service to 2 replicas. I double dare you... 
* What happens? Why?
* Can we change this behaviour? Is it worth it?


## Stop the project and then start it again
```
docker-compose stop
docker-compose start
```

Curl into the `web` service.
* Is it still counting? Did it restart?

## Down with the project... but...

Set the project down but remove also local images created at `build` time

```
docker-compose down --rmi local
```

## Turn it up and force building
Don't go detached.

```
docker-compose up --build
```
* Hit `^C` (or equivalent to send SIGINT to process) ONCE!
* Wait for it to stop
* «Up-buildit» again!! BUT do it **detached**

Now, was it any faster?

## What about that volume?
Is it storing anything? Not really. It's not modified at all by the software inside the container. It's just a mount example that may be useful for developers.

## Some Challenges
 
### see permissions on existing file
There is a file called `empty.file` in this source code, at directory `shared`.
* Find the file inside the container.
* What permissions does it have? Are the same as in the host?
* What about UID?
* What happens if you change permissions inside container to make it belong to `root`? Is it changed in host?
### Change the code...
Open `flask_test/entrypoint.py` and replace the `Hello, world. ....` with `Hello, visitor, ...`.

* Will image be rebuilt automatically?
* If not, will `docker-compose up` (no parameters) use the existing one?

Try!

### Question everything...
* Is this image really needing an `entrypoint` instead of a `cmd`?
* Is it alright to put stuff in the default folder? being it `/`?
* Is it better to run this as default user, `root` in this case, instead of using a different one inside the container?

### last task... Clean after yourself!!
Clean the mess you created on docker... if unsure... `prune` the `docker system`.
 

# EOF ;)
