# Docker more Information 

##  Kernel Version 
<img src="k.png">

## image registry 

<img src="reg.png">

## Introduction to Docker hub 

<img src="dh.png">

### image pushing process

<img src="imgpush.png">

### image name reality 

<img src="imgname.png">

## commands to remove images and container 

```
 113  docker  ps  -a -q
  114  docker  rm  $(docker  ps  -a -q)
  115  docker  ps -a
  116  docker  images
  117  docker  rmi  d4ff818577bc
  118  docker  images
  
```

### steps to push docker image on docker hub 

```
ubuntu@ip-172-31-51-76:~$ docker  tag   ashuhttpd:v1   dockerashu/ashuhttpd:v1  
ubuntu@ip-172-31-51-76:~$ docker  images
REPOSITORY             TAG       IMAGE ID       CREATED        SIZE
dockerashu/ashuhttpd   v1        892e93144045   47 hours ago   252MB
ashuhttpd              v1        892e93144045   47 hours ago   252MB
ashupy                 v2        5d032bdd5dd0   2 days ago     886MB
ashupy                 v1        ac2a14093af5   2 days ago     141MB
ubuntu                 latest    9873176a8ff5   7 days ago     72.7MB
alpine                 latest    d4ff818577bc   9 days ago     5.6MB
python                 latest    5b3b4504ff1f   4 weeks ago    886MB
centos                 latest    300e315adb2f   6 months ago   209MB
ubuntu@ip-172-31-51-76:~$ docker  login -u dockerashu 
Password: 
WARNING! Your password will be stored unencrypted in /home/ubuntu/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded
ubuntu@ip-172-31-51-76:~$ docker  push dockerashu/ashuhttpd:v1 
The push refers to repository [docker.io/dockerashu/ashuhttpd]
17a393eda6af: Pushed 
d83e33d80f62: Pushed 
2653d992f4ef: Mounted from library/centos 
v1: digest: sha256:970f293f76ef3b8b4f1894716b79c4a1b0580e8059e51910d262d9c297cdf19f size: 948
ubuntu@ip-172-31-51-76:~$ docker  logout 
Removing login credentials for https://index.docker.io/v1/

```

### Introduction to docker compose 

<img src="compsoe.png">

### Installing docker compose on Ec2

```
ubuntu@ip-172-31-51-76:~/devops_project$ sudo apt  install docker-compose -y
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following additional packages will be installed:
  pigz python3-cached-property python3-docker python3-dockerpty python3-docopt python3-texttable python3-websocket
Recommended packages:
  docker.io
The following NEW packages will be installed:
  docker-compose pigz python3-ca
  
```

### Better to install latest version of docker compose 

[link](https://docs.docker.com/compose/install/)

```

ubuntu@ip-172-31-51-76:~/devops_project/compsoe_examples/example1$ sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/bin/docker-compose
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   633  100   633    0     0  21827      0 --:--:-- --:--:-- --:--:-- 21827
100 12.1M  100 12.1M    0     0  59.2M      0 --:--:-- --:--:-- --:--:-- 91.8M
ubuntu@ip-172-31-51-76:~/devops_project/compsoe_examples/example1$ sudo chmod +x  /usr/bin/docker-compose 
ubuntu@ip-172-31-51-76:~/devops_project/compsoe_examples/example1$ docker-compose  -v
docker-compose version 1.29.2, build 5becea4c
ubuntu@ip-172-31-51-76:~/devops_project/compsoe_examples/example1$ 

```

### Docker-compose commands 

```
buntu@ip-172-31-51-76:~/devops_project/compsoe_examples/example1$ 
ubuntu@ip-172-31-51-76:~/devops_project/compsoe_examples/example1$ docker-compose  images
Container   Repository    Tag       Image Id       Size  
---------------------------------------------------------
ashuc111    alpine       latest   d4ff818577bc   5.595 MB
ubuntu@ip-172-31-51-76:~/devops_project/compsoe_examples/example1$ docker-compose  ps
  Name         Command       State   Ports
------------------------------------------
ashuc111   ping google.com   Up           
ubuntu@ip-172-31-51-76:~/devops_project/compsoe_examples/example1$ docker-compose  stop
Stopping ashuc111 ... done
ubuntu@ip-172-31-51-76:~/devops_project/compsoe_examples/example1$ docker-compose  ps
  Name         Command        State     Ports
---------------------------------------------
ashuc111   ping google.com   Exit 137        
ubuntu@ip-172-31-51-76:~/devops_project/compsoe_examples/example1$ docker-compose  start
Starting ashuapp1 ... done
ubuntu@ip-172-31-51-76:~/devops_project/compsoe_examples/example1$ docker-compose  ps
  Name         Command       State   Ports
------------------------------------------
ashuc111   ping google.com   Up           

```
### more compose commands

```
 docker  exec -it  ashuc1  sh 
  108  cd compsoe_examples/example1/
  109  ls
  110  docker-compose  up -d
  111  docker-compose   ps
  112  docker-compose   stop
  113  docker-compose   ps
  114  docker-compose   start  ashuapp1
  115  history 
  116  docker-compose  ps
  117  docker-compose  stop  ashuapp1
  118  docker-compose  down
  
  ```
  
  

