def report_event(event: str) -> None:
    # e.g., POST to an external API
    print(f"[analytics] {event}")
    raise ValueError("must be mocked while testing")
