# Real-Time Two-Client Chat App

This is a full-stack real-time chat application built using:

- **Next.js** — Frontend (React)
- **Express + Socket.IO** — Backend (WebSocket server)
- **Vercel** — For frontend deployment
- **Render** (or Fly.io) — For backend deployment

---

## Project Structure

```
chat-app/
├── frontend/              # Next.js app
│   ├── pages/
│   ├── package.json
│   └── ...
├── backend/               # Express + Socket.IO server
│   ├── index.js
│   ├── package.json
│   └── ...
├── README.md             
```

---

### Features

- Two-client real-time chat (no page refresh)
- Built-in message broadcasting via WebSockets
- Simple and clean chat UI
- Easy to deploy on free hosting services

---

## Usage

1. Open the deployed frontend in **two browser tabs**
2. Type a message and click **Send**
3. Messages appear in real-time in both tabs

---

## Tech Stack

| Tech        | Role               |
|-------------|--------------------|
| Next.js     | Frontend framework |
| React       | UI components      |
| Socket.IO   | WebSocket layer    |
| Express.js  | Backend server     |
| Vercel      | Frontend hosting   |
| Render      | Backend hosting    |
