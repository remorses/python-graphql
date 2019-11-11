FROM python:3.7.4-alpine

RUN apk update && apk add --no-cache build-base libffi-dev dumb-init cmake bison flex

WORKDIR /src

COPY requirements.txt /src/

RUN pip install -r requirements.txt

COPY . /src/


ENTRYPOINT ["dumb-init", "--", ""]
CMD ["python", "-m", "module"]

