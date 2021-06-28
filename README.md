# Project flow 

## Working structure 

### portal access

<img src="web.png">

### Copy data into running container 

```
buntu@ip-172-31-51-76:~/devops_project/webcode$ docker  cp   index.html   webui:/var/www/html/
ubuntu@ip-172-31-51-76:~/devops_project/webcode$ docker  exec -it  webui bash 
[root@c1469785683c /]# cat  /var/www/html/index.html 
<!DOCTYPE html>
<html lang="en">
<head>
    <title>project</title>
</head>
<body>
    <h1> Welcome to HTML base Code</h1>
    
```

## VOlume sharing concept in docker container 

```
ubuntu@ip-172-31-51-76:~/devops_project/webcode$ pwd
/home/ubuntu/devops_project/webcode
ubuntu@ip-172-31-51-76:~/devops_project/webcode$ ls
index.html
ubuntu@ip-172-31-51-76:~/devops_project/webcode$ docker ps
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                                   NAMES
c1469785683c   892e93144045   "/bin/sh -c 'httpd -…"   13 minutes ago   Up 13 minutes   0.0.0.0:1234->80/tcp, :::1234->80/tcp   webui
ubuntu@ip-172-31-51-76:~/devops_project/webcode$ docker rm  webui -f
webui
ubuntu@ip-172-31-51-76:~/devops_project/webcode$ docker run -itd --name webui -p 1234:80  -v  /home/ubuntu/devops_project/webcode:/var/www/html/   892e93144045 
d2883aea1b563a23aa328770edfc6f4355fadff11a49a442989c68f931cb9b0c
ubuntu@ip-172-31-51-76:~/devops_project/webcode$ docker  ps
CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS         PORTS                                   NAMES
d2883aea1b56   892e93144045   "/bin/sh -c 'httpd -…"   4 seconds ago   Up 3 seconds   0.0.0.0:1234->80/tcp, :::1234->80/tcp   webui
ubuntu@ip-172-31-51-76:~/devops_pr

```


  
