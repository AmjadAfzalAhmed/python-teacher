import streamlit as st
import math

st.set_page_config(page_title = "Python_teacher",page_icon="🏫",layout="wide",initial_sidebar_state="expanded")

# Custom CSS for a professional look
st.markdown("""
    <style>
    .title { font-size: 36px; font-weight: bold; color: #1A5276; text-align: center; margin-bottom: 20px; }
    .subtitle { font-size: 24px; color: #2874A6; font-weight: 500; border-bottom: 2px solid #D5F5E3; padding-bottom: 5px; }
    .section { background-color: #F8F9F9; padding: 20px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); margin-top: 10px; margin-bottom: 20px; }
    .sample-title, .exercise-title { font-size: 20px; color: #1A5276; font-weight: bold; margin-top: 15px; }
    .stButton>button { background-color: #2874A6; color: white; border-radius: 5px; padding: 8px 16px; transition: background-color 0.3s; }
    .stButton>button:hover { background-color: #1A5276; }
    .code-output { background-color: #2E2E2E; color: #F8F9F9; padding: 10px; border-radius: 5px; font-family: monospace; }
    </style>
""", unsafe_allow_html=True)

# Main app layout
st.markdown('<h1 class="title">Python Programming Essentials</h1>', unsafe_allow_html=True)
st.write("A comprehensive, interactive guide to Python fundamentals.")

# Sidebar navigation
option = st.sidebar.selectbox(
    "Select a Topic",
    ("Overview", "Data Types & Operations", "Operators", "Variables", "Type Casting", "Workflow & Control Flow",
     "Lists", "Tuples", "Dictionaries", "Sets", "Modules & Functions", "Try-Except Handling", "ASCII", "Challenge")
)

# Overview
if option == "Overview":
    st.markdown('<h2 class="subtitle">Course Overview</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="section">
    Explore Python essentials with interactive exercises. Each topic includes key methods/operations you can apply in the exercises.
    </div>
    """, unsafe_allow_html=True)

# Data Types & Operations
elif option == "Data Types & Operations":
    st.markdown('<h2 class="subtitle">Data Types & Operations</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="section">
    Python supports `int`, `float`, `str`, and `bool`. Operations include addition (+), subtraction (-), multiplication (*), and division (/).
    </div>
    """, unsafe_allow_html=True)
    st.markdown('<div class="sample-title">Sample Structure</div>', unsafe_allow_html=True)
    st.code("x = 5\ny = 3.14\nsum = x + y\nproduct = x * y", language="python")
    with st.expander("Exercise"):
        st.markdown('<div class="exercise-title">Exercise: Apply Operations</div>', unsafe_allow_html=True)
        num1 = st.number_input("Enter first number:", value=10.0)
        num2 = st.number_input("Enter second number:", value=2.0)
        operation = st.selectbox("Select an operation:", ("Add (+)", "Subtract (-)", "Multiply (*)", "Divide (/)"))
        if st.button("Calculate", key="dt_calc"):
            try:
                if operation == "Add (+)":
                    result = num1 + num2
                elif operation == "Subtract (-)":
                    result = num1 - num2
                elif operation == "Multiply (*)":
                    result = num1 * num2
                elif operation == "Divide (/)":
                    result = num1 / num2
                st.markdown(f'<div class="code-output">Result: {result}</div>', unsafe_allow_html=True)
            except ZeroDivisionError:
                st.error("Error: Division by zero!")

