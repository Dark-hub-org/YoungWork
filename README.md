# YoungWork :earth_asia:

YoungWork - это полнофункциональная платформа для поиска работы \
и трудоустройства, построенная на Django REST API + Vue.js \
Приложение позволяет работодателям создавать вакансии, а соискателям - размещать резюме и откликаться на вакансии.

🏗️ Архитектура проекта 

**Backend (Django):**
- **Django 5.0.3** + Django REST Framework
- **PostgreSQL** база данных
- **JWT аутентификация** (30 дней access, 180 дней refresh)
- **WebSocket** для чата (Channels + Redis)
- **Webpack** для сборки фронтенда

**Frontend (Vue.js 2.7):**
- **Vue 2.7.16** с Composition API
- **Vuex** для управления состоянием
- **Vue Router** для маршрутизации
- **Axios** для HTTP запросов
- **Socket.io** для WebSocket соединений
- **SCSS** для стилизации

## Preview :desktop_computer:

![Young_work](https://i.ibb.co/jh1H3mk/image.png)

## General ⚙️

### 📦 **Основные модули**

| Модуль | Функциональность |
|--------|------------------|
| **accounts** | Пользователи, аутентификация, профили |
| **profiles** | Профили соискателей и работодателей |
| **jobs** | Вакансии, поиск работы |
| **resume** | Резюме соискателей |
| **chat** | Real-time чат между пользователями |
| **notification** | Система уведомлений |
| **favorites** | Избранные вакансии/резюме |
| **response** | Отклики на вакансии |

## Installation and launch ℹ️

1. Download repository
2. Install all required libraries for backend:
   - ``` virtual venv ```
   - ```venv/script/activate```
   - ``` pip install -r requirements.txt ```
   - ``` py manage.py makemigrations ```
   - ``` py manage.py migrate```
4. Follow the path YoungWork\frontend
5. Install all required libraries for frontend:
   a. ```npm upgrade```
6. In the terminal ```npm run build```
7. Go to root .\YoungWork\
8. In the terminal ```sh run.sh prod```

## Notes :bookmark_tabs:

### 🔐 **Модели данных**

**User (accounts):**
```python
```

**Applicant (profiles):**
```python
- OneToOne с User
- Портфолио (ManyToMany с изображениями)
- Счетчик резюме
- Массив откликов
```

**Employer (profiles):**
```python
- OneToOne с User
- Данные организации (название, ИНН, логотип)
- Статус проверки ИНН
- Достижения (ManyToMany с изображениями)
- Счетчик вакансий
```

**Vacancies (jobs):**
```python
- UUID primary key
- Описание вакансии (название, описание, задачи)
- Зарплата (мин/макс)
- Требования и опыт
- Тип занятости (ArrayField)
- График работы
- Локация (страна, регион, город)
```

**Resume (resume):**
```python
- UUID primary key
- Название резюме
- Зарплата
- Навыки и качества (ArrayField)
- Опыт работы
- О себе
- Контактные данные
```

### 🎯 **Ключевые функции**

1. **Двусторонняя регистрация** - работодатели и соискатели
2. **Создание и управление вакансиями**
3. **Создание и редактирование резюме**
4. **Система откликов** на вакансии
5. **Real-time чат** между пользователями
6. **Система уведомлений** для всех действий
7. **Избранное** - сохранение вакансий/резюме
8. **Переключение профилей** (работодатель ↔ соискатель)
9. **Валидация ИНН** для работодателей
10. **Поиск и фильтрация** вакансий/резюме


### 📈 **Потенциал для масштабирования**

Приложение имеет хорошую архитектурную основу для развития:
- **Микросервисная архитектура** (уже разделено на модули)
- **WebSocket поддержка** для real-time функций
- **REST API** для мобильных приложений
- **PostgreSQL** для сложных запросов

**YoungWork** - это качественный проект с современным стеком технологий, но требует серьезных улучшений в области безопасности и производительности для продакшена.
