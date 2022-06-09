let addBtn = document.getElementById("btn-add");
let delBtn = document.getElementById("delete");
let editBtn = document.getElementById("edit");
let title = document.getElementById("note-title");
let content = document.getElementById("note-text");
let notes = localStorage.getItem("notes");
console.log(notes)
if (notes == null){
    notesObj = [];
} else {
    notesObj = JSON.parse(notes);
}

showNotes()


addBtn.addEventListener("click", (e) => {
    if (title.value == ""){
        return alert("Please add note title");
    }
    if (content.value == ""){
        return alert("Please add note content");
    }
    let myObj = {
        title: title.value,
        text: content.value
    }
    notesObj.push(myObj);
    localStorage.setItem("notes", JSON.stringify(notesObj));
    title.value = "";
    content.value = "";

    showNotes()
});

function showNotes() {
    notes = localStorage.getItem("notes");

    if (notes == null){
        notesObj = [];
    } else {
        notesObj = JSON.parse(notes);
    }

    let html = "";
    notesObj.forEach(function(element, index){
        html += `
        <div id="note${index}" class="note">
            <h3 class="note-title">${element.title}</h3>
            <p class="note-text">${element.text}</p>
            <button id="${index}" onclick="deleteNote(this.id)" class="note-btn delete">Delete</button>
            <button id="${index}" onclick="editNote(this.id)" class="note-btn edit">Edit</button>
        </div>
        `;
    });
    let noteElement = document.getElementById("notes");
    if (notesObj.length > 0){
        noteElement.innerHTML = html;
    } else {
        noteElement.innerHTML = `<h3>You do not have any notes stored</h3>`
    }
}

function deleteNote(noteID) {
    notesObj.splice(noteID, 1);
    localStorage.setItem("notes", JSON.stringify(notesObj));
    showNotes();
}

function editNote(noteID){
    if (title.value != ""){
        return alert("Title field has to be empty!");
    }
    if (content.value != ""){
        return alert("Text field has to be empty!");
    }
    title.value = notesObj[noteID].title
    content.value = notesObj[noteID].text
    notesObj.splice(noteID, 1);
    localStorage.setItem("notes", JSON.stringify(notesObj));
    showNotes()
}