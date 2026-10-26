# Code Girls United — practice bank runner
#
# Question group edits notebooks/questions.json (new examples).
# Code group edits this file (new question types, the click checker, the buttons).
#
# An example is data: a name, a number, a list. This file turns one example
# into the questions for that category. It does not trust a pasted snippet.
# Python runs the snippet it built and checks the expected answers.
#
# One random example is drawn each time a category runs.
# Check the bank:  python notebooks/practice_bank.py

from __future__ import annotations

import ast
import html
import json
import keyword
import random
import sys
from pathlib import Path


class BankError(Exception):
    """The JSON is readable, but an example or category does not check out."""


BANK_VERSION = 1

# answers: keys on each example, and keys in prompts / hints / notes.
# fixed: a question whose wording is the same for every example in the category.
SPECS = {
    "assign_and_print": {
        "answers": ("name", "value", "print_with", "output"),
        "fixed": (),
    },
    "one_update": {
        "answers": ("value", "op"),
        "fixed": (),
    },
    "for_list": {
        "answers": ("iterations", "last"),
        "fixed": ("meaning",),
    },
    "for_index": {
        "answers": ("iterations", "last"),
        "fixed": ("meaning",),
    },
    "for_range": {
        "answers": ("iterations", "last"),
        "fixed": ("meaning",),
    },
    "for_range_start_stop": {
        "answers": ("iterations", "first", "last", "includes_stop"),
        "fixed": (),
    },
    "for_range_step": {
        "answers": ("iterations", "last", "printed"),
        "fixed": ("step_means",),
    },
    "while_count": {
        "answers": ("iterations", "last", "stops"),
        "fixed": (),
    },
    "for_blank": {
        "answers": ("iterations", "output"),
        "fixed": ("meaning",),
    },
    "plus_equals": {
        "answers": ("same_as", "value", "iterations"),
        "fixed": (),
    },
    "enumerate": {
        "answers": ("iterations", "last"),
        "fixed": ("meaning",),
    },
}

OP_WORDS = {
    "+": "adds",
    "-": "subtracts",
    "*": "multiplies",
    "//": "whole-number divide",
    "%": "remainder",
}

SHORTHAND = {
    "+=": "+",
    "-=": "-",
    "*=": "*",
}

BANNED_NAMES = {
    "print",
    "range",
    "len",
    "enumerate",
    "input",
    "exec",
    "eval",
    "open",
    "compile",
    "globals",
    "locals",
    "vars",
    "getattr",
    "setattr",
}

OPTIONAL_EXAMPLE_KEYS = {"added_by", "note"}


def questions_path():
    """Find questions.json next to this file, in the working folder, or in Colab."""
    here = Path(__file__).resolve().parent
    candidates = [
        here / "questions.json",
        Path.cwd() / "questions.json",
        Path.cwd() / "notebooks" / "questions.json",
        Path("/content/questions.json"),
    ]
    for candidate in candidates:
        if candidate.is_file():
            return candidate
    raise BankError(
        "Could not find questions.json. Keep it next to practice_bank.py. "
        "In Colab: click the folder icon and upload questions.json."
    )


def load_bank(path=None):
    path = Path(path) if path else questions_path()
    try:
        raw = path.read_text(encoding="utf-8")
    except OSError as err:
        raise BankError(f"Could not read {path}: {err}") from err
    try:
        bank = json.loads(raw)
    except json.JSONDecodeError as err:
        raise BankError(
            "questions.json is not valid JSON "
            f"({err.msg}, line {err.lineno}). "
            "A comma after the last item, or a missing quote, does this."
        ) from err
    if not isinstance(bank, dict):
        raise BankError("questions.json must be one object, { ... }.")
    if bank.get("bank_version") != BANK_VERSION:
        raise BankError(
            f'bank_version must be {BANK_VERSION}. Leave it alone unless the code group changes the shape.'
        )
    categories = bank.get("categories")
    if not isinstance(categories, list) or not categories:
        raise BankError("categories must be a non-empty list.")
    return bank


def _as_int(value, label):
    if isinstance(value, bool) or not isinstance(value, int):
        raise BankError(f"{label} must be a whole number, not {value!r}.")
    if value < -100 or value > 100:
        raise BankError(f"{label} must stay between -100 and 100.")
    return value


def _as_text(value, label):
    if not isinstance(value, str) or not value.strip():
        raise BankError(f"{label} must be a non-empty string.")
    if len(value) > 40:
        raise BankError(f"{label} must be 40 characters or fewer.")
    if any(ch in value for ch in '\n\r"\\'):
        raise BankError(f'{label} cannot contain quotes, backslashes, or new lines.')
    return value


def _as_name(value, label):
    if not isinstance(value, str) or not value.isidentifier() or keyword.iskeyword(value):
        raise BankError(f"{label} must be a variable name, like score or count.")
    if value.startswith("_") or value in BANNED_NAMES:
        raise BankError(f"{label} cannot be {value!r}. Pick an ordinary name.")
    return value


