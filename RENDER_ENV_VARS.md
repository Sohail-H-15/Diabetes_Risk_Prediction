# Environment Variables for Render Deployment

## Required Environment Variables

### ✅ **FLASK_ENV** (Recommended)
- **Value:** `production`
- **Why:** Disables debug mode for security and performance
- **Required:** No, but highly recommended

---

## Optional Environment Variables

### **PYTHON_VERSION** (Optional)
- **Value:** `3.12.0` (or your preferred version)
- **Why:** Ensures consistent Python version
- **Note:** Can also be set in `render.yaml` (already configured)

---

## How to Set in Render

### Method 1: Via Render Dashboard (Easiest)

1. Go to your Render dashboard
2. Click on your web service
3. Go to **"Environment"** tab
4. Click **"Add Environment Variable"**
5. Add:
   - **Key:** `FLASK_ENV`
   - **Value:** `production`
6. Click **"Save Changes"**
7. Render will automatically redeploy

### Method 2: Via render.yaml (Already Configured)

The `render.yaml` file already includes Python version:
```yaml
envVars:
  - key: PYTHON_VERSION
    value: 3.12.0
```

You can add FLASK_ENV there too:
```yaml
envVars:
  - key: PYTHON_VERSION
    value: 3.12.0
  - key: FLASK_ENV
    value: production
```

---

## What Each Variable Does

### `FLASK_ENV=production`
- ✅ Disables debug mode (security)
- ✅ Disables auto-reloader (performance)
- ✅ Better error handling for production
- ✅ Prevents code execution in error pages

### `PORT` (Auto-set by Render)
- ✅ Automatically set by Render
- ❌ **Don't set this manually** - Render handles it

### `PYTHON_VERSION`
- ✅ Ensures consistent Python version
- ✅ Prevents version conflicts

---

## Summary

**Minimum Required:**
- None! The app will work without any environment variables.

**Recommended:**
- `FLASK_ENV=production` - Set this for security

**Already Handled:**
- `PORT` - Automatically set by Render
- `PYTHON_VERSION` - Already in render.yaml

---

## Quick Setup in Render

1. **Dashboard** → Your Service → **Environment** tab
2. Click **"Add Environment Variable"**
3. **Key:** `FLASK_ENV`
4. **Value:** `production`
5. **Save** → Auto-redeploys

That's it! 🎉

