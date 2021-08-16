# Octo Spork
This is the main microservice to the <b>Mogen</b> project


## How to contribute
* Fork and download the repository
* Copy the file **env-sample**, rename to **.env** and put your env variables
* Run
  * `docker exec <container_id> python manager.py db init`
  * `docker exec <container_id> python manager.py db migrate`
  * `docker exec <container_id> python manager.py db upgrade`
    
* Code and then open a PR ;)