def literal(value):
    """Turn a JSON number or string into the Python text we show and run."""
    if isinstance(value, bool) or not isinstance(value, (int, str)):
        raise BankError(f"A value must be a number or text, not {value!r}.")
    if isinstance(value, int):
        _as_int(value, "value")
        return str(value)
    return '"' + _as_text(value, "value") + '"'


def list_literal(items):
    return "[" + ", ".join(literal(item) for item in items) + "]"


def show(value):
    """What print shows. Text has no quote marks. Numbers stay numbers."""
    if isinstance(value, str):
        return value
    return str(value)


def _run(code):
    """Run a snippet this file built. Capture print. Return names and lines."""
    printed = []

    def _print(*args, **kwargs):
        printed.append(" ".join(str(arg) for arg in args))

    ns = {"print": _print}
    exec(code, ns, ns)
    return ns, printed


def _assigned_names(code):
    tree = ast.parse(code)
    found = []
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    found.append(target.id)
    return found


def correct_answer(q):
    """The click Python accepts. Runnable kinds are checked by running the snippet."""
    kind = q["kind"]
    if kind == "stored":
        return q["answer"]
    code = q["code"]
    if kind == "variable":
        names = _assigned_names(code)
        if len(names) != 1:
            raise BankError("A variable question needs exactly one name on the left of =.")
        return names[0]
    if kind == "value":
        ns, _printed = _run(code)
        target = q["target"]
        if target not in ns:
            raise BankError(f"{target} was never set by this snippet.")
        return show(ns[target])
    _ns, printed = _run(code)
    if kind == "print_count":
        return str(len(printed))
    if kind == "first_print":
        if not printed:
            raise BankError("This snippet printed nothing.")
        return printed[0]
    if kind == "last_print":
        if not printed:
            raise BankError("This snippet printed nothing.")
        return printed[-1]
    if kind == "all_prints":
        if not printed:
            raise BankError("This snippet printed nothing.")
        return ", ".join(printed)
    raise BankError(f"Unknown kind {kind!r}.")


def unique_choices(answer, decoys):
    if not isinstance(answer, str) or answer == "":
        raise BankError(f"expected answer must be text, not {answer!r}.")
    choices = [answer]
    for decoy in decoys:
        text = str(decoy)
        if text and text not in choices:
            choices.append(text)
        if len(choices) == 3:
            break
    if len(choices) < 2:
        raise BankError(f"need a wrong choice besides {answer!r}.")
    return choices


def _block(cat, group, ask):
    block = cat.get(group)
    if not isinstance(block, dict) or ask not in block:
        raise BankError(f'{cat.get("id", "?")} is missing {group}.{ask}.')
    text = block[ask]
    if not isinstance(text, str) or not text.strip():
        raise BankError(f"{group}.{ask} must be non-empty text.")
    return text.strip()


def data_q(cat, ask, code, answer, kind, decoys, target=None):
    question = {
        "ask": ask,
        "prompt": _block(cat, "prompts", ask),
        "code": code,
        "choices": unique_choices(answer, decoys),
        "answer": answer,
        "kind": kind,
        "hint": _block(cat, "hints", ask),
        "note": _block(cat, "notes", ask),
    }
    if target is not None:
        question["target"] = target
    got = correct_answer(question)
    if got != answer:
        raise BankError(
            f"{ask}: the file says {answer!r} but running the snippet gives {got!r}."
        )
    return question


def fixed_q(cat, ask, code):
    fixed = cat.get("fixed")
    if not isinstance(fixed, dict) or ask not in fixed:
        raise BankError(f'{cat.get("id", "?")} is missing fixed.{ask}.')
    block = fixed[ask]
    for field in ("prompt", "answer", "hint", "note", "decoys"):
        if field not in block:
            raise BankError(f"fixed.{ask} is missing {field}.")
    answer = block["answer"]
    if not isinstance(answer, str) or not answer.strip():
        raise BankError(f"fixed.{ask}.answer must be non-empty text.")
    decoys = block["decoys"]
    if not isinstance(decoys, list) or len(decoys) < 2:
        raise BankError(f"fixed.{ask}.decoys needs at least two wrong choices.")
    return {
        "ask": ask,
        "prompt": str(block["prompt"]).strip(),
        "code": code,
        "choices": unique_choices(answer.strip(), decoys),
        "answer": answer.strip(),
        "kind": "stored",
        "hint": str(block["hint"]).strip(),
        "note": str(block["note"]).strip(),
    }


def _expect(answers, key, computed):
    if not isinstance(answers, dict) or key not in answers:
        raise BankError(f"answers.{key} is missing.")
    got = answers[key]
    if not isinstance(got, str):
        raise BankError(
            f'answers.{key} must be text, like "{computed}", not {got!r}.'
        )
    if got != computed:
        raise BankError(
            f"answers.{key} is {got!r} but this example should be {computed!r}."
        )
    return computed


