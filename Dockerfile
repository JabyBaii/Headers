FROM python:3.10.12
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python3", "book_page.py"]
