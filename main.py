import streamlit as st
from functions import get_todos, write_todos

todos = get_todos()



def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    write_todos(todos)


st.title("My ToDO Application")
st.divider()
st.subheader("presenting my TO-DO app")
st.write("this application helps you to manage your day to day task and improve your work efficiency")
st.divider()

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="", placeholder="add a todo", on_change=add_todo, key="new_todo")

# st.session_state  # this will give you a dictionary in webpage to inspect