def _require_answer_keys(answers, keys):
    if not isinstance(answers, dict):
        raise BankError("answers must be an object.")
    extra = set(answers) - set(keys)
    missing = set(keys) - set(answers)
    if extra or missing:
        raise BankError(
            "answers keys must be "
            + ", ".join(keys)
            + (
                (". Unexpected: " + ", ".join(sorted(extra))) if extra else ""
            )
            + (
                (". Missing: " + ", ".join(sorted(missing))) if missing else ""
            )
            + "."
        )


def _attach_note(questions, example):
    extra = example.get("note", "")
    if not extra:
        return questions
    if not isinstance(extra, str) or not extra.strip():
        raise BankError("note must be a sentence, or leave it off.")
    last = questions[-1]
    last["note"] = last["note"] + " " + extra.strip()
    return questions


def _iteration_decoys(count, also=()):
    decoys = list(also)
    decoys.append(str(count - 1))
    decoys.append(str(count + 1))
    return decoys


def expand_assign_and_print(cat, example):
    name = _as_name(example.get("name"), "name")
    if "value" not in example:
        raise BankError("value is missing.")
    value_text = literal(example["value"])
    shown = show(example["value"])
    full = f"{name} = {value_text}\nprint({name})"
    blank = f"{name} = {value_text}\nprint(???)"
    answers = example["answers"]
    _require_answer_keys(answers, SPECS["assign_and_print"]["answers"])
    _expect(answers, "name", name)
    _expect(answers, "value", shown)
    _expect(answers, "print_with", name)
    _expect(answers, "output", shown)
    quoted_name = '"' + name + '"'
    quoted_value = '"' + shown + '"'
    nearby = "1" if shown == "0" else "0"
    if isinstance(example["value"], int):
        nearby = str(example["value"] + (1 if example["value"] < 100 else -1))
    questions = [
        data_q(
            cat, "name", full, name, "variable",
            [shown, "value", quoted_name],
        ),
        data_q(
            cat, "value", full, shown, "value",
            [name, nearby, quoted_value],
            target=name,
        ),
        data_q(
            cat, "print_with", blank, name, "stored",
            [shown, quoted_name, nearby],
        ),
        data_q(
            cat, "output", full, shown, "last_print",
            [name, quoted_value, nearby],
        ),
    ]
    return _attach_note(questions, example)


def expand_one_update(cat, example):
    name = _as_name(example.get("name"), "name")
    start = _as_int(example.get("start"), "start")
    amount = _as_int(example.get("amount"), "amount")
    op = example.get("op")
    if op not in OP_WORDS:
        raise BankError("op must be one of +  -  *  //  %.")
    if amount == 0:
        raise BankError("amount cannot be 0.")
    code = f"{name} = {start}\n{name} = {name} {op} {amount}"
    result = show(_run(code)[0][name])
    word = OP_WORDS[op]
    answers = example["answers"]
    _require_answer_keys(answers, SPECS["one_update"]["answers"])
    _expect(answers, "value", result)
    _expect(answers, "op", word)
    other_words = [text for text in OP_WORDS.values() if text != word]
    questions = [
        data_q(
            cat, "value", code, result, "value",
            [str(start), str(amount), name],
            target=name,
        ),
        data_q(cat, "op", code, word, "stored", other_words),
    ]
    return _attach_note(questions, example)


def _items(example):
    items = example.get("items")
    if not isinstance(items, list) or not items:
        raise BankError("items must be a non-empty list.")
    if len(items) > 8:
        raise BankError("items can hold at most 8 values.")
    for item in items:
        literal(item)
    return items


def _pair_names(example):
    list_name = _as_name(example.get("list_name"), "list_name")
    var = _as_name(example.get("var"), "var")
    if list_name == var:
        raise BankError("list_name and var must be different words.")
    return list_name, var


def expand_for_list(cat, example):
    list_name, var = _pair_names(example)
    items = _items(example)
    code = (
        f"{list_name} = {list_literal(items)}\n"
        f"for {var} in {list_name}:\n"
        f"    print({var})"
    )
    printed = [show(item) for item in items]
    count = len(printed)
    answers = example["answers"]
    _require_answer_keys(answers, SPECS["for_list"]["answers"])
    _expect(answers, "iterations", str(count))
    _expect(answers, "last", printed[-1])
    questions = [
        data_q(
            cat, "iterations", code, str(count), "print_count",
            _iteration_decoys(count),
        ),
        data_q(
            cat, "last", code, printed[-1], "last_print",
            [printed[0], list_name, str(count)],
        ),
        fixed_q(cat, "meaning", code),
    ]
    return _attach_note(questions, example)


def _index_code(list_name, index, items, body):
    return (
        f"{list_name} = {list_literal(items)}\n"
        f"for {index} in range(len({list_name})):\n"
        f"    {body}"
    )


