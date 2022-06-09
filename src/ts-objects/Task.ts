
type tasktatus = "Not Started" | "In progress" | "Finished"
type taskurgency = "Minor" | "Medium" | "Major" | "Critical"

class Task {
    name: string;
    dueDate: Date;
    description: string;
    status: tasktatus;
    urgency: taskurgency;

    constructor(taskname: string, dateDue: string, desc: string) {
        this.name = taskname
        this.dueDate = new Date(dateDue)
        this.description = desc
        this.status = "Not Started"
        this.urgency = "Medium"
    }

    setStatus(newStatus: tasktatus): void {
        this.status = newStatus
    }
}

export default Task