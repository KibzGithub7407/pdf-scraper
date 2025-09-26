# PDF Scraper

A beginner-friendly web tool to scrape and extract text from all PDFs linked on a web page. Built with Flask (Python), deployed via GitHub Pages using GitHub Actions.

---

## 🚀 Features

- **Input a webpage URL** to search for PDFs
- **Extracts and displays text** from all found PDFs
- **Simple, scrollable interface**
- **Deploys automatically** to GitHub Pages

---

## 🛠️ Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/KibzGithub7407/pdf-scraper.git
   cd pdf-scraper
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run locally:**
   ```bash
   flask run
   ```
   Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.

---

## 🌐 Deploy to GitHub Pages

1. Push your code to GitHub.
2. GitHub Actions will build and deploy the static frontend to the `gh-pages` branch.
3. Enable GitHub Pages in your repo settings (select `gh-pages` branch as source).

> **Note:**  
> The backend (Flask) won't run on GitHub Pages—only the static frontend is deployed. For a live backend, deploy to a platform like Render, Heroku, or use GitHub Codespaces.

---

## 📄 File Structure

```
pdf-scraper/
│
├── app.py                  # Flask backend (PDF scraping logic)
├── freeze.py               # For static site generation
├── requirements.txt        # Python dependencies
├── static/
│   └── style.css           # Basic CSS styling
├── templates/
│   └── index.html          # Frontend form for URL input
├── .github/workflows/
│   └── deploy.yml          # GitHub Actions for auto-deployment
└── README.md               # Setup instructions
```

---

## ⚡ Customization

- Edit `static/style.css` to change the look and feel.
- The `/scrape` endpoint in `app.py` contains all scraping logic.
- Add more error handling or improve UI as needed.

---

## ❓ FAQ

**Q:** Can I scrape PDFs from any site?  
**A:** Most public sites, yes. Some sites may block bots or require authentication.

**Q:** Does this extract images or tables?  
**A:** No, only plain text is extracted from each PDF.

**Q:** Can I deploy the full backend to GitHub Pages?  
**A:** No—GitHub Pages only hosts static files. Deploy backend elsewhere for full functionality.

---

## 📬 Feedback

Open Issues or Pull Requests for bug reports, feature ideas, or contributions!
