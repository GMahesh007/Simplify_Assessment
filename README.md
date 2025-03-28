# Simplify_Assessment

# FastAPI Chat Summarization

## 🚀 Overview
A FastAPI-based chat summarization system that stores user conversations, retrieves them, and generates AI-powered summaries using OpenAI’s LLM.

---

## 📌 Installation & Setup

### **1. Clone the Repository**
```sh
git clone <your-repo-url>
cd fastapi-chat-summarization
```

### **2. Create a Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate  # For Windows
```

### **3. Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4. Set Up the Database**
#### ✅ Option 1: MongoDB  
- Ensure MongoDB is installed and running locally or use a cloud database like MongoDB Atlas.
- Update `database.py` with your MongoDB connection string.

#### ✅ Option 2: PostgreSQL  
- Install PostgreSQL.
- Update `database.py` with PostgreSQL connection details.

### **5. Run the FastAPI Server**
```sh
uvicorn main:app --reload
```
- The API will be available at: **http://127.0.0.1:8000**.
- Open **http://127.0.0.1:8000/docs** to see interactive API documentation.

---

## 📌 API Documentation

### **1. Store Chat Message**
```http
POST /chats
```
**Request Body (JSON):**
```json
{
  "user_id": "123",
  "conversation_id": "conv_001",
  "message": "Hello, how are you?"
}
```
**Response:**
```json
{
  "message": "Chat stored successfully"
}
```

### **2. Retrieve Chat Messages**
```http
GET /chats/{conversation_id}
```
**Response:**
```json
[
  {
    "user_id": "123",
    "conversation_id": "conv_001",
    "message": "Hello, how are you?",
    "timestamp": "2025-03-28T12:00:00"
  }
]
```

### **3. Summarize Chat**
```http
POST /chats/summarize
```
**Request Body (JSON):**
```json
{
  "conversation_id": "conv_001"
}
```
**Response:**
```json
{
  "conversation_id": "conv_001",
  "summary": "User discussed general well-being."
}
```

---

## 📌 Deployment Instructions

### **1. Docker Deployment**
#### **Step 1: Build Docker Image**
```sh
docker build -t fastapi-chat .
```

#### **Step 2: Run Docker Container**
```sh
docker run -p 8000:8000 fastapi-chat
```

### **2. Deploy to Cloud**
#### ✅ **Using Render/Vercel**
- Push your code to GitHub.
- Connect the repo to **Render** or **Vercel**.
- Set up a **Python environment** and start the application with:
```sh
uvicorn main:app --host 0.0.0.0 --port 8000
```

#### ✅ **Deploying on AWS EC2**
- Launch an EC2 instance.
- Install Python & FastAPI:
```sh
sudo apt update
sudo apt install python3-pip
pip3 install fastapi uvicorn
```
- Run FastAPI:
```sh
uvicorn main:app --host 0.0.0.0 --port 8000
```

---

## 📌 Submission Instructions

1. Upload your project to **GitHub** (ensure README.md is included).
2. Test your API with **curl** or **Postman** to confirm it’s working.
3. Share the **GitHub link** or create a **ZIP file** of your project.
4. Submit your **README**, **API documentation**, and **deployment notes**.

---

## 📌 Technologies Used
- **FastAPI** – Web framework
- **MongoDB/PostgreSQL** – Database
- **OpenAI GPT** – Chat summarization
- **Docker** – Containerization
- **Uvicorn** – ASGI server

---

## 📌 Contributors
- **[Your Name]** – Developer
- **[Your Teammates]** – Contributors

---

## 📌 License
This project is licensed under the **MIT License**.

