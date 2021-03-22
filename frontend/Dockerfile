# BUILD

FROM node:latest as build

WORKDIR /app

COPY package*.json .

RUN yarn install

COPY . .

RUN yarn build


# RUN

FROM nginx:latest

WORKDIR /usr/share/nginx/html

COPY --from=build /app/dist .

EXPOSE 80

CMD [ "nginx", "-g", "daemon off;" ]