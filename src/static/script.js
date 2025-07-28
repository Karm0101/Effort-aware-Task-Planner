const addTaskButton = document.getElementById("addTaskButton");
const enterTasksButton = document.getElementById("enterTasksButton");
const taskContainer = document.getElementById('taskContainer');
const removeTasksButton = document.getElementById('removeTasksButton');
const orderedTasksContainer = document.getElementById("orderedTasksContainer");

function addTask(event) {
    event.preventDefault();

    const newDiv = document.createElement("div");
    const taskBox = document.createElement("input");
    const deadlineBox = document.createElement("input");

    newDiv.appendChild(taskBox);
    newDiv.appendChild(deadlineBox);

    taskBox.placeholder = 'Enter task here...';
    taskBox.name = 'task';
    taskBox.required = true;

    deadlineBox.name = 'deadline';
    deadlineBox.type = "date";

    taskBox.classList.add("taskClass");
    deadlineBox.classList.add("deadlineClass");

    taskContainer.appendChild(newDiv);
}

function enterTasks(event){
    event.preventDefault();
    const taskData = document.querySelectorAll('#taskContainer input');
    const currentDate = new Date();
    let tasksArray = [];

    for(let i =0; i < taskData.length; i+=2){
        let endDate = new Date(taskData[i+1].value);
        timeDifference = endDate - currentDate;
        numOfDays = Math.ceil(timeDifference / (1000 * 3600 * 24));
        tasksArray.push({'task': taskData[i].value, 'deadline': numOfDays});
    }

    fetch('/process_tasks', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(tasksArray)
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        }
        else {}
    })
    .then(data => {
        taskContainer.innerHTML = '<div id="controlButtons"><button id="addTaskButton">Add a new task</button><button id="enterTasksButton" type="submit">Plan task order</button><button id="removeTasksButton" disabled="true">Remove ordered tasks</button></div>';
        document.getElementById('addTaskButton').disabled = true;
        document.getElementById('enterTasksButton').disabled = true;
        document.getElementById('removeTasksButton').disabled = false;

        for (let i = 0; i < data.length; i++) {
            const newDiv = document.createElement("div");
            const newCheckBox = document.createElement("input");
            const taskBox = document.createElement("p");
            const deadlineBox = document.createElement("p");

            newDiv.appendChild(newCheckBox);
            newDiv.appendChild(taskBox);
            newDiv.appendChild(deadlineBox);

            newDiv.classList.add('taskContainerClass')
            newCheckBox.classList.add('checkBoxClass');
            taskBox.classList.add('orderedTaskClass');
            deadlineBox.classList.add('orderedDeadlineClass');

            newCheckBox.type = 'checkbox'

            taskBox.textContent = data[i]

            orderedTasksContainer.appendChild(newDiv);
        }
    })
    .catch(error => console.log('Error'));
}

function removeOrderedTasks() {
    orderedTasksContainer.innerHTML = '<div id="orderedTasksContainer"></div>';
    addTaskButton.disabled = false;
    enterTasksButton.disabled = false;
    removeTasksButton.disabled = true;
}

addTaskButton.addEventListener("click", addTask);
enterTasksButton.addEventListener("click", enterTasks);
removeTasksButton.addEventListener("click", removeOrderedTasks)