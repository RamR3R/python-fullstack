// function add(x , y){
//     return x + y;
// }

// const add = function(x,y){
//     return x + y;
// }

// const add = (x, y) => {
//     return x + y;
// }

const add = (x,y) => x + y;

// const sum = (a , b , calback ) =>{
//     x = a + b;
//     calback();
//     return x;
// }

// const sum = (a,b , fun) => {
//     return fun(a,b);
// }

// console.log(sum(4, 5, () => console.log("calculating.....")));

// console.log(sum(4 , 5 , add))

// result = (() => {
//     console.log("inside this anon function")
//     return 100
// })();

// console.log(result);


const obj = {
    name : "Ram",
    age : 23
}

// console.log(obj.age)
// console.log(obj["name"])

// const userDetails = {
//     ...obj,
//     isAdminUser : true
// }

// console.log(userDetails)


const arr = [ 1, 2, 3 , 4, 5 ]

console.log(arr);
const newArr = arr.filter((xxxyy , index) => {

    if(xxxyy % 2 == 0)
        return true;
    else
        return false;
})
console.log(newArr);