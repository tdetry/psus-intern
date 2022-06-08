import { Vector } from "~/types";

export class Brick {
  private brickImg: HTMLImageElement = new Image();

  constructor(
    private brickWidth: number,
    private brickHeight: number,
    private position: Vector,
    private brickEnergy: number,
    image: string
  ) {
    this.brickWidth = brickWidth;
    this.brickHeight = brickHeight;
    this.position = position;
    this.brickEnergy = brickEnergy;
    this.brickImg.src = image;
  }

  // Getters
  get width(): number {
    return this.brickWidth;
  }

  get height(): number {
    return this.brickHeight;
  }

  get pos(): Vector {
    return this.position;
  }

  get image(): HTMLImageElement {
    return this.brickImg;  
  }

  get energy(): number {
    return this.brickEnergy;
  }

  // Setters

  set energy(energy: number) {
    this.brickEnergy = energy;
  }
}