## Сервис по сжатию сслылок 

### Запуск

Сборка образа
```bash
docker build -t shorten_url .     
```

### Запуск контейнера
```bash
docker run -i -p 8080:8080  -t shorten_url  
```

### Запуск с Docker-compose
```bash
docker-compose up -d  
```
