"""Read and summarize a local text file without modifying it."""
from pathlib import Path


def summarize_text(path: Path) -> dict[str, int]:
    text = path.read_text(encoding="utf-8")
    return {
        "lines": len(text.splitlines()),
        "words": len(text.split()),
        "characters": len(text),
    }


if __name__ == "__main__":
    sample = Path(__file__).resolve().parent.parent / "README.md"
    print(f"Statistics for {sample.name}: {summarize_text(sample)}")
