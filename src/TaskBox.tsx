import Task from "./ts-objects/Task";
import { FunctionComponent } from "react";

function TaskBox({ name, dueDate, description, status, urgency }: Task) {
  return (
    <div style={{ border: "1px solid black", margin: 10 }}>
      <h3>{name}</h3>
      <p>{description}</p>
      <h6>{dueDate.toISOString().slice(0, 10)}</h6>
      <p>Status: {status}</p>
      <label>Set Status</label>
      <select
        name="statusbar"
        onClick={() => alert("Not implemented")}
      ></select>
    </div>
  );
}

export default TaskBox;
