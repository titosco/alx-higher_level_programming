#!/usr/bin/python3

if __name__ == "__main__":
    """Print names defined by hidden_4 module."""
    import hidden_4

    name = dir(hidden_4)
    for names in name:
        if names[:2] != "__":
            print(names)
