const addTaskButton = document.getElementById("addTaskButton");
const enterTasksButton = document.getElementById("enterTasksButton");

function addTask(pointerEvent) {
    pointerEvent.preventDefault();

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

    document.getElementById("taskContainer").appendChild(newDiv);
}

function enterTasks(){
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
            return response.json()
        }
        else {}
    })
    .then(data => console.log(data))
    .catch(error => console.log('Error'))
}

addTaskButton.addEventListener("click", addTask);
enterTasksButton.addEventListener("click", enterTasks);