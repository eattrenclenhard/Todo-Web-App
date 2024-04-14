import streamlit as st
import modules.functions as ft

todos = ft.get_todos()


def add_todo():
    todo = st.session_state['new_todo'].strip() + '\n'
    if todo != '\n': # prevents empty input
        print('Adding', todo)
        todos.append(todo)
        ft.write_todos(todos)


st.title('My Todo App')
st.subheader('This is Sparta!')
st.write('This app strives to increase your productivity.')

for t in todos:
    checkbox = st.checkbox(t, key=t)
    if checkbox:
        print(t)
        todos.remove(t)
        ft.write_todos(todos)
        # don't forget to update streamlit session state too!
        del st.session_state[t]
        st.experimental_rerun() # or st.rerun()
        # required for checkboxes, checkboxes element won't be deleted in real time otherwise

# st.subheader('Manual checkboxes')
# st.checkbox('Sample 1')
# st.checkbox('Sample 2')

st.text_input(label='Enter a todo:', placeholder='Add a new todo...',
              on_change=add_todo,  # callback function
              key='new_todo')
# the key argument serves as an identifier for this widget
# notice that whenever user presses the enter button,
# the entire script is executed from TOP-to-BOTTOM!

print('the lion sleeps tonight')

# st.session_state  # surprisingly, this will be rendered

# streamlit trivia
# the script executes on every reload/refresh
# use pip freeze > requirements.txt command
# to generate required packages of the project