def expand_for_index(cat, example):
    list_name = _as_name(example.get("list_name"), "list_name")
    index = _as_name(example.get("index"), "index")
    if list_name == index:
        raise BankError("list_name and index must be different words.")
    items = _items(example)
    body = f"print({index}, {list_name}[{index}])"
    code = _index_code(list_name, index, items, body)
    last = f"{len(items) - 1} {show(items[-1])}"
    count = len(items)
    answers = example["answers"]
    _require_answer_keys(answers, SPECS["for_index"]["answers"])
    _expect(answers, "iterations", str(count))
    _expect(answers, "last", last)
    questions = [
        data_q(
            cat, "iterations", code, str(count), "print_count",
            _iteration_decoys(count, [str(items[-1]) if not isinstance(items[-1], str) else "0"]),
        ),
        data_q(
            cat, "last", code, last, "last_print",
            [show(items[-1]), f"1 {show(items[0])}", str(count)],
        ),
        fixed_q(cat, "meaning", code),
    ]
    return _attach_note(questions, example)


def _range_values(start, stop, step):
    step = _as_int(step, "step")
    start = _as_int(start, "start")
    stop = _as_int(stop, "stop")
    if step == 0:
        raise BankError("step cannot be 0.")
    values = list(range(start, stop, step))
    if not values:
        raise BankError("this range never runs. Check start, stop, and step.")
    if len(values) > 12:
        raise BankError("keep the loop to 12 passes or fewer.")
    return values


def expand_for_range(cat, example):
    var = _as_name(example.get("var"), "var")
    stop = _as_int(example.get("stop"), "stop")
    if stop < 1:
        raise BankError("stop must be at least 1.")
    values = _range_values(0, stop, 1)
    code = f"for {var} in range({stop}):\n    print({var})"
    count = len(values)
    last = str(values[-1])
    answers = example["answers"]
    _require_answer_keys(answers, SPECS["for_range"]["answers"])
    _expect(answers, "iterations", str(count))
    _expect(answers, "last", last)
    questions = [
        data_q(
            cat, "iterations", code, str(count), "print_count",
            _iteration_decoys(count, [str(stop)]),
        ),
        data_q(
            cat, "last", code, last, "last_print",
            [str(stop), "0", str(count)],
        ),
        fixed_q(cat, "meaning", code),
    ]
    return _attach_note(questions, example)


def expand_for_range_start_stop(cat, example):
    var = _as_name(example.get("var"), "var")
    start = _as_int(example.get("start"), "start")
    stop = _as_int(example.get("stop"), "stop")
    values = _range_values(start, stop, 1)
    code = f"for {var} in range({start}, {stop}):\n    print({var})"
    count = len(values)
    first = str(values[0])
    last = str(values[-1])
    includes = f"No. It stops before {stop}"
    answers = example["answers"]
    _require_answer_keys(answers, SPECS["for_range_start_stop"]["answers"])
    _expect(answers, "iterations", str(count))
    _expect(answers, "first", first)
    _expect(answers, "last", last)
    _expect(answers, "includes_stop", includes)
    questions = [
        data_q(
            cat, "iterations", code, str(count), "print_count",
            _iteration_decoys(count, [str(stop), str(start)]),
        ),
        data_q(
            cat, "first", code, first, "first_print",
            ["0", str(stop), last],
        ),
        data_q(
            cat, "last", code, last, "last_print",
            [str(stop), first, str(count)],
        ),
        data_q(
            cat, "includes_stop", code, includes, "stored",
            [f"Yes. It prints {stop}", f"It prints only {stop}"],
        ),
    ]
    return _attach_note(questions, example)


def _join(values):
    return ", ".join(str(value) for value in values)


def expand_for_range_step(cat, example):
    var = _as_name(example.get("var"), "var")
    start = _as_int(example.get("start"), "start")
    stop = _as_int(example.get("stop"), "stop")
    step = _as_int(example.get("step"), "step")
    values = _range_values(start, stop, step)
    code = f"for {var} in range({start}, {stop}, {step}):\n    print({var})"
    count = len(values)
    last = str(values[-1])
    printed = _join(values)
    direction = 1 if step > 0 else -1
    by_one = list(range(start, stop, direction))
    answers = example["answers"]
    _require_answer_keys(answers, SPECS["for_range_step"]["answers"])
    _expect(answers, "iterations", str(count))
    _expect(answers, "last", last)
    _expect(answers, "printed", printed)
    questions = [
        data_q(
            cat, "iterations", code, str(count), "print_count",
            _iteration_decoys(count, [str(abs(stop - start))]),
        ),
        data_q(
            cat, "last", code, last, "last_print",
            [str(stop), str(values[0]), str(count)],
        ),
        data_q(
            cat, "printed", code, printed, "all_prints",
            [_join(values + [stop]), _join(by_one), _join(list(reversed(values)))],
        ),
        fixed_q(cat, "step_means", code),
    ]
    return _attach_note(questions, example)


def _while_values(start, limit, comparison):
    if comparison not in ("<", "<="):
        raise BankError('comparison must be "<" or "<=".')
    values = []
    current = start
    for _pass in range(21):
        if comparison == "<" and not current < limit:
            break
        if comparison == "<=" and not current <= limit:
            break
        values.append(current)
        current += 1
    else:
        raise BankError("this while does not end. Check start, limit, and comparison.")
    if not values:
        raise BankError("this while never runs. Start below the limit.")
    if len(values) > 12:
        raise BankError("keep the while loop to 12 passes or fewer.")
    return values


