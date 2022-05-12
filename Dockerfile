FROM continuumio/miniconda3
WORKDIR data

COPY dataframe /data/dataframe
COPY setup.py /data
COPY requirements-dev.txt /data
COPY requirements.txt /data
COPY tests /data/tests
COPY main.py /data

RUN pip install -e /data


ENTRYPOINT ["python", "main.py"]