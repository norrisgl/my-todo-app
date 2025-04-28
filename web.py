import streamlit as st
import utils


def add_todo():
    new_todo = st.session_state["new_todo"].title() + '.\n'
    todos.append(new_todo)
    utils.write_todos(todos)
    st.session_state["new_todo"] = ""


todos = utils.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        utils.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a todo", placeholder="Add a new todo...",
              on_change=add_todo, key='new_todo',
              label_visibility="collapsed")
