from stage1_ocean import find_lookalikes
from stage2_prospeo import find_decision_makers
from stage3_eazyreach import resolve_emails
from stage4_brevo import send_emails

def main():
    print("=" * 50)
    print("   AUTOMATED OUTREACH PIPELINE")
    print("=" * 50)

    # Get seed domain from user
    seed_domain = input("\nEnter seed domain (e.g. stripe.com): ").strip()
    if not seed_domain:
        print("No domain entered. Exiting.")
        return

    # Stage 1 - Find lookalike companies
    print("\n[Stage 1] Finding lookalike companies...")
    domains = find_lookalikes(seed_domain)
    if not domains:
        print("No lookalike companies found. Exiting.")
        return
    print(f"✓ Stage 1 complete — {len(domains)} companies found")

    # Stage 2 - Find decision makers
    print("\n[Stage 2] Finding decision makers...")
    contacts = find_decision_makers(domains)
    if not contacts:
        print("No contacts found. Exiting.")
        return
    print(f"✓ Stage 2 complete — {len(contacts)} contacts found")

    # Stage 3 - Resolve emails
    print("\n[Stage 3] Resolving work emails...")
    contacts = resolve_emails(contacts)
    if not contacts:
        print("No emails resolved. Exiting.")
        return
    print(f"✓ Stage 3 complete — {len(contacts)} emails resolved")

    # Safety checkpoint before sending
    print("\n" + "=" * 50)
    print("  SUMMARY — About to send emails to:")
    print("=" * 50)
    for contact in contacts:
        print(f"  • {contact.get('first_name')} {contact.get('last_name')} "
              f"| {contact.get('position')} "
              f"| {contact.get('email')}")

    print(f"\nTotal: {len(contacts)} emails will be sent")
    confirm = input("\nProceed and send emails? (yes/no): ").strip().lower()
    if confirm != "yes":
        print("Cancelled. No emails sent.")
        return

    # Stage 4 - Send emails
    print("\n[Stage 4] Sending emails...")
    sent = send_emails(contacts)

    print("\n" + "=" * 50)
    print(f"  PIPELINE COMPLETE — {sent} emails sent")
    print("=" * 50)

if __name__ == "__main__":
    main()