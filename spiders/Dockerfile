FROM alpine:3.7

ENV ALPINE_VERSION=3.7

# Install needed packages. Notes:
#   * dumb-init: a proper init system for containers, to reap zombie children
#   * musl: standard C library
#   * lib6-compat: compatibility libraries for glibc
#   * linux-headers: commonly needed, and an unusual package name from Alpine.
#   * build-base: used so we include the basic development packages (gcc)
#   * bash: so we can access /bin/bash
#   * git: to ease up clones of repos
#   * ca-certificates: for SSL verification during Pip and easy_install
#   * python: the binaries themselves
#   * python-dev: are used for gevent e.g.
ENV PACKAGES=" \
  dumb-init \
  musl \
  libc6-compat \
  linux-headers \
  build-base \
  bash \
  git \
  ca-certificates \
  python3 \
  python3-dev \
  openssl-dev \
  libffi-dev \
  libxml2-dev libxslt-dev \
"

RUN echo \
  && echo "http://dl-cdn.alpinelinux.org/alpine/v$ALPINE_VERSION/testing" > /etc/apk/repositories \
  && echo "http://dl-cdn.alpinelinux.org/alpine/v$ALPINE_VERSION/community" >> /etc/apk/repositories \
  && echo "http://dl-cdn.alpinelinux.org/alpine/v$ALPINE_VERSION/main" >> /etc/apk/repositories \
  && apk add --no-cache $PACKAGES || (sed -i -e 's/dl-cdn/dl-4/g' /etc/apk/repositories && apk add --no-cache $PACKAGES) \
  && echo "http://dl-cdn.alpinelinux.org/alpine/v$ALPINE_VERSION/main/" > /etc/apk/repositories \
  && if [[ ! -e /usr/bin/python ]];        then ln -sf /usr/bin/python3 /usr/bin/python; fi \
  && if [[ ! -e /usr/bin/python-config ]]; then ln -sf /usr/bin/python3-config /usr/bin/python-config; fi \
  && if [[ ! -e /usr/bin/pydoc ]];         then ln -sf /usr/bin/pydoc3 /usr/bin/pydoc; fi \
  && if [[ ! -e /usr/bin/easy_install ]];  then ln -sf $(ls /usr/bin/easy_install*) /usr/bin/easy_install; fi \
  && easy_install pip \
  && pip install --upgrade pip \
  && if [[ ! -e /usr/bin/pip ]]; then ln -sf /usr/bin/pip3 /usr/bin/pip; fi


WORKDIR /app
ADD ./data /app
RUN pip install -r /app/requirements.txt
ENTRYPOINT ["/usr/bin/dumb-init"]

CMD ["python"]
