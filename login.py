def login(utilizador, password):
    if len(password) < 8:
        return False
    print(f"A autenticar {utilizador}...")
    return True