// console.log(`Hello`);
// console.log(`world`);

// window.alert(`Hello`);
// window.alert(`world`);

//INTRODUCTION
document.getElementById("title").textContent = `Learning Javascript`;
document.getElementById("para").textContent = `Learning Javascript, HTML, and CSS`;
//VARIABLES
x = 2; 
y = 4;
console.log(`x is ${x}`);
console.log(`x has the type of ${typeof x}`);
/* OUTPUT
    x is 2
    x has the type of number
*/
let username;
username = window.prompt("Whats your username? ");
document.getElementById("user").textContent = `${username}`

