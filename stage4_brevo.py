import requests
from config import BREVO_API_KEY

def send_emails(contacts):
    """Takes a list of contacts with emails and sends personalized outreach"""
    sent = 0
    failed = 0

    for contact in contacts:
        email = contact.get("email")
        if not email:
            print(f"  ✗ No email for {contact.get('first_name', 'Unknown')} - skipping")
            continue

        first_name = contact.get("first_name", "there")
        company = contact.get("domain", "your company").replace(".com", "")
        position = contact.get("position", "")

        print(f"  Sending to {first_name} at {email}...")

        try:
            response = requests.post(
                "https://api.brevo.com/v3/smtp/email",
                headers={
                    "Content-Type": "application/json",
                    "api-key": BREVO_API_KEY
                },
                json={
                    "sender": {
                        "name": "Hiran Krishna",
                        "email": "hiran.ise24@cmrit.ac.in"
                    },
                    "to": [{"email": email, "name": f"{first_name}"}],
                    "subject": f"Quick idea for {company.capitalize()}",
                    "htmlContent": f"""
                        <p>Hi {first_name},</p>
                        <p>I came across {company.capitalize()} and was impressed by what you're building.</p>
                        <p>I'm reaching out because I think there's a real opportunity to help {company.capitalize()} 
                        scale its outreach — specifically by automating the process of finding and contacting 
                        the right decision-makers.</p>
                        <p>Would you be open to a quick 15-minute call to explore if this could be valuable for your team?</p>
                        <p>Best,<br>Hiran Krishna<br>hiran.ise24@cmrit.ac.in</p>
                    """
                }
            )

            if response.status_code == 201:
                print(f"    ✓ Sent to {first_name} at {email}")
                sent += 1
            else:
                print(f"    ✗ Failed for {email}: {response.text}")
                failed += 1

        except Exception as e:
            print(f"    ✗ Error sending to {email}: {e}")
            failed += 1

    print(f"\n  Emails sent: {sent} | Failed: {failed}")
    return sent