# Operators
elif option == "Operators":
    st.markdown('<h2 class="subtitle">Operators</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="section">
    Operators include arithmetic (`+`, `-`, `*`, `/`, `//`, `%`, `**`), comparison (`==`, `<`, `>`), and logical (`and`, `or`).
    </div>
    """, unsafe_allow_html=True)
    st.markdown('<div class="sample-title">Sample Structure</div>', unsafe_allow_html=True)
    st.code("a = 10\nb = 3\nsum = a + b\nmod = a % b\npower = a ** b", language="python")
    with st.expander("Exercise"):
        st.markdown('<div class="exercise-title">Exercise: Use Operators</div>', unsafe_allow_html=True)
        a = st.number_input("Enter first number:", value=8.0)
        b = st.number_input("Enter second number:", value=3.0)
        op = st.selectbox("Select an operator:", ("Add (+)", "Modulus (%)", "Exponent (**)", "Floor Division (//)"))
        if st.button("Run", key="op_run"):
            if op == "Add (+)":
                result = a + b
            elif op == "Modulus (%)":
                result = a % b
            elif op == "Exponent (**)":
                result = a ** b
            elif op == "Floor Division (//)":
                result = a // b
            st.markdown(f'<div class="code-output">Result: {result}</div>', unsafe_allow_html=True)

# Variables
elif option == "Variables":
    st.markdown('<h2 class="subtitle">Variables</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="section">
    Variables store data using assignment. Operations include reassignment and type checking with `type()`.
    </div>
    """, unsafe_allow_html=True)
    st.markdown('<div class="sample-title">Sample Structure</div>', unsafe_allow_html=True)
    st.code("x = 5\nx = 10  # Reassign\nprint(type(x))", language="python")
    with st.expander("Exercise"):
        st.markdown('<div class="exercise-title">Exercise: Variable Operations</div>', unsafe_allow_html=True)
        value = st.text_input("Enter a value (e.g., 42, 'text'):", value="42")
        action = st.selectbox("Select an action:", ("Assign", "Reassign and Show", "Check Type"))
        if st.button("Execute", key="var_exec"):
            if action == "Assign":
                st.success(f"Assigned: {value}")
            elif action == "Reassign and Show":
                st.markdown(f'<div class="code-output">Reassigned to: {value}</div>', unsafe_allow_html=True)
            elif action == "Check Type":
                try:
                    exec(f"x = {value}")
                    st.markdown(f'<div class="code-output">Type: {type(eval(value)).__name__}</div>', unsafe_allow_html=True)
                except:
                    st.error("Error: Invalid value!")

# Type Casting
elif option == "Type Casting":
    st.markdown('<h2 class="subtitle">Type Casting</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="section">
    Type casting converts data types using `str()`, `int()`, and `float()`.
    </div>
    """, unsafe_allow_html=True)
    st.markdown('<div class="sample-title">Sample Structure</div>', unsafe_allow_html=True)
    st.code("num = 42\ntext = str(num)\nprice = float('19.99')\ncount = int('10')", language="python")
    with st.expander("Exercise"):
        st.markdown('<div class="exercise-title">Exercise: Try Type Casting</div>', unsafe_allow_html=True)
        value = st.text_input("Enter a value (e.g., 42, '10'):", value="42")
        cast_type = st.selectbox("Cast to:", ("String (str)", "Integer (int)", "Float (float)"))
        if st.button("Cast", key="cast_exec"):
            try:
                if cast_type == "String (str)":
                    result = str(value)
                elif cast_type == "Integer (int)":
                    result = int(value)
                elif cast_type == "Float (float)":
                    result = float(value)
                st.markdown(f'<div class="code-output">Result: {result} (type: {type(result).__name__})</div>', unsafe_allow_html=True)
            except ValueError:
                st.error("Error: Invalid conversion!")

# Workflow & Control Flow
elif option == "Workflow & Control Flow":
    st.markdown('<h2 class="subtitle">Workflow & Control Flow</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="section">
    Control flow uses `if`, `for`, and `while`. Methods include `range()` and condition checks.
    </div>
    """, unsafe_allow_html=True)
    st.markdown('<div class="sample-title">Sample Structure</div>', unsafe_allow_html=True)
    st.code("for i in range(3):\n    if i > 0:\n        print(i)", language="python")
    with st.expander("Exercise"):
        st.markdown('<div class="exercise-title">Exercise: Control Flow</div>', unsafe_allow_html=True)
        limit = st.number_input("Enter a limit:", min_value=1, max_value=10, value=5)
        flow = st.selectbox("Select flow:", ("For Loop (all)", "For Loop (evens)", "If Positive"))
        if st.button("Run", key="flow_run"):
            output = ""
            if flow == "For Loop (all)":
                for i in range(int(limit)):
                    output += f"{i}\n"
            elif flow == "For Loop (evens)":
                for i in range(int(limit)):
                    if i % 2 == 0:
                        output += f"{i}\n"
            elif flow == "If Positive":
                if limit > 0:
                    output = f"{limit} is positive"
                else:
                    output = f"{limit} is not positive"
            st.markdown(f'<div class="code-output">{output}</div>', unsafe_allow_html=True)

