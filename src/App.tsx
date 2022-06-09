import React from "react";
import "./App.css";

import Task from "./ts-objects/Task";
import TaskBox from "./TaskBox";

function App() {
  const [taskName, setTaskName] = React.useState("");
  const [taskDate, setTaskDate] = React.useState("");
  const [taskDesc, setTaskDesc] = React.useState("");
  const [tasks, setTasks] = React.useState<Task[]>([]);

  function handleSubmit(event: React.FormEvent<HTMLFormElement>): void {
    event.preventDefault();
    let ret = createTask();
    if (ret === 1) {
      return; // prevent form clear
    }
    setTaskName("");
    setTaskDate("");
    setTaskDesc("");
  }

  function createTask(): number {
    if (taskName === "" || taskDate === "") {
      alert("CreateTask Missing Fields");
      return 1;
    }
    let input_task: Task = new Task(taskName, taskDate, taskDesc);
    setTasks((tasks) => [...(tasks ?? []), input_task]);
    return 0;
  }

  return (
    <div className="App">
      <h1> Odoo Task App</h1>
      <h5>(Typescript)</h5>
      <hr />
      <form onSubmit={handleSubmit}>
        <div>
          <h3>Create Task</h3>
          <input
            placeholder="Task Name"
            value={taskName}
            style={{ margin: 5 }}
            onChange={(e) => setTaskName(e.target.value)}
          ></input>
          <br />
          <input
            placeholder="Description"
            value={taskDesc}
            style={{ margin: 5 }}
            onChange={(e) => setTaskDesc(e.target.value)}
          ></input>
          <br />
          <input
            type="date"
            placeholder="Due Date"
            value={taskDate}
            style={{ margin: 5 }}
            onChange={(e) => setTaskDate(e.target.value)}
          ></input>
        </div>
        <button type="submit">Create Task</button>
      </form>
      <hr />
      <div style={{ display: "grid" }}>
        {tasks.map((task) => {
          return (
            <TaskBox
              name={task.name}
              dueDate={task.dueDate}
              description={task.description}
              status={task.status}
              urgency={task.urgency}
              setStatus={function () {}} // Not implemented
            />
          );
        })}
      </div>
    </div>
  );
}

export default App;
