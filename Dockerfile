FROM python:3

COPY Basics/5.SMSCODE.py .
RUN pip install twilio

ENV ACCOUNT_SID=ACb01d3ccc58b1b0eff822c25c736fffbb AUTH_TOKEN=03178c2d5f8daceb8e5006c082f55ba9

CMD ["python", "5.SMSCODE.py"]
