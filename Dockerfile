#FROM python:3.7-slim
FROM jupyter/scipy-notebook:cf6258237ff9

# install the notebook package
RUN pip install --no-cache --upgrade pip && \
    pip install --no-cache notebook
##RUN git clone https://github.com/yamryo/notebooks.git

# create user with a home directory
ARG NB_USER=jovyan
ARG NB_UID=1000
ENV USER ${NB_USER}
ENV HOME /home/${NB_USER}

#RUN adduser --disabled-password \
#    --gecos "Default user" \
#    --uid ${NB_UID} \
#    ${NB_USER}

COPY . ${HOME}
USER root
RUN chown -R ${NB_UID} ${HOME}
WORKDIR ${HOME}
USER ${USER}
