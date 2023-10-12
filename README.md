# celery-redis-upstash

##  Setup & Installation 
Create a virtual environment and install the dependencies:
```bash
$ python3 -m venv venv
$ source env/bin/activate

$ pip install -r requirements.txt
```


## Usage
On settings there's a variable `REDIS_URL` in the format of `os.getenv("REDIS_URL")`. This variable is used to connect to Redis. You can either set it as an environment variable or just replace it with your Redis URL. </br>
If you want to use Upstash Redis, you can create a free account and get the Redis URL from there. </br>
```bash
$ export REDIS_URL=<YOUR_REDIS_URL>
# or use any other way to set the environment variable
```

Spin up a new terminal and start the celery worker:
```bash
$ celery -A celery_redis worker --loglevel=info
```
Now start also a Django server:
```bash
$ python manage.py runserver
```

Send a task to celery worker by calling the endpoint `/trigger-task/` with a `GET` request from browser or with `curl`:

```bash
$ curl http://localhost:8000/trigger-task/
```
This will trigger a new task which will be stored in Upstash Redis. After that Celery will receive the task from Redis queue and it will execute it.
<br/>

Verify by looking the looks on the terminal where you started the celery worker:
```bash
[2023-10-12 20:04:30,499: INFO/MainProcess] mingle: searching for neighbors
[2023-10-12 20:04:31,970: INFO/MainProcess] mingle: all alone
[2023-10-12 20:04:32,677: INFO/MainProcess] celery@my-pc ready.
[2023-10-12 20:04:39,088: INFO/MainProcess] Task celery_redis.celery.reverse_and_sleep[7ec800a8-476b-4357-afbe-7d08824f63fc] received
[2023-10-12 20:04:49,324: INFO/ForkPoolWorker-16] Task celery_redis.celery.reverse_and_sleep[7ec800a8-476b-4357-afbe-7d08824f63fc] succeeded in 10.2348608289999s: '!yreleC ,olleH'
```

## What to do next?
Just expand the usage of the celery, define your tasks and keep doing amazing stuff :)

## Contact:
If you have any questions regarding the topic or anything else, feel free to reach to me on: </br>
* [LinkedIn](https://www.linkedin.com/in/valon-januzaj-b02692187/) </br>
* [Github](https://github.com/vjanz) </br>
* [Email](mailto:valon.januzaj98@gmail.com)

## References
* [Upstash Redis & Kafka](https://upstash.com/)
* [Redis](https://redis.io/)
* [Celery](https://docs.celeryq.dev/en/stable/getting-started/introduction.html)

## License
This project is licensed under the terms of the MIT license.


