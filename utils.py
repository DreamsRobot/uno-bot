def format_card(card: str) -> str:
    """Optional helper to make card names pretty"""
    mapping = {"R": "🔴", "G": "🟢", "B": "🔵", "Y": "🟡"}
    for k, v in mapping.items():
        if card.startswith(k):
            return v + card[1:]
    if "WILD" in card:
        return "🌈" + card
    return card