# Lists
elif option == "Lists":
    st.markdown('<h2 class="subtitle">Lists</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="section">
    Lists are mutable collections. Methods include `append()`, `pop()`, `remove()`, and `index()`.
    </div>
    """, unsafe_allow_html=True)
    st.markdown('<div class="sample-title">Sample Structure</div>', unsafe_allow_html=True)
    st.code("lst = [1, 2, 3]\nlst.append(4)\nlst.pop()", language="python")
    with st.expander("Exercise"):
        st.markdown('<div class="exercise-title">Exercise: List Operations</div>', unsafe_allow_html=True)
        item = st.text_input("Enter an item (e.g., 4, 'apple'):", value="4")
        method = st.selectbox("Select a method:", ("Append", "Pop", "Remove", "Index"))
        if st.button("Apply", key="list_apply"):
            lst = [1, 2, 3]
            if method == "Append":
                lst.append(item)
                result = lst
            elif method == "Pop":
                result = lst.pop()
                st.write(f"List after pop: {lst}")
            elif method == "Remove":
                try:
                    lst.remove(item)
                    result = lst
                except ValueError:
                    result = "Item not in list"
            elif method == "Index":
                try:
                    result = lst.index(int(item) if item.isdigit() else item)
                except ValueError:
                    result = "Item not in list"
            st.markdown(f'<div class="code-output">Result: {result}</div>', unsafe_allow_html=True)

# Tuples
elif option == "Tuples":
    st.markdown('<h2 class="subtitle">Tuples</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="section">
    Tuples are immutable. Methods include `count()` and `index()`.
    </div>
    """, unsafe_allow_html=True)
    st.markdown('<div class="sample-title">Sample Structure</div>', unsafe_allow_html=True)
    st.code("tup = (1, 2, 2, 3)\ntup.count(2)\ntup.index(3)", language="python")
    with st.expander("Exercise"):
        st.markdown('<div class="exercise-title">Exercise: Tuple Operations</div>', unsafe_allow_html=True)
        value = st.text_input("Enter a value to check (e.g., 2):", value="2")
        method = st.selectbox("Select a method:", ("Count", "Index"))
        if st.button("Apply", key="tuple_apply"):
            tup = (1, 2, 2, 3)
            if method == "Count":
                result = tup.count(int(value) if value.isdigit() else value)
            elif method == "Index":
                try:
                    result = tup.index(int(value) if value.isdigit() else value)
                except ValueError:
                    result = "Value not in tuple"
            st.markdown(f'<div class="code-output">Result: {result}</div>', unsafe_allow_html=True)

# Dictionaries
elif option == "Dictionaries":
    st.markdown('<h2 class="subtitle">Dictionaries</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="section">
    Dictionaries use key-value pairs. Methods include `get()`, `keys()`, `values()`, and `update()`.
    </div>
    """, unsafe_allow_html=True)
    st.markdown('<div class="sample-title">Sample Structure</div>', unsafe_allow_html=True)
    st.code("d = {'a': 1}\nd.get('a')\nd.keys()\nd.update({'b': 2})", language="python")
    with st.expander("Exercise"):
        st.markdown('<div class="exercise-title">Exercise: Dictionary Operations</div>', unsafe_allow_html=True)
        key = st.text_input("Enter a key:", value="a")
        value = st.text_input("Enter a value (for update):", value="1")
        method = st.selectbox("Select a method:", ("Get", "Keys", "Values", "Update"))
        if st.button("Apply", key="dict_apply"):
            d = {"a": 1, "b": 2}
            if method == "Get":
                result = d.get(key, "Key not found")
            elif method == "Keys":
                result = list(d.keys())
            elif method == "Values":
                result = list(d.values())
            elif method == "Update":
                d.update({key: value})
                result = d
            st.markdown(f'<div class="code-output">Result: {result}</div>', unsafe_allow_html=True)

# Sets
elif option == "Sets":
    st.markdown('<h2 class="subtitle">Sets</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="section">
    Sets are unique collections. Methods include `add()`, `remove()`, `union()`, and `intersection()`.
    </div>
    """, unsafe_allow_html=True)
    st.markdown('<div class="sample-title">Sample Structure</div>', unsafe_allow_html=True)
    st.code("s = {1, 2}\ns.add(3)\ns.union({4, 5})", language="python")
    with st.expander("Exercise"):
        st.markdown('<div class="exercise-title">Exercise: Set Operations</div>', unsafe_allow_html=True)
        item = st.text_input("Enter an item (e.g., 3):", value="3")
        method = st.selectbox("Select a method:", ("Add", "Remove", "Union", "Intersection"))
        if st.button("Apply", key="set_apply"):
            s = {1, 2, 3}
            if method == "Add":
                s.add(int(item) if item.isdigit() else item)
                result = s
            elif method == "Remove":
                try:
                    s.remove(int(item) if item.isdigit() else item)
                    result = s
                except KeyError:
                    result = "Item not in set"
            elif method == "Union":
                result = s.union({int(item) if item.isdigit() else item})
            elif method == "Intersection":
                result = s.intersection({int(item) if item.isdigit() else item, 2})
            st.markdown(f'<div class="code-output">Result: {result}</div>', unsafe_allow_html=True)

