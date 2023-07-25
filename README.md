# 1 About this project

This project is a web application which is intended to realize a safe chatroom, which is both easy to deploy and handy to use.

## 1.1 Technologies

|    Back-end     |      Front-end      |
| :-------------: | :-----------------: |
|     Django      | Vue \| Element Plus |
| SQLite \| Redis |                     |

## 1.2 Goals

This project is still under developing, and here are all to-dos I've planned.

- [x] Login/ Register
- [ ] Logout
- [x] Inbox
- [x] Reminder
- [ ] Detailed personal bio
- [x] User search/ Add friend
- [x] Friend list
- [ ] Group search/ Group list
- [ ] Group list
- [ ] Chatroom
- [ ] Square
- [ ] Settings/ Account management

# 2 Running this project

1. In `/CyberSpace/Backend` run

    ```bash
    python manage.py runserver
    ```

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
   

