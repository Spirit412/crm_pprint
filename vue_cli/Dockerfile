FROM node:15.10.0-alpine3.10 as build

ARG APP_DIR=app
WORKDIR /${APP_DIR}
ENV PATH /app/node_modules/.bin:$PATH

COPY package.json ./
RUN npm install npm@latest
RUN npm install   --no-progress --ignore-optional
RUN npm install @vue/cli -g

EXPOSE 5000

CMD ["npm", "run", "serve"]
