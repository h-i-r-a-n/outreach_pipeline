import requests
import time
from config import PROSPEO_API_KEY

def find_decision_makers(domains):
    """Takes a list of domains, returns list of contacts with clean details"""
    contacts = []

    for domain in domains:
        print(f"  Finding decision makers for {domain}...")

        try:
            response = requests.post(
                "https://api.prospeo.io/search-person",
                headers={
                    "Content-Type": "application/json",
                    "X-KEY": PROSPEO_API_KEY
                },
                json={
                    "page": 1,
                    "filters": {
                        "company": {
                            "websites": {
                                "include": [domain]
                            }
                        }
                    }
                }
            )

            data = response.json()

            if not data.get("error") and data.get("results"):
                for item in data["results"][:3]:
                    person = item.get("person", {})
                    
                    # 1. Safely extract the email string out of the inner email object
                    email_obj = person.get("email", {}) or item.get("email", {})
                    email_str = ""
                    if isinstance(email_obj, dict):
                        email_str = email_obj.get("email", "")
                    elif isinstance(email_obj, str):
                        email_str = email_obj

                    contact = {
                        "domain": domain,
                        "person_id": person.get("person_id", ""),
                        "first_name": person.get("first_name", ""),
                        "last_name": person.get("last_name", ""),
                        "position": person.get("title", "") or person.get("job_title", ""), # Fallback mapping for job titles
                        "linkedin": person.get("linkedin_url", ""),
                        "email": email_str  
                    }
                    contacts.append(contact)
                    
                    status = f"✓ Found: {contact['first_name']} {contact['last_name']}"
                    if contact["email"]:
                        status += f" ({contact['email']})"
                    print(f"    {status}")
            else:
                print(f"    ✗ No results for {domain}: {data.get('error_code', 'unknown')}")

        except Exception as e:
            print(f"    ✗ Error for {domain}: {e}")

        time.sleep(2)

    return contacts