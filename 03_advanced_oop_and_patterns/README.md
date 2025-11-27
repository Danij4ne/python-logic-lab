# 03 - Advanced OOP and Patterns

This module focuses on object-oriented programming concepts and more advanced Python patterns.  
The exercises explore how to model real-world entities, structure code using inheritance, handle errors properly, and work with iterators, generators, and decorators.

The goal is to build a deeper understanding of how Python organizes behavior, extends functionality, and manages execution flow.

---

## 1. OOP Basics

### Purpose
This section introduces the fundamentals of working with classes and objects.

### Concepts Addressed
- Defining classes
- Initializing attributes with `__init__`
- Instance methods
- Representing real-world entities in code

### Practical Use
Object-oriented programming is used to create reusable, structured, and maintainable code in applications of all sizes.

### Exercises
- `ex01_class_person.py`
- `ex02_bank_account.py`
- `ex03_library_book.py`

---

## 2. Inheritance and Polymorphism

### Purpose
This section expands class behavior by allowing one class to inherit from another and modify or extend its functionality.

### Concepts Addressed
- Class inheritance
- Method overriding
- Extending base behavior
- Specializing functionality in subclasses

### Practical Use
Inheritance helps avoid duplicated code and creates logical hierarchies, which are common in larger applications and frameworks.

### Exercises
- `ex01_shape_area_circle_rectangle.py`
- `ex02_employee_manager_inheritance.py`
- `ex03_vehicle_hierarchy.py`

---

## 3. Error Handling

### Purpose
This section explores how to handle exceptions to prevent programs from crashing and how to create custom error types.

### Concepts Addressed
- try/except blocks
- Handling common runtime errors
- Custom exception classes
- Graceful failure and error messaging

### Practical Use
Robust error handling is essential in production software, APIs, file systems, and user-facing applications.

### Exercises
- `ex01_safe_division.py`
- `ex02_read_file_with_exceptions.py`
- `ex03_custom_exceptions_bank.py`

---

## 4. Iterators and Generators

### Purpose
This section examines how Python retrieves data one item at a time, enabling efficient looping and incremental processing.

### Concepts Addressed
- The iterator protocol (`__iter__`, `__next__`)
- Generator functions using `yield`
- Producing sequences lazily instead of storing everything in memory

### Practical Use
Iterators and generators are widely used in data streaming, large dataset processing, and performance-sensitive applications.

### Exercises
- `ex01_custom_range_iterator.py`
- `ex02_even_numbers_generator.py`
- `ex03_paginated_reader_generator.py`

---

## 5. Decorators and Advanced Patterns

### Purpose
This section introduces decorators as a way to wrap and extend existing functions without modifying their code directly.

### Concepts Addressed
- Function wrapping
- Measuring execution time
- Logging function calls
- Retrying logic with decorator parameters

### Practical Use
Decorators are heavily used in frameworks like Flask, Django, FastAPI, and logging, authentication, caching, and performance monitoring systems.

### Exercises
- `ex01_timer_decorator.py`
- `ex02_logger_decorator.py`
- `ex03_retry_on_error_decorator.py`

---

## Module Summary

This module builds skills in:

- Structuring programs with classes
- Extending behavior through inheritance
- Handling errors safely
- Producing values efficiently with iterators and generators
- Enhancing functions using decorators

These concepts form a strong foundation for advanced Python development, larger applications, and professional software architectures.
