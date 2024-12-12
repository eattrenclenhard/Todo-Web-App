import streamlit as st
import modules.functions as ft

todos = ft.get_todos()

# st.set_page_config(layout='wide')

def add_todo():
    # analogous to key-value pair of GET request
    todo = st.session_state['new_todo'].strip() + '\n'
    if todo != '\n': # prevents empty input
        print('Adding', todo)
        if todos[-1][-1] != '\n':
            '''ensure new item starts on new line'''
            # print('INSERTING Break Line')
            # raw_string=rf"last character is: {todos[-1]}"
            # print(raw_string)
            todos[-1] += '\n'
#             print('after revision: ', repr(todos[-1]))
        todos.append(todo)
        ft.write_todos(todos)


st.title('My Todo App')
st.subheader('This is Sparta!')
st.write('This app strives to increase your <b>productivity</b>.',
         unsafe_allow_html=True) # </h1></h1>

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

print('Todo Web App is running...')

# st.session_state  # surprisingly, this will be rendered
# value of checkbox object will be false if unchecked

# streamlit trivia
# the script executes on every reload/refresh
# use pip freeze > requirements.txt command
# to generate required packages of the project