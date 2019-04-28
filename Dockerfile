FROM python:2.7
MAINTAINER "Frederick Ishimwe" <frederick1989@gmail.com>
RUN apt-get update -y && apt-get install nano
RUN pip install pytest
ENV PATH="/usr/local/bin:/usr/bin:/bin:/usr/bin/env:/app/tests:{$PATH}"
WORKDIR /app
COPY . .
WORKDIR /app/tests

CMD [ "pytest","-vv","run_test.py" ]