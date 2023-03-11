
docker build -t invoice:dev .

docker run --rm -d --name invoice -p 80:80 invoice:dev