def expand_while_count(cat, example):
    var = _as_name(example.get("var"), "var")
    start = _as_int(example.get("start"), "start")
    limit = _as_int(example.get("limit"), "limit")
    comparison = example.get("comparison")
    values = _while_values(start, limit, comparison)
    code = (
        f"{var} = {start}\n"
        f"while {var} {comparison} {limit}:\n"
        f"    print({var})\n"
        f"    {var} = {var} + 1"
    )
    count = len(values)
    last = str(values[-1])
    stops = f"When {var} {comparison} {limit} is false"
    other = "<=" if comparison == "<" else "<"
    answers = example["answers"]
    _require_answer_keys(answers, SPECS["while_count"]["answers"])
    _expect(answers, "iterations", str(count))
    _expect(answers, "last", last)
    _expect(answers, "stops", stops)
    questions = [
        data_q(
            cat, "iterations", code, str(count), "print_count",
            _iteration_decoys(count, [str(limit)]),
        ),
        data_q(
            cat, "last", code, last, "last_print",
            [str(limit), str(limit + 1), str(start), str(count)],
        ),
        data_q(
            cat, "stops", code, stops, "stored",
            [
                f"When {var} {other} {limit} is false",
                "It never stops",
                "When the indented line has run once",
            ],
        ),
    ]
    return _attach_note(questions, example)


def expand_for_blank(cat, example):
    times = _as_int(example.get("times"), "times")
    if times < 1 or times > 12:
        raise BankError("times must be from 1 to 12.")
    message = _as_text(example.get("message"), "message")
    code = f'for _ in range({times}):\n    print("{message}")'
    answers = example["answers"]
    _require_answer_keys(answers, SPECS["for_blank"]["answers"])
    _expect(answers, "iterations", str(times))
    _expect(answers, "output", message)
    questions = [
        data_q(
            cat, "iterations", code, str(times), "print_count",
            _iteration_decoys(times),
        ),
        data_q(
            cat, "output", code, message, "last_print",
            [str(times), "_", "range"],
        ),
        fixed_q(cat, "meaning", code),
    ]
    return _attach_note(questions, example)


def _apply_shorthand(start, op, amount, times):
    value = start
    plain = SHORTHAND[op]
    for _pass in range(times):
        if plain == "+":
            value = value + amount
        elif plain == "-":
            value = value - amount
        else:
            value = value * amount
    return value


def expand_plus_equals(cat, example):
    var = _as_name(example.get("var"), "var")
    if var == "n":
        raise BankError('name the variable something other than n. The loop uses n.')
    start = _as_int(example.get("start"), "start")
    amount = _as_int(example.get("amount"), "amount")
    times = _as_int(example.get("times"), "times")
    op = example.get("op")
    if op not in SHORTHAND:
        raise BankError("op must be += or -= or *=.")
    if times < 1 or times > 12:
        raise BankError("times must be from 1 to 12.")
    if amount == 0:
        raise BankError("amount cannot be 0.")
    plain = SHORTHAND[op]
    code = f"{var} = {start}\nfor n in range({times}):\n    {var} {op} {amount}"
    result = show(_apply_shorthand(start, op, amount, times))
    ran = show(_run(code)[0][var])
    if ran != result:
        raise BankError(f"shorthand result mismatch: {ran!r} vs {result!r}.")
    same_as = f"{var} = {var} {plain} {amount}"
    answers = example["answers"]
    _require_answer_keys(answers, SPECS["plus_equals"]["answers"])
    _expect(answers, "same_as", same_as)
    _expect(answers, "value", result)
    _expect(answers, "iterations", str(times))
    other_lines = [
        f"{var} = {var} {symbol} {amount}"
        for symbol in ("+", "-", "*")
        if symbol != plain
    ]
    questions = [
        data_q(
            cat, "same_as", code, same_as, "stored",
            other_lines + [f"{var} {plain} {amount}"],
        ),
        data_q(
            cat, "value", code, result, "value",
            [str(start), str(amount), str(times)],
            target=var,
        ),
        data_q(
            cat, "iterations", code, str(times), "stored",
            _iteration_decoys(times),
        ),
    ]
    return _attach_note(questions, example)


def expand_enumerate(cat, example):
    list_name = _as_name(example.get("list_name"), "list_name")
    index = _as_name(example.get("index"), "index")
    var = _as_name(example.get("var"), "var")
    names = {list_name, index, var}
    if len(names) < 3:
        raise BankError("list_name, index, and var must be three different words.")
    items = _items(example)
    code = (
        f"{list_name} = {list_literal(items)}\n"
        f"for {index}, {var} in enumerate({list_name}):\n"
        f"    print({index}, {var})"
    )
    count = len(items)
    last = f"{count - 1} {show(items[-1])}"
    answers = example["answers"]
    _require_answer_keys(answers, SPECS["enumerate"]["answers"])
    _expect(answers, "iterations", str(count))
    _expect(answers, "last", last)
    questions = [
        data_q(
            cat, "iterations", code, str(count), "print_count",
            _iteration_decoys(count),
        ),
        data_q(
            cat, "last", code, last, "last_print",
            [show(items[-1]), f"1 {show(items[0])}", str(count)],
        ),
        fixed_q(cat, "meaning", code),
    ]
    return _attach_note(questions, example)


