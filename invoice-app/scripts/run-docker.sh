
docker build -t invoice:dev .

docker run --rm --name -d invoice -p 80:80 invoice:dev