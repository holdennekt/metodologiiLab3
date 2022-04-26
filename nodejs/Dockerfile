FROM node:16.14.2 as build

WORKDIR /app

COPY package*.json /app

RUN npm i

COPY . /app

FROM gcr.io/distroless/nodejs:16

COPY --from=build /app /app

WORKDIR /app

CMD ["index.js"]