EXPANDERS = {
    "assign_and_print": expand_assign_and_print,
    "one_update": expand_one_update,
    "for_list": expand_for_list,
    "for_index": expand_for_index,
    "for_range": expand_for_range,
    "for_range_start_stop": expand_for_range_start_stop,
    "for_range_step": expand_for_range_step,
    "while_count": expand_while_count,
    "for_blank": expand_for_blank,
    "plus_equals": expand_plus_equals,
    "enumerate": expand_enumerate,
}

EXAMPLE_FIELDS = {
    "assign_and_print": {"name", "value"},
    "one_update": {"name", "start", "op", "amount"},
    "for_list": {"list_name", "var", "items"},
    "for_index": {"list_name", "index", "items"},
    "for_range": {"var", "stop"},
    "for_range_start_stop": {"var", "start", "stop"},
    "for_range_step": {"var", "start", "stop", "step"},
    "while_count": {"var", "start", "limit", "comparison"},
    "for_blank": {"times", "message"},
    "plus_equals": {"var", "start", "op", "amount", "times"},
    "enumerate": {"list_name", "index", "var", "items"},
}

CATEGORY_KEYS = {
    "id",
    "title",
    "pattern",
    "blurb",
    "closing",
    "prompts",
    "hints",
    "notes",
    "examples",
    "fixed",
}


def _check_words(cat, group, keys):
    block = cat.get(group)
    if not isinstance(block, dict):
        raise BankError(f"{group} must be an object of sentences.")
    extra = set(block) - set(keys)
    missing = set(keys) - set(block)
    if extra or missing:
        raise BankError(
            f"{group} keys must be "
            + ", ".join(keys)
            + (
                (". Unexpected: " + ", ".join(sorted(extra))) if extra else ""
            )
            + (
                (". Missing: " + ", ".join(sorted(missing))) if missing else ""
            )
            + "."
        )
    for key in keys:
        text = block[key]
        if not isinstance(text, str) or not text.strip():
            raise BankError(f"{group}.{key} must be non-empty text.")


def _check_added_by(example):
    if "added_by" not in example:
        return
    who = example["added_by"]
    if not isinstance(who, str) or not who.strip() or len(who) > 40 or "@" in who:
        raise BankError("added_by should be a first name or initials, not an email.")


def _check_example_id(example_id, seen):
    if not isinstance(example_id, str) or not example_id.replace("-", "").isalnum():
        raise BankError(f"example id {example_id!r} should be short words and dashes, like age-14.")
    if example_id in seen:
        raise BankError(f"example id {example_id!r} is used twice in this category.")
    seen.add(example_id)


def expand_example(cat, example):
    pattern = cat["pattern"]
    if pattern not in EXPANDERS:
        known = ", ".join(EXPANDERS)
        raise BankError(f"unknown pattern {pattern!r}. Known patterns: {known}.")
    return EXPANDERS[pattern](cat, example)


def check_loaded(bank):
    """Return a list of problems. Empty means every example matches what Python runs."""
    errors = []
    seen_categories = set()
    for cat in bank["categories"]:
        if not isinstance(cat, dict):
            errors.append("A category must be an object.")
            continue
        cat_id = cat.get("id", "?")
        try:
            unknown = set(cat) - CATEGORY_KEYS
            if unknown:
                raise BankError("unexpected fields: " + ", ".join(sorted(unknown)))
            for field in ("id", "title", "pattern", "blurb", "closing"):
                text = cat.get(field)
                if not isinstance(text, str) or not text.strip():
                    raise BankError(f"{field} must be non-empty text.")
            if cat_id in seen_categories:
                raise BankError("duplicate category id.")
            seen_categories.add(cat_id)
            pattern = cat["pattern"]
            if pattern not in SPECS:
                raise BankError(
                    f"unknown pattern {pattern!r}. Known: {', '.join(SPECS)}."
                )
            spec = SPECS[pattern]
            _check_words(cat, "prompts", spec["answers"])
            _check_words(cat, "hints", spec["answers"])
            _check_words(cat, "notes", spec["answers"])
            if spec["fixed"]:
                if "fixed" not in cat:
                    raise BankError("this pattern needs a fixed block.")
                fixed = cat["fixed"]
                if set(fixed) != set(spec["fixed"]):
                    raise BankError(
                        "fixed keys must be " + ", ".join(spec["fixed"]) + "."
                    )
                for key in spec["fixed"]:
                    fixed_q(cat, key, "pass")
            elif "fixed" in cat:
                raise BankError("this pattern does not use a fixed block. Remove it.")
            examples = cat.get("examples")
            if not isinstance(examples, list) or not examples:
                raise BankError("examples must be a non-empty list.")
            seen_examples = set()
            required = {"id", "answers"} | EXAMPLE_FIELDS[pattern]
            allowed = required | OPTIONAL_EXAMPLE_KEYS
            for example in examples:
                example_id = "?"
                try:
                    if not isinstance(example, dict):
                        raise BankError("an example must be an object.")
                    example_id = str(example.get("id", "?"))
                    _check_example_id(example.get("id"), seen_examples)
                    extra = set(example) - allowed
                    missing = required - set(example)
                    if extra:
                        raise BankError(
                            "unexpected fields: " + ", ".join(sorted(extra))
                        )
                    if missing:
                        raise BankError(
                            "missing fields: " + ", ".join(sorted(missing))
                        )
                    _check_added_by(example)
                    questions = expand_example(cat, example)
                    if len(questions) < 2:
                        raise BankError("a category question set needs at least two questions.")
                    for question in questions:
                        if question["answer"] not in question["choices"]:
                            raise BankError(
                                f"{question['ask']}: the expected answer is not one of the choices."
                            )
                        if len(set(question["choices"])) != len(question["choices"]):
                            raise BankError(f"{question['ask']}: a choice is repeated.")
                except BankError as err:
                    errors.append(f"{cat_id} / {example_id}: {err}")
        except BankError as err:
            errors.append(f"{cat_id}: {err}")
    return errors


