def load_dotenv(filename: str = ".env") -> dict:
    env = {}
    try:
        with open(filename, "r") as fh:
            for line in fh:
                key, val = line.split("=", 1)
                env[key.strip()] = val.strip()
    except:
        pass
    finally:
        return env