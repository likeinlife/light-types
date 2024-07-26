def fully_qualified_name(cls: type) -> str:
    return f"{cls.__module__}.{cls.__qualname__}"
