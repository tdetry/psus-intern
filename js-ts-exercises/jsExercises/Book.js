class Book{
    constructor(author){
        this._author=author;
    }

    get writer(){
        return this._author;s
    }

    set writer(updatedAuthor){
        this._author =updatedAuthor;
    }
}

