# Algorithm and Data Structure Search Engine

🚀 **Live Demo:** [The project is deployed here.](https://dsa-based-search-engine.onrender.com)

An efficient search engine dedicated to algorithms and data structure problems. Instantly find coding challenges and solutions using a relevance-ranked search process.

---

## 🚀 Introduction
This project provides a specialized search engine for algorithmic problems and data structures. It streamlines searching through an extensive collection, offering **fast, optimized access** to coding challenges useful for interview preparation and computer science study.

---

## 🏗 Project Architecture

### Core Components
- **Backend Server:** Node.js + Express.js  
- **Search Implementation:** TF-IDF (Term Frequency–Inverse Document Frequency)  
- **View Engine:** EJS (Embedded JavaScript Templating)  
- **Database:** File-based system of problem descriptions  

### File Structure
├── index.js # Main server file
├── package.json # Project dependencies
├── tf-idf.json # Search index data
├── idx_vec.json # Vector indexing
├── uniqueKeys.json # Unique identifiers
├── Database/ # Problem collection
├── public/ # Static assets
└── views/ # EJS templates

---

## ✨ Key Features

### 📚 Problem Database
- Rich, growing collection of algorithm challenges  
- Organized in a searchable, indexed text system  

### ⚡ Fast, Relevant Search
- TF-IDF–based ranking for precise results  
- Fast response with efficient text preprocessing  

---

## 🔍 Search Algorithm

The engine uses the **TF-IDF** algorithm:

\[
TF\text{-}IDF(t,d,D) = TF(t,d) \times IDF(t,D)
\]

Where:
- **t** → term  
- **d** → document  
- **D** → collection  
- **TF** → term frequency  
- **IDF** → inverse document frequency  

---

## 🛠 Usage

### 1. Install dependencies

npm install

2. Start the server
npm start
3. Access the dashboard

http://localhost:3000
📦 Dependencies
express – Web server framework

ejs – View templating

nodemon – Development server

wink-lemmatizer – Text processing

🔮 Future Enhancements
Advanced search filters

Problem difficulty ratings