def check_bank(path=None):
    return check_loaded(load_bank(path))


def bank_summary(bank=None):
    bank = bank or load_bank()
    count = sum(len(cat["examples"]) for cat in bank["categories"])
    return (
        f"{len(bank['categories'])} categories, {count} examples. "
        "Each run draws one random example from that category."
    )


def _lead(q):
    ask = q["ask"]
    answer = q["answer"]
    if ask == "name":
        return f"{answer} is the variable."
    if ask == "value":
        return f"After those lines, {q.get('target', 'it')} is {answer}."
    if ask == "print_with":
        return f"Put {answer} inside print( )."
    if ask == "output":
        return f"The print shows {answer}."
    if ask == "iterations":
        word = "time" if answer == "1" else "times"
        return f"It runs {answer} {word}."
    if ask == "last":
        return f"The last line is {answer}."
    if ask == "first":
        return f"The first line is {answer}."
    if ask == "printed":
        return f"In order, it prints {answer}."
    if answer.endswith("."):
        return answer
    return answer + "."


def _explain(q):
    lead = _lead(q)
    note = q.get("note", "").strip()
    if note:
        return lead + " " + note
    return lead


def preview_text(rng=None):
    """One random example per category, with the expected answer under each question."""
    rng = rng or random.Random()
    bank = load_bank()
    errors = check_loaded(bank)
    lines = [bank_summary(bank), ""]
    if errors:
        lines.append("Fix questions.json before a lesson:")
        for err in errors:
            lines.append("- " + err)
        return "\n".join(lines)
    for cat in bank["categories"]:
        example = rng.choice(cat["examples"])
        lines.append(cat["title"] + "  (" + example["id"] + ")")
        lines.append(cat["blurb"])
        for number, question in enumerate(expand_example(cat, example), start=1):
            lines.append("")
            lines.append(f"{number}. {question['prompt']}")
            lines.append(question["code"])
            lines.append("expected: " + question["answer"])
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def _banner(text, bg, fg):
    safe = html.escape(text)
    return (
        "<div style='background:"
        + bg
        + ";color:"
        + fg
        + ";padding:10px 12px;border-radius:8px;margin-top:8px;"
        + "font:15px/1.45 system-ui,sans-serif'>"
        + safe
        + "</div>"
    )


def _widgets():
    try:
        import ipywidgets as widgets
        from IPython.display import clear_output, display
    except ImportError:
        return None, None, None
    return widgets, clear_output, display


