def resolve_emails(contacts):
    """Filters out contacts that do not contain a valid email string"""
    resolved = []

    for contact in contacts:
        email = contact.get("email")
        first_name = contact.get("first_name")
        last_name = contact.get("last_name")

        if email and isinstance(email, str) and "@" in email:
            print(f"  ✓ Email verified for {first_name} {last_name}: {email}")
            resolved.append(contact)
        else:
            print(f"  ✗ No valid email available for {first_name} {last_name} — skipping")

    return resolved