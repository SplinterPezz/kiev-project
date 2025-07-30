FROM node:14.9

# Create app directory
RUN mkdir -p /src/app
WORKDIR /src/app

# to make npm test run only once non-interactively
ENV CI=true

# Install app dependencies
COPY client/package.json /src/app/
RUN npm install && \
    npm install -g pushstate-server

# Bundle app source
COPY client/ /src/app

# Build and optimize react app
RUN npm run build

EXPOSE 3000

# defined in package.json
CMD [ "npm", "run", "start" ]