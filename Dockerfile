FROM ubuntu:latest
# FROM node:16-alpine
LABEL authors="arctfx"


# Set working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package*.json ./
RUN npm install --production

# Copy the rest of the application code
COPY . .

# Expose the application port
EXPOSE 3000

# Start the application
CMD ["npm", "start"]
ENTRYPOINT ["top", "-b"]