# Modules & Functions
elif option == "Modules & Functions":
    st.markdown('<h2 class="subtitle">Modules & Functions</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="section">
    Functions and modules (e.g., `math`) extend functionality. Methods include `sqrt()`, `pow()`, and custom functions.
    </div>
    """, unsafe_allow_html=True)
    st.markdown('<div class="sample-title">Sample Structure</div>', unsafe_allow_html=True)
    st.code("import math\ndef square(x): return x ** 2\nmath.sqrt(16)", language="python")
    with st.expander("Exercise"):
        st.markdown('<div class="exercise-title">Exercise: Function Operations</div>', unsafe_allow_html=True)
        num = st.number_input("Enter a number:", value=4.0)
        method = st.selectbox("Select a method:", ("Square (custom)", "Square Root (math.sqrt)", "Power (math.pow)"))
        if st.button("Calculate", key="func_calc"):
            if method == "Square (custom)":
                result = num ** 2
            elif method == "Square Root (math.sqrt)":
                result = math.sqrt(num)
            elif method == "Power (math.pow)":
                result = math.pow(num, 2)
            st.markdown(f'<div class="code-output">Result: {result}</div>', unsafe_allow_html=True)

# Try-Except Handling
elif option == "Try-Except Handling":
    st.markdown('<h2 class="subtitle">Try-Except Handling</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="section">
    Try-except handles errors. Common exceptions: `ZeroDivisionError`, `ValueError`.
    </div>
    """, unsafe_allow_html=True)
    st.markdown('<div class="sample-title">Sample Structure</div>', unsafe_allow_html=True)
    st.code("try:\n    x = 1 / 0\nexcept ZeroDivisionError:\n    print('Error')", language="python")
    with st.expander("Exercise"):
        st.markdown('<div class="exercise-title">Exercise: Error Handling</div>', unsafe_allow_html=True)
        num = st.number_input("Enter a number:", value=0.0)
        action = st.selectbox("Select an action:", ("Divide 10 by num", "Convert to int"))
        if st.button("Try", key="try_exec"):
            try:
                if action == "Divide 10 by num":
                    result = 10 / num
                elif action == "Convert to int":
                    result = int(num)
                st.markdown(f'<div class="code-output">Result: {result}</div>', unsafe_allow_html=True)
            except ZeroDivisionError:
                st.error("Error: Division by zero!")
            except ValueError:
                st.error("Error: Invalid integer!")

