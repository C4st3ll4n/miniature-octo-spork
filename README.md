# Octo Spork
This is the admin microservice to the <b>Mogen</b> project


## How to contribute
* Fork and download the repository
* Run
  * `docker exec <container_id> python manager.py db init`
  * `docker exec <container_id> python manager.py db migrate`
  * `docker exec <container_id> python manager.py db upgrade`
    
* Code and then open a PR ;)