const addTaskButton = document.getElementById("addTaskButton");
const enterTasksButton = document.getElementById("enterTasksButton");

function addTask() {
    const newDiv = document.createElement("div");
    const taskBox = document.createElement("input");
    const deadlineBox = document.createElement("input");

    newDiv.appendChild(taskBox);
    newDiv.appendChild(deadlineBox);

    taskBox.classList.add("taskClass");
    deadlineBox.classList.add("deadlineClass");

    document.getElementById("taskContainer").appendChild(newDiv);
}

function enterTasks(){}

addTaskButton.addEventListener("click", addTask);
enterTasksButton.addEventListener("click", enterTasks);