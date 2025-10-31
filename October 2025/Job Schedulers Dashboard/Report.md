# Job Scheduler Dashboard  

A full-stack dashboard to schedule, monitor, and manage background jobs in real time.  

**Live Links:**  
- **Backend (API):** [Render](https://job-schedulers-dashboard.onrender.com)  
- **Frontend (Dashboard):** [Vercel](https://job-schedulers-dashboard.vercel.app/login)  

---

## Tech Stack  

**Backend:** Django, Django REST Framework, Celery, Redis, Channels, PostgreSQL  
**Frontend:** Next.js, Tailwind CSS, Axios, WebSockets  
**Deployment:** Render (API) · Vercel (UI)  

---

## Features  

- Job Management: Create, edit, delete, and schedule background jobs  
- Real-Time Monitoring: Live job updates via WebSockets  
- Analytics: Success and failure statistics with execution logs  
- Authentication: Secure multi-user access  
- Responsive UI: Modern dashboard with interactive charts and live progress  

---

## Workflow  

1. User schedules a job through the dashboard.  
2. The Django REST API adds the job to the Celery queue.  
3. Redis manages communication between Celery workers.  
4. Job progress updates are sent through Channels and WebSockets.  
5. The frontend dashboard displays live updates and analytics.  

---

## Summary  

The Job Scheduler Dashboard is a scalable and secure system for automated job scheduling and real-time monitoring. It combines a robust Django-Celery-Redis backend with a modern Next.js frontend to deliver an intuitive and efficient user experience.  
