def escape_response(state: dict) -> str:
    return "ESCAPE" if state.get("threat") else "MONITORING"
