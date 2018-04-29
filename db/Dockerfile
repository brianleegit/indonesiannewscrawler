FROM mongo:3.6

WORKDIR /data/db
ADD ./mongodb /data/db

expose 27017

ENTRYPOINT ['mongod --bind_ip_all']

CMD ["mongo"]
