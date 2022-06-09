var board = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9: 0}
var winCombinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7],
                       [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]];
const readline = require('readline').createInterface({
input: process.stdin,
output: process.stdout,
});
var player_swap = {'X':'Y', 'Y':'X'}
function printboard(){
    console.log("Board is")
    console.log('\n'+board[1] +' '+board[2]+ ' '+ board[3]+'\n' + board[4]+' ' + board[5]+' '+board[6]+'\n'+ board[7]+' '+ board[8]+ ' ' + board[9]+ '\n')
}
function play(player){
    printboard()
    console.log("Player: "+player+"\'s turn")
    // let user_input;
    const prompt = require('prompt-sync')({sigint: true});
    let user_input = prompt('Enter a number: ');
    // readline.question("select a number", num => {user_input = num; readline.close() })
    // readline.close()
    console.log('reached here')
    if( !isNaN(user_input) ){
        

        if( user_input<1 || user_input>9){
            
            play(player)
        }
        else if(board[user_input]!= 0){
            console.log("Position already filled choose another position");
            play(player);
        }else{
            board[user_input] = player
            var game_op = checkWin(player)
            if(game_op){
                console.log("Game won by player "+player);
            }else{
                console.log("reached here")
                player = player_swap[player]
                play(player)
            }
        }
    }else{
        console.log("Please enter a number in the range 1 - 9 ")
    }
    
}
function checkWin(player) {
    var i, j, markCount
    for (i = 0; i < winCombinations.length; i++) {
        markCount = 0;
        for (j = 0; j < winCombinations[i].length; j++) {
            if (board[winCombinations[i][j]] === player) {
                markCount++;
            }
            if (markCount === 3) {
                return true;
            }
        }
    }
    return false;
}
play('X')