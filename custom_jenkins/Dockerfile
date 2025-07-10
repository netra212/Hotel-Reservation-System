FROM jenkins/jenkins:lts

USER root

# Install Docker CLI (compatible with M1 Mac)
RUN apt-get update && \
    apt-get install -y apt-transport-https ca-certificates curl gnupg software-properties-common && \
    mkdir -m 0755 -p /etc/apt/keyrings && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg && \
    echo "deb [arch=arm64 signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian bullseye stable" > /etc/apt/sources.list.d/docker.list && \
    apt-get update && \
    apt-get install -y docker-ce-cli && \
    apt-get clean

# Add Jenkins user to Docker group
RUN groupadd -f docker && usermod -aG docker jenkins

# Create the Docker directory and volume for DinD
RUN mkdir -p /var/lib/docker
VOLUME /var/lib/docker

USER jenkins
