FROM python:3.10
WORKDIR /code
COPY requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY . /code

#CMD echo ass
#CMD sleep 5 && alembic upgrade head
CMD uivcorn main:app --reload