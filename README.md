# Automata Project

## Table of Contents
1. [DFA (Deterministic Finite Automata)](#DFA (Deterministic Finite Automata))
    1. [Class `DFA`](#Class `DFA`)
        1. [Example Usage](#Example Usage)
    2. [Methods](#Methods)
         1. [accept_string (self, string)](#accept_string (self, string))
         2. [union (self, other)](#union (self, other))
         3. [intersection (self, other)](#intersection (self, other))
         4. [complement (self)](#complement (self))
         5. [difference (self, other)](#difference (self, other))
         6. [separate (self,dfa)](#separate (self,dfa))
         7. [is_empty (self)](#is_empty (self))
         8. [all_string_accepte (self, min_lenght, max_lenght, answer)](#all_string_accepte (self, min_lenght, max_lenght, answer))
         9. [is_finite (self)](#is_finite (self))
         10. [shortest_string (self)](#shortest_string (self))
         11. [longest_string (self)](#longest_string (self))
         12. [minimize (self)](#minimize (self))
         13. [regex_to_dfa (self, regex)](#regex_to_dfa (self, regex))
         14. [dfa_to_regex (self, dfa)](#dfa_to_regex (self, dfa))
2. [NFA (Non-Deterministic Finite Automata)](#NFA (Non-Deterministic Finite Automata))
    1. [Class `NFA`](#Class `NFA`)
        1. [Example Usage](#Example Usage)
    2. [Methods](#Methods)
         1. [lambda_closure(states_set, transitions)](#lambda_closure (states_set, transitions))
         2. [eliminate_nondeterminism(self)](#eliminate_nondeterminism (self))
3. [DPDA (Deterministic Pushdown Automata)](#DPDA (Deterministic Pushdown Automata))
    1. [Class `DPDA`](#Class `DPDA`)
        1. [Example Usage](#Example Usage)
    2. [Methods](#Methods)
         1. [accept_string (self, string)](#accept_string (self, string))

# DFA (Deterministic Finite Automata)


This is a Python implementation of a Deterministic Finite Automata (DFA), which is a simple abstract machine that recognizes patterns in strings. The implementation provides a basic framework for defining and working with DFAs.

## Class `DFA`

The `DFA` class represents a DFA. It has the following methods:

```def __init__(self, states, input_symbols, transitions, initial_state, final_states)```

This method is the constructor for the `DFA` class. It takes the following parameters:

*   `states`: A list of the states in the DFA.
*   `input_symbols`: A list of the symbols in the alphabet that the DFA will accept.
*   `transitions`: A dictionary that defines the transition function of the DFA. The keys are pairs of states and symbols, and the values are the states to which the DFA transitions when it is in the key's state and reads the key's symbol.
*   `initial_state`: The state in which the DFA starts.
*   `final_states`: A list of the accept states of the DFA.

### Example Usage

Here's an example of how to use the `DFA` class to define:

```python
DFA (states={'q0', 'q1', 'q2'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q0', '1': 'q1'},
        'q1': {'0': 'q0', '1': 'q2'},
        'q2': {'0': 'q2', '1': 'q1'}
    },
    initial_state='q0',
    final_states={'q1'})
 ```

## Methods

### accept_string (self, string)
The accept_string method checks if a given string is accepted by the DFA. It iterates over the characters in the string and uses the transition function to move from one state to another. If the final state is in the set of accept states, the method returns True, indicating the string is accepted. Otherwise, it returns False.

```python
DFA.accept_string('0101')
# True
```

### union (self, other)

```python
DFA.union(dfa1,dfa2)
# return a new DFA that accepts the union of the language of dfa1 and dfa2
```

### intersection (self, other)

```python
DFA.intersection(dfa1,dfa2)
# return a new DFA that accepts the intersection of the language of dfa1 and dfa2
```

### complement (self)

```python
DFA.complement(dfa)
# return a new DFA that accepts the complement of the language of dfa
```

### difference (self, other)

```python
DFA.difference(dfa1,dfa2)
# return a new DFA that accepts the difference of the language of dfa1 and dfa2
```

### separate (self,dfa)

```python
DFA.separate(dfa1,dfa2)
# return a TRUE if dfa1 and dfa2 are separable
```

### is_empty (self)

```python
DFA.is_empty(dfa)
# return a TRUE if dfa is empty
```

### all_string_accepte (self, min_lenght, max_lenght, answer)

```python
DFA.all_string_accepte(dfa, min_lenght, max_lenght, answer)
# return all string accepted by dfa between min_lenght and max_lenght
```

### is_finite (self)

```python
DFA.is_finite(dfa)
# return a TRUE if dfa is finite
```

### shortest_string (self)

```python
DFA.shortest_string(dfa)
# return the shortest string accepted by dfa
```

### longest_string (self)

```python
DFA.longest_string(dfa)
# return the longest string accepted by dfa
```

### minimize (self)

```python
DFA.minimize(dfa)
# return a new DFA that accepts the same language as dfa but with the minimum number of states
```

### regex_to_dfa (self, regex)

```python
DFA.regex_to_dfa(regex)
# return a new DFA that accepts the same language as regex
```

### dfa_to_regex (self, dfa)

```python
DFA.dfa_to_regex(dfa)
# return a new regex that accepts the same language as dfa
```

# NFA (Non-Deterministic Finite Automata) 
This is a Python implementation of a Non-Deterministic Finite Automata (NFA), which is a simple abstract machine that recognizes patterns in strings. The implementation provides a basic framework for defining and working with NFAs.

## Class `NFA`

The `NFA` class represents a DFA. It has the following methods:

```def __init__(self, states, input_symbols, transitions, initial_state, final_states)```

This method is the constructor for the `DFA` class. It takes the following parameters:

*   `states`: A list of the states in the DFA.
*   `input_symbols`: A list of the symbols in the alphabet that the DFA will accept.
*   `transitions`: A dictionary that defines the transition function of the DFA. The keys are pairs of states and symbols, and the values are the states to which the DFA transitions when it is in the key's state and reads the key's symbol.
*   `initial_state`: The state in which the DFA starts.
*   `final_states`: A list of the accept states of the DFA.

### Example Usage

Here's an example of how to use the `NFA` class to define:

```python
NFA(
    states=['q0','q1', 'q2', 'q3','q4'],
    input_symbols=['a', 'b'],
    transitions={
        'q0': {'a':['q1','q2'],'b':['q4']},
        'q1': {'a': ['q0']},
        'q2': {'a': ['q3']},
        'q3': {'b': ['q0']},
        'q4': {},
        
    },
    initial_state='q0',
    final_states=['q4']
 ```

## Methods

### eliminate_nondeterminism(self)
    
```python
NFA.eliminate_nondeterminism(nfa)
# return a new DFA that accepts the same language as nfa
```

###  lambda_closure(states_set, transitions)
    
```python
NFA.lambda_closure(states_set, transitions)
# returns the lambda-closure set of a set of states
```

# DPDA (Deterministic Pushdown Automata)
This is a Python implementation of a Deterministic Pushdown Automata (DPDA), which is a simple abstract machine that recognizes patterns in strings. The implementation provides a basic framework for defining and working with DPDA.

## Class `DPDA`
The DPDA class is initialized with several parameters that define the properties of the DPDA:

* `states`: a list of all states in the DPDA
* `input_symbols`: the set of all input symbols that the DPDA can accept
* `stack_symbols`: the set of all stack symbols that the DPDA uses
* `transitions`: a dictionary that defines the transition function for the DPDA, where the keys are state-input symbol pairs and the values are lists of tuples that specify the next state, the symbol to be pushed onto the stack, and the symbol to be popped from the stack for that transition
* `initial_state`: the start state for the DPDA
* `initial_stack_symbol`: the start symbol for the stack
* `final_states`: a set of states that are designated as accept states

### Example Usage

Here's an example of how to use the `DPDA` class to define:

```python
DPDA(
    states={'q0', 'q1', 'q2','q3'},
    input_symbols={'a', 'b'},
    stack_symbols = {'a','b','Z0'},
    initial_stack_symbol = 'Z0',
    transitions={
        'q0': {['a','Z0']: ['q1',['a','Z0']]},
        'q1': {['a','a']: ['q1',['a','a']], ['b','a']: ['q2',[]]}, # [] or ['']
        'q2': {['b','a']: ['q2',[]], ['','Z0']: ['q3',['Z0']]}
    },
    initial_state='q0',
    final_states={'q3'}
)
```

## Methods

### accept_string (self, string)

```python
DPDA.accept_string(dpda, string)
# return a TRUE if dpda accepts string
```

# Authors
this document was generated by **AI**

# License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details