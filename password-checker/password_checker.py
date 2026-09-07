#
import string
import tkinter as tk
from tkinter import messagebox


common_passwords = [
    "password",
    "password123",
    "123456",
    "qwerty",
    "letmein",
    "admin",
]

predictable_patterns = [
    "password",
    "password123",
    "123456",
    "qwerty",
    "letmein",
    "admin",
]

def check_password():
    password = password_entry.get()
    if not password:
        messagebox.showwarning(
            "Input Required",
            "Please enter a password."
        )
        return

    length = len(password)
    meets_length_requirement = length >=12

    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_number = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    is_common = password.lower() in common_passwords
    is_predictable = any( pattern in password.lower() for pattern in predictable_patterns)

    score = 0

    if length >= 12:
        score +=1

    if has_uppercase:
        score += 1

    if has_lowercase:
        score += 1

    if has_number:
        score += 1

    if has_special:
        score += 1

    if not meets_length_requirement or is_common or is_predictable:
        strength = "Weak"
    elif score <=1:
        strength = "Very Weak"
    elif score ==2:
        strength = "Weak"
    elif score == 3:
        strength = "Moderate"
    elif score == 4:
        strength = "Strong"
    else:
         strength = "Very Strong"

    recommendations =[]

    if not meets_length_requirement:
        recommendations.append("- Use atleast 12 characters")
    if not has_uppercase:
        recommendations.append("- Add atleast one uppercase character")
    if not has_lowercase:
        recommendations.append("- Add atleast one lowercase character")
    if not has_number:
        recommendations.append("- Add atleast one number")
    if not has_special:
        recommendations.append("- Add atleast one special character")
    if is_common:
        recommendations.append("- Avoid using a common password")
    if is_predictable:
        recommendations.append("- Avoid using predictable password patterns")
    if not recommendations:
        recommendations.append(
            "No reccomendations, password passed all checks.")

    results = f"""

password length: {length}
Meets minimum length:
{meets_length_requirement}

Has uppercase: {has_uppercase}
Has lowercase: {has_lowercase}
Has number: {has_number}
Has special character: {has_special}

Common password: {is_common}
Predictable pattern {is_predictable}

Complexity score: {score}/5

PASSWORD STRENGTH: {strength}

""" + " \n".join(recommendations)

    results_text.config(state="normal")
    results_text.delete("1.0", tk.END)
    results_text.insert(tk.END, results)
    results_text.config(state="disabled")

def toggle_password():

    if password_entry.cget("show") == "*":
       password_entry.config(show="")
       show_button.config(text="Hide")

    else:
        password_entry.config(show="*")
        show_button.config(text="Show")

def clear_results():
    password_entry.delete(0, tk.END)
    results_text.config(state="normal")
    results_text.delete("1.0", tk.END)
    results_text.config(state="disabled")

window = tk.Tk()

window.title("Business Password Security Checker")

window.geometry("700x750")

window.resizable(False, False)

title_label = tk.Label (
    window,
    text="Password Security Checker",
    font=("Arial", 20, "bold")
)

title_label.pack(pady=20)

description_label = tk.Label(
    window,
    text= "Analyse password security against multiple security checks.",
    font=("Arial", 11)
)

description_label.pack(pady=5)

password_label = tk.Label(
    window,
    text="Enter a password:",
    font=("Arial", 12, "bold")
)

password_label.pack(pady=(20, 5))

password_entry = tk.Entry(
    window,
    width=45,
    show="*",
    font=("Arial", 13)
)

password_entry.pack(pady=5)

show_button = tk.Button(
    window,
    text="show",
    command =toggle_password,
    width=10,
)

show_button.pack(pady=5)

check_button =tk.Button(
    window,
    text="Check Password",
    command=check_password,
    font=("Arial", 12, "bold"),
    width=20
)

check_button.pack(pady=5)

results_label = tk.Label(
    window,
    text="Security Results",
    font=("Arial", 14, "bold")
)

results_label.pack(pady=(15, 5))

results_text = tk.Text(
    window,
    width=75,
    height=27,
    font=("Courier", 10)
)

results_text.pack(padx=20, pady=10)

results_text.config(state="disabled")

window.mainloop()


