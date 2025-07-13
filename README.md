# YoungWork :earth_asia:

YoungWork - это полнофункциональная платформа для поиска работы \
и трудоустройства, построенная на Django REST API + Vue.js \
Приложение позволяет работодателям создавать вакансии, а соискателям - размещать резюме и откликаться на вакансии.

🏗️ Архитектура проекта
Backend (Django): \
Django 5.0.3 + Django REST Framework
PostgreSQL база данных
JWT аутентификация (30 дней access, 180 дней refresh)
WebSocket для чата (Channels + Redis)
Webpack для сборки фронтенда
Frontend (Vue.js 2.7):
Vue 2.7.16 с Composition API
Vuex для управления состоянием
Vue Router для маршрутизации
Axios для HTTP запросов
Socket.io для WebSocket соединений
SCSS для стилизации

## Preview :desktop_computer:

![Young_work](https://i.ibb.co/jh1H3mk/image.png)

## General ⚙️

📦 Основные модули

|Модуль | Функциональность| \
|accounts | Пользователи, аутентификация, профили| \
|profiles |	Профили соискателей и работодателей| \
|jobs |	Вакансии, поиск работы| \
|resume |	Резюме соискателей| \
|chat	Real-time | чат между пользователями| \
|notification |	Система уведомлений| \
|favorites |	Избранные вакансии резюме| \
|response |	Отклики на вакансии|

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

Libraries for python can be installed from requirements.txt
Libraries for Vue can be installed "npm upgrade"
Command 'sh' can only be used in bash terminal

## 📊 Анализ веб-приложения YoungWork

### 🎯 **Общее описание**
**YoungWork** - это полнофункциональная платформа для поиска работы и трудоустройства, построенная на Django REST API + Vue.js. Приложение позволяет работодателям создавать вакансии, а соискателям - размещать резюме и откликаться на вакансии.

### 🏗️ **Архитектура проекта**

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

### ⚠️ **Проблемы и недостатки**

#### 🔴 **Критические проблемы безопасности:**
1. **SECRET_KEY в коде** - должен быть в переменных окружения
2. **DEBUG = True** в продакшене
3. **Пустые ALLOWED_HOSTS** в dev настройках
4. **AllowAny разрешения** по умолчанию
5. **Пароли БД в коде** - небезопасно

#### 🟡 **Архитектурные проблемы:**
1. **Дублирование данных** - контакты в User и Resume/Vacancies
2. **Отсутствие валидации** на фронтенде
3. **Нет rate limiting** для API
4. **Отсутствие логирования** ошибок
5. **Нет кэширования** для частых запросов

#### 🟠 **UX/UI проблемы:**
1. **Vue 2.7** - устаревшая версия
2. **Отсутствие PWA** возможностей
3. **Нет мобильной адаптации** (видно по структуре)
4. **Отсутствие тестов** (unit/integration)

### 💡 **Рекомендации по улучшению**

####  **Безопасность:**
```python
# 1. Создать .env файл
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')

# 2. Настроить CORS правильно
CORS_ALLOWED_ORIGINS = [
    'https://yourdomain.com',
    'https://www.yourdomain.com',
]

# 3. Добавить rate limiting
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/day',
        'user': '1000/day'
    }
}
```

#### ️ **Архитектура:**
```python
# 1. Добавить кэширование
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
    }
}

# 2. Настроить логирование
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
```

#### 🎨 **Frontend улучшения:**
```javascript
// 1. Обновить до Vue 3
// 2. Добавить TypeScript
// 3. Использовать Composition API
// 4. Добавить PWA
// 5. Улучшить мобильную адаптацию
```

#### 📊 **Производительность:**
1. **Добавить пагинацию** для всех списков
2. **Оптимизировать запросы** (select_related, prefetch_related)
3. **Добавить индексы** в базу данных
4. **Настроить CDN** для статических файлов
5. **Добавить мониторинг** (Sentry, New Relic)

####  **Тестирование:**
```python
# 1. Добавить unit тесты
# 2. Добавить integration тесты
# 3. Настроить CI/CD
# 4. Добавить code coverage
```

#### 🔍 **SEO и доступность:**
1. **Добавить мета-теги**
2. **Настроить sitemap.xml**
3. **Улучшить accessibility**
4. **Добавить structured data**

### 📈 **Потенциал для масштабирования**

Приложение имеет хорошую архитектурную основу для развития:
- **Микросервисная архитектура** (уже разделено на модули)
- **WebSocket поддержка** для real-time функций
- **REST API** для мобильных приложений
- **PostgreSQL** для сложных запросов

**YoungWork** - это качественный проект с современным стеком технологий, но требует серьезных улучшений в области безопасности и производительности для продакшена.
