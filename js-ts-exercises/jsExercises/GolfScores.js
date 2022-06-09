var names = ["Hole in one","Eagle","Birdie","Par","Bogey"];
function golfScore(par,strokes){
    if(strokes == 1){
        return names[0];
    } 
    else if( strokes <= par -2){
        return names[1];
    }
    else if(strokes == par -1){
        return names[2];
    }

    return ""
}

golfScore(5,4);