import streamlit as st
import function

todos = function.python_project()

def add_todo():
    todo = st.session_state['new_todo'] +'\n'
    todos.append(todo)
    function.write_todos(todos)

st.title("To do app")
st.subheader("This is my todo list.")
st.write("This app is to increase your productivity "
         "and help to stay disciplined.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        function.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder='Add new todo....',
              on_change=add_todo, key='new_todo')


