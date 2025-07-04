## 🐦 Twitter Complaint & Suggestion Analyzer (Django)
A web-based Tweet Analyzer built with Django and Python that analyzes tweets mentioning @chennaicorp, classifies them as Complaints or Suggestions, detects the language (Tamil or English), and categorizes complaints into specific civic issues (e.g., garbage, road, water, etc.).

### ✨ Features
🔍 Tweet Analysis
* Detects if a tweet is a Complaint, Suggestion, or General

* Auto-detects language (Tamil or English)

* Classifies complaints into categories:

   🚮 Garbage

   🚧 Road

   🚰 Water

   💡 Electricity

   🔊 Noise

   🐕 Stray Animals

   🧼 Public Toilet

   ⚙️ General

   💡 Explanation Logic
  
* Each tweet gets a smart explanation

* Explanation changes based on keywords and context


🌐 Language Detection
* Supports both Tamil and English tweets using langdetect

👥 User Interface

✅ Clean and responsive UI

✅ Tweet input with analyze and history buttons

✅ Result shows:

   * Tweet Language

   * Type of Tweet

   * Category

   * Explanation


📜 Analysis History
* Stores each tweet analysis in SQLite DB

* History page shows last analyzed tweets

* Includes option to download all results as CSV

### 🛠 Tech Stack

| Layer           | Tech Used                         |
|----------------|-----------------------------------|
| Backend         | Django (Python)                   |
| Frontend        | HTML, CSS (Poppins Font), Flexbox |
| Language Detection | `langdetect` (Python)         |
| Database        | SQLite                            |
| Version Control | Git + GitHub                      |


## 📸 Screenshots

### Home Page
![Image](output/Home_page.png)

---

### Tweet Input and Result Page
![Image](output/input_page.png)

---

### Complaint_output
![Image](output/complaint_output.png)

---

### Suggestion_output
![Image](output/suggestion_output.png)

---

### General_output
![Image](output/general_output.png)



