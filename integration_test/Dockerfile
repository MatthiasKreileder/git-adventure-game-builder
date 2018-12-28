FROM python

RUN wget https://github.com/libgit2/libgit2/archive/v0.27.0.tar.gz \
    && tar xzf v0.27.0.tar.gz \
    && cd libgit2-0.27.0 \
    && apt-get update \
    && apt-get install -y cmake \
    && cmake . \
    && make \
    && make install \
    && ldconfig \
    && pip install pygit2