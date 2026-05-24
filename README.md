# Travel Planner ✈️

A sleek, beautiful travel planning and budget tracking web application built with **Flask** and styled with a vibrant, modern **Mango Popsicle** color palette.

---

## 🎨 Design Theme: Mango Popsicle
The application features a premium, summery, and warm user interface:
- **Primary / Mango Gold (`#f2b949`)**
- **Creamy Yellow (`#edd377`)**
- **Bright Lemon (`#f2e829`)**
- **Vibrant Orange / Accent (`#f27430`)**
- **Soft Cream Background (`#faf8f2` / `#fffcf4`)** with a blurred parallax background image on all core pages.
- **Material Icons** integrated seamlessly instead of standard emojis for interest selection checkbox inputs.

---

## 📁 Project Structure
```
travel-planner-flask/
├── app.py                  # Main Flask application logic & routing
├── requirements.txt        # Production dependencies (Flask & Gunicorn)
├── .gitignore              # Files excluded from version control
├── README.md               # Project documentation & deployment guide
├── static/
│   ├── style.css           # Global stylesheet with custom CSS variables
│   ├── homebg.jpg          # Background image
│   └── welcomebg.jpg       # Welcome background asset
└── templates/
    ├── welcome.html        # Welcome splash screen
    ├── index.html          # Trip planner generation form page
    ├── plan.html           # Generated itinerary detail page (supports PDF download)
    ├── budget.html         # Expense adder & budget tracking system
    ├── saved.html          # Saved itineraries dashboard
    ├── profile.html        # User activity and travel preferences page
    └── edit_profile.html   # Profile settings page
```

---

## 🚀 Local Installation & Run

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd travel-planner-flask
   ```

2. **Set up a virtual environment (recommended):**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the development server:**
   ```bash
   python app.py
   ```
   Open `http://127.0.0.1:5000` in your web browser.

---

## ☁️ Deployment on Render

This project is pre-configured for seamless deployment to **Render** as a Python Web Service.

### Deployment Checklist

1. **Push your code to GitHub or GitLab:**
   Ensure all changes (including `requirements.txt` and `.gitignore`) are committed and pushed to your remote repository.
   *Note: Local temporary database files (`plans.json`, `profile.json`, `saved_plans.json`) and compiled python cache files (`__pycache__/`) are excluded via `.gitignore` so they won't bloat your build.*

2. **Create a New Web Service on Render:**
   - Log in to your [Render Dashboard](https://dashboard.render.com).
   - Click **New +** and select **Web Service**.
   - Connect your GitHub/GitLab repository.

3. **Configure Web Service Settings:**
   - **Name:** `travel-planner` (or your preferred name)
   - **Region:** Choose a region close to your target audience.
   - **Branch:** `main` (or your default branch)
   - **Runtime:** `Python 3`
   - **Build Command:**
     ```bash
     pip install -r requirements.txt
     ```
   - **Start Command:**
     ```bash
     gunicorn app:app
     ```
     *(This runs the app in production mode using Gunicorn instead of Flask's dev server).*

4. **Select Plan:**
   Select the **Free** tier (or any suitable instance plan).

5. **Deploy!**
   Click **Deploy Web Service**. Render will build and deploy the app automatically.
