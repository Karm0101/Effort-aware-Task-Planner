const addTaskButton = document.getElementById('addTaskButton');

function addTask() {
    const newDiv = document.createElement("div");
    document.body.appendChild(newDiv)
    const taskBox = document.createElement("input");
    const deadlineBox = document.createElement("input");

    newDiv.appendChild(taskBox);
    newDiv.appendChild(deadlineBox);

    console.log("hi");
}

addTaskButton.addEventListener("click", addTask);