FROM rubydata/datascience-notebook

RUN pip install tqdm plotly line_profiler
RUN pip install jupyter jupyterhub ethercalc-python
RUN git clone https://github.com/yamryo/notebooks.git
ARG NB_USER=jovyan
ARG NB_UID=1000
ENV USER ${NB_USER}
ENV NB_UID ${NB_UID}
ENV HOME /home/${NB_USER}

# RUN adduser --disabled-password \
#    --gecos "Default user" \
#    --uid ${NB_UID} \
#    ${NB_USER}

COPY . ${HOME}
USER root
RUN chown -R ${NB_UID} ${HOME}
USER ${NB_USER}
