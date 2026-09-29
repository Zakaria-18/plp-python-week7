# Python - List Warmup, Shopping List Manager & List Report

## Files
- `list_warmup.py` - Warm up with list basics: index access (`fruits[0]`, `fruits[-1]`), `.append()`, `.remove()`, and `len()`.
- `shopping_list.py` - An interactive shopping list manager that loops through add / remove / show / done and never crashes, even when removing a missing item.
- `list_report.py` - Loops through a fixed list to print it numbered, count how many names have more than 4 letters, and find the longest name.

## Reflection
It is safer to check `in` before calling `.remove()` because `.remove()`
raises a `ValueError` when the value is not in the list - and that crashes
the program unless you wrap it in a `try` / `except`. By testing
`if item in shopping_list:` first, the program can print a friendly
message and keep running instead of stopping with an error. The `in`
check turns a potential crash into an ordinary branch of the code.
