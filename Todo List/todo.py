import streamlit as st
import time

def main():
    st.title("To-Do List App")
    
    if "tasks" not in st.session_state:
        st.session_state.tasks = []

    title = st.text_input("Title :")
    description = st.text_area("Description :")
    
    if st.button("Add Task"):
        if title:
            task_data = {
                "title": title,
                "description": description if description else "",
                "time": time.strftime("%Y-%m-%d %H:%M:%S")
            }
            st.session_state.tasks.append(task_data)
            st.success("Task added successfully!")
        else:
            st.warning("Title cannot be empty!")
    
    # Display task list as a table
    if st.session_state.tasks:
        st.write("### Task List")
        task_table = "<table><tr><th>Serial Number</th><th>Title</th><th>Description</th><th>Time</th></tr>"
        for i, task_data in enumerate(st.session_state.tasks):
            task_table += f"<tr><td>{i+1}</td><td>{task_data['title']}</td><td>{task_data['description']}</td><td>{task_data['time']}</td></tr>"
        task_table += "</table>"
        st.write(task_table, unsafe_allow_html=True)
        
    # Deletion choice box
    delete_task = st.selectbox("Select task to delete:", options=["None"] + [task_data['title'] for task_data in st.session_state.tasks])
    if delete_task != "None":
        st.session_state.tasks = [task_data for task_data in st.session_state.tasks if task_data['title'] != delete_task]
        st.success("Task deleted successfully!")
        time.sleep(2)
        st.rerun()

if __name__ == "__main__":
    main()
