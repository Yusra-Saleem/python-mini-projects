"""
🔐 The Cryptographic Vault Guardian 🔐
===================================
Where passwords transform into
mystical digital signatures!
===================================
"""

from hashlib import sha256
import time
from typing import Dict

def login(email: str, stored_logins: Dict[str, str], password_to_check: str) -> bool:
    """Verifies digital signatures in the cryptographic vault"""
    print(f"\n🔍 Analyzing credentials for: {email}")
    print("⚡ Initiating quantum verification sequence...")
    time.sleep(1)
    
    if email not in stored_logins:
        print("❌ Email address not found in the system")
        return False
    
    password_hash = hash_password(password_to_check)
    is_valid = stored_logins[email] == password_hash
    
    print("🔄 Processing security protocols...")
    time.sleep(0.5)
    
    if is_valid:
        print("✅ Access granted! Authentication successful")
    else:
        print("❌ Access denied! Invalid credentials")
    
    return is_valid

def hash_password(password: str) -> str:
    """Transforms passwords into secure digital signatures"""
    print("🔒 Generating cryptographic signature...")
    time.sleep(0.5)
    return sha256(password.encode()).hexdigest()

def display_security_status(email: str, attempt_successful: bool) -> None:
    """Displays enhanced security information"""
    print("\n📊 Security Report")
    print("═" * 40)
    print(f"🔹 Account: {email}")
    print(f"🔹 Status: {'Authenticated ✅' if attempt_successful else 'Access Denied ❌'}")
    print(f"🔹 Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("═" * 40)

def main():
    print("🌟 Welcome to the Cryptographic Vault Guardian! 🌟")
    print("Where security meets sophistication...\n")
    
    stored_logins = {
        "sentinel@cyber.net": hash_password("quantum123"),
        "guardian@secure.org": hash_password("fortress456"),
        "keeper@vault.io": hash_password("crystal789")
    }
    
    while True:
        print("\n🔐 Authentication Portal")
        print("═" * 40)
        email = input("📧 Enter email (or press Enter to exit): ").strip()
        
        if not email:
            print("\n✨ Thank you for using the Cryptographic Vault Guardian!")
            print("Stay secure in the digital realm! 🔒")
            break
            
        password = input("🔑 Enter password: ")
        success = login(email, stored_logins, password)
        display_security_status(email, success)

if __name__ == '__main__':
    main()