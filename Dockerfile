FROM python:3.6.1-alpine
RUN pip install flask
RUN pip install gunicorn
COPY ./demoAKS /app
WORKDIR /app 
EXPOSE 8080
RUN apk add --no-cache bash
RUN chmod +x entrypoint.sh
CMD ["/bin/bash","entrypoint.sh"]
