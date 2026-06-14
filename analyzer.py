import re
import math

def analyze_password(password):
    score = 0
    feedback = []
    
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
        
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")
        
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")
        
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Password should include at least one number.")
        
    if re.search(r"[!@#$%^&*(),._?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Password should include at least one special character.")
        
    return score, feedback


def estimate_crack_time(password):
    charset = 0
    
    if re.search(r"[a-z]", password):
        charset += 26
    if re.search(r"[A-Z]", password):
        charset += 26
    if re.search(r"[0-9]", password):
        charset += 10
    if re.search(r"[!@#$%^&*(),._?\":{}|<>]", password):
        charset += 32
    
    combinations = charset ** len(password)
    guesses_per_second = 1_000_000_000
    
    return combinations / guesses_per_second


def format_time(seconds):
    if seconds < 60:
        return f"{seconds:.2f} seconds"
    elif seconds < 3600:
        return f"{seconds / 60:.2f} minutes"
    elif seconds < 86400:
        return f"{seconds / 3600:.2f} hours"
    elif seconds < 31536000:
        return f"{seconds / 86400:.2f} days"
    else:
        return f"{seconds / 31536000:.2f} years"
    
        