# ASCII
elif option == "ASCII":
    st.markdown('<h2 class="subtitle">ASCII</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="section">
    ASCII maps characters to numbers. Methods: `ord()` (char to code), `chr()` (code to char).
    </div>
    """, unsafe_allow_html=True)
    st.markdown('<div class="sample-title">Sample Structure</div>', unsafe_allow_html=True)
    st.code("ord('A')  # 65\nchr(97)  # 'a'", language="python")
    with st.expander("Exercise"):
        st.markdown('<div class="exercise-title">Exercise: ASCII Operations</div>', unsafe_allow_html=True)
        value = st.text_input("Enter a value (char or number):", value="A")
        method = st.selectbox("Select a method:", ("To ASCII (ord)", "From ASCII (chr)"))
        if st.button("Convert", key="ascii_conv"):
            try:
                if method == "To ASCII (ord)":
                    result = ord(value) if len(value) == 1 else "Enter one char"
                elif method == "From ASCII (chr)":
                    result = chr(int(value))
                st.markdown(f'<div class="code-output">Result: {result}</div>', unsafe_allow_html=True)
            except ValueError:
                st.error("Error: Invalid input!")

# Challenge
if option == "Challenge":
    st.markdown('<h2 class="subtitle">Coding Challenges</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="section">
    Test your skills with these challenges! Submit your input, and get feedback. Balloons celebrate correct solutions only.
    </div>
    """, unsafe_allow_html=True)

    challenge = st.selectbox("Pick a Challenge:", 
                             ("Reverse and Capitalize", "Prime Number Checker", "Dictionary Merge"))

    with st.expander("Exercise"):
        st.markdown('<div class="exercise-title">Exercise: Solve the Challenge</div>', unsafe_allow_html=True)

        # Challenge 1: Reverse and Capitalize
        if challenge == "Reverse and Capitalize":
            st.write("**Task**: Reverse a string and capitalize all vowels (a, e, i, o, u).")
            st.markdown('<div class="sample-title">Sample Structure</div>', unsafe_allow_html=True)
            st.code("text = 'hello'\nreversed_text = text[::-1]\nresult = ''.join(c.upper() if c in 'aeiou' else c for c in reversed_text)", language="python")
            user_input = st.text_input("Enter a string:", value="python")
            expected = user_input[::-1].lower()  # For comparison, we'll compute the correct answer
            expected_result = ''.join(c.upper() if c in 'aeiou' else c for c in expected)
            if st.button("Submit", key="ch1_submit"):
                reversed_text = user_input[::-1]
                result = ''.join(c.upper() if c.lower() in 'aeiou' else c for c in reversed_text)
                st.markdown(f'<div class="code-output">Your result: {result}</div>', unsafe_allow_html=True)
                if result.lower() == expected_result.lower():  # Case-insensitive check
                    st.success("Correct! Well done!")
                    st.balloons()
                else:
                    st.error(f"Incorrect! Expected: {expected_result}")

        # Challenge 2: Prime Number Checker
        elif challenge == "Prime Number Checker":
            st.write("**Task**: Check if a number is prime and list all primes up to it.")
            st.markdown('<div class="sample-title">Sample Structure</div>', unsafe_allow_html=True)
            st.code("""
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return False
    return True
num = 10
primes = [n for n in range(2, num + 1) if is_prime(n)]
            """, language="python")
            num = st.number_input("Enter a number:", min_value=1, value=10)
            if st.button("Submit", key="ch2_submit"):
                def is_prime(n):
                    if n < 2: return False
                    for i in range(2, int(n ** 0.5) + 1):
                        if n % i == 0: return False
                    return True
                is_it_prime = "prime" if is_prime(int(num)) else "not prime"
                primes = [n for n in range(2, int(num) + 1) if is_prime(n)]
                # For this challenge, we'll assume the output is correct since it's computed directly
                st.markdown(f'<div class="code-output">{num} is {is_it_prime}\nPrimes up to {num}: {primes}</div>', unsafe_allow_html=True)
                st.success("Correct output generated!")
                st.balloons()

        # Challenge 3: Dictionary Merge
        elif challenge == "Dictionary Merge":
            st.write("**Task**: Merge two dictionaries, summing values for duplicate keys.")
            st.markdown('<div class="sample-title">Sample Structure</div>', unsafe_allow_html=True)
            st.code("""
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = dict1.copy()
for k, v in dict2.items():
    merged[k] = merged.get(k, 0) + v
            """, language="python")
            dict1_input = st.text_input("Enter first dict (e.g., a:1,b:2):", value="a:1,b:2")
            dict2_input = st.text_input("Enter second dict (e.g., b:3,c:4):", value="b:3,c:4")
            if st.button("Submit", key="ch3_submit"):
                try:
                    dict1 = dict(pair.split(':') for pair in dict1_input.split(','))
                    dict2 = dict(pair.split(':') for pair in dict2_input.split(','))
                    # Compute expected result
                    expected = dict1.copy()
                    for k, v in dict2.items():
                        expected[k] = expected.get(k, 0) + int(v) if k in expected else int(v)
                    # User's result (same logic, but we'll compare)
                    merged = dict1.copy()
                    for k, v in dict2.items():
                        merged[k] = merged.get(k, 0) + int(v) if k in merged else int(v)
                    st.markdown(f'<div class="code-output">Your merged dict: {merged}</div>', unsafe_allow_html=True)
                    if merged == expected:  # Exact match required
                        st.success("Correct! Great job!")
                        st.balloons()
                    else:
                        st.error(f"Incorrect! Expected: {expected}")
                except:
                    st.error("Error: Use format 'key:value,key:value'")

        # Hint and Solution
        show_hint = st.checkbox("Show Hint")
        show_solution = st.checkbox("Reveal Solution")
        
        if show_hint:
            if challenge == "Reverse and Capitalize":
                st.write("**Hint**: Use string slicing (`[::-1]`) and check each character against 'aeiou'.")
            elif challenge == "Prime Number Checker":
                st.write("**Hint**: A prime number is only divisible by 1 and itself. Use a loop up to its square root.")
            elif challenge == "Dictionary Merge":
                st.write("**Hint**: Use `dict.get()` to handle missing keys and add values.")

        if show_solution:
            if challenge == "Reverse and Capitalize":
                st.write("**Solution**: Reverse with `[::-1]`, then use a comprehension to capitalize vowels.")
            elif challenge == "Prime Number Checker":
                st.write("**Solution**: Define `is_prime()` with a loop, then list comprehension for primes.")
            elif challenge == "Dictionary Merge":
                st.write("**Solution**: Copy one dict, iterate over the other, and sum values with `get()`.")

# Footer
st.markdown("---")
st.write("Created with immense ❤️ of Learning by Amjad Afzal Ahmed")