# AI E-Commerce Recommendation System

A full-stack, AI-powered e-commerce application built entirely in Python using [Reflex](https://reflex.dev/). This project integrates a complete shopping experience with advanced machine learning recommendation models, Firebase authentication, and a Razorpay payment gateway checkout flow.

## 🚀 Features

* **Advanced AI Recommendations**:
  * **Collaborative Filtering**: Recommends products based on user behavior and similar user profiles.
  * **Content-Based Filtering**: Suggests products similar to those the user has viewed based on tags and descriptions.
  * **Rating-Based Sorting**: Highlights top-rated products.
* **Full E-Commerce Flow**: Browse products, view product details, manage a shopping cart, and complete a checkout.
* **Smart Search & Filtering**: Real-time category filtering and text-based search (by product name, brand, or description).
* **Payment Integration**: Mock payment processing using the Razorpay Sandbox via their Python SDK and frontend checkout script.
* **Authentication**: User Signup, Login, and secure session management via Firebase.
* **Responsive UI**: A modern, responsive web application interface designed with Reflex components.

## 🛠️ Technology Stack

* **Framework**: [Reflex](https://reflex.dev/) (Full-stack Python Web Framework)
* **Data Processing & ML**: `pandas`, `scikit-learn`
* **Authentication**: [Firebase Admin SDK](https://firebase.google.com/docs/admin/setup)
* **Payments**: [Razorpay](https://razorpay.com/) Python Client
* **Environment Management**: `python-dotenv`

## 📁 Project Structure

```text
ai_recomadation_system/
├── ai_recomadation_system/
│   ├── backend/         # ML models, data cleaning, and Firebase services
│   ├── components/      # Reusable Reflex UI components (Navbar, Product Cards, etc.)
│   ├── pages/           # Application routes (Home, Products, Cart, Checkout, Auth, etc.)
│   ├── state/           # Global Reflex State (Cart, User, Recommendations)
│   └── ai_recomadation_system.py # Main app routing and config
├── assets/              # Static files and images
├── clean_data.csv       # E-Commerce dataset powering the products and ML
├── rxconfig.py          # Reflex configuration
└── requirements.txt     # Python dependencies
```

## ⚙️ Prerequisites

* Python 3.10+
* A [Firebase Project](https://console.firebase.google.com/) with Email/Password Authentication enabled.
* A [Razorpay](https://razorpay.com/) Sandbox Account for test keys.

## 🔧 Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Harshwardhan-rawani/ai_recommendation_engine.git
   cd ai_recomadation_system
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On Mac/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables Config**:
   Create a `.env` file in the root directory and add your API keys:
   ```ini
   # Firebase Config
   FIREBASE_API_KEY="your_firebase_api_key_here"
   FIREBASE_AUTH_DOMAIN="your_firebase_auth_domain_here"

   # Razorpay Test Config
   RAZORPAY_KEY_ID="rzp_test_your_key_here"
   RAZORPAY_KEY_SECRET="your_razorpay_secret_here"
   ```

5. **Firebase Admin Config**:
   Download your Firebase Service Account JSON key from the Firebase Console and save it as `firebase.json` corresponding to your backend layout.

## 🏃‍♂️ Running the Application

To start the local development server, run:
```bash
reflex run
```
The application will be accessible at `http://localhost:3000`.

## 🤝 Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.
