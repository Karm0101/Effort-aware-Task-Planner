const addTaskButton = document.getElementById('addTaskButton');

function addTask() {
    const newDiv = document.createElement("div");
    const taskBox = document.createElement("input");
    const deadlineBox = document.createElement("input");

    newDiv.appendChild(taskBox);
    newDiv.appendChild(deadlineBox);

    taskBox.classList.add("taskClass")
    deadlineBox.classList.add("deadlineClass")

    document.getElementById('taskContainer').appendChild(newDiv);
}

addTaskButton.addEventListener("click", addTask);