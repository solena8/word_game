from dataclasses import dataclass


@dataclass
class Result:
    result: str
    good_letter: list[int]

# Result(result="G..M.")
