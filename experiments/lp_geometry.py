"""A tiny LP-geometry experiment for Week 1.

The feasible region is the triangle

    x1 >= 0, x2 >= 0, x1 + x2 <= 1.

We enumerate its vertices and evaluate a linear objective there.  The point is
not to implement an LP solver, but to make the extreme-point picture concrete.
"""

from __future__ import annotations


VERTICES = ((0.0, 0.0), (1.0, 0.0), (0.0, 1.0))


def objective(x: tuple[float, float]) -> float:
    """Evaluate -2*x1 - x2."""

    x1, x2 = x
    return -2.0 * x1 - x2


def main() -> None:
    values = [(vertex, objective(vertex)) for vertex in VERTICES]
    best_vertex, best_value = min(values, key=lambda item: item[1])

    print("Vertices and objective values:")
    for vertex, value in values:
        print(f"  {vertex}: {value:g}")
    print(f"\nBest vertex: {best_vertex}")
    print(f"Best objective value: {best_value:g}")
    print("\nInterpretation: this linear objective reaches its minimum at an extreme point.")


if __name__ == "__main__":
    main()

