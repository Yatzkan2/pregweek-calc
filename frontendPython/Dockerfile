FROM python:3.10

WORKDIR /app

COPY . . 
 
RUN pip install -r reqs.txt

EXPOSE 8501

CMD ["streamlit", "run", "pregweek.py", "--server.port", "8501"]