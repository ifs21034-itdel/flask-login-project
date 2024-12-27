# Flask Login Project

This project is a simple user login and authentication system built using Flask. It demonstrates basic user authentication and includes features like registering, logging in, and managing user sessions.

---

## **Features**

- User registration
- User login
- Password hashing with secure storage
- Session management

---

## **Technologies Used**

- **Backend:** Flask (Python)
- **Database:** MariaDB
- **Frontend:** HTML, CSS, Jinja2 Templates
- **Environment Management:** Docker, Docker Compose

---

## **Setup Instructions**

### **1. Clone the Repository**

```bash
git clone https://github.com/username/flask-login-project.git
cd flask-login-project
```

### **2. Create and Activate Virtual Environment**

Create a virtual environment to manage dependencies:

```bash
python -m venv .venv
```

Activate the environment:

- **Windows**:
  ```bash
  .venv\Scripts\activate
  ```
- **Mac/Linux**:
  ```bash
  source .venv/bin/activate
  ```

### **3. Install Dependencies**

Install required packages:

```bash
pip install -r requirements.txt
```

### **4. Set Up the Database**

Make sure MariaDB is running, then:

- Configure the database in the `.env` file (see the provided `.env.example`). Example:
  ```env
  DATABASE_URL=mysql://root:password@127.0.0.1:3308/sdlc_programmer
  ```
- Apply database migrations:
  ```bash
  flask db upgrade
  ```

### **5. Run the Application**

Start the Flask development server:

```bash
flask run
```

The application will be accessible at `http://127.0.0.1:5000`.

### **6. (Optional) Docker Setup**

If you prefer to use Docker:

- Build and start the containers:
  ```bash
  docker-compose up --build
  ```
- The application will run at `http://127.0.0.1:5000`.

---

## **Folder Structure**

```plaintext
flask-login-project/
├── app/                # Main Flask application files
├── migrations/         # Database migrations
├── templates/          # HTML templates
├── sdlc_programmer_data/ # Local MariaDB volume
├── Dockerfile          # Dockerfile for Flask app
├── docker-compose.yml  # Docker Compose configuration
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variable example file
```

---

## **Future Improvements**

- Implement email verification
- Add user roles (e.g., admin and standard user)
- Improve UI with a modern CSS framework (e.g., Bootstrap)

---

## **License**

This project is licensed under the MIT License. See `LICENSE` for more details.

---

## **Contributors**

- [Enrico Hezkiel Sirait](https://github.com/ifs21034-itdel)
