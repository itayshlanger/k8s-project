# Use the official Nginx image from the Docker Hub
FROM nginx:alpine

# Set the working directory
WORKDIR /usr/share/nginx/html

# Copy the index.html file into the Nginx directory
COPY index.html .

# Expose port 80 to allow external traffic
EXPOSE 80

# The Nginx server will start automatically when the container runs
