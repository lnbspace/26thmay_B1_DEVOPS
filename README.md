# APache httpd with FROnt end and Backend python connection 

## python CGI 

<img src="cgi.png">

## apache httpd cgi location 

<img src="cgil.png">

## SHE bang code base

<img src="bang.png">

## After build docker image from dockerfile present in repo 

### creating container 

```
docker  run -itd --name project  -p 1234:80 -v /home/ubuntu/devops_project/webcode:/var/www/html   -v /home/ubuntu/devops_project/webbackend:/var/www/cgi-bin/   dockerashu/devops:projectv1
```
