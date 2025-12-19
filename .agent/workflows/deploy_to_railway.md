---
description: Simple one-page guide to deploying on Railway
---

# Deploy to Railway (Simple Guide)

Follow these 5 steps to get your portfolio live.

## 📋 Copy-Paste Details

| Setting | Backend Service 🐍 | Frontend Service 🟢 |
| :--- | :--- | :--- |
| **Root Directory** | `/portfolio_api` | `/frontend` |
| **Start Command** | `gunicorn portfolio_api.wsgi:application` | `npm run preview -- --host --port $PORT` |

---

## Step 1: Create Project
1. Go to [Railway Dashboard](https://railway.app/dashboard) > **New Project** > **Deploy from GitHub repo**.
2. Select your repository.

## Step 2: Set up Backend
1. Click the **new service** card.
2. **Settings** Tab > **Root Directory**: change to `/portfolio_api`.
3. **Variables** Tab > Add these:
   - `SECRET_KEY`: `any-random-text`
   - `DEBUG`: `False`
   - `ALLOWED_HOSTS`: `*`
4. **Database**: Right-click canvas > **New** > **Database** > **PostgreSQL**.
5. **Deploy**: Go to **Deployments** tab > **Redeploy** (if it failed earlier).

## Step 3: Set up Frontend
1. Click **New** > **GitHub Repo** > Select **same repository** again.
2. Click the **new service**.
3. **Settings** Tab > **Root Directory**: change to `/frontend`.
4. **Variables** Tab > Add `VITE_API_URL`.
   - *Value*: Get the **Public Domain** from your **Backend** service settings (e.g. `https://xxx.up.railway.app`).

## Step 4: Connect Them
1. Copy your **Frontend Public Domain** (e.g. `https://yyy.up.railway.app`).
2. Go to **Backend Service** > **Variables**.
3. Add `CSRF_TRUSTED_ORIGINS`: paste the frontend URL (start with `https://`).

## Step 5: Final Polish
1. Go to **Backend Service** > **Settings** > **Build Command**.
2. Enter: `python manage.py migrate`
3. Allow a few minutes for deployment to finish. **You are done!** 🚀
