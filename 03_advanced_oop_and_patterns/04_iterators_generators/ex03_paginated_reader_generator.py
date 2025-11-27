

"""
Ex03 - Paginated Reader Generator

Description:
    Create a generator that simulates reading a list of items in pages.
    Each iteration should return a "page" containing a fixed number of items.

Requirements:
    - Define a function named paginated_reader(data, page_size).
    - The function should:
        - take a list (data)
        - take a page_size (number of items per page)
        - yield slices (sub-lists) of the data, page by page
    - In the main part of the script, create a sample list and
      iterate through the generator, printing each page.

Notes:
    - No user input is required.
    - The last page may contain fewer items if the list size is not divisible by page_size.

Example (expected behavior):
    Page: [1, 2, 3]
    Page: [4, 5, 6]
    Page: [7, 8]
"""

# TODO:
# 1. Define paginated_reader(data, page_size).
# 2. Yield slices of the list, page by page.
# 3. Test the generator with a sample list and print each page.
