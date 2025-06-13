let myPromise = new Promise((resolved , rejected )=>{
    if(true)
    resolved("promise success");

    rejected(400);
})

// myPromise.then((msg)=>{
//     console.log("result resolved , :" , msg)
// })
// .catch((msg)=>{
//     console.log("result failed : " , msg)
// })


console.log("hai");

const getData = async () => {
    // const response = fetch("https://jsonplaceholder.typicode.com/todos");
    // console.log(response);
    // response.then((res) =>{
    //     console.log(res);
    //     return res.json();
    // })
    // .then((data) => {
    //     console.log(data);
    // })
    let list = [];
    
    const response = await fetch("https://jsonplaceholder.typicode.com/todos")
                    .then(res => res.json())
                    .then(data => {
                        list = data;
                        localStorage.setItem("data" , JSON.stringify(data))
                    })
                    .catch(err => console.log(err))

    list.forEach((item) =>{

        const todoItem = document.createElement("p");
        todoItem.textContent = item.title;

        //add completed data 
        // if false => red bg
        // if true => green bg


        document.getElementById("container").append(todoItem);
    })
    
}

getData();




// fetch("url")
// .then(res => res.json())
// .then(data => data)
// .catch(error => console.log(error))