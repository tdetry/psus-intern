// class revisions
//
interface Person {
  name: string;
  age?: number;
  move(): void;
}

class Point {
  x: number
  //members are public by default
  
  constructor(x: number, public y: number = 0) {
    this.x = x;
  }

  norm(): number {
    return Math.sqrt(this.x * this.x + this.y * this.y);
  }

  static origin = new Point(0,0);
}

class Point3D extends Point {
  constructor (x:number, y: number, public z: number = 0) {
    super(x,y); // obligatory call in inheritance
  }
  
  //override parent methods
  norm(): number {
    let d = super.norm();
    return Math.sqrt(d*d + this.z * this.z);
  }
}


