FROM centos
# docker engine will pull image from docker hub
LABEL "author.name"="ashutoshh"
LABEL  "author.email"="ashutosh@linux.com"
LABEL  "author.contact"="9509957594"
RUN dnf  install httpd -y
# dnf / yum are same for installing httpd 
ADD  index.html  /var/www/html/index.html
# add is similar to COPY Instruction 
CMD httpd -DFOREGROUND 