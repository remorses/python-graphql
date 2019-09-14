FROM python:3.7.2

RUN apt-get update && apt-get install -y dumb-init cmake bison flex git jq

WORKDIR /src

COPY requirements.txt /src/

RUN pip install -r requirements.txt

COPY . /src/


ENTRYPOINT ["dumb-init", "--", ""]
CMD ["python", "-m", "module"]

