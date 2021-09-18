FROM python:3

COPY . .

RUN pip install requests
RUN pip install lxml
RUN pip install bs4

CMD ["web_scraping.py"]

ENTRYPOINT ["python3"]