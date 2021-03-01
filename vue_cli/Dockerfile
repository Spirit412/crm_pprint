FROM node:lts-alpine3.13

ARG APP_DIR=app
WORKDIR /${APP_DIR}
ENV PATH /app/node_modules/.bin:$PATH

COPY package.json ./
RUN npm install --no-progress --ignore-optional
RUN npm install @vue/cli -g

EXPOSE 5000

CMD ["npm", "run", "serve"]
