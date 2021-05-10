def base_convert(data, base, base_out):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    valueof = {k:v for v, k in enumerate(digits)}
    assert 2 <= base <= 36 and 2 <= base_out <= 36
    s, scale = 0, 1
    for d in reversed(data):
        s += scale * digits.index(d)
        scale *= base
    data_out = "0" if s==0 else ""
    while s > 0:
        data_out = digits[s%base_out] + data_out
        s //= base_out
    return data_out

print(base_convert("EF", 16, 2))