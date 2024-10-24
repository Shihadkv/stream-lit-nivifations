import streamlit as st

def show_todo_list():
    # Page Title with custom color
    st.markdown("<h1 style='color:#4CAF50;'>📝 To-Do List</h1>", unsafe_allow_html=True)
    
    # Task Input
    new_task = st.text_input("Add a new task", "")
    
    # Initialize session state for tasks
    if 'tasks' not in st.session_state:
        st.session_state.tasks = []

    # Add Task Button
    if st.button("Add Task"):
        if new_task:
            st.session_state.tasks.append({"task": new_task, "done": False})
            st.success(f"Task '{new_task}' added!")
        else:
            st.error("Please enter a task before adding.")

    st.markdown("### Your Tasks:")

    # Task Progress Bar
    total_tasks = len(st.session_state.tasks)
    completed_tasks = sum(1 for task in st.session_state.tasks if task["done"])
    if total_tasks > 0:
        progress = completed_tasks / total_tasks
        st.progress(progress)
        st.write(f"Completed {completed_tasks}/{total_tasks} tasks.")
    else:
        st.write("No tasks yet.")

    # Task List Display with Checkboxes and Remove Option
    for idx, task_info in enumerate(st.session_state.tasks):
        task = task_info["task"]
        is_done = task_info["done"]
        
        col1, col2, col3 = st.columns([0.1, 0.7, 0.2])

        # Task Checkbox (mark as done/undone)
        with col1:
            task_info["done"] = st.checkbox("", value=is_done, key=f"task_{idx}")

        # Task Description
        with col2:
            task_style = "line-through" if task_info["done"] else "none"
            st.markdown(f"<span style='text-decoration:{task_style};'>{task}</span>", unsafe_allow_html=True)

        # Remove Task Button
        with col3:
            if st.button("Remove", key=f"remove_{idx}"):
                st.session_state.tasks.pop(idx)
               

    # Clear All Tasks Button
    if st.button("Clear All Tasks"):
        st.session_state.tasks = []
       
