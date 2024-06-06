chmod +x file.sh
docker-compose up -d --build
docker exec -it django /bin/sh
./manage.py startapp app_name

systemctl start docker

docker system prune -a --volumes