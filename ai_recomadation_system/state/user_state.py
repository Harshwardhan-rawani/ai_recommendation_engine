import reflex as rx
import os
import requests
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, auth

load_dotenv()

FIREBASE_API_KEY = os.getenv("FIREBASE_API_KEY", "")

# Initialize Firebase Admin SDK
cred_path = os.path.join(os.path.dirname(__file__), "..", "backend", "firebase.json")
if os.path.exists(cred_path):
    if not firebase_admin._apps:
        try:
            cred = credentials.Certificate(cred_path)
            firebase_admin.initialize_app(cred)
            print("Firebase Admin SDK initialized successfully.")
        except Exception as e:
            print(f"Error initializing Firebase Admin SDK: {e}")

class UserState(rx.State):
    email: str = ""
    password: str = ""
    
    logged_in: bool = False
    firebase_uid: str = ""
    # Map firebase UID to our numeric dataset ID
    dataset_user_id: int = -1
    
    # State mapping cache (simulate DB table linking Firebase UIDs to dataset IDs)
    uid_mapping: dict[str, int] = {}
    next_user_id: int = 1000
    
    auth_error: str = ""
    
    @rx.var
    def user_type(self) -> str:
        """ Returns 'new' if user is not in original dataset, 'old' if they are """
        if self.dataset_user_id == -1:
            return "unknown"
        elif self.dataset_user_id >= 1000:
            return "new"
        return "existing"

    def assign_dataset_id(self):
        """Map the firebase uid to a numeric id."""
        # For demo purposes, we assign known ids to showcase collaborative filtering
        if self.email == "test@test.com" or self.email == "user@test.com":
             self.dataset_user_id = 101 # Existing user from dataset
        else:
             if self.firebase_uid not in self.uid_mapping:
                 self.uid_mapping[self.firebase_uid] = self.next_user_id
                 self.next_user_id += 1
             self.dataset_user_id = self.uid_mapping[self.firebase_uid]

    def login(self):
        self.auth_error = ""
        if "dummy" in FIREBASE_API_KEY.lower() or not FIREBASE_API_KEY:
            # Fallback to mock authentication
            if self.email and self.password:
                self.firebase_uid = f"mock_uid_{self.email}"
                self.logged_in = True
                self.assign_dataset_id()
                return rx.redirect("/")
            else:
                self.auth_error = "Email and password required"
                return

        # Real Firebase Auth logic via Identity Toolkit REST API
        url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={FIREBASE_API_KEY}"
        data = {"email": self.email, "password": self.password, "returnSecureToken": True}
        try:
            res = requests.post(url, json=data)
            if res.status_code == 200:
                response_data = res.json()
                id_token = response_data.get("idToken")
                if id_token:
                    # Verify the token server-side for security
                    try:
                        decoded_token = auth.verify_id_token(id_token)
                        self.firebase_uid = decoded_token['uid']
                        self.logged_in = True
                        self.assign_dataset_id()
                        return rx.redirect("/")
                    except Exception as verify_error:
                        self.auth_error = f"Token verification failed: {str(verify_error)}"
                        return
                else:
                    self.auth_error = "No ID token received"
                    return
            else:
                error_data = res.json()
                error_message = error_data.get("error", {}).get("message", "Login failed")

                # If Firebase is not configured, fall back to mock authentication
                if "CONFIGURATION_NOT_FOUND" in error_message or "PROJECT_NOT_FOUND" in error_message:
                    print("Firebase not configured, falling back to mock authentication")
                    if self.email and self.password:
                        self.firebase_uid = f"mock_uid_{self.email}"
                        self.logged_in = True
                        self.assign_dataset_id()
                        return rx.redirect("/")
                    else:
                        self.auth_error = "Email and password required"
                        return
                else:
                    self.auth_error = f"Login failed: {error_message}"
        except Exception as e:
            self.auth_error = f"Login error: {str(e)}"

    def signup(self):
        self.auth_error = ""
        if "dummy" in FIREBASE_API_KEY.lower() or not FIREBASE_API_KEY:
            # Fallback to mock authentication
            if self.email and self.password:
                self.firebase_uid = f"mock_uid_{self.email}"
                self.logged_in = True
                self.assign_dataset_id()
                return rx.redirect("/")
            else:
                self.auth_error = "Email and password required"
                return

        url = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={FIREBASE_API_KEY}"
        data = {"email": self.email, "password": self.password, "returnSecureToken": True}
        try:
            res = requests.post(url, json=data)
            if res.status_code == 200:
                response_data = res.json()
                id_token = response_data.get("idToken")
                if id_token:
                    # Verify the token server-side for security
                    try:
                        decoded_token = auth.verify_id_token(id_token)
                        self.firebase_uid = decoded_token['uid']
                        self.logged_in = True
                        self.assign_dataset_id()
                        return rx.redirect("/")
                    except Exception as verify_error:
                        self.auth_error = f"Token verification failed: {str(verify_error)}"
                        return
                else:
                    self.auth_error = "No ID token received"
                    return
            else:
                error_data = res.json()
                error_message = error_data.get("error", {}).get("message", "Signup failed")

                # If Firebase is not configured, fall back to mock authentication
                if "CONFIGURATION_NOT_FOUND" in error_message or "PROJECT_NOT_FOUND" in error_message:
                    print("Firebase not configured, falling back to mock authentication")
                    if self.email and self.password:
                        self.firebase_uid = f"mock_uid_{self.email}"
                        self.logged_in = True
                        self.assign_dataset_id()
                        return rx.redirect("/")
                    else:
                        self.auth_error = "Email and password required"
                        return
                else:
                    self.auth_error = f"Signup failed: {error_message}"
        except Exception as e:
            self.auth_error = f"Signup error: {str(e)}"

    def logout(self):
        self.logged_in = False
        self.firebase_uid = ""
        self.dataset_user_id = -1
        self.email = ""
        self.password = ""
        return rx.redirect("/login")
