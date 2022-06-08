module Geometry {
  export class Square {
    constructor(public sideLength: number = 0) { 
    }

    area() {
      return Math.pow(this.sideLength, 2);
    }
  }
}


let s1 = new Geometry.Square(2);
