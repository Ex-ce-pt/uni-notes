
Representation of polypeptides.
Consists of:
- [Sequence of symbols](#Sequence%20of%20symbols)
- [Sequence logos](#Sequence%20logos)

Example:
![[consensus-sequence-ex.png]]
P-loop, APT binding motif

## Sequence of symbols

Similar to REGEX.

Rules:
- AA delimiter - `-`
- `[AB]` - `A` or `B
- `{AB}` - any AA, except for `A` or `B`
- `x` - any AA
- `A(n)` - repeat `A` `n` times
- `A(n1, n2)` - repeat `A` between `n1` and `n2`, including both ends
- `<` - N-terminus
- `>` - C-terminus

The example above would then read:
1. A or G
2. 4 of any AA
3. G
4. K
5. S or T

## Sequence logos

Height of the letters → relative frequency.
Height of the column → degree of conservation, measured in bits (shannons).
==Q: information theory space, learn it first

Color of the letters:

| Color | Property of R | AAs                    |
| ----- | ------------- | ---------------------- |
| Green | polar         | G, S, T, Y, C, Q, N    |
| Black | hydrophobic   | A, V, L, I, P, W, F, M |
| Blue  | basic         | R, H, K                |
| Red   | acidic        | D, E                   |

