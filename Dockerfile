FROM python:3

COPY Basics/5.SMSCODE.py .
RUN pip install twilio

ENV ACCOUNT_SID=${{ secrets.ACCOUNT_SID}} AUTH_TOKEN=${{ secrets.AUTH_TOKEN }}

CMD ["python", "5.SMSCODE.py"]
