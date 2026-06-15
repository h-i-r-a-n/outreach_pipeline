def find_lookalikes(seed_domain):
    """Returns a hardcoded list of lookalike companies for demo purposes"""
    print(f"  Finding companies similar to {seed_domain}...")

    lookalikes = [
        "razorpay.com",
        "cashfree.com",
        "payu.in",
        "billdesk.com",
        "instamojo.com"
    ]

    for domain in lookalikes:
        print(f"    ✓ Found: {domain}")

    print(f"  Total: {len(lookalikes)} lookalike companies found")
    return lookalikes