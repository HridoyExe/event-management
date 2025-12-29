# EventMaster - Professional Event Management System

**EventMaster** is a robust and visually stunning web application designed to streamline the event management process. Built with **Django** and styled with **Tailwind CSS**, it serves three distinct user roles: **Admins**, **Organizers**, and **Participants**, providing a seamless experience for creating, managing, and attending events.

## 🚀 Features

### 🎨 Modern UI/UX
-   **Responsive Design**: Fully responsive layout optimized for desktop, tablet, and mobile.
-   **Glassmorphism**: Trendy glass-effect navigation and cards.
-   **Interactive Elements**: Smooth transitions, hover effects, and animated components.

### 👥 User Roles & Dashboards
-   **Admin**: Complete control over the system, user management, and event oversight.
-   **Organizer**: Create and manage events, track ticket sales, and view participant analytics.
-   **Participant**: Browse events, book tickets, and manage bookings from a personal dashboard.

### 🔐 Authentication & Profile
-   Secure User Registration & Login.
-   Role-based access control.
-   Profile management with avatar support.
-   Password reset functionality.

### 📅 Event Management
-   **Create Events**: Detailed event forms with categories, dates, and locations.
-   **Browse & Search**: Advanced filtering and search capabilities for participants.
-   **Ticketing**: Simple and secure booking flow (Mockup/Integrated).

## 🛠️ Technology Stack

-   **Backend**: Python, Django
-   **Frontend**: HTML5, Tailwind CSS, JavaScript (Vanilla)
-   **Database**: SQLite (Default) / PostgreSQL (Supported)
-   **Styling**: Google Fonts (Inter)

## 📦 Installation

Prerequisites: Python 3.8+ installed.

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/event-management.git
    cd event-management
    ```

2.  **Create a Virtual Environment**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply Migrations**
    ```bash
    python manage.py migrate
    ```

5.  **Create Superuser (Admin)**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the Server**
    ```bash
    python manage.py runserver
    ```

7.  **Access the App**
    -   Open `http://127.0.0.1:8000/` in your browser.

## 📂 Project Structure

```
event-management/
├── core/               # Core functionality (Home, Base templates)
├── users/              # Authentication & User Profiles
├── events/             # Event logic, Dashboards, Forms
├── templates/          # Global templates
├── static/             # Static assets (CSS, JS, Images)
└── manage.py           # Django CLI utility
```

---

