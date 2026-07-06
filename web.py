import streamlit as st
import functions


todos = functions.get_todos()

def add_todo():
    todo = st.session_state['new_todo'].strip()

    if todo:
        todos.append(todo)
        functions.write_todos(todos)

    st.session_state["new_todo"] = ""

st.title("My todo app 📝")
st.caption("Stay organized and get things done!")

if not todos:
    st.info("No Tasks yet. Add you first todo!")


st.write(f"Total Tasks: {len(todos)}")
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a todo: ",
              placeholder="Add a new todo...", 
              on_change=add_todo, key="new_todo", 
              label_visibility="collapsed")

if len(todos) == 0:
    st.success("All Tasks Completed!")
    st.balloons()

st.write("Made with ❤️ by Jashan")