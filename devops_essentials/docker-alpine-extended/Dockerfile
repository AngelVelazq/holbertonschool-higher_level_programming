# Use the official Alpine base image
FROM alpine:latest

# Install curl
RUN apk add --no-cache curl

# Copy config.txt to /app/config.txt
COPY config.txt /app/config.txt

# Specify the command to run by default when the container starts
CMD ["echo", "Container setup complete!"]
