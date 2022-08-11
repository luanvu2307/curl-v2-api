EXPOSE_PORT=2307 \
    CONTAINER_IMAGE=curl-impersonate \
    CONTAINER_NAME=curl-v2-api \
    docker-compose down --remove-orphans

# EXPOSE_PORT=2307 \
#    CONTAINER_IMAGE=curl-impersonate \
#    CONTAINER_NAME=curl-v2-api  \
#    docker-compose build --force-rm

# EXPOSE_PORT=2307 \
#     CONTAINER_IMAGE=curl-impersonate \
#     CONTAINER_NAME=curl-v2-api \
#     docker-compose up -d
