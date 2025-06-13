// console.log("Hai BVC")
// let x       //declering
// x = 200     //initiazing

// let w = 98
// w = 900

// // let x = 400; cannot redeclare

// var y = 100;
// var y = 120
// const z = 300;
// block1
// {
//     let x = 20;
//     var y = 120;
//     console.log(y); //120
//     const z = 300
// }
// console.log(y); //120
// // const z = 400; cannot redeclare


// console.log(x,y,z,w);






// let x = 6;
// let y = 10;
// let x = 5 , y = 10;
// console.log(x / y);

// x += 4; // => x = x + 5
// console.log(x)

// x = "10";
// console.log(x === y) //strict with type

// // and or not 
// is_boring = true
// feeling_sleepy = true

// if condition:
        // block of if

//if(condition)
//{}

// if(is_boring && feeling_sleepy)
// {
//     console.log("boring and sleeping");
//     console.log("here");
// }

// if(is_boring || feeling_sleepy) //or => ||
//     console.log("drink water");

// if( !is_boring) // not => !
//     console.log("Trainer Happy")

// let n = 100;
// let m = 100;

// if(n <= m)
// {
//     console.log("n is smaller")
// }
// else if(m <= n)
// {
//     console.log("m is smaller")
// }
// else
// {
//     console.log("both are Equal")
// }

//=>
// for i in range(1,100):

// i++ => i = i + 1

// for(let i = 1 ; i < 100 ; i++)
// {
//     console.log(i)
// }
// let x = 10
// while(x > 0)
// {
//     console.log(x);
//     x--; // => x = x - 1
// }
// let x = 0;
// do
// {
//     console.log(x); //3 2 1
//     x--; // 3 => 2 => 1 => 0
// }
// while(x > 0);

// const myFunction = () =>{

// }


// array = [2,3,4,5] //array index => 0 => length -1

// console.log(array.length);
// console.log(array[array.length - 1]); //len(list)
// array[0] = 100
// console.log(array)

// for(let i = 0 ; i < array.length ; i++)
// {
//     console.log("index : " , i , ", element : " , array[i])
// }

// for(let i of array) // for i in list:
// {
//     console.log(i)
// }


// arr = [1,2,3,4,100]

// console.log(arr);
// arr.push(10)
// console.log(arr);
// arr.pop()
// console.log(arr);
// arr.shift();
// console.log(arr);
// arr.unshift(100);
// arr.unshift(200);
// console.log(arr);

// console.log(arr.includes(100));
// console.log(arr.indexOf(100));

list = [0,1,2,3,4,5]
newArr = list.slice(0,3)
list.splice(3,3)
console.log(list)

let [x , y] = [10, 20 ,30]  // destructring
console.log(y);
