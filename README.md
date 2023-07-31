This web application aims to satisfy such demands:

- Local network with no Internet connection, but lack of ***a light-weight tool*** to communicate online.
- Unwilling to transport messages through unprivate server, but only wish to enjoy communication service which can **easily deployed** on his own, with ***high-level security*** as well as ***fast speed***.

Based on these demands, **SecFlow** comes up.

# 1 About this project

This project is a web application which is intended to realize a safe chatroom, which is both easy to deploy and handy to use.

## 1.1 Technologies

|       Back-end        |      Front-end      |
| :-------------------: | :-----------------: |
|        Django         | Vue \| Element Plus |
|    SQLite \| Redis    |        Vuex         |
| Django REST framework |                     |
|          JWT          |                     |
|  Daphne \| Websocket  |                     |

## 1.2 Goals

This project is still under developing, and here are all to-dos I've planned.

- [x] Login/ Register
- [x] Logout
- [x] Inbox
- [x] Reminder
- [ ] Detailed personal bio
- [x] User search/ Add friend
- [x] Friend list
- [ ] Group search/ Group list
- [ ] Group list
- [x] Chatroom
- [ ] Cipher suite
- [ ] Square
- [x] Settings/ Account management

# 2 Running this project

## 2.1 Installing Dependencies

Installing `daphne` is a must, otherwise `python manage.py runserver` may not respond.

Run

```bash
pip install daphne
```

## 2.2 Running Django & Vue & Nginx separately

1. In `/CyberSpace/Backend` run

    ```bash
    python manage.py runserver
    ```

    If you come across error like `FoundError: No module named 'channels'`, you may use `pip install channels` to install such package.

2. In `/CyberSpace/Backend/Redis-x64-5.0.14.1` run

   ```bash
   .\redis-server.exe .\redis.windows.conf
   ```

3. In `/CyberSpace/Frontend/CyberSpace` run

   ```bash
   npm run build
   # or, for developing
   npm run dev
   ```