def start_lesson(title, questions, closing):
    """Click a choice. Next appears after a right answer or a second miss."""
    widgets, clear_output, display = _widgets()
    if widgets is None:
        print("Open this notebook in Google Colab to click answers. Colab already has ipywidgets.")
        print(title)
        for number, question in enumerate(questions, start=1):
            print()
            print(f"{number}. {question['prompt']}")
            print(question["code"])
            print("expected: " + question["answer"])
        return

    clear_output(wait=True)
    state = {
        "i": 0,
        "misses": 0,
        "first_try": 0,
        "locked": False,
        "done": False,
    }

    progress_w = widgets.HTML()
    prompt_w = widgets.HTML()
    code_w = widgets.HTML()
    buttons_w = widgets.HBox(layout=widgets.Layout(flex_flow="row wrap"))
    feedback_w = widgets.HTML()
    next_w = widgets.Button(
        description="Next",
        button_style="success",
        layout=widgets.Layout(
            width="140px",
            height="40px",
            margin="10px 0 0 0",
            visibility="hidden",
        ),
    )

    def mark_correct(correct):
        for btn in buttons_w.children:
            btn.disabled = True
            if btn.description == correct:
                btn.button_style = "success"

    def show_done():
        n = len(questions)
        buttons_w.children = ()
        next_w.layout.visibility = "hidden"
        code_w.value = ""
        prompt_w.value = ""
        progress_w.value = (
            "<div style='font:14px/1.4 system-ui,sans-serif;color:#555'>"
            + html.escape(title)
            + " · done</div>"
        )
        feedback_w.value = _banner(
            "Lesson complete. Right on the first click: "
            + str(state["first_try"])
            + " of "
            + str(n)
            + ". "
            + closing,
            "#e7f2ea",
            "#145c2a",
        )

    def show():
        q = questions[state["i"]]
        state["misses"] = 0
        state["locked"] = False
        n = len(questions)
        progress_w.value = (
            "<div style='font:14px/1.4 system-ui,sans-serif;color:#555'>"
            + html.escape(title)
            + " · "
            + str(state["i"] + 1)
            + " of "
            + str(n)
            + "</div>"
        )
        prompt_w.value = (
            "<div style='font:18px/1.35 system-ui,sans-serif;font-weight:600;"
            "margin:10px 0 6px'>"
            + html.escape(q["prompt"])
            + "</div>"
        )
        code_w.value = (
            "<pre style='font-family:Consolas,monospace;background:#f6f3ee;"
            "color:#1a1a1a;padding:14px 16px;border-radius:8px;"
            "border:1px solid #e2d9cc;font-size:16px;line-height:1.45;"
            "margin:8px 0 12px'>"
            + html.escape(q["code"])
            + "</pre>"
        )
        feedback_w.value = ""
        next_w.layout.visibility = "hidden"
        next_w.description = "Finish" if state["i"] == n - 1 else "Next"

        def make_click(choice):
            def _on_click(btn):
                on_pick(choice, btn)

            return _on_click

        made = []
        for choice in q["choices"]:
            width = max(140, min(520, 9 * len(choice) + 36))
            btn = widgets.Button(
                description=choice,
                tooltip=choice,
                layout=widgets.Layout(width=f"{width}px", height="40px", margin="4px"),
            )
            btn.on_click(make_click(choice))
            made.append(btn)
        buttons_w.children = tuple(made)

    def on_pick(choice, btn):
        if state["locked"] or state["done"] or btn.disabled:
            return
        q = questions[state["i"]]
        correct = correct_answer(q)
        if choice == correct:
            state["locked"] = True
            if state["misses"] == 0:
                state["first_try"] += 1
            mark_correct(correct)
            feedback_w.value = _banner(
                "That's it. " + _explain(q),
                "#e7f2ea",
                "#145c2a",
            )
            next_w.layout.visibility = "visible"
            return
        state["misses"] += 1
        btn.disabled = True
        btn.button_style = "warning"
        if state["misses"] >= 2:
            state["locked"] = True
            mark_correct(correct)
            feedback_w.value = _banner(
                "Here it is. " + _explain(q),
                "#fdecea",
                "#8a1f11",
            )
            next_w.layout.visibility = "visible"
        else:
            feedback_w.value = _banner(
                "Not yet. " + q["hint"],
                "#fff6e0",
                "#6b4e00",
            )

    def on_next(_btn):
        if state["done"]:
            return
        if state["i"] >= len(questions) - 1:
            state["done"] = True
            show_done()
            return
        state["i"] += 1
        show()

    next_w.on_click(on_next)
    show()
    display(
        widgets.VBox(
            [progress_w, prompt_w, code_w, buttons_w, feedback_w, next_w],
            layout=widgets.Layout(
                max_width="720px",
                border="1px solid #eadfce",
                padding="12px 14px 8px 14px",
            ),
        )
    )


def start_category(category_id, rng=None):
    """Draw one example from a category and show its questions."""
    try:
        bank = load_bank()
    except BankError as err:
        print(err)
        return
    errors = check_loaded(bank)
    if errors:
        print("Fix questions.json before running a lesson:")
        for err in errors:
            print("-", err)
        return
    matches = [cat for cat in bank["categories"] if cat["id"] == category_id]
    if not matches:
        print(f"No category {category_id!r}. Categories:")
        for cat in bank["categories"]:
            print("-", cat["id"])
        return
    cat = matches[0]
    rng = rng or random.Random()
    example = rng.choice(cat["examples"])
    questions = expand_example(cat, example)
    for question in questions:
        rng.shuffle(question["choices"])
    # One example per run. Later, the code group can keep drawing until 5 are right.
    start_lesson(
        cat["title"] + " (" + example["id"] + ")",
        questions,
        cat["closing"],
    )


def main():
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass
    try:
        errors = check_bank()
    except BankError as err:
        print(err)
        return 1
    if errors:
        print("Fix questions.json:")
        for err in errors:
            print("-", err)
        return 1
    print(preview_text())
    return 0


if __name__ == "__main__":
    sys.exit(main())
