import React, { useEffect, useState } from 'react'
import '../styles/home.css'
import TodoItem from '../Components/TodoItem';

const Home = () => {

    const [todoList , setTodoList] = useState([]);

    const list = JSON.parse(localStorage.getItem("todoList")) || [];

    const apiUrl = `https://684e85b9f0c9c9848d285ba2.mockapi.io/todo`

    if(list.length)
        setTodoList(list);


    const handleStatusChange = (data , index) =>{
        const newData = {...data , status : !data.status}
        const newTodoList = [...todoList]
        newTodoList[index] = newData;
        setTodoList(newTodoList);
    };

    const fetchData = async() =>{
        const response = await fetch(apiUrl)
                        .then( res => res.json())
                        .then( data => data)
                        .catch( error => console.log("Error occured : ", error));
        console.log( "response" , response);
        setTodoList(response);
        localStorage.setItem(todoList , JSON.stringify(response))
    };

    useEffect(()=>{
        fetchData();
    } , [])



  return (
    <div className='container'>
        <div className='container todo-container'>
                {todoList.length ?
                    todoList.map((item , index)=>{
                        return <TodoItem data={item} index={index} handleStatusChange={handleStatusChange} />
                    })
                    :
                    <div>No Todos Found</div>
                }
        </div>
        <div className='container '>
            {"Add Form for adding TODO"}
        </div>
    </div>
  )
};

export default Home;