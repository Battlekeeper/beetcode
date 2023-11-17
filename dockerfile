FROM alpine:latest


RUN mkdir "/app"
WORKDIR "/app"

COPY . .

RUN apk update && apk upgrade
RUN apk add nodejs npm
RUN apk add python3
RUN python -m ensurepip --upgrade

EXPOSE 3000 3001

RUN npm install
RUN npm run build

WORKDIR "/app/backend"
RUN pip3 install -r requirements.txt

WORKDIR "/app"
ENTRYPOINT ["sh", "start.sh"]