FROM node:13.12.0-alpine AS build

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY history-service/. .

RUN npm install

CMD ["npm", "start"]
