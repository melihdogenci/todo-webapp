import streamlit as st
import functions
import os

# Ensure "todos.txt" exists
if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as f:
        pass

# Load the todos from the file
todos = functions.get_todos()

# Initialize todos in session state if not already set
if 'todos' not in st.session_state:
    st.session_state.todos = todos

if 'completed_todos' not in st.session_state:
    st.session_state.completed_todos = set()

def add_todo():
    """Add a new to-do to the list."""
    todo = st.session_state["new_todo"].strip()
    if todo:  # Check for empty input
        if todo + "\n" not in st.session_state.todos:  # Avoid duplicates
            st.session_state.todos.append(todo + "\n")
            functions.write_todos(st.session_state.todos)
            st.session_state["new_todo"] = ""  # Clear input after adding
        else:
            st.warning("To-do already exists.")  # Provide a warning for duplicates

def remove_todo(todo_item):
    """Remove the specified to-do item from the list."""
    st.session_state.todos.remove(todo_item)
    functions.write_todos(st.session_state.todos)
    st.success(f"Completed: {todo_item.strip()}")  # Show a success message
    st.session_state.completed_todos.add(todo_item)  # Track completed todos

st.title('My To-Do App')
st.subheader('This is my to-do app.')
st.write("This app is designed to increase productivity.")

# Display todos with checkboxes
for todo in st.session_state.todos:
    todo_item = todo.strip()
    if todo_item not in st.session_state.completed_todos:
        if st.checkbox(todo_item, key=f"checkbox_{todo_item}"):
            remove_todo(todo)

# Input for adding a new to-do
st.text_input(label="", placeholder="Add a new to-do...",
              on_change=add_todo, key="new_todo")
















