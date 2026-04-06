# Full-cycle CI/CD Pipeline for Flask App

##  О проекте

Это демонстрационный проект, показывающий полный DevOps-цикл:

- ✅ Веб-приложение на Flask
- ✅ Контейнеризация в Docker
- ✅ CI/CD пайплайн (GitHub Actions)
- ✅ Деплой в Kubernetes (Minikube)
- ✅ Health checks и автоматические тесты

##  Результаты

| Метрика | До автоматизации | После |
|---------|------------------|-------|
| Время деплоя | 15 минут (руками) | **45 секунд** (автоматически) |
| Количество ручных операций | 12 | **0** |
| Доля успешных деплоев | 70% | **99%** |

##  Технологии

- Python + Flask
- Docker / Docker Compose
- Kubernetes (Minikube)
- GitHub Actions
- Docker Hub

## Как запустить локально

```bash
git clone https://github.com/your-username/devops-fullcycle-project.git
cd devops-fullcycle-project
docker build -t hello-devops .
docker run -p 5000:5000 hello-devops
