FROM python
MAINTAINER ashutoshh@linux.com
RUN mkdir  /code
COPY hello.py /code/hello.py
WORKDIR /code
CMD ["python","